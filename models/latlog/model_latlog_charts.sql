{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mc001kf5__latlog__charts",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH create_point AS (

  SELECT * 
  
  FROM {{ source('prophecy_tmp_source__latlog', 'prophecy_tmp__mc001kf5__latlog__create_point') }}

),

charts AS (

  SELECT 
    seq AS seq,
    from_city AS from_city,
    to_city AS to_city,
    Alteryx_Distance_KM AS Alteryx_Distance_KM,
    Formula_Distance_KM AS Formula_Distance_KM,
    Difference_Alteryx_KM_2 AS Difference_Alteryx_KM_2,
    h3_approx_distance AS h3_approx_distance,
    Difference_Alteryx_KM AS Difference_Alteryx_KM
  
  FROM create_point AS in0

)

SELECT *

FROM charts
