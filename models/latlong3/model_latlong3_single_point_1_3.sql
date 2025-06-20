{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mbrjvs6c__latlong3__single_point_1_3",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH test_new_seed_with_date AS (

  SELECT * 
  
  FROM {{ ref('test_new_seed_with_date')}}

),

create_point_1_3 AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    CONCAT('POINT(', from_lon, ' ', from_lat, ')') AS from_wkt,
    CONCAT('POINT(', to_lon, ' ', to_lat, ')') AS to_wkt,
    distance_km AS distance_km,
    category AS category,
    date AS date,
    timestampNTZ AS timestampNTZ,
    time AS time,
    date_field AS date_field,
    customer_count AS customer_count,
    sales_amount AS sales_amount,
    growth_rate AS growth_rate
  
  FROM test_new_seed_with_date AS in0

),

points_1_3 AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    from_wkt AS from_wkt,
    date AS date
  
  FROM create_point_1_3 AS in0

),

single_point_1_3 AS (

  SELECT * 
  
  FROM points_1_3 AS in0
  
  LIMIT 1

)

SELECT *

FROM single_point_1_3
