import pickle
from pandas import DataFrame, get_dummies
from sklearn.preprocessing import StandardScaler
import pandas as pd 

model = pickle.load(open('pipe.sav','rb'))
real_columns = pickle.load(open('real_dfcolumn.sav','rb'))
dummy_columns = pickle.load(open('dffinal_dummies_colomn.sav','rb'))

new_data = [1,1,1,1,1,1,'No','At some of my previous employers','None did','None did','No','No','No','No','No','No','Male','No','No','Mental health',"I don't know",'Mental health','Never','Above 50']

def prediction(data):
#     # new_data = data
#     df = DataFrame([new_data],columns=real_columns)
#     df = get_dummies(df)
#     df = df.reindex(columns=dummy_columns,fill_value=0)
#     hasil = model.predict(df)
#     return hasil
# df = DataFrame([new_data],columns=real_columns)
# df = get_dummies(df)
# df = df.reindex(columns=dummy_columns,fill_value=0)
# print(df)
#    return model.predict_proba([data])
    return model.predict([data])

def prob(data):
    return model.predict_proba([data])




