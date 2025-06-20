{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mc001kf5__latlog__distance_comparison",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH create_point AS (

  SELECT * 
  
  FROM {{ source('prophecy_tmp_source__latlog', 'prophecy_tmp__mc001kf5__latlog__create_point') }}

),

distance AS (

  SELECT * 
  
  FROM create_point AS in0

),

points AS (

  SELECT * 
  
  FROM {{ source('prophecy_tmp_source__latlog', 'prophecy_tmp__mc001kf5__latlog__points') }}

),

distance_comparison AS (

  SELECT 
    in1.seq AS seq,
    in1.from_city AS from_city,
    in1.to_city AS to_city,
    in1.from_wkt AS from_wkt,
    in1.Alteryx_Distance_KM AS Alteryx_Distance_KM,
    in1.Formula_Distance_KM AS Formula_Distance_KM,
    in1.Difference_Alteryx_KM_2 AS Difference_Alteryx_KM_2,
    in1.h3_approx_distance AS h3_approx_distance,
    in1.Difference_Alteryx_KM AS Difference_Alteryx_KM,
    in0.seq AS seq1,
    in0.from_city AS from_city1,
    in0.to_city AS to_city1,
    in0.from_wkt AS from_wkt1,
    in0.to_wkt AS to_wkt1,
    in0.Alteryx_Distance_KM AS Alteryx_Distance_KM1,
    in0.Formula_Distance_KM AS Formula_Distance_KM1,
    in0.Difference_Alteryx_KM_2 AS Difference_Alteryx_KM_21,
    in0.h3_approx_distance AS h3_approx_distance1,
    in0.Difference_Alteryx_KM AS Difference_Alteryx_KM1
  
  FROM distance AS in0
  INNER JOIN points AS in1
     ON true

)

SELECT *

FROM distance_comparison
