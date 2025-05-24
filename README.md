# Soluciones de Machine Learning para Seguros

[Notebook del Proyecto](https://github.com/emanuelcaesario/practicum-projects/blob/Project-11-Linear-Algebra/Project%2011%20Linear%20Algebra.ipynb)

## Resumen del Proyecto

Este proyecto muestra aplicaciones prácticas del álgebra lineal, combinando su belleza matemática con tareas del mundo real. El objetivo principal es demostrar la **precisión del algoritmo**, más que seleccionar el mejor modelo. La plantilla del proyecto incluye código inicial y descripciones de tareas que no deben eliminarse, junto con dos apéndices con información útil.

En este proyecto, una aseguradora llamada **"Sure Tomorrow"** busca soluciones de *machine learning* para diversas tareas:

- **Tarea 1: Perfilado de clientes** – Encontrar clientes similares según criterios específicos para marketing efectivo.  
- **Tarea 2: Predicción de reclamos** – Determinar si nuevos clientes es probable que hagan reclamos al seguro, y comparar el modelo con un modelo dummy.  
- **Tarea 3: Regresión** – Predecir la cantidad de reclamos de seguro que pueden recibir nuevos clientes utilizando regresión lineal.  
- **Tarea 4: Protección de privacidad de datos** – Desarrollar algoritmos de transformación de datos para ocultar o enmascarar la información privada de los clientes, manteniendo la precisión del modelo. El objetivo es prevenir el uso indebido o acceso no autorizado a los datos personales sin comprometer el rendimiento del modelo.

## Descripción de los Datos

El conjunto de datos se encuentra en el archivo `insurance_us.csv`. A continuación se describen las variables:

- **Características:**
  - `Gender`: Género de la persona asegurada (por ejemplo, masculino o femenino).
  - `Age`: Edad de la persona asegurada (valor numérico).
  - `Income`: Ingreso de la persona asegurada (valor numérico).
  - `Family Members`: Número de miembros de la familia cubiertos por el seguro.

- **Variable objetivo:**
  - `Insurance Benefits`: Monto de beneficios recibidos por el asegurado durante los últimos cinco años. Representa los reclamos recibidos de la compañía de seguros.

## Etapas

El proyecto abarcará las siguientes etapas:

1. **Carga e Inicialización de Datos:**
   - Cargar el conjunto de datos desde el archivo `insurance_us.csv`.
   - Explorar el conjunto de datos para comprender su estructura y contenido.
   - Verificar valores faltantes, tipos de datos y estadísticas básicas.

2. **Análisis Exploratorio de Datos (EDA):**
   - Analizar las relaciones entre las características y la variable objetivo (`insurance_benefits`).
   - Identificar patrones o correlaciones mediante visualizaciones.

3. **Tarea 1 - Clientes Similares:**
   - Crear una función que muestre los *k-nearest neighbors* para el objeto n utilizando una métrica de distancia específica.

4. **Tarea 2 - Predicción de Reclamos de Seguro:**
   - Evaluar si el modelo de clasificación kNN supera al modelo dummy para predecir la aceptación de reclamos.

5. **Tarea 3 - Regresión (con Regresión Lineal):**
   - Utilizando `insurance_benefits` como variable objetivo, evaluar el **RMSE** (Root Mean Squared Error) del modelo de regresión lineal.

6. **Tarea 4 - Ofuscación de Datos:**
   - Aplicar ofuscación multiplicando las características numéricas (matriz 𝑋) por una matriz invertible 𝑃.
   - Demostrar la efectividad de la ofuscación con regresión lineal.

7. **Prueba de Regresión Lineal con Datos Ofuscados:**
   - Evaluar el rendimiento y la precisión del modelo con datos ofuscados.

## Librerías

- Pandas versión: 1.4.4  
- NumPy versión: 1.23.5  
- Matplotlib versión: 3.7.1  
- Seaborn versión: 0.12.2  
- Scikit-learn versión: 1.2.2