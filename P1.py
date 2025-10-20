import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data.csv")
X=data
X1=X.copy()
categorycolumns=X1.select_dtypes(include="object").columns
for col in categorycolumns:
    X1[col+'_encoded']=X1[col].astype('category').cat.codes
    X1=X1.drop(col,axis=1)
    # List comprehension method 
    X2=data.copy()
    Employment_encodings={
        "full_time":0,
        "part_time":1,
        "contract":2,
        "intern":3
    }
    X2=data.copy()
    X2["Employment_Type_Encoded"]=X2['Employment_Type'].map(Employment_encodings)
    X2.drop("Employment_Type",axis=1)
    print(X2.head())
    
