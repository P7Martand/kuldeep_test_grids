{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mbz0tvui__latlog_test2__create_point_1_1",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH dataLatLong_csv_1 AS (

  SELECT * 
  
  FROM {{ source('prophecy_tmp_source__latlog_test2', 'prophecy_tmp__mbz0tvui__latlog_test2__dataLatLong_csv_1') }}

),

create_point_1_1 AS (

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
  
  FROM dataLatLong_csv_1 AS in0

)

SELECT *

FROM create_point_1_1
