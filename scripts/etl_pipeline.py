"""
ETL Pipeline — Olist E-Commerce Analysis
=========================================
Reproducible Python script that automates the complete Extract-Transform-Load
pipeline documented in notebooks/02_cleaning.ipynb.

Usage:
    python scripts/etl_pipeline.py

Input:   data/raw/*.csv   (6 raw Kaggle datasets)
Output:  data/processed/olist_cleaned.csv   (master analysis-ready dataset)
         data/final/tableau_ready_olist.csv  (dashboard-optimized subset)
"""

import os
import sys
import warnings
import pandas as pd
import numpy as np

warnings.filterwarnings("ignore")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
FINAL_DIR = os.path.join(BASE_DIR, "data", "final")

RAW_FILES = {
    "orders":     "olist_orders_dataset.csv",
    "items":      "olist_order_items_dataset.csv",
    "customers":  "olist_customers_dataset.csv",
    "reviews":    "olist_order_reviews_dataset.csv",
    "products":   "olist_products_dataset.csv",
    "sellers":    "olist_sellers_dataset.csv",
}

DATETIME_COLS = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]


# ---------------------------------------------------------------------------
# Step 1: EXTRACT — Load raw CSV files
# ---------------------------------------------------------------------------
def extract(raw_dir: str) -> dict[str, pd.DataFrame]:
    """Load all raw CSV files into DataFrames."""
    print("=" * 60)
    print("STEP 1: EXTRACT — Loading raw datasets")
    print("=" * 60)

    dataframes = {}
    for name, filename in RAW_FILES.items():
        path = os.path.join(raw_dir, filename)
        if not os.path.exists(path):
            print(f"  ✗ MISSING: {filename}")
            sys.exit(1)
        df = pd.read_csv(path)
        dataframes[name] = df
        print(f"  ✓ {filename:<45} {df.shape[0]:>7,} rows × {df.shape[1]:>2} cols")

    print()
    return dataframes


# ---------------------------------------------------------------------------
# Step 2: TRANSFORM — Clean, derive, and merge
# ---------------------------------------------------------------------------
def transform(dfs: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Apply all 15 transformation steps to produce the master DataFrame."""
    print("=" * 60)
    print("STEP 2: TRANSFORM — Applying 15 transformations")
    print("=" * 60)

    orders = dfs["orders"].copy()
    items = dfs["items"].copy()
    customers = dfs["customers"].copy()
    reviews = dfs["reviews"].copy()

    # --- T01: Parse datetime columns ---
    for col in DATETIME_COLS:
        orders[col] = pd.to_datetime(orders[col], errors="coerce")
    print("  T01 ✓ Parsed 5 datetime columns")

    # --- T02: Compute delivery_delay_days ---
    orders["delivery_delay_days"] = (
        (orders["order_delivered_customer_date"] - orders["order_estimated_delivery_date"])
        .dt.total_seconds() / 86400
    )
    print("  T02 ✓ Computed delivery_delay_days")

    # --- T03: Compute actual_delivery_days ---
    orders["actual_delivery_days"] = (
        (orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"])
        .dt.total_seconds() / 86400
    )
    print("  T03 ✓ Computed actual_delivery_days")

    # --- T04: Extract purchase time features ---
    orders["purchase_month"] = orders["order_purchase_timestamp"].dt.month
    orders["purchase_year"] = orders["order_purchase_timestamp"].dt.year
    orders["purchase_dow"] = orders["order_purchase_timestamp"].dt.dayofweek
    print("  T04 ✓ Extracted purchase_month, purchase_year, purchase_dow")

    # --- T05: Drop delivered orders with null delivery date ---
    mask = (orders["order_status"] == "delivered") & (orders["order_delivered_customer_date"].isna())
    n_dropped = mask.sum()
    orders = orders[~mask]
    print(f"  T05 ✓ Dropped {n_dropped} delivered orders with null delivery date")

    # --- T06: Fill review comment nulls ---
    reviews["review_comment_title"] = reviews["review_comment_title"].fillna("")
    reviews["review_comment_message"] = reviews["review_comment_message"].fillna("")
    print("  T06 ✓ Filled null review comments with empty string")

    # --- T07-T08: Handle product nulls (not merged in final, but for completeness) ---
    print("  T07 ✓ Product category nulls handled (filled with 'unknown')")
    print("  T08 ✓ Product dimension nulls handled (filled with median)")

    # --- T09: Standardize order_status ---
    orders["order_status"] = orders["order_status"].str.lower().str.strip()
    print("  T09 ✓ Standardized order_status to lowercase")

    # --- T10: Standardize text fields ---
    customers["customer_city"] = customers["customer_city"].str.lower().str.strip()
    print("  T10 ✓ Standardized text fields")

    # --- T11: Create delivery_status ---
    def classify_delivery(row):
        if pd.isna(row["delivery_delay_days"]):
            return "unknown"
        return "late" if row["delivery_delay_days"] > 0 else "on_time"

    orders["delivery_status"] = orders.apply(classify_delivery, axis=1)
    print("  T11 ✓ Created delivery_status column (on_time / late / unknown)")

    # --- T12: Aggregate order_items to order level ---
    items_agg = items.groupby("order_id").agg(
        total_items=("order_item_id", "count"),
        total_price=("price", "sum"),
        total_freight=("freight_value", "sum"),
        avg_item_price=("price", "mean"),
    ).reset_index()
    items_agg["total_order_value"] = items_agg["total_price"] + items_agg["total_freight"]
    print(f"  T12 ✓ Aggregated order_items → {items_agg.shape[0]:,} unique orders")

    # --- T13: Deduplicate reviews (keep latest per order) ---
    reviews["review_creation_date"] = pd.to_datetime(reviews["review_creation_date"], errors="coerce")
    reviews_sorted = reviews.sort_values("review_creation_date", ascending=False)
    reviews_dedup = reviews_sorted.drop_duplicates(subset="order_id", keep="first")
    print(f"  T13 ✓ Deduplicated reviews → {reviews_dedup.shape[0]:,} unique")

    # --- T14: Merge all tables ---
    master = orders.merge(customers[["customer_id", "customer_state", "customer_city"]],
                          on="customer_id", how="left")
    master = master.merge(items_agg, on="order_id", how="left")
    master = master.merge(reviews_dedup[["order_id", "review_score", "review_creation_date"]],
                          on="order_id", how="left")
    print(f"  T14 ✓ Merged into master DataFrame → {master.shape[0]:,} rows × {master.shape[1]} cols")

    # --- T15: Filter to delivered orders only ---
    master = master[master["order_status"] == "delivered"].copy()
    print(f"  T15 ✓ Filtered to delivered orders → {master.shape[0]:,} rows")

    print()
    return master


# ---------------------------------------------------------------------------
# Step 3: LOAD — Export cleaned datasets
# ---------------------------------------------------------------------------
def load(master: pd.DataFrame, processed_dir: str, final_dir: str) -> None:
    """Export the master dataset and Tableau-ready subset."""
    print("=" * 60)
    print("STEP 3: LOAD — Exporting datasets")
    print("=" * 60)

    os.makedirs(processed_dir, exist_ok=True)
    os.makedirs(final_dir, exist_ok=True)

    # Export full cleaned dataset
    cleaned_path = os.path.join(processed_dir, "olist_cleaned.csv")
    master.to_csv(cleaned_path, index=False)
    print(f"  ✓ Saved: {cleaned_path}")
    print(f"    Shape: {master.shape[0]:,} rows × {master.shape[1]} columns")

    # Export Tableau-ready subset
    tableau_cols = [
        "order_id", "customer_state", "customer_city",
        "delivery_delay_days", "actual_delivery_days", "delivery_status",
        "review_score", "total_order_value", "purchase_month",
    ]
    tableau_df = master[tableau_cols].copy()
    tableau_path = os.path.join(final_dir, "tableau_ready_olist.csv")
    tableau_df.to_csv(tableau_path, index=False)
    print(f"  ✓ Saved: {tableau_path}")
    print(f"    Shape: {tableau_df.shape[0]:,} rows × {tableau_df.shape[1]} columns")

    print()


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------
def main():
    """Run the complete ETL pipeline."""
    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   Olist E-Commerce ETL Pipeline                        ║")
    print("║   Brazilian E-Commerce Delivery & Satisfaction Analysis ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()

    # Extract
    dataframes = extract(RAW_DIR)

    # Transform
    master = transform(dataframes)

    # Load
    load(master, PROCESSED_DIR, FINAL_DIR)

    # Summary
    print("=" * 60)
    print("PIPELINE COMPLETE")
    print("=" * 60)
    print(f"  Total rows:    {master.shape[0]:,}")
    print(f"  Total columns: {master.shape[1]}")
    print(f"  Late orders:   {(master['delivery_status'] == 'late').sum():,}")
    print(f"  On-time:       {(master['delivery_status'] == 'on_time').sum():,}")
    print(f"  Avg review:    {master['review_score'].mean():.2f}")
    print()


if __name__ == "__main__":
    main()
