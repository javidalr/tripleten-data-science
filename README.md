# Modelo de Verificación de Edad

## Descripción del Proyecto

**Good Seed**, una cadena de supermercados, ha iniciado un proyecto para explorar la aplicación de la Ciencia de Datos con el objetivo de cumplir con las leyes de restricción por edad. Buscan asegurarse de no vender productos restringidos por edad a clientes menores de edad.

La empresa ha equipado sus tiendas con cámaras en el área de cajas, las cuales pueden detectar productos con restricción de edad durante las transacciones. Para verificar la edad de una persona, planean emplear técnicas de visión por computadora capaces de determinar la edad de un individuo a partir de una fotografía.

Este proyecto fue desarrollado en la plataforma de **TripleTen**, utilizando sus recursos de GPU para acelerar el proceso de aprendizaje automático. A continuación, se presentan los resultados obtenidos.

## Objetivo

El objetivo de este proyecto es construir y evaluar un modelo que pueda verificar con precisión la edad de una persona basándose en las fotografías capturadas por las cámaras en la zona de cajas. Con ello, **Good Seed** busca garantizar el cumplimiento de las normativas legales, evitar ventas a menores de edad y respetar los requisitos legales.

EL proyecto consiste en construir y entrenar una red neuronal convolucional en una plataforma con GPU, utilizando un conjunto de datos con fotografías humanas. El objetivo es lograr una puntuación **MAE** menor o igual a **8** en el conjunto de prueba.

## Descripción de los Datos

Los conjuntos de datos requeridos están almacenados en la carpeta `/datasets/faces/` de la plataforma de Tripleten, e incluyen:

- La carpeta `final_file` que contiene aproximadamente 7.600 fotografías.
- El archivo `labels.csv`, que contiene las etiquetas correspondientes para las imágenes, con dos columnas: `file_name` y `real_age`.

Debido a la gran cantidad de archivos de imagen, no se recomienda cargarlos todos simultáneamente, ya que podría consumir demasiados recursos computacionales. En su lugar, se recomienda utilizar `ImageDataGenerator` para crear un generador.

El archivo de etiquetas `labels.csv` se puede cargar fácilmente como un archivo CSV común, lo cual permite acceder cómodamente a las etiquetas asociadas para su posterior procesamiento y análisis.

## Etapas

Este proyecto se desarrollará en las siguientes etapas:

- Importar las librerías de visión por computadora y cargar los datos disponibles.
- Realizar análisis exploratorio de datos, incluyendo estadísticas descriptivas, visualización de muestras, análisis de aumento de datos, distribución de clases y calidad de imágenes.
- Continuar con la fase de modelado, creando funciones para ejecutarse en la plataforma con GPU de Tripleten.
- Desarrollar scripts de código basados en dichas funciones para ser ejecutadas en la plataforma.
- Registrar los resultados obtenidos desde la plataforma GPU en celdas Markdown.

## Librerías

- Pandas
- Matplotlib
- Seaborn
- TensorFlow

## Este proyecto no se logro concluir por problemas técnicos de GPU