import preprocessing as preprocessing
from flask_restful import Api, Resource, request
from scipy.stats import stats
import matplotlib.pyplot as plt
from endpoints.csvToDFUtil import csvToDFUtil
import pandas as pd
import numpy as np
import requests
import io

#big help from -> https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b

class SummaryStats(Resource):
    def get(self):
        result_status, result_data = buildSummary()
        return {'resultStatus': result_status, 'resultData': result_data}

def buildSummary():
    result_status = 'Fail'
    result_data = []
    try:
        zz = csvToDFUtil()
        df = zz.get()

        attributes = df.columns
        df = df.apply(lambda x: x.fillna(x.value_counts().index[0]))
        for att in attributes:
            df[att] = df[att].replace("No Value", np.NaN)

        category_col = ['workclass', 'race', 'educational_level', 'marital_status', 'occupation', 'relationship', 'sex',
                        'country', 'over_50k']
        # need to do label encoding for supervised learning#
        # getting error MissingValues object has no attribute to_list#
        # labelEncoder = preprocessing.LabelEncoder()
        # print(labelEncoder)
        # mapping_dict = {}
        # for col in category_col:
        #     df[col] = labelEncoder.fit_transform(df[col])
        #     le_name_mapping = dict(zip(labelEncoder.classes_, labelEncoder.transform(labelEncoder.classes_)))
        #     mapping_dict[col] = le_name_mapping
        # print(mapping_dict)

        # lets play around with hours_week and age#
        numerical_summary = str(df[["hours_week", "age"]].describe())
        hwmed = float(df['hours_week'].median())
        agemed = float(df['age'].median())
        x_ = df["hours_week"]
        y_ = df["age"]
        r, p = stats.pearsonr(x_, y_)
        lin = str(stats.linregress(x_, y_))

        fig, ax = plt.subplots()
        ax.boxplot((x_.values.tolist(), y_.values.tolist()), vert=False, showmeans=True, meanline=True,
                   labels=("hours worked weekly", "age"), patch_artist=True,
                   medianprops={'linewidth': 2, 'color': 'yellow'},
                   meanprops={'linewidth': 2, 'color': 'yellow'})
        # plt.savefig()#

        # try a quick decision tree once I can bugfix the preprocessing#
        # X = df.values[:, 0:12]
        # Y = df.values[:, 12]
        #
        # X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=100)
        # dt_clf_gini = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=5, min_samples_leaf=5)
        # dt_clf_gini.fit(X_train, y_train)
        # y_pred_gini = dt_clf_gini.predict(X_test)
        #
        # print("Desicion Tree using Gini Index\nAccuracy is ", accuracy_score(y_test,y_pred_gini)*100 )
        #
        #
        # print(lin)
        # print(r)
        # print(p)
        # proportional50 = df["over_50k"].sum()/df.shape[0]
        jsonResult = {'numSum': numerical_summary, 'hwmed': hwmed, 'agemed': agemed, 'linreg': lin}
        result_data.append(jsonResult)
        result_status = 'Success'

    except Exception as inst:
        result_data.append({'message': repr(inst)})

    return result_status, result_data
