-- -------- CREATE TABLE --------
-- Delete old records from this table every time you make predictions.
DROP TABLE IF EXISTS sales_analytics.scoring_ml_leticiacb1;

-- Create prediction table
CREATE TABLE IF NOT EXISTS sales_analytics.scoring_ml_leticiacb1 (
  store_id int4 NOT NULL,
  date_sale date NOT NULL,
  total_sales numeric(10,2)
)