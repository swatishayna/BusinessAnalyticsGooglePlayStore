import streamlit as st
from src.data_cleaning import rawdatacleaning
import pandas as pd
from apps.config import Config
import os

class Raw_Data:
    raw = rawdatacleaning()



    def run(self):
        st.title("Google Play Store Analytics\n\n")
        view_df = st.checkbox("View RawDataset")
        if view_df:
            st.dataframe(rawdatacleaning.gps)

        df_info = st.checkbox("Brief Information of the dataset")
        if df_info:
            st.write("It is the web scraped data of 10k Play Store apps for analyzing the Android market. "
                     "It consists of in total of 10841 rows and 13 columns.")


        view_missing_values = st.checkbox("View Number of Missing Values")
        if view_missing_values:
            st.dataframe(pd.DataFrame(rawdatacleaning.gps.isnull().sum()).T)

        view_data_types = st.checkbox("View datatypes of the dataset")
        if view_data_types:
            st.write(self.raw.datatype(rawdatacleaning.gps))

        clean_data = st.checkbox("Clean dataset")
        if clean_data:
            st.markdown("Cleaning is required to:")
            st.write("""
            1.Reviews : It has to be a numerical column and datatype into int/float\n
            2.Size : Every Entry has "M" and "K" which needs to be removed and datatype into int/float\n
            3.Installs: Every entry has "+" at the end which needs to be removed and datatype into int/float also it has entries like "Free"\n
            4.Price : It has "$" at the begining it needs to be cleaned and datatype into int/float\n
            5.LastUpdtaed : it is date time column ,datatype shouldbe changed accordingly and in feature engineering we will splitt the column into year and month\n
            6.Current Ver : The entries are 1.0.1,1.2.1,1.2 so we will make it 101,121,120 , correct upto 3 places\n
            7.Android Ver : we will remove "And up" from the end and making 4.0.3 as 403
            """)
            clean = st.button("CleanData")
            if clean:
                data = rawdatacleaning.gps.copy()
                self.raw.cleandataframe(data)
                path_cleaned =os.path.join(Config.DATA_PATH, "gpscleaned.csv")
                cleaned_dataframe = pd.read_csv(path_cleaned)
                st.dataframe(cleaned_dataframe)
                st.write(self.raw.datatype(cleaned_dataframe))



