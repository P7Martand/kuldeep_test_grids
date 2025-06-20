{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mbz0tvui__latlog_test2__single_point_1",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH create_point_gem_seed_3 AS (

  SELECT * 
  
  FROM {{ source('sony.orch_test', 'create_point_gem_seed') }}

),

create_point_1 AS (

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
  
  FROM create_point_gem_seed_3 AS in0

),

points_1 AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    from_wkt AS from_wkt,
    Alteryx_Distance_KM AS Alteryx_Distance_KM,
    Formula_Distance_KM AS Formula_Distance_KM,
    Difference_Alteryx_KM_2 AS Difference_Alteryx_KM_2,
    h3_approx_distance AS h3_approx_distance,
    Difference_Alteryx_KM AS Difference_Alteryx_KM
  
  FROM create_point_1 AS in0

),

single_point_1 AS (

  SELECT * 
  
  FROM points_1 AS in0
  
  LIMIT 1

)

SELECT *

FROM single_point_1
