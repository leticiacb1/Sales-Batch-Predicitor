-- -------- UPDATE TABLE WITH PREDICTIONS --------

UPDATE 
    sales_analytics.scoring_ml_leticiacb1
SET 
    total_sales = :predict_value
WHERE 
    store_id = :store_id AND date_sale = :date