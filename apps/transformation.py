import streamlit as st
from src import transformtraindata
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor



class Transform_Train:
    def run(self):
        st.title("Google Play Store Analytics\n\n")
        data = transformtraindata.get_data('transform')



        transformed_data = transformtraindata.encode_data(data)
        imputed_data = transformtraindata.impute_nan(transformed_data)
        data_new = transformtraindata.final_data(imputed_data)


        ## Splitting the data for training and testing

        data = transformtraindata.get_data('train')
        X = data.drop(columns=['Rating'])
        Y = data['Rating']
        train_X, test_X, train_y, test_y = train_test_split(X, Y, test_size=.15, random_state=45)


        # model training
        rfr = RandomForestRegressor(oob_score=True, verbose=True, n_jobs=5,max_features='sqrt', min_samples_leaf=2,
                      n_estimators=1500)
        rfr.fit(train_X, train_y)
