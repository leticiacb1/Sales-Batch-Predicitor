-- -------- GENERATE DATA --------
-- Generate data for the table using CTEs
WITH generate_date_sales AS (
  SELECT 
    CURRENT_DATE + i AS date_sale
  FROM 
    generate_series(0, :num_days - 1) AS gs (i)                            -- How many days in the future
), store_ids AS (
  SELECT 
    :start_id + gs.i AS store_id
  FROM 
    generate_series(0, :end_id - :start_id) AS gs (i)                      -- Generate random store_id from start_store_id to end_store_id
)
INSERT INTO 
    sales_analytics.scoring_ml_leticiacb1 (store_id, date_sale, total_sales)
    SELECT 
        s.store_id, d.date_sale, NULL
    FROM 
        store_ids AS s CROSS JOIN generate_date_sales AS d;