import streamlit as st
from  PIL import Image
import os
st.set_page_config(
    page_icon= "✨",
    page_title= "Churn app",
    layout = "centered"
)

st.sidebar.header("Select Language:")
language = st.sidebar.selectbox("", ["English", "Español"])

if language == "Español":
    st.title(f"**Predicción de abandono de clientes** :runner::department_store:")

    st.write(
        """
        Esta aplicación predice la probabilidad de abandono de un cliente. Utiliza un modelo de aprendizaje automático entrenado en un conjunto de datos de características de clientes. El modelo predice si un cliente abandonará o no basado en las características de entrada.

        **Nota:** Esta aplicación es solo para fines de demostración. No proporciona predicciones en tiempo real.

        ### **¿Por qué es importante la predicción de abandono de clientes?**

        [La pérdida de clientes](https://www.questionpro.com/blog/customer-churn/), también conocida como deserción de clientes, es la pérdida de clientes en un período de tiempo determinado. Es un problema común que enfrentan las empresas y puede tener consecuencias significativas, incluida una disminución en los ingresos y una pérdida de participación en el mercado.

        Al utilizar el aprendizaje automático para predecir el abandono de clientes, las empresas pueden tomar medidas proactivas para retener clientes y reducir el impacto negativo de la deserción.

        #### **¿Cómo funciona la aplicación?**

        La aplicación le permite ingresar una variedad de características del cliente, como Antigüedad, Tipo de contrato y Cargos totales. Basándose en estas características, el modelo de aprendizaje automático predecirá si un cliente está en riesgo de abandonar.

        **Características clave:**

        * Interfaz fácil de usar
        * Modelos de aprendizaje automático de alta precisión

        **Rendimiento del modelo:**

        Nuestros modelos de aprendizaje automático se han entrenado en un gran conjunto de datos de características de clientes y han alcanzado una precisión del 80%.
        """
    )

    # Imagen
    chun_img = Image.open(
        os.path.join(
            os.getcwd(),
            "assets/images/chun customer image.jpg"
        )
    )

    # Mostrar imagen
    st.image(
        chun_img,
        use_column_width=True,
        caption="Las abejas representan experiencias negativas que pueden alejar a los clientes."
    )

    st.markdown(
        """
        #### **Beneficios de utilizar esta aplicación**
        - **Advertencias tempranas:** Obtenga información sobre qué clientes están en riesgo de irse, lo que le permite intervenir antes de que sea demasiado tarde.
        - **Decisiones basadas en datos:** Base sus esfuerzos de retención en predicciones objetivas, no solo en intuición.
        - **Alcance personalizado:** Adapte sus estrategias de retención a las necesidades y preocupaciones específicas de los clientes en riesgo.
        - **ROI mejorado:** Invierta en retener clientes existentes en lugar de adquirir nuevos, a menudo a un costo menor.
        """
    )

    st.markdown(
        """
        #### **El impacto del abandono de clientes**
        💭 Los estudios muestran que perder un cliente puede costar de 5 a 10 veces más que adquirir uno nuevo.

        💭 Aumentar la retención de clientes en solo un 5% puede aumentar los beneficios en un 25-95%.
        """
    )

    # Llamado a la acción
    st.write("## ¡Pruébalo❗")
    st.write("*¿Listo para comenzar a predecir el abandono?*:eyes:")

    # Mostrar GIF
    gif_path = 'assets/images/hell-yeah-hell-to-the-yeah meme.gif'
    st.image(
        gif_path,
        caption='A continuación, identifique y retenga a los clientes felices'
    )

    # Instrucciones
    st.write(
        """
        Diríjase a la [*página de Predicción*](http://localhost:8501/Predict) para ingresar fácilmente la información del cliente y descubrir su riesgo de abandono.

        Para obtener más detalles sobre la funcionalidad y el rendimiento de la aplicación, explore la página **Bienvenida**.
        """
    )
else:
    # Translate content to English
    st.title(f"**Customer Churn Predictor** :runner::department_store:")

    st.write(
        """
        This app predicts the likelihood of a customer churning. It uses a machine learning model trained on a dataset of customer features. The model predicts whether a customer will churn or not based on the input features.

        **Note:** This app is for demonstration purposes only. It does not provide real-time predictions.

        ### **Why is customer churn prediction important?**

        [Customer churn](https://www.questionpro.com/blog/customer-churn/) also known as customer attrition, is the loss of customers over a given period of time. It is a common problem faced by businesses and can have significant consequences, including a decline in revenue and a loss of market share.

        By using machine learning to predict customer churn, businesses can take proactive steps to retain customers and reduce the negative impact of churn.

        #### **How does the app work?**

        The app allows you to input a variety of customer features, such as Tenure,Contract type, and Total charges. Based on these features, the machine learning model will predict whether a customer is at risk of churning.

        **Key features:**

        * User-friendly interface
        * High accuracy machine learning models

        **Model performance:**

        Our machine learning models have been trained on a large dataset of customer features and has achieved an accuracy of 80%.
        """
    )

    #image
    chun_img = Image.open(
        os.path.join (
            os.getcwd(),
            "assets/images/chun customer image.jpg"
            )
    )

    #display img
    st.image(
        chun_img,
        use_column_width=True,
        caption= "Bees represent negative experiences that can drive customers away."
    )

    #st.header("Benefits of Using This App:")
    st.markdown(
        """
        #### **Benefits of Using This App**
        - **Early warnings:** Gain insights into which customers are at risk of leaving, allowing you to intervene before it's too late.
        - **Data-driven decisions:** Base your retention efforts on objective predictions, not just intuition.
        - **Personalized outreach:** Tailor your retention strategies to the specific needs and concerns of at-risk customers.
        - **Improved ROI:** Invest in retaining existing customers rather than acquiring new ones, often at a lower cost.
        """
    )

    st.markdown(
        """
        #### **The impact of customer churn**
        💭 Studies show that losing a customer can cost 5-10 times more than acquiring a new one.

        💭 Increasing customer retention by just 5% can boost profits by 25-95%.
        """
    )

    # Call-to-action
    st.write("## Try it out❗") 
    st.write ("*Ready to start predicting churn?*:eyes:")

    # display GIF
    gif_path = 'assets/images/hell-yeah-hell-to-the-yeah meme.gif'
    st.image(
        gif_path, 
        caption='Below Identify & Retain Happy Customers'
    )

    # Instructions
    st.write(
        """
        Head over to the [*Predict page* ](http://localhost:8501/Predict) to easily input customer information and discover their churn risk.

        For further details on the app's functionality and performance, explore the **Welcome** page. 
        """
    )

# Link 
st.write(
    """
**Source Code:** [GitHub Repository](https://github.com/Code-str8/Churn-Prediction-ML-app)
"""
)
