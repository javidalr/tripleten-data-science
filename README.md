# Análisis de la Compañía de Taxis - Proyecto 07

## Descripción del Proyecto

En la fase inicial, los datos meteorológicos de Chicago, fueron extraidos desde el sitio web: https://code.s3.yandex.net/data-analyst-eng/chicago_weather_2017.html. Posteriormente, se realiza un análisis exploratorio de datos utilizando SQL en la base de datos de Tripleten para extraer los datos necesarios para el análisis.

Para este estudio, es una empresa de transporte compartido en Chicago. El objetivo es descubrir patrones dentro de los datos disponibles y obtener información sobre las preferencias de los pasajeros y la influencia de factores externos en el comportamiento de viaje.

Con la base de datos proporcionados, se estudian datos de la competencia y se realizan pruebas de hipótesis para evaluar el impacto de las condiciones climáticas en la frecuencia de los viajes.

## Descripción de los datos

### project_sql_result_01.csv

Este conjunto de datos contiene información sobre la cantidad de viajes por compañía.

company_name: Nombre de la compañía de taxis.

trips_amount: Número total de viajes realizados por cada compañía de taxis durante el 15 y 16 de noviembre de 2017.

### project_sql_result_04.csv

Este conjunto de datos contiene información sobre el número promedio de viajes que terminan en diferentes zonas de Chicago.

dropoff_location_name: Nombre del área de Chicago donde finalizó el viaje.

average_trips: Número promedio de viajes que terminaron en cada zona durante noviembre de 2017.

### project_sql_result_07.csv

Este conjunto de datos contiene información sobre viajes desde The Loop hacia el Aeropuerto Internacional O'Hare.

start_ts: Fecha y hora de recogida.

weather_conditions: Condiciones climáticas al inicio del viaje.

duration_seconds: Duración del viaje en segundos.

## Hipótesis

- H0 (Hipótesis nula): La duración promedio de los viajes desde The Loop hacia el Aeropuerto O'Hare permanece igual los sábados lluviosos.

- H1 (Hipótesis alternativa): La duración promedio de los viajes desde The Loop hacia el Aeropuerto O'Hare cambia los sábados lluviosos.

## Librerías

- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
