import streamlit as st
from src import transformdata

class Transform_Train:
    def run(self):
        st.title("Google Play Store Analytics\n\n")
        data = transformdata.get_data()



        transformed_data = transformdata.encode_data(data)
        imputed_data = transformdata.impute_nan(transformed_data)
        data_new = transformdata.final_data(imputed_data)


        ## Splitting the data for training and testing