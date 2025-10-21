import numpy as np 
import pandas as pd 
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data.csv")
X=data
X1=X.copy()
datacolumn = X1['Performance_Rating'].astype('category')
codes = datacolumn.cat.codes
categories = datacolumn.cat.categories
numcategories = len(categories)
numsamples = len(datacolumn)
OneHotarray = np.identity(numcategories)[codes]
columnnames = [f'Dept{cat}'for cat in categories]
OneHotDf = pd.DataFrame(OneHotarray,columns=columnnames,index=X1.index)
Xencoded = pd.concat([X1.drop('Department',axis=1),OneHotDf],axis=1)
print(Xencoded.head())


