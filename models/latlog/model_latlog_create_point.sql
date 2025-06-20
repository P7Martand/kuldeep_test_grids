{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mc001kf5__latlog__create_point",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH raw_points AS (

  SELECT * 
  
  FROM {{ ref('create_point_gem_seed')}}

),

create_point AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    CONCAT('POINT(', from_lon, ' ', from_lat, ')') AS from_wkt,
    CONCAT('POINT(', to_lon, ' ', to_lat, ')') AS to_wkt,
    Alteryx_Distance_KM AS Alteryx_Distance_KM,
    Formula_Distance_KM AS Formula_Distance_KM,
    Difference_Alteryx_KM_2 AS Difference_Alteryx_KM_2,
    h3_approx_distance AS h3_approx_distance,
    Difference_Alteryx_KM AS Difference_Alteryx_KM
  
  FROM raw_points AS in0

)

SELECT *

FROM create_point
