{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mbz0tvui__latlog_test2__single_point_1_1",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH test_seed AS (

  SELECT * 
  
  FROM {{ ref('test_seed')}}

),

create_point_1_2 AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    CONCAT('POINT(', from_lon, ' ', from_lat, ')') AS from_wkt,
    CONCAT('POINT(', to_lon, ' ', to_lat, ')') AS to_wkt,
    distance_km AS distance_km,
    growth_rate AS growth_rate
  
  FROM test_seed AS in0

),

points_1_1 AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    from_wkt AS from_wkt,
    to_wkt AS to_wkt,
    distance_km AS distance_km,
    growth_rate AS growth_rate
  
  FROM create_point_1_2 AS in0

),

single_point_1_1 AS (

  SELECT * 
  
  FROM points_1_1 AS in0
  
  LIMIT 1

)

SELECT *

FROM single_point_1_1
