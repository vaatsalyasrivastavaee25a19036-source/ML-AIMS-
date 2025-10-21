import numpy as np 
import pandas as pd 
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data.csv")
X=data
X1=X.copy()
column = X1['Performance_Rating'].astype('category')
codes = column.cat.codes
categories = column.cat.categories
numcategories = len(categories)
numsamples = len(column)
array = np.identity(numcategories)[codes]
columnnames = [f'Dept{cat}'for cat in categories]
Df = pd.DataFrame(array,columns=columnnames,index=X1.index)
Xencoded = pd.concat([X1.drop('Department',axis=1),Df],axis=1)
print(Xencoded.head())



