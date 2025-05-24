## Introducción

La empresa minera OilyGiant planea seleccionar una región para desarrollar nuevos pozos petroleros. Este proyecto tiene como objetivo elegir la región con el mayor margen de ganancia.

## Objetivo

- Desarrollar un modelo de machine learning que prediga el volumen de reservas en los nuevos pozos. Utilizando estas predicciones junto con la técnica de bootstrapping, se seleccionarán los pozos con los valores estimados más altos y la región con el mayor beneficio esperado.

## Datos

Descripción de los datos

- Características

id: Identificador único del pozo petrolero

f0, f1, f2: Tres características de los puntos (su significado específico no es importante, pero sí lo son para predecir el objetivo)

- Variable objetivo

product: Volumen de reservas en el pozo petrolero (en miles de barriles)

## Principales bibliotecas utilizadas

Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn