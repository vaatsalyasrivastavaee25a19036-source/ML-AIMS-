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
#using median 
import numpy as np 
import pandas as pd 
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data_with_missing.csv")
X=data
X1=X.copy()
X1 = X.copy()
colsmissing = [col for col in X1.columns if X1[col].isnull().any()]
meanvalues = X1[colsmissing].median().to_dict()
X1.fillna(value=meanvalues, inplace=True)
print(X1.head(25))
#using mode
import numpy as np 
import pandas as pd 
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data_with_missing.csv")
X=data
X1=X.copy()
X1 = X.copy()
colsmissing = [col for col in X1.columns if X1[col].isnull().any()]
modevalues = X1[colsmissing].mode().iloc[0].to_dict()
X1.fillna(value=modevalues, inplace=True)
print(X1.head(25))
#using custom
import numpy as np 
import pandas as pd
data=pd.read_csv("C:/Users/vaats/Downloads/employee_categorical_data_with_missing.csv")
X=data
X1=X.copy()
standard_val="50"
cols_with_missing_val=[col for col in X1.columns
                       if X1[col].isnull().any()]
X1.fillna(value=standard_val,inplace=True)
print(X1.head(25))
# 3.using extended imputations
X3 = X.copy()
colsmissing = [col for col in X3.columns if X3[col].isnull().any()]
for col in colsmissing:
 X3[col + '_was_missing'] = X3[col].isnull()
meanvalues = X3[colsmissing].mean().to_dict()
X3.fillna(value=meanvalues, inplace=True)
print(X3.head(25))


