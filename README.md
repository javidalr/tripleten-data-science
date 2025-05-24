## Introducción

La compañía de seguros Sure Tomorrow desea resolver varias tareas relacionadas con los beneficios de seguro de sus clientes. Este proyecto tiene como objetivo abordar dichas tareas mediante modelos de machine learning y proteger la privacidad de los datos personales de los clientes.

## Objetivo

Resolver las siguientes tareas solicitadas por la compañía de seguros Sure Tomorrow:

- Tarea 1: Encontrar clientes similares a uno dado. Esto ayudará a los agentes de la compañía en sus campañas de marketing.

- Tarea 2: Predecir si un nuevo cliente probablemente recibirá un beneficio de seguro. ¿Puede un modelo de predicción superar a un modelo base (dummy)?

- Tarea 3: Predecir cuántos beneficios de seguro recibirá un nuevo cliente usando un modelo de regresión lineal.

- Tarea 4: Proteger los datos personales de los clientes sin afectar el modelo de la tarea anterior. Es necesario desarrollar un algoritmo de transformación de datos que haga difícil recuperar información personal en caso de que los datos caigan en manos equivocadas. Esto se conoce como enmascaramiento de datos o ofuscación de datos. Sin embargo, los datos deben protegerse de manera que la calidad de los modelos de machine learning no se vea comprometida. No es necesario seleccionar el mejor modelo, solo demostrar que el algoritmo funciona correctamente.

## Datos

Descripción de los datos

- Características

Gender: Género de la persona asegurada

Age: Edad de la persona asegurada

Salary: Ingreso anual de la persona asegurada

Family members: Número de familiares de la persona asegurada

- Variable objetivo

Insurance benefits: Número de beneficios de seguro recibidos por la persona asegurada en los últimos cinco años

## Principales bibliotecas utilizadas

Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn