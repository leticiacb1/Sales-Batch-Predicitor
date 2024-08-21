-- -------- PROCESS_DATA --------
WITH processed_data AS (
    select
        store_id,
        date_sale,
        total_sales,
        EXTRACT(YEAR FROM date_sale)::INT AS year,         -- Extract year information from date_sale 
        EXTRACT(MONTH FROM date_sale)::INT AS month,       -- Extract month information from date_sale
        EXTRACT(DAY FROM date_sale)::INT AS day,           -- Extract day information from date_sale
        EXTRACT(DOW FROM date_sale)::INT AS weekday        -- Extract weekday information from date_sale
    FROM
        sales_analytics.scoring_ml_leticiacb1
)

-- -------- RETURN PREDICT DATA --------
SELECT store_id, date_sale, year, month, day, weekday FROM processed_data;
