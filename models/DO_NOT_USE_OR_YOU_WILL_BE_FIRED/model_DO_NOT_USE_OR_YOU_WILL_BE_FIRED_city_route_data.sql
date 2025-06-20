{{
  config({    
    "materialized": "table",
    "alias": "prophecy_tmp__mbrjvhe7__DO_NOT_USE_OR_YOU_WILL_BE_FIRED__city_route_data",
    "database": "sony",
    "schema": "orch_test"
  })
}}

WITH route_data AS (

  SELECT * 
  
  FROM {{ ref('route_data')}}

),

city_information AS (

  SELECT * 
  
  FROM {{ ref('city_data')}}

),

high_gdp_cities_1 AS (

  SELECT * 
  
  FROM city_information
  
  WHERE GDP_billion_USD > 30

),

city_pairs AS (

  SELECT 
    h2.city AS h2_city,
    h1.city AS h1_city
  
  FROM high_gdp_cities_1 AS h1
  CROSS JOIN high_gdp_cities_1 AS h2

),

different_city_pairs AS (

  SELECT * 
  
  FROM city_pairs
  
  WHERE h1_city <> h2_city

),

city_combinations AS (

  SELECT 
    h1_city AS city1,
    h2_city AS city2
  
  FROM different_city_pairs

),

city_route_mappings AS (

  SELECT 
    cc.city2 AS cc_city2,
    rd.from_city AS rd_from_city,
    rd.to_city AS rd_to_city,
    cc.city1 AS cc_city1
  
  FROM city_combinations AS cc
  LEFT JOIN route_data AS rd
     ON cc.city1 = rd.from_city AND cc.city2 = rd.to_city

),

missing_route_data AS (

  SELECT * 
  
  FROM city_route_mappings
  
  WHERE rd_from_city IS NULL AND rd_to_city IS NULL

),

city_combinations_not_in_routes AS (

  SELECT 
    cc_city1 AS city1,
    cc_city2 AS city2
  
  FROM missing_route_data

),

airport_information AS (

  SELECT * 
  
  FROM {{ ref('airport')}}

),

enriched_city_combinations AS (

  SELECT 
    ccnir.city1,
    ccnir.city2,
    a1.airport_name AS city1_airport,
    a2.airport_name AS city2_airport,
    CONCAT('POINT(', a1.longitude, ' ', a1.latitude, ')') AS city1_wkt_point,
    CONCAT('POINT(', a2.longitude, ' ', a2.latitude, ')') AS city2_wkt_point
  
  FROM city_combinations_not_in_routes AS ccnir
  JOIN airport_information AS a1
     ON ccnir.city1 = a1.city
  JOIN airport_information AS a2
     ON ccnir.city2 = a2.city

),

unique_city_routes AS (

  SELECT 
    city1,
    city1_wkt_point,
    COUNT(DISTINCT city2) AS UNIQUE_ROUTES
  
  FROM enriched_city_combinations
  
  GROUP BY 
    city1, city1_wkt_point

),

city_route_data AS (

  SELECT 
    city1 AS ORIGIN_CITY,
    city1_wkt_point AS ORIGIN_CITY_WKT_POINT,
    UNIQUE_ROUTES AS TOTAL_UNIQUE_ROUTES
  
  FROM unique_city_routes

)

SELECT *

FROM city_route_data
