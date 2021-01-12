from flask_restful import Api, Resource, request
from scipy.stats import stats
import matplotlib.pyplot as plt
from sklearn import preprocessing, linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, RobustScaler, QuantileTransformer
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.pipeline import Pipeline

from endpoints.csvToDFUtil import csvToDFUtil
import pandas as pd
import numpy as np
import requests
import io

# big help from -> https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b

result_status = 'Fail'
result_data = [ ]

zz = csvToDFUtil()
df = zz.get()
df

# replaces NaN with previous columns value#
attributes = df.columns
for att in attributes:
    df[ att ] = df[ att ].replace("No Value", np.NaN)
df = df.apply(lambda x: x.fillna(x.value_counts().index[ 0 ]))
df.isnull().any()
regression_col = [ "hours_week", "age"]
for reg_col in regression_col:
    df[ reg_col ] = df[ reg_col ].fillna(df[reg_col].median())


df.isnull().any()
category_col = [ 'workclass', 'race', 'educational_level', 'marital_status', 'occupation', 'relationship', 'sex',
                 'country', 'over_50k' ]
attributes = df.columns
for att in attributes:
    df[ att ] = df[ att ].replace("?", "No Value")

dropped = df.dropna()
df.isnull().any()
# need to do label encoding for supervised learning#
# getting error MissingValues object has no attribute to_list#
# lets play around with hours_week and age#
numerical_summary = str(df[ [ "hours_week", "age" ] ].describe())
hwmed = float(df[ 'hours_week' ].median())
agemed = float(df[ 'age' ].median())

#removing outliers by zscore#
#hours_no_outliers = df[ (np.abs(stats.zscore(df[ "hours_week" ])) < 3) ]
#age_no_outliers = hours_no_outliers[ (np.abs(stats.zscore(hours_no_outliers[ "age" ])) < 3) ]
#x_ = age_no_outliers[ "hours_week" ]
#y_ = age_no_outliers[ "age" ]

x_ = df[ "hours_week" ]
y_ = df[ "age" ]



fig, ax = plt.subplots()
ax.boxplot((x_.values.tolist(), y_.values.tolist()), vert=False, showmeans=True, meanline=True, showfliers=True,
           labels=("hours worked weekly", "age"), patch_artist=True,
           medianprops={'linewidth': 2, 'color': 'yellow'},
           meanprops={'linewidth': 2, 'color': 'yellow'})


#preprocessing for linear regression#
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('reduce_dim', PCA()),
    ('regressor', Ridge())
    ])

X = x_.values.reshape(-1, 1)
Y = y_.values.reshape(-1, 1)
print(type(X))
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=100)
print(type(y_test))
for i in y_test:
    print(type(i))
regr = linear_model.LinearRegression(fit_intercept=True,
                 normalize=True,
                 copy_X=True,
                 n_jobs=None)
regr.fit(X_train, y_train)
LinearRegression(fit_intercept=True,
                 normalize=True,
                 copy_X=True,
                 n_jobs=None)
#X_train.fillna(X_train.mean())
#pipe = pipe.fit(X_train, y_train)
#print('Testing score: ', pipe.score(X_test, y_test))



r, p = stats.pearsonr(x_, y_)
lin = str(stats.linregress(x_, y_))
#bytes_image = io.BytesIO()
#plt.savefig('endpoints/images/box.png', format='png')
#bytes_image.seek(0)






# dt_clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=5, min_samples_leaf=5)
# dt_clf_gini.fit(X_train, y_train)
# y_pred_gini = dt_clf_gini.predict(X_test)
#
# print("Decision Tree using Gini Index\nAccuracy is ", accuracy_score(y_test,y_pred_gini)*100 )
#
#
# print(lin)
# print(r)
# print(p)
# proportional50 = df["over_50k"].sum()/df.shape[0]
jsonResult = {'numSum': numerical_summary, 'hwmed': hwmed, 'agemed': agemed, 'linreg': lin}
result_data.append(jsonResult)
result_status = 'Success'



# return result_status, result_data
