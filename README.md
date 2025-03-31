# Modelo de Machine Learning para planes de telecomunicaciones - Proyecto 08

## Descripción del Proyecto

Este proyecto es una continuación de nuestro trabajo previo en el Proyecto 4: Análisis Estadístico de Datos. Aquí, seguimos colaborando con Megaline, un operador móvil, para abordar su preocupación sobre los clientes que continúan utilizando planes antiguos.

La empresa desea desarrollar un modelo capaz de analizar el comportamiento del consumidor y proporcionar recomendaciones personalizadas para los dos nuevos planes de Megaline: Smart y Ultra.

Los objetivos de este proyecto incluyen:

Analizar los patrones de comportamiento de los clientes de Megaline que ya han cambiado al nuevo paquete.

Desarrollar modelos de aprendizaje automático para estudiar el comportamiento de estos usuarios.

Utilizar los modelos para proporcionar recomendaciones de paquetes adecuadas a los clientes que aún no han adoptado el nuevo plan.

## Descripción de los Datos
Para construir este modelo, utilizaremos los datos preprocesados disponibles en el archivo users_behavior.csv.

Cada observación en el conjunto de datos proporciona información mensual sobre el comportamiento de un usuario, incluyendo las siguientes variables:

calls: número de llamadas realizadas por el usuario

minutes: duración total de las llamadas en minutos

messages: número de mensajes de texto enviados por el usuario

mb_used: cantidad de tráfico de internet consumido en megabytes (MB)

is_ultra: paquete suscrito por el usuario en el mes actual (Ultra = 1, Smart = 0)

Etapas
Habiendo realizado previamente un análisis estadístico de los datos de los clientes de Megaline en el Proyecto 4, ahora pasamos directamente a la etapa de modelado, asumiendo que el paso de preprocesamiento de datos ya está completado.

El objetivo de esta tarea de clasificación es desarrollar un modelo que pueda recomendar con precisión el paquete adecuado para los clientes de Megaline que aún no han cambiado al nuevo plan.

Nuestro objetivo es crear un modelo con la mayor precisión posible, con un mínimo de 0.75 de accuracy como umbral para este proyecto.

## Librerías

- Pandas
- NumPy
- Scikit-learn
