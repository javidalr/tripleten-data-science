# Modelo de Predicción de Pedidos de Taxi

## Descripción del Proyecto

Trabajamos para una empresa de taxis llamada **Sweet Lift**, que ha recopilado datos históricos sobre pedidos de taxi en el aeropuerto. Nuestra tarea consiste en predecir el número de pedidos de taxi para la próxima hora, con el objetivo de atraer más conductores durante las horas punta. La meta es construir un modelo predictivo cuya métrica **RMSE** en el conjunto de prueba **no supere los 48**.

Este proyecto tiene como objetivos:
- Aplicar habilidades de procesamiento de series temporales en un proyecto del mundo real.
- Analizar las características de los datos para identificar patrones, tendencias y estacionalidad.
- Crear varios modelos de predicción.
- Elegir y recomendar el mejor modelo para su implementación.

## Descripción de los Datos

Los datos están almacenados en el archivo `taxi.csv`, y el número de pedidos está representado en la columna `num_orders`.
- `datetime` — contiene la secuencia de fechas y horas en que se obtuvieron los datos.
- `num_orders` — representa la cantidad de pedidos de taxi por unidad de tiempo.

## Etapas

Este proyecto se desarrollará en las siguientes etapas:
- Importación de archivos y formateo de los datos para el análisis de series temporales.
- Estudio de la información general de los datos y verificación de su calidad.
- Análisis exploratorio para comprender sus características.
- Creación de un modelo predictivo preciso.
- Prueba del modelo en un conjunto de datos de prueba separado.
- Elaboración de conclusiones y selección del mejor modelo para implementar.

## Librerías

- Pandas versión: 1.4.4  
- NumPy versión: 1.23.5  
- Matplotlib versión: 3.7.1  
- Seaborn versión: 0.12.2  
- Scikit-learn versión: 1.2.2  
- CatBoost versión: 1.1.1  
- LightGBM versión: 3.3.5  
- XGBoost versión: 1.7.3  
- Statsmodels versión: 0.13.5  
- Scipy versión: 1.10.1  
- Pmdarima versión: 1.8.5  
- Prophet versión: 1.0