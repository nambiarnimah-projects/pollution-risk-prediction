import streamlit as st
import joblib
model=joblib.load(r"aqi_model.pkl")
def get_aqi_category(aqi):
    if aqi <= 50:
        return "Good", "green"
    elif aqi <= 100:
        return "Satisfactory", "lightgreen"
    elif aqi <= 200:
        return "Moderate", "orange"
    elif aqi <= 300:
        return "Poor", "red"
    elif aqi <= 400:
        return "Very Poor", "darkred"
    else:
        return "Severe", "purple"
st.title("AQI Prediction app")
st.write("Enter the pollution and weather data to predict AQI")
pm25=st.number_input("PM2.5")
pm10=st.number_input("PM10")
no2 = st.number_input("NO2")
so2 = st.number_input("SO2")
co = st.number_input("CO")
o3 = st.number_input("O3")
temp = st.number_input("Temperature Min")
precip = st.number_input("Precipitation")
wind = st.number_input("Wind Gust")
if st.button("Predict AQI"):
    no2 = no2 * 1.88
    so2 = so2 * 2.62
    co = co*0.001145
    o3 = o3 * 2
    input_data=[[pm25,
    pm10,no2,so2,co,o3,temp,precip,wind]]
    
    prediction=model.predict(input_data)
    aqi_value = prediction[0]
    st.success(f"Predicted AQI: {aqi_value:.2f}")
    category, color = get_aqi_category(aqi_value)

    st.markdown(
        f"<h2 style='color:{color};'>AQI Category: {category}</h2>",
        unsafe_allow_html=True
    )
