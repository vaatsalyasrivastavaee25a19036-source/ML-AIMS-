import pandas as pd
import numpy as np
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data.csv")
y=data.Employment_Type
X=data.drop(['Employment_Type'],axis=1)
cardinalitycols = [K for K in X.columns if X[K].nunique() < 10 and 
                        X[K].dtype == "object"]
numerical_cols = [M for M in X.columns if X[M].dtype in ['int64', 'float64']]
boolseries = (X.dtypes == 'object')
object_cols = list(boolseries[boolseries].index)
print("Categorical variables:")
print(object_cols)
X1=X.copy()
categorycolumns=X1.select_dtypes(include="object").columns
for col in categorycolumns:
    X1[col+'_encoded']=X1[col].astype('category').cat.codes
    X1=X1.drop(col,axis=1)
