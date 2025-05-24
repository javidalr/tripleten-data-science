## Introducción

Los clientes de Beta Bank están abandonando el banco poco a poco cada mes. Los ejecutivos del banco han identificado que es más rentable retener a los clientes actuales que atraer nuevos. Este proyecto tiene como objetivo construir un modelo para predecir si un cliente dejará el banco próximamente.

## Objetivo

- Desarrollar un modelo de clasificación binaria que analice los datos sobre el comportamiento pasado de los clientes y la finalización de contratos, con el fin de identificar a los clientes que probablemente se irán.

- El modelo debe alcanzar una puntuación F1 de al menos 59%, según lo solicitado por Beta Bank.

## Datos

Descripción de los datos

- Características

RowNumber: Índice de la fila en el conjunto de datos

CustomerId: Identificador único del cliente

Surname: Apellido

CreditScore: Puntuación crediticia

Geography: País de residencia

Gender: Género

Age: Edad

Tenure: Tiempo de permanencia del depósito a plazo fijo (años)

Balance: Saldo de la cuenta

NumOfProducts: Número de productos bancarios utilizados por el cliente

HasCrCard: Indica si el cliente tiene tarjeta de crédito

IsActiveMember: Nivel de actividad del cliente

EstimatedSalary: Salario estimado

- Variable objetivo

Exited: Indica si el cliente abandonó el banco

## Principales bibliotecas utilizadas

Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn