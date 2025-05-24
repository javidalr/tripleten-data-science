# Modelo de Precio de Autos

## Resumen del Proyecto

Nuestra tarea consiste en ayudar a **Rusty Bargain**, una empresa dedicada a la compra y venta de autos usados, con el desarrollo de una app para atraer nuevos compradores. La app permitirá a los usuarios que deseen vender su auto conocer rápidamente su valor de mercado.

Para lograrlo, contamos con acceso a datos históricos, especificaciones técnicas de diversos vehículos, diferentes versiones de modelos y sus precios correspondientes. Nuestro objetivo principal es crear un modelo que prediga con precisión el valor de mercado de estos autos.

Factores clave de interés para Rusty Bargain incluyen:
- la calidad de la predicción  
- la velocidad del modelo de predicción  
- el tiempo requerido para entrenar el modelo  

## Descripción de los Datos

Los datos están almacenados en el archivo `car_data.csv`.

**Características**
- `DateCrawled`: Fecha en que el perfil fue descargado de la base de datos.  
- `VehicleType`: Tipo de carrocería del vehículo.  
- `RegistrationYear`: Año de registro del vehículo.  
- `Gearbox`: Tipo de transmisión.  
- `Power`: Potencia del vehículo (en caballos de fuerza).  
- `Model`: Modelo del vehículo.  
- `Mileage`: Kilometraje del vehículo (en kilómetros, según el origen regional de los datos).  
- `RegistrationMonth`: Mes de registro del vehículo.  
- `FuelType`: Tipo de combustible utilizado.  
- `Brand`: Marca del vehículo.  
- `NotRepaired`: Indica si el vehículo ha sido reparado previamente.  
- `DateCreated`: Fecha de creación del perfil.  
- `NumberOfPictures`: Número de imágenes disponibles del vehículo.  
- `PostalCode`: Código postal del propietario del perfil (usuario).  
- `LastSeen`: Fecha de la última actividad del usuario.  

**Variable Objetivo**
- `Price`: Precio del vehículo (en euros).  

## Etapas

El proyecto se desarrollará en las siguientes etapas:

1. **Recolección de Datos**  
   - Reunir datos históricos sobre autos usados desde diversas fuentes.  
   - Recopilar información sobre especificaciones técnicas, versiones de modelos y precios.  
   - Almacenar los datos obtenidos en el archivo `/datasets/car_data.csv`.

2. **Análisis de Datos**  
   - Explorar las características y estructura de los datos para obtener información general.  
   - Identificar características irrelevantes para eliminarlas.  
   - Abordar valores cero y valores atípicos en ciertas columnas.  
   - Eliminar duplicados y completar valores faltantes con 'unknown'.

3. **Preprocesamiento de Datos**  
   - Preparar dos conjuntos de datos: `df` y `df_new` para diferentes enfoques de modelado.  
   - Codificar variables categóricas mediante One-Hot Encoding en el conjunto `df`.  
   - Escalar características numéricas para estandarizarlas.

4. **Selección y Entrenamiento de Modelos**  
   - Entrenar y evaluar varios modelos de machine learning, incluyendo:  
     - Regresión Lineal  
     - Árbol de Decisión  
     - Bosque Aleatorio  
     - XGBoost Regressor  
     - LightGBM Regressor  
     - CatBoost Regressor  
   - Utilizar técnicas de validación cruzada para evaluar los modelos.  
   - Ajustar hiperparámetros mediante `RandomizedSearchCV` para optimizar el rendimiento de cada modelo.

5. **Evaluación del Modelo**  
   - Comparar el rendimiento de cada modelo en base al RMSE (Root Mean Squared Error) y tiempos de entrenamiento.  
   - Identificar el mejor modelo que logre un equilibrio entre precisión y velocidad de entrenamiento.

6. **Conclusión**  
   - Resumir los hallazgos y observaciones de la evaluación de modelos.  
   - Recomendar el modelo más adecuado (**CatBoost Regressor**) para Rusty Bargain en función de los criterios de calidad de predicción, velocidad y tiempo de entrenamiento.

## Librerías

- Pandas versión: 1.4.4  
- NumPy versión: 1.23.5  
- Matplotlib versión: 3.7.1  
- Seaborn versión: 0.12.2  
- Scikit-learn versión: 1.2.2  
- CatBoost versión: 1.1.1  
- LightGBM versión: 3.3.5  
- XGBoost versión: 1.7.3