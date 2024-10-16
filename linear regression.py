import pandas as pd
Boston=pd.read_csv('./BostonHousing.csv')

import pandas as pd
from google.colab import files
import io


uploaded = files.upload()
Boston = pd.read_csv(io.BytesIO(uploaded['BostonHousing.csv']))
Boston.head()

# Applying LR algorithm
y=Boston[['medv']] # dependant variable
x=Boston[['crim']]  # independant variable
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
lr=LinearRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
y_test.head()

y_pred[0:5]

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test,y_pred)

x=Boston[['lstat']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
lr2=LinearRegression()
lr2.fit(x_train,y_train)
y_pred2=lr2.predict(x_test)
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test,y_pred2)