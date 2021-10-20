import pandas as pd
from apps.config import Config
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

def get_data():
    data = os.path.join(Config.DATA_PATH, "gpscleaned.csv")
    data = pd.read_csv(data)
    return data


def generate_dictionary(data):
    dict_category = {}
    val = 0
    for i in data["Category"].unique():
        dict_category[i] = val
        val += 1
    dict_content_rating = {"Adults only 18+": 0, "Everyone": 1, "Everyone 10+": 2, "Mature 17+": 3, "Teen": 4}
    return dict_category,dict_content_rating

def encode_data(data):
    encoder = LabelEncoder()
    data["Category_new"] = encoder.fit_transform(data.Category)
    data["Content_Rating_new"] = encoder.fit_transform(data["Content Rating"])
    data['Type_new'] = encoder.fit_transform(data["Type"])
    return data

def impute_nan(data):
    impute = SimpleImputer()
    data['Rating'] = impute.fit_transform(data[['Rating']])
    # removing entries with "Varies with Device= total 1695 rows will be removed
    data = data[data['Size_New'] != 'Varies with device']
    data['Size_New'] = pd.to_numeric(data['Size_New'])
    return data

def final_data(data):

    newdata = data.drop(
        columns=['App', 'Category', 'Type', 'Content Rating', 'CurrentVer_New', 'AndroidVersion_New',
                 'LastUpdated_New','Genres'])
    newdata.to_csv('Data_given\gpsfinal.csv', index=False)
    return newdata