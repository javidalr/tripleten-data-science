## Introducción

El proveedor de servicios de venta de autos usados Rusty Bargain planea desarrollar una aplicación para atraer nuevos clientes. La app permitirá a los usuarios conocer rápidamente el valor de mercado de sus vehículos.

## Objetivo

Este proyecto tiene como objetivo construir un modelo de regresión para predecir los precios de los autos. El rendimiento del modelo debe evaluarse según los siguientes criterios establecidos por Rusty Bargain:

- La calidad de la predicción

- La velocidad de la predicción

- El tiempo requerido para el entrenamiento

## Datos

Descripción de los datos

- Características

DateCrawled: Fecha en que el perfil fue descargado de la base de datos

VehicleType: Tipo de carrocería del vehículo

RegistrationYear: Año de registro del vehículo

Gearbox: Tipo de caja de cambios

Power: Potencia del motor (caballos de fuerza)

Model: Modelo del vehículo

Mileage: Kilometraje (medido en km según especificaciones regionales del conjunto de datos)

RegistrationMonth: Mes de registro del vehículo

FuelType: Tipo de combustible (gasolina, diésel, etc.)

Brand: Marca del vehículo

NotRepaired: Indica si el vehículo ha sido reparado o no

DateCreated: Fecha de creación del perfil

NumberOfPictures: Número de fotos del vehículo

PostalCode: Código postal del propietario del perfil (usuario)

LastSeen: Fecha de la última actividad del usuario

- Variable objetivo

Price: Precio (en euros) del vehículo

## Principales bibliotecas utilizadas

Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, XGBoost, CatBoost, LightGBM