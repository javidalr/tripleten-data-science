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

- Pandas
- NumPy
- Matplotlib
- Seaborn
- NLTK
- Regex
- spaCy
- Scikit-learn
- CatBoost
- LightGBM
- XGBoost