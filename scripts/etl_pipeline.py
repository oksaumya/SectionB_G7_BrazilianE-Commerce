from pathlib import Path
import pandas as pd


def run_pipeline(raw_dir: Path, output_path: Path) -> pd.DataFrame:

    # -------------------------------------------------------------------------
    # STEP 1 — Load raw files
    # -------------------------------------------------------------------------
    print(f"Loading raw data from {raw_dir} ...")

    orders       = pd.read_csv(raw_dir / "olist_orders_dataset.csv")
    order_items  = pd.read_csv(raw_dir / "olist_order_items_dataset.csv")
    customers    = pd.read_csv(raw_dir / "olist_customers_dataset.csv")
    sellers      = pd.read_csv(raw_dir / "olist_sellers_dataset.csv")
    products     = pd.read_csv(raw_dir / "olist_products_dataset.csv")
    payments     = pd.read_csv(raw_dir / "olist_order_payments_dataset.csv")
    reviews      = pd.read_csv(raw_dir / "olist_order_reviews_dataset.csv")
    geolocation  = pd.read_csv(raw_dir / "olist_geolocation_dataset.csv")
    category_tr  = pd.read_csv(raw_dir / "product_category_name_translation.csv")

    # -------------------------------------------------------------------------
    # STEP 2 — Parse datetimes
    # -------------------------------------------------------------------------
    print("Parsing datetimes ...")

    date_cols = [
        'order_purchase_timestamp',
        'order_approved_at',
        'order_delivered_carrier_date',
        'order_delivered_customer_date',
        'order_estimated_delivery_date'
    ]
    for col in date_cols:
        orders[col] = pd.to_datetime(orders[col])

    order_items['shipping_limit_date'] = pd.to_datetime(
        order_items['shipping_limit_date']
    )

    # -------------------------------------------------------------------------
    # STEP 3 — Fix typos & clean individual tables
    # -------------------------------------------------------------------------
    print("Fixing typos ...")

    # Products — fix column name typos
    products.rename(columns={
        'product_name_lenght'       : 'product_name_length',
        'product_description_lenght': 'product_description_length'
    }, inplace=True)

    # Products — merge English category names
    products = products.merge(category_tr, on='product_category_name', how='left')
    products['product_category_name_english'] = (
        products['product_category_name_english'].fillna('unknown')
    )

    # Products — fill numeric nulls with median
    for col in ['product_weight_g', 'product_length_cm',
                'product_height_cm', 'product_width_cm']:
        products[col] = products[col].fillna(products[col].median())

    # Products — drop columns not needed for analysis
    products.drop(columns=[
        'product_name_length',
        'product_description_length',
        'product_photos_qty',
        'product_category_name'       # keeping English version only
    ], errors='ignore', inplace=True)

    # Geolocation — deduplicate by averaging lat/lng per zip code
    geolocation = (
        geolocation
        .groupby('geolocation_zip_code_prefix')
        .agg(
            geolocation_lat=('geolocation_lat', 'mean'),
            geolocation_lng=('geolocation_lng', 'mean')
        )
        .reset_index()
    )

    # Reviews — fill missing comment text
    reviews['review_comment_message'] = (
        reviews['review_comment_message'].fillna('no comment')
    )
    reviews = reviews[['order_id', 'review_score', 'review_comment_message']]

    # -------------------------------------------------------------------------
    # STEP 4 — Merge all tables into master
    # -------------------------------------------------------------------------
    print("Merging tables ...")

    # Aggregate payments to order level
    payments_agg = (
        payments
        .groupby('order_id')
        .agg(
            payment_type=('payment_type', 'first'),
            payment_installments=('payment_installments', 'sum'),
            payment_value=('payment_value', 'sum')
        )
        .reset_index()
    )

    master = orders.copy()
    master = master.merge(order_items,   on='order_id',    how='left')
    master = master.merge(products,      on='product_id',  how='left')
    master = master.merge(sellers,       on='seller_id',   how='left')
    master = master.merge(customers,     on='customer_id', how='left')
    master = master.merge(payments_agg,  on='order_id',    how='left')
    master = master.merge(reviews,       on='order_id',    how='left')
    master = master.merge(
        geolocation.rename(columns={
            'geolocation_zip_code_prefix': 'customer_zip_code_prefix',
            'geolocation_lat'            : 'customer_lat',
            'geolocation_lng'            : 'customer_lng'
        }),
        on='customer_zip_code_prefix',
        how='left'
    )

    # -------------------------------------------------------------------------
    # STEP 5 — Feature engineering
    # -------------------------------------------------------------------------
    print("Engineering features ...")

    # Time features
    master['order_year']         = master['order_purchase_timestamp'].dt.year
    master['order_month']        = master['order_purchase_timestamp'].dt.month
    master['order_month_name']   = master['order_purchase_timestamp'].dt.strftime('%b')
    master['order_day_of_week']  = master['order_purchase_timestamp'].dt.strftime('%A')
    master['order_quarter']      = master['order_purchase_timestamp'].dt.quarter

    # Delivery features
    master['delivery_time_days'] = (
        master['order_delivered_customer_date']
        - master['order_purchase_timestamp']
    ).dt.days

    master['estimated_delivery_days'] = (
        master['order_estimated_delivery_date']
        - master['order_purchase_timestamp']
    ).dt.days

    master['delay_days'] = (
        master['order_delivered_customer_date']
        - master['order_estimated_delivery_date']
    ).dt.days

    master['is_late'] = (
        master['order_delivered_customer_date']
        > master['order_estimated_delivery_date']
    ).astype('Int64')

    # Revenue feature
    master['total_item_value'] = master['price'] + master['freight_value']

    # -------------------------------------------------------------------------
    # STEP 6 — Final cleanup
    # -------------------------------------------------------------------------
    print("Final cleanup ...")

    # Only keep rows where order_status is meaningful for analysis
    # (keep all statuses — cancellations are part of the business problem)

    # Reset index cleanly
    master = master.reset_index(drop=True)

    # -------------------------------------------------------------------------
    # STEP 7 — Save output
    # -------------------------------------------------------------------------
    output_path.parent.mkdir(parents=True, exist_ok=True)
    master.to_csv(output_path, index=False)

    size_mb = output_path.stat().st_size / (1024 * 1024)
    print(f"Done → {output_path}")
    print(f"Rows: {master.shape[0]:,}  |  Columns: {master.shape[1]}  |  "
          f"Size: {size_mb:.1f} MB")

    return master