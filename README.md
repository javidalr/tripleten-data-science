# Análisis de Sentimientos en Reseñas de Películas

## Descripción del Proyecto

**Film Junky Union**, una nueva comunidad para fanáticos del cine clásico, está desarrollando un sistema para filtrar y categorizar reseñas de películas. El objetivo es entrenar un modelo capaz de detectar automáticamente reseñas negativas. Nuestra tarea consiste en utilizar el conjunto de datos de reseñas de películas de **IMDB** con etiquetas de polaridad, y crear un modelo que clasifique con precisión las reseñas como positivas o negativas. La meta establecida para este modelo es alcanzar una puntuación **F1 de al menos 0.85**.

## Descripción de los Datos

Los datos están almacenados en el archivo `imdb_reviews.tsv`.

Este conjunto de datos fue recopilado por Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng y Christopher Potts. (2011). *Learning Word Vectors for Sentiment Analysis*. The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).

A continuación, se describen las columnas seleccionadas:

- `review` — texto de la reseña  
- `pos` — variable objetivo, '0' para negativo y '1' para positivo  
- `ds_part` — 'train'/'test' indica si pertenece al conjunto de entrenamiento o prueba  

Estas tres columnas son el foco principal de esta tarea, aunque el conjunto de datos contiene otras columnas adicionales.

## Etapas

Este proyecto se llevará a cabo en las siguientes etapas:

1. Cargar y estudiar los datos.  
2. Realizar un preprocesamiento inicial.  
3. Realizar análisis exploratorio de datos (EDA) y tratar el desbalance de clases.  
4. Preprocesar los datos para prepararlos para el modelado.  
5. Entrenar al menos tres modelos utilizando el conjunto de entrenamiento.  
6. Evaluar los modelos usando el conjunto de prueba.  
7. Escribir reseñas adicionales y clasificarlas con todos los modelos.  
8. Analizar y comparar los resultados de las pruebas de los modelos, explicando las diferencias observadas.

## Librerías

- Pandas versión: 1.4.4  
- NumPy versión: 1.23.5  
- Matplotlib versión: 3.7.1  
- Seaborn versión: 0.12.2  
- NLTK versión: 3.7  
- Regex versión: 2.2.1  
- spaCy versión: 3.3.1  
- Scikit-learn versión: 1.2.2  
- CatBoost versión: 1.1.1  
- LightGBM versión: 3.3.5  
- XGBoost versión: 1.7.3