# Análisis de Ubicación para Pozos Petroleros

## Resumen del Proyecto

**OilyGiant**, una empresa de extracción de petróleo, busca expandir su exploración a nuevas ubicaciones. Nuestra tarea es encontrar una ubicación adecuada para perforar un nuevo pozo petrolero. Para lograrlo, desarrollaremos un modelo de *machine learning* que ayude a identificar la ubicación óptima para futuras exploraciones.

Se nos ha proporcionado información de muestras de petróleo de tres regiones, incluyendo parámetros de cada pozo en esas zonas. El objetivo es construir un modelo que ayude a la empresa a seleccionar la región con el mayor margen de beneficio. Para ello, realizaremos un análisis de ganancias y riesgos potenciales utilizando técnicas de *bootstrapping*.

Los pasos a seguir para seleccionar la nueva ubicación son los siguientes:

1. Recolectar parámetros relacionados con la calidad del petróleo y el volumen de reservas en las áreas seleccionadas.  
2. Desarrollar un modelo capaz de predecir el volumen de reservas en nuevos pozos.  
3. Determinar los pozos con mayor valor estimado.  
4. Elegir la región que ofrezca el mayor beneficio total con base en los pozos seleccionados.

El objetivo de este proyecto es identificar nuevas ubicaciones de extracción que ofrezcan **los márgenes de ganancia más altos** para la empresa.

## Descripción de los Datos

Los datos proporcionados para este proyecto son artificiales y no contienen detalles contractuales ni características específicas de los pozos. La información de exploración geológica de las tres regiones está almacenada en archivos separados:
- `geo_data_0.csv`
- `geo_data_1.csv`
- `geo_data_2.csv`

**Características:**
- `id` – ID único del pozo  
- `f0`, `f1`, `f2` – tres características numéricas del pozo (el significado específico no es relevante, pero son útiles para el modelo)

**Variable objetivo:**
- `product` – volumen de reservas de petróleo en el pozo (en miles de barriles)

**Condiciones:**
- Solo se puede usar regresión lineal para entrenar el modelo, ya que otros algoritmos no son adecuados para la predicción.  
- En la exploración de cada región se analizan 500 puntos y se seleccionan los 200 mejores para el cálculo de beneficios.  
- El presupuesto para desarrollar 200 pozos es de **100 millones de USD**.  
- Los ingresos por un barril de crudo son de **4.5 USD**, por lo que un valor unitario de `product` (mil barriles) equivale a **4.500 USD**.  
- Solo se consideran regiones con un **riesgo de pérdida inferior al 2.5%**. Entre las elegibles, se elige la que tenga el **mayor beneficio promedio**.

## Etapas

Este proyecto se llevará a cabo en varias fases:

- Preparación de los datos  
- Entrenamiento y prueba del modelo para cada región  
- Cálculo estimado de ganancias  
- Desarrollo de una función para calcular ganancias basadas en pozos seleccionados y predicciones del modelo  
- Evaluación de riesgos y ganancias potenciales para cada región

## Librerías

- Pandas versión: 1.4.4  
- NumPy versión: 1.23.5  
- Matplotlib versión: 3.7.1  
- Seaborn versión: 0.12.2  
- Scikit-learn versión: 1.2.2