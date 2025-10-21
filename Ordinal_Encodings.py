import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data.csv")
X=data
X1=data.copy()
categorycolumns=X1.select_dtypes(include="object").columns
for col in categorycolumns:
    X1[col+'encoded']=X1[col].astype('category').cat.codes
    X1=X1.drop(col,axis=1)
    print(X1.head())
    # List comprehension method 
    X2=data.copy()
    Genderencodings={
      "Male":0,
      "Female":1,
      "Other":2
    }
    X2=data.copy()
    X2["GenderEncoded"]=X2['Gender'].map(Genderencodings)
    X2.drop("Gender",axis=1)
    print(X2.head())
    
