## Introducción
La compañia de telecomunicaciones, Interconnect, desea identificar a los clientes que podrían estar pensando en cancelar el servicio. Si detectan que un cliente planea irse, le ofrecerán códigos promocionales y planes especiales. El equipo de marketing de Interconnect ha recopilado algunos datos personales de sus clientes, incluyendo información sobre sus planes y contratos.

## Objetivo

- Identificar las características y comportamientos que distinguen a los clientes activos de aquellos que probablemente abandonen el servicio.

- Desarrollar un modelo de machine learning para predecir la pérdida de clientes (churn) con una puntuación AUC-ROC de al menos 0.85.

## Datos

- Descripción de los datos de contrato

customerID: Identificador único del cliente.

BeginDate: Fecha en la que el cliente comenzó a usar el/los servicio(s).

EndDate: Fecha en la que el cliente dio de baja el servicio. Un valor de "No" indica que el cliente aún utiliza el servicio al momento de la extracción de datos (1 de febrero de 2020).

Type: Tipo de contrato (por ejemplo, mes a mes, anual, etc.).

PaperlessBilling: Valor binario que indica si el cliente optó por facturación sin papel.

PaymentMethod: Método de pago utilizado para los servicios contratados (por ejemplo, cheque electrónico, cheque por correo, etc.).

MonthlyCharges: Monto cobrado mensualmente al cliente.

TotalCharges: Monto total acumulado cobrado al cliente durante todo el período de suscripción.

- Descripción de los datos personales

customerID: Identificador único del cliente.

gender: Género del cliente (por ejemplo, Femenino, Masculino).

SeniorCitizen: Valor binario que indica si el cliente es un adulto mayor.

Partner: Valor binario que indica si el cliente tiene pareja.

Dependents: Valor binario que indica si el cliente tiene personas a su cargo (como hijos u otras personas dependientes).

- Descripción de los datos de internet

customerID: Identificador único del cliente.

InternetService: Tipo de servicio de internet contratado (por ejemplo, DSL, fibra óptica).

OnlineSecurity: Valor binario que indica si el cliente tiene el servicio de seguridad en línea.

OnlineBackup: Valor binario que indica si el cliente tiene servicio de respaldo en línea.

DeviceProtection: Valor binario que indica si el cliente tiene protección para sus dispositivos conectados.

TechSupport: Valor binario que indica si el cliente tiene acceso a soporte técnico.

StreamingTV: Valor binario que indica si el cliente está suscrito al servicio de TV en streaming.

StreamingMovies: Valor binario que indica si el cliente está suscrito al servicio de películas en streaming.

- Descripción de los datos de teléfono

customerID: Identificador único del cliente.

MultipleLines: Valor binario que indica si el cliente contrató múltiples líneas telefónicas.

## Principales bibliotecas utilizadas

Pandas, Numpy, Matplotlib, Seaborn, Scikit-Learn, LightGBM, XGBoost, CatBoost, Boruta, SMOTENC