import pandas as pd


# Every Entry in Size column has "M" , "+" and "K" which needs to be removed and datatype into int/float
# function which will remove these
def Size_mk(column):
    for i in column:
        if str(i).endswith("M"):
            i = i.replace(",","")
            return float(i[:-1])*1000
        elif str(i).endswith("k"):
            i = i.replace(",","")
            return float(i[:-1])
        elif str(i).endswith("+"):
            i =  i.replace(",","")
            return (float(i[:-1]))
        else:
            return(i)

# Every entry has "+" at the end which needs to be removed and datatype into int/float
def Installs_removeplus(column):
    for i in column:
        if str(i).endswith("+"):
            i =  i.replace(",","")
            return (int(i[:-1]))
        else:
            return i


# It has "$" at the begining it needs to be cleaned and datatype into int/float
def Price_cleandollar(column):
    for i in column:
        if str(i).startswith("$"):
            return float(i[1:])
        else:
            return i


#CurrentVer: The entries are 1.0.1, 1.2.1, 1.2 so we will make it 101, 121, 120, correct upto 3 places
def Currentver_clean(column):
    for i in column:
        i = ("").join(str(i).split('.'))
        i = i.strip()
        if i.isnumeric():
            if len(i) < 3:
                req = 3 - len(i)
                i = i + ('0' * req)
                return int(i)
            elif len(i) > 3:
                return int(i[0:3])
            elif len(i) == 3:
                return int(i)
        else:
            return i

def generate_Androidversion_cleanedlist(data):
    # we need to remove 'and up' from the entries where it is present and should write '2.0.1' as 201 also we need to make '7.0 - 7.1.1' as 700
    version_clean = []
    for i in data['Android Ver']:
        if type(i) == float:
            version_clean.append(i)
        else:
            i = ('').join(i.replace('and up', '').strip().split('.'))
            try:
                i = i.split('-')[1].strip()
            except:
                pass
            finally:
                if i.isnumeric():
                    if len(i) <= 2:
                        i = i + str((0 * (2 - len(i))))
                    i = int(i[:2])
                elif i == '44W':
                    i = int(i[:2])
                version_clean.append(i)
    return version_clean

def change_datatype(data):
    data.Reviews = data.Reviews.astype('int8')
    data['Installs_New'] = data['Installs_New'].astype("int32")
    data['Price_New'] = data['Price_New'].astype('int8')
    # LastUpdtaed
    # it is date time column ,datatype shouldbe changed accordingly and in feature engineering we will splitt the column into year and month
    data['LastUpdated_New'] = pd.to_datetime(data['Last Updated'])
    data['Size_New'] = data['Size_New'].astype("category")
    return data


class rawdatacleaning:

    #reading the dataset
    gps = pd.read_csv("Data_given\googleplaystore.csv")

    def view_missingvalues(self):
        return self.gps.isnull().sum()

    def datatype(self,df):
        index, data_type = df.dtypes.index, df.dtypes.values
        d = {}
        for key, value in zip(index,data_type):
            d[key]=value
        return d


    def cleandataframe(self,df):

        # Reviews
        df.loc[df.Reviews == '3.0M','Reviews'] = 3000000

        # Sizecolumn
        df["Size_New"] = df[['Size']].apply(Size_mk, axis=1)

        #Install Column
        df["Installs_New"] = df[["Installs"]].apply(Installs_removeplus, axis=1)
        # there are certain entries like free which is result of bad data collection we can delete this record
        # as well as there is no rating for it also the reviews are in negative number
        free = df[df["Installs_New"] == "Free"]
        df.drop(free.index, inplace=True)



        #Price Column
        df['Price_New'] = df[['Price']].apply(Price_cleandollar, axis=1)
        print("##############################################################")



        #Current Ver Column
        df['CurrentVer_New'] = df[['Current Ver']].apply(Currentver_clean, axis=1)
        # there are 4 values which starts with "Version", we can clean them
        version = df[df['CurrentVer_New'].str.contains('Version').fillna(False)]['CurrentVer_New']
        for i in version:
            df.loc[version.index, 'CurrentVer_New'] = int(i[8:])

        # Android Version
        version_clean =generate_Androidversion_cleanedlist(df)
        df['AndroidVersion_New'] = pd.Series(version_clean)

        #change the datatype of the column
        sdf = change_datatype(df)

        #droping the old uncleaned columns as new columns for them are created
        df.drop(['Android Ver', 'Current Ver', 'Last Updated', 'Price', 'Installs', 'Size'], axis=1, inplace=True)

        #storing the dataset in a destination directory: Data_given
        df.to_csv('Data_given\gpscleaned.csv', index=False)

