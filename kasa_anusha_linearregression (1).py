# -*- coding: utf-8 -*-
"""Kasa_Anusha_LinearRegression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10HOv_7oLQRbGzFDX_yXJmLIZ_Zo4NOSA

Importing Libraries
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.preprocessing import MinMaxScaler
from sklearn import preprocessing

"""Reading Dataset"""

df=pd.read_csv("/content/monet.csv")

df.head()

df.shape

df.isnull().sum()

df.describe()

df['Area']=df['HEIGHT']*df['WIDTH']

"""Applying Logrithmic Transformation"""

df['Area_log']=np.log(df['Area'])

sns.heatmap(df.corr())

sns.pairplot(df.corr())

X = df['Area_log']
y=df['PRICE']

"""scatter plot with regression line"""

plt.plot(X, y, 'o')
m, b = np.polyfit(X, y, 1)
plt.plot(X, m*X+b)

X = X.to_frame()

"""Train test split"""

X_train, X_test,y_train,y_test = train_test_split(X,y,test_size =0.2)

"""Defining Model"""

Linear_model = LinearRegression()

"""Fitting Model for Arealog and Price as independent and dependent variables"""

Linear_model.fit(X_train,y_train)

y_pred=Linear_model.predict(X_test)

"""calculating root mean square error"""

print("Root Mean squared error: %.2f" % sqrt(mean_squared_error(y_test, y_pred)))

"""Fitting Model for WIDTH and Price as independent and dependent variables"""

X2=df['WIDTH']
Y2=df['PRICE']

sns.regplot(X2, Y2, ci=None)

X2 = X2.to_frame()

X2_train, X2_test,Y2_train,Y2_test = train_test_split(X2,Y2,test_size =0.2)

Linear_model.fit(X2_train,Y2_train)

Y2_pred=Linear_model.predict(X2_test)

"""calculating root mean square error"""

print ("Root Mean squared error: %.2f" % sqrt(mean_squared_error(Y2_test, Y2_pred)))

"""Multivariate regression"""

data=pd.read_csv("/content/monet.csv")

"""Normalizing data"""

names=['PRICE','HEIGHT','WIDTH','SIGNED','PICTURE','HOUSE']
d = preprocessing.normalize(data)
scaled_df = pd.DataFrame(d, columns=names)
scaled_df.head()

"""Defining X and Y"""

XM = scaled_df[['HEIGHT','WIDTH','SIGNED','PICTURE','HOUSE']]
YM = scaled_df['PRICE']

"""Doing Train Test split"""

XM_train, XM_test,YM_train,YM_test = train_test_split(XM,YM,test_size =0.2)

"""Fitting Model"""

Linear_model.fit(XM_train,YM_train)

YM_pred=Linear_model.predict(XM_test)

"""Calculating root Mean Square error"""

print("Root Mean squared error: %.2f" % sqrt(mean_squared_error(YM_test, YM_pred)))