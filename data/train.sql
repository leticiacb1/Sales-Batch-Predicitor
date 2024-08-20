WITH vars AS (
    -- Create variables
     SELECT INTERVAL :delta_year AS year_interval, INTERVAL :end_day AS day_interval   
),
processed_item_sales AS (
    select
        store_id,
        SUM(price) AS total_sales,                         -- Sum sales using gruoping as GRoUP BY statement
        EXTRACT(YEAR FROM date_sale)::INT AS year,         -- Extract year information from date_sale 
        EXTRACT(MONTH FROM date_sale)::INT AS month,       -- Extract month information from date_sale
        EXTRACT(DAY FROM date_sale)::INT AS day,           -- Extract day information from date_sale
        EXTRACT(DOW FROM date_sale)::INT AS weekday        -- Extract weekday information from date_sale
    FROM
        sales.item_sale, vars                              
    WHERE
        date_sale >= (CURRENT_DATE - vars.year_interval)   -- Delta time used for get data
        AND 
        date_sale <= (CURRENT_DATE - vars.day_interval)    
    GROUP BY
        store_id,
        date_sale,
        day,
        month,
        year,
        weekday
)
SELECT * FROM processed_item_sales;