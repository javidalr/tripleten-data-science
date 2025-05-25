# Modelo de ML para Planes de Telecomunicaciones

## Resumen del Proyecto

Este proyecto, es una continuación del trabajo revio en el **Proyecto 4: Análisis Estadístico de Datos**. En esta ocasión, se sigue colaborando con **Megaline**, una operadora móvil que desea abordar el problema de clientes que continúan utilizando paquetes antiguos.

La empresa busca desarrollar un modelo capaz de analizar el comportamiento de los usuarios y ofrecer recomendaciones personalizadas entre los dos nuevos paquetes de Megaline: **Smart** y **Ultra**.

Los objetivos de este proyecto incluyen:

- Analizar los patrones de comportamiento de los clientes que ya migraron al nuevo paquete.  
- Desarrollar modelos de *machine learning* para estudiar el comportamiento de estos usuarios.  
- Utilizar los modelos para recomendar el paquete adecuado a los clientes que aún no han actualizado su plan.

## Descripción de los Datos

Para construir este modelo, se utilizaran los datos ya preprocesados contenidos en el archivo `users_behavior.csv`.

Cada observación en el conjunto de datos representa información mensual sobre el comportamiento de un usuario individual, incluyendo las siguientes variables:

- `calls`: número de llamadas realizadas por el usuario  
- `minutes`: duración total de las llamadas en minutos  
- `messages`: número de mensajes de texto enviados  
- `mb_used`: cantidad de tráfico de internet usado (en megabytes)  
- `is_ultra`: paquete contratado por el usuario ese mes (Ultra = 1, Smart = 0)

## Etapas

El análisis estadístico se realizó en el Proyecto 4, por ello, se aplicará directamente la etapa de modelado, asumiendo que el preprocesamiento ya esta realizado.

El objetivo de esta tarea de clasificación, es desarrollar un modelo que pueda recomendar con precisión el plan adecuado para los clientes de Megaline que aún no han cambiado a uno de los paquetes más recientes.

La meta es lograr **la mayor precisión posible**, con un umbral mínimo de **0.75 de accuracy** para este proyecto.

## Librerías

- Pandas  
- NumPy
- Scikit-learn