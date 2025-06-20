{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mbz0tvui__latlog_test2__single_point_1_2",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH create_point_1_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy_tmp_source__latlog_test2', 'prophecy_tmp__mbz0tvui__latlog_test2__create_point_1_1') }}

),

points_1_2 AS (

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
  
  FROM create_point_1_1 AS in0

),

single_point_1_2 AS (

  SELECT * 
  
  FROM points_1_2 AS in0
  
  LIMIT 1

)

SELECT *

FROM single_point_1_2
