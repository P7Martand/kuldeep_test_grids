{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mc001kf5__latlog__single_point",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH points AS (

  SELECT * 
  
  FROM {{ source('prophecy_tmp_source__latlog', 'prophecy_tmp__mc001kf5__latlog__points') }}

),

single_point AS (

  SELECT * 
  
  FROM points AS in0
  
  LIMIT 1

)

SELECT *

FROM single_point
