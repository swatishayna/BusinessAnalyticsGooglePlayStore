import streamlit as st
from apps.transformation import Transform_Train
from src import transformdata

def run():
    st.header("Google Play Store Rating Prediction App")



    #['Category NUM', 'Reviews', 'Size', 'Installs', 'Price', 'Content Rating NUM']
    data = transformdata.get_data()
    dict_category = transformdata.generate_dictionary(data)[0]
    dict_content_rating =transformdata.generate_dictionary(data)[1]

    # inputs
    Category = st.selectbox("Input the category of the Android Application", dict_category.keys())