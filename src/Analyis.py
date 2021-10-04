import pandas as pd
import numpy as np
from src.data_cleaning import rawdatacleaning
import plotly.figure_factory as ff
import plotly.express as px




class VisualisationAnalysis(rawdatacleaning):
    data = pd.read_csv("Data_given\gpscleaned.csv")
    x_val = data['Installs_New'].groupby(by=data['Category']).sum().sort_values(ascending=False)
    x_rat_cat = data['Rating'].groupby(by=data['Category']).mean().sort_values(ascending=False)
    x_cat_rev = data['Reviews'].groupby(by=data['Category']).sum().sort_values(ascending=False)
    paid_data = data[data.Type == 'Paid']
    paid_cat_install = paid_data['Installs_New'].groupby(by=paid_data['Category']).sum().sort_values(ascending=False)
    paid_rev_cat = paid_data['Reviews'].groupby(by=paid_data['Category']).sum().sort_values(ascending=False)
    install_cr = data['Installs_New'].groupby(by=data['Content Rating']).count().sort_values(ascending=False)




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
    def highestinstallations(self):

        fig = px.bar(self.data,x = self.x_val.index,y = self.x_val, color=self.x_val.index)
        return fig
    def avg_CategoryRating(self):
        #x_rat_cat = self.data['Rating'].groupby(by=self.data['Category']).mean().sort_values(ascending=False)
        fig1 = px.bar(self.data, x=self.x_rat_cat.index, y=self.x_rat_cat.values, color=self.x_rat_cat)
        fig2 = px.bar(self.data, x=self.x_val.head(10).index, y=self.x_rat_cat[self.x_val.head(10).index], color=self.x_val.head(10).index)
        return fig1,fig2
    def max_reviews(self):
        #self.x_cat_rev = self.data['Reviews'].groupby(by=self.data['Category']).sum().sort_values(ascending=False)
        fig = px.bar(self.data, x=self.x_cat_rev.index, y=self.x_cat_rev.values, color=self.x_cat_rev.index)
        return fig
    def highestinstalled_highestreviews(self):
        fig = px.bar(self.data, x=self.x_cat_rev[self.x_val.head(10).index].index, y=self.x_cat_rev[self.x_val.head(10).index].values,
               color=self.x_cat_rev[self.x_val.head(10).index].index)
        return fig
    def paid_categories(self):
        #self.paid_data = self.data[self.data.Type == 'Paid']
        fig = px.bar( self.paid_data, x= self.paid_data['Category'].value_counts().index, y= self.paid_data['Category'].value_counts().values,
               color= self.paid_data['Category'].value_counts().index)
        return fig
    def highest_paid_installed(self):
        #paid_cat_install = self.paid_data['Installs_New'].groupby(by=self.paid_data['Category']).sum().sort_values(ascending=False)
        fig = px.bar(self.paid_data, x=self.paid_cat_install.index, y=self.paid_cat_install.values, color=self.paid_cat_install)
        return fig
    def paid_highestrating(self):
        fig = px.bar(self.paid_data, x=self.paid_data['Rating'].groupby(by=self.paid_data['Category']).mean().sort_values().dropna().index,
               y=self.paid_data['Rating'].groupby(by=self.paid_data['Category']).mean().sort_values().dropna().values,
               color=self.paid_data['Rating'].groupby(by=self.paid_data['Category']).mean().sort_values().dropna().index)
        return fig
    def highestReviews_paid(self):
        #paid_rev_cat = self.paid_data['Reviews'].groupby(by=self.paid_data['Category']).sum().sort_values(ascending=False)
        fig = px.bar(self.paid_data, x=self.paid_rev_cat.index, y=self.paid_rev_cat.values, color=self.paid_rev_cat.index, text=self.paid_cat_install)
        return fig
    def contentrating_highestinstall(self):
        #install_cr = self.data['Installs_New'].groupby(by=self.data['Content Rating']).count().sort_values(ascending=False)
        fig = px.bar(self.data, x=self.install_cr.index, y=self.install_cr.values, color=self.install_cr.index)
        return fig

    def temp_df(self):
        self.data_fixedSize = self.data[self.data['Size_New'] != 'Varies with device']
        self.data_fixedSize['Size_New'] = self.data_fixedSize['Size_New'].astype(float)
        return self.data_fixedSize['Size_New'].min(),self.data_fixedSize['Size_New'].max()
    def size_apps(self,app_size=67000):
        app_number = self.data_fixedSize[self.data_fixedSize['Size_New'] > app_size]['Size_New'].groupby(by=self.data_fixedSize['Category']).count().sort_values(ascending=False)
        fig = px.bar(self.data_fixedSize, x=app_number.index, y=app_number.values, color=app_number.index)
        return fig