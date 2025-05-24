# Proyecto Final: Predicción de la Tasa de Cancelación de Clientes de Telco

## Estructura del Proyecto

Este proyecto final forma parte de un curso de ciencia de datos en Practicum, donde aplicamos todo lo que hemos aprendido durante el bootcamp en una simulación del mundo real. A diferencia de proyectos anteriores, este proyecto final simula situaciones laborales reales en empresas. Participamos en simulaciones de roles, con el equipo de tutores interpretando los roles de nuestros compañeros:

- El Tutor 1 actúa como líder del equipo, asignando tareas y asegurando su correcta finalización.
- El Tutor 2 cumple el rol de colega senior, respondiendo preguntas comunes sobre machine learning y ofreciendo ayuda cuando sea necesario.
- Los revisores de código evalúan nuestro código.

**Detalles de la Tarea:**

1. **Crear un Plan de Trabajo**
   - Estudiar las tareas proporcionadas y buscar aclaraciones con el líder del equipo si es necesario.
   - Desarrollar un plan de trabajo y realizar análisis exploratorio de datos (EDA).
   - Crear una lista de preguntas que requieran aclaración y esbozar un plan general al final del Jupyter Notebook, definiendo de 3 a 5 pasos básicos y explicando cada paso en una o dos frases.
   - El líder del equipo revisará las preguntas y el plan de trabajo, brindando retroalimentación si se encuentran dudas.
   - El código EDA será revisado por el líder del equipo para garantizar su corrección.

2. **Desarrollar el Código del Modelo**
   - Desarrollar código para abordar los problemas identificados en los proyectos aprobados.
   - Asegurar que el código compilado siga los pasos adecuados y esté bien ejecutado.
   - Verificar que el código de solución cumpla con los requisitos de la tarea.
   - Asegurar que el modelo de machine learning creado cumpla con la puntuación de calidad objetivo.
   - Enviar el código al revisor del proyecto para su evaluación.

3. **Crear un Informe de Tarea**
   - Preparar un informe documentando los pasos realizados durante el proyecto, junto con los resultados y recomendaciones.
   - Abordar las siguientes preguntas en el informe:
     - ¿Qué pasos realizaste y cuáles omitiste? Explica las razones detrás de tus decisiones.
     - ¿Qué desafíos encontraste y cómo los superaste?
     - Resume los pasos clave realizados para completar la tarea.
     - Describe tu modelo final y su puntuación de calidad.
   - Enviar el informe al líder del equipo para su revisión y asegurar la finalización adecuada de la tarea.
   - El líder del equipo considerará factores como la integridad y claridad de nuestras respuestas en la evaluación.
   - La puntuación final depende en gran medida de la calidad de nuestros modelos.
   - Para tener éxito, necesitamos alcanzar cinco puntos de historia (SP). Los puntos de historia (SP) se utilizan para medir el nivel de dificultad de una tarea, y podemos ganar de 4 a 6 SP por el proyecto principal y 1 SP por tareas adicionales.

## Descripción del Proyecto

Un operador de telecomunicaciones llamado Interconnect quiere predecir la tasa de cancelación de sus clientes. Si se sabe que un cliente planea cancelar el servicio, se le ofrecerán códigos promocionales y paquetes especiales. El equipo de marketing de Interconnect ha recopilado algunos datos personales de los clientes, incluyendo información sobre los planes de datos seleccionados y sus contratos.

**Servicios de Interconnect**

Interconnect ofrece dos tipos principales de servicios:

1. Red fija: los teléfonos pueden conectarse a múltiples canales simultáneamente.
2. Internet: las redes de internet pueden gestionarse mediante líneas telefónicas (DSL) o cables de fibra óptica.

Algunos de los otros servicios que ofrece Interconnect incluyen:

- Seguridad en internet: software antivirus (DeviceProtection) y bloqueador de sitios web maliciosos (OnlineSecurity)
- Línea de soporte técnico dedicada (TechSupport)
- Almacenamiento en la nube para archivos y respaldo de datos (OnlineBackup)
- Televisión en streaming (StreamingTV) y catálogos de películas (StreamingMovies)

Los clientes pueden elegir pagar mensualmente o firmar un contrato por 1 o 2 años. Pueden usar varios métodos de pago y recibir facturas electrónicas después de cada transacción.

## Descripción de los Datos

Los datos disponibles consisten en cuatro archivos obtenidos de diferentes fuentes:

- contract.csv — contiene información de contratos
- personal.csv — contiene datos personales de los clientes
- internet.csv — contiene información sobre los servicios de internet
- phone.csv — contiene información sobre los servicios telefónicos

Cada archivo incluye una columna customerID con un código único asignado a cada cliente.

La información de los contratos está actualizada al 1 de febrero de 2020.

Los conjuntos de datos combinados tienen un total de 20 características. Aquí hay una breve descripción de cada una:

1. customerID: ID único asignado a cada cliente.
2. BeginDate: Fecha de inicio del servicio.
3. EndDate: Fecha de finalización del servicio.
4. Type: Tipo de servicio (mensual/anual/bianual).
5. PaperlessBilling: Indica si se utiliza facturación electrónica (sí/no).
6. PaymentMethod: Método de pago utilizado por el cliente.
7. MonthlyCharges: Cargos mensuales por el servicio.
8. TotalCharges: Cargos totales por el uso del servicio.
9. InternetService: Tipo de servicio de internet utilizado.
10. OnlineSecurity: Indica si incluye seguridad en línea (sí/no).
11. OnlineBackup: Indica si incluye respaldo en línea (sí/no).
12. DeviceProtection: Indica si incluye protección de dispositivos (sí/no).
13. TechSupport: Indica si incluye soporte técnico (sí/no).
14. StreamingTV: Indica si incluye servicio de televisión por streaming (sí/no).
15. StreamingMovies: Indica si incluye servicio de películas por streaming (sí/no).
16. gender: Género del cliente (masculino/femenino).
17. SeniorCitizen: Indica si el cliente es adulto mayor (sí/no).
18. Partner: Indica si el cliente tiene pareja (sí/no).
19. Dependents: Indica si el cliente tiene personas a su cargo (sí/no).
20. MultipleLines: Indica si usa múltiples líneas telefónicas (sí/no).

## Objetivos del Proyecto

Este proyecto tiene tres objetivos principales:

- Analizar los datos proporcionados para identificar factores que pueden influir en la tasa de cancelación de clientes.
- Desarrollar modelos de machine learning que puedan predecir eficientemente la probabilidad de que los clientes abandonen los servicios de Interconnect.
- Generar recomendaciones promocionales relevantes para mitigar la cancelación de clientes y retener su fidelidad al servicio.

## Etapas de Finalización del Proyecto

Este proyecto se llevará a cabo en cuatro fases:

1. Preprocesamiento de datos: mejorar la calidad de los datos para facilitar un análisis más efectivo.
2. Análisis exploratorio de datos: investigar los factores que influyen en la tasa de cancelación de clientes.
3. Modelado con machine learning: desarrollar un modelo de machine learning capaz de predecir con precisión la tasa de cancelación.
4. Informe final y recomendaciones: resumir la implementación del proyecto y proponer estrategias promocionales apropiadas basadas en los factores clave que contribuyen a la cancelación de clientes en los servicios de Interconnect.

## Librerías

- Pandas versión: 1.4.4
- NumPy versión: 1.23.5
- Matplotlib versión: 3.7.1
- Seaborn versión: 0.12.2
- RegEx versión: 2.2.1
- Scikit-learn versión: 1.2.2
- SciPy versión: 1.10.1
- LightGBM versión: 3.3.5
- XGBoost versión: 1.7.3
- CatBoost versión: 1.1.1