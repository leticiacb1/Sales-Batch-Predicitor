-- Delest existing view
DROP VIEW IF EXISTS sales_analytics.view_abt_train_leticiacb1;

-- Create view
CREATE OR REPLACE VIEW sales_analytics.view_abt_train_leticiacb1 AS
	SELECT 
		store_id,
		EXTRACT(YEAR FROM date_sale)::INT AS year,         -- Extract year information from date_sale 
		EXTRACT(MONTH FROM date_sale)::INT AS month,       -- Extract month information from date_sale
		EXTRACT(DAY FROM date_sale)::INT AS day,           -- Extract day information from date_sale
		EXTRACT(DOW FROM date_sale)::INT AS weekday,       -- Extract weekday information from date_sale
		SUM(price) AS total_sales                          -- Sum sales using gruoping as GRoUP BY statement
	FROM
		sales.item_sale                              
	WHERE
		date_sale >= (CURRENT_DATE - INTERVAL :delta_year) -- Delta time used for get data
		AND 
		date_sale <= (CURRENT_DATE - INTERVAL :delta_day)    
	GROUP BY
		store_id,
		day,
		month,
		year,
		weekday;
	