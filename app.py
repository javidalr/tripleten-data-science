import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")


st.title("Análisis de Precios de Vehículos")

# Información Preliminar ============================================================================================

st.header("1.Información Preliminar")

st.subheader("1.1.Carga y Exploración de Datos")

if 'data' not in st.session_state:
    st.session_state.data = pd.read_csv('vehicles_us.csv')

data = st.session_state.data

option = st.checkbox('Muestra de dataset')
if option:
    st.dataframe(data, use_container_width=True)

st.subheader("1.2.Nombre de las Variables")
st.write(data.columns)

st.subheader("1.3.Tamaño del Dataset")
st.write(data.shape)

st.subheader("1.4.Descripción Estadística")
st.write(data.describe())

st.subheader("1.4.Tramiento de Valores Ausentes")
st.write('Antes',data.isna().sum())
data['is_4wd'] = data['is_4wd'].where(data['is_4wd'] == 1, 0).astype('bool')
data['paint_color'] = data['paint_color'].fillna('unknown')
data.dropna(inplace=True)
data.reset_index(drop=True, inplace=True)
st.write('Despues',data.isna().sum())


st.subheader("1.5.Features Engineering")
data['model_year'] = pd.to_numeric(data['model_year'], errors='coerce').astype('Int64')
data['cylinders'] = pd.to_numeric(data['cylinders'], errors='coerce').astype('Int64')
data['odometer'] = pd.to_numeric(data['odometer'], errors='coerce').astype('Int64')
data['date_posted'] = pd.to_datetime(data['date_posted'], format='%Y-%m-%d', errors='coerce')

data['day_posted'] = data['date_posted'].dt.day_name()
data['month_posted'] = data['date_posted'].dt.month_name()
data['year_posted'] = data['date_posted'].dt.year
data['age_year'] = data['year_posted'] - data['model_year']
data['age_year'] = data['age_year'].replace(0, pd.NA) 
data['age_year'] = data['age_year'].where(data['age_year'] != 0, 1)
data['mileage_per_year'] = data['odometer'] / data['age_year']
data['condition_rank'] = data['condition'].replace(['new', 'like new', 'excellent', 'good', 'fair', 'salvage'], [5, 4, 3, 2, 1, 0])
data.insert(4, 'condition_rank', data.pop('condition_rank'))
condition_dict = data[['condition_rank','condition']].drop_duplicates().sort_values('condition_rank').reset_index(drop=True)

option = st.checkbox('Muestra de dataset final')
if option:
    st.dataframe(data, use_container_width=True)
    st.write('Nuevo tamaño del dataset', data.shape)


# # Análisis Exploratorio de Datos ============================================================================================

st.header("2.Análisis Exploratorio de Datos")

st.markdown('''
            Se analizaran los siguientes parametros:
                
                - Precio ('price')
                - Antiguedad ('age_year')
                - Kilometraje ('odometer')
                - Numero de Cilindros ('cylinders')
                - Condicion ('condition_rank')
            ''')
st.subheader('Distribución de parámetros')
fig = plt.figure(figsize=(18, 10))
plt.subplot(2, 3, 1)
plt.title('Precio')
sns.boxplot(x=data['price'])
plt.subplot(2, 3, 2)
plt.title('Antigüedad del Vehículo')
sns.boxplot(x=data['age_year'])
plt.subplot(2, 3, 3)
plt.title('Kilometraje')
sns.boxplot(x=data['odometer'])
plt.subplot(2, 3, 4)
plt.title('Cantidad de Cilindros')
sns.countplot(x=data['cylinders'], palette='husl')
plt.subplot(2, 3, 5)
plt.title('Condición')
sns.countplot(x=data['condition_rank'], palette='husl')
st.pyplot(fig)
st.markdown('''
Hallazgos:

- Las columnas `price`, `age_year` y `odometer` contienen una cantidad significativa de valores atípicos.

- La distribución de los tipos de cilindros de los vehículos se concentra principalmente en 4, 6 y 8 cilindros, lo que coincide con las configuraciones más comunes en la mayoría de los vehículos. Sin embargo, todavía hay algunos vehículos con una cantidad distinta de cilindros en el conjunto de datos.

- La mayoría de los vehículos del conjunto de datos están clasificados como de calidad moderada, dentro de las categorías "good" y "excellent".

- Para asegurar un análisis más limpio y preciso, se eliminaran todos los valores atípicos. Cabe destacar que esto puede reducir la cantidad de datos disponibles para el análisis. Sin embargo, el conjunto resultante ofrecerá una base más clara y confiable para el análisis.
''')




st.write('Selecciona el tipo de vehiculo')
option_1 = st.checkbox('Sedan')
option_2 = st.checkbox('SUV')

button = st.button('Construir gráfico(s)')  # crear un botón

if option_1 & option_2:
    if button:
        st.write('Creación de un histograma y gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        # crear un histograma
        fig = px.histogram(
            data, x="odometer", title='Histograma del kilometraje de los vehiculo segun su condición', color='condition')
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(fig, use_container_width=True)
        # crear un gráfico de dispersión
        disp = px.scatter(data, x="odometer", y="price",
                          title='Gráfico de Dispersión kilometraje vs precio')
        st.plotly_chart(disp, use_container_width=True)
elif option_1:
    if button:
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
        # crear un histograma
        hist = px.histogram(data, x="odometer", title='Histograma del kilometraje de los vehiculo segun su condición', color='condition')
        # mostrar un gráfico Plotly interactivo
        st.plotly_chart(hist, use_container_width=True)
elif option_2:
    if button:
        st.write(
            'Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
        # crear un gráfico de dispersión
        disp = px.scatter(data, x="odometer", y="price",
                          title='Gráfico de Dispersión kilometraje vs precio')
        st.plotly_chart(disp, use_container_width=True)
else:
    if button:
        st.write('Debe seleccionar uno o ambos gráficos')













# st.subheader("1.Sedan")
# fig1, ax1 = plt.subplots()
# sns.histplot(data['price'], bins=50, kde=True, ax=ax1)
# st.pyplot(fig1)

# st.subheader("2.Suv")
# fig2, ax2 = plt.subplots()
# sns.scatterplot(x='model_year', y='price', data=data, ax=ax2)
# st.pyplot(fig2)

# # Puedes agregar más gráficos según los análisis del notebook

# st.header("3. Conclusion General")
# st.markdown("""
# - La mayoría de los vehículos tienen un precio entre ciertos rangos típicos.
# - La antigüedad del vehículo tiene una relación con el precio.
# - Se identificaron valores atípicos que pueden afectar el análisis.
# - El dataset incluye información relevante como tipo de combustible, tipo de caja de cambios, tracción, entre otros.
# """)

# st.markdown("**Nota**: Asegúrate de colocar el archivo CSV en la carpeta `datasets/` para que la app funcione correctamente.")
