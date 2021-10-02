import pandas as pd
import numpy as np
from src.data_cleaning import rawdatacleaning

class VisualisationAnalysis(rawdatacleaning):
    data = pd.read_csv("Data_given\gpscleaned.csv")

    def missing_values(self):
       return  np.round(self.data.isnull().mean(), 2)

    def datatype(self):
       return super().datatype(self.data)

    def categoricalanalysis(self):
        # number of class in each categorical feature
        categorical_feature = [feature for feature in self.data.columns if self.data[feature].dtypes == 'object' and feature not in ['LastUpdated_New', 'Size_New','AndroidVersion_New']]
        d = {}
        for feature in categorical_feature:
            key = "total number of categories in " + feature
            d[key] = self.data[feature].nunique()

        return d