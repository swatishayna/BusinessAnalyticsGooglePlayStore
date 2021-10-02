from src.Analyis import VisualisationAnalysis

import streamlit  as st


class Analysis:
    analysis = VisualisationAnalysis()


    def run(self):
        st.title("Google Play Store Analytics\n\n\n\n")

        cleaned_data = st.checkbox("View Cleaned data")
        if cleaned_data:
            st.dataframe(self.analysis.data)


        missing_values = st.checkbox("Missing Values of the Cleaned Data")
        if missing_values:
            st.table(self.analysis.missing_values())

        data_types = st.checkbox("View Data Types of Cleaned data")
        if data_types:
            st.write(self.analysis.datatype())
            st.header("findings 1")
            st.write("Size_New, AndroidVersion_New : All the etries are numeric except 'Varies with Devices' so we will consider this as numerical columns")
            st.write("LastUpdated_New: datetime column , we will treat this later")
            st.write("14% of the data is missing in Rating Feature")
        categorical_analysis = st.checkbox("View Categorical analysis of the cleaned dataset")
        if categorical_analysis:
            st.write(self.analysis.categoricalanalysis())





