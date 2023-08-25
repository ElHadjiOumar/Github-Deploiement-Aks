/*
    Welcome to your gold dbt model!
    Temperature, humidity, and wind speed.
*/

{{ config(materialized='table') }}

with silver_data as (

    SELECT
      dt,
      main_temp,
      main_humidity,
      wind_speed
    FROM  {{ source('sourcesilver', 'weathersil') }}

)

select 
    dt,
    main_temp,
    main_humidity,
    wind_speed
from silver_data
