import numpy as np 
import pandas as pd 
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data_with_missing.csv")
X=data
# 1.dropping the columns with missing values in them 
X1=X.copy()
colsmissing = [col for col in X1.columns
               if X1[col].isnull().any()]
reducedX = X1.drop(colsmissing, axis=1)
print(reducedX.head(25))
# 2. using simple inputations
X2=X.copy()
X2 = X1.copy()
colsmissing = [col for col in X2.columns if X2[col].isnull().any()]
meanvalues = X2[colsmissing].mean().to_dict()
X2.fillna(value=meanvalues, inplace=True)
print(X2.head(25))
# 3.using extended imputations
X3 = X.copy()
colsmissing = [col for col in X3.columns if X3[col].isnull().any()]
for col in colsmissing:
 X3[col + '_was_missing'] = X3[col].isnull()
meanvalues = X3[colsmissing].mean().to_dict()
X3.fillna(value=meanvalues, inplace=True)
print(X3.head(25))

