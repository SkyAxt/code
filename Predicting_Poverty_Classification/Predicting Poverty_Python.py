#!/usr/bin/env python
# coding: utf-8
#Project is still incomplete and lacks prediction scores. 
#Project is a continuation of the R Code but attempts to utilize more
#advance methods, hyperparamater tuning, more complex data processing

import pandas as pd
import numpy as np
from pprint import pprint


# In[305]:


from sklearn.preprocessing import  LabelEncoder
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.utils import resample
from sklearn.ensemble import RandomForestClassifier as RFC
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import log_loss


# In[306]:


from keras.regularizers import l2
from keras.layers import Input, Embedding, Dense, Dropout, Flatten
from keras.models import Model
from keras.layers.core import Lambda
from keras import layers
from keras import optimizers


# In[307]:


def country_def(pred, feat):
    country_sub = pd.Dataframe(data=preds,
                              columns=['poor'],
                              index=feat.index)
    country_sub["country"] = "A"
    return country_sub[["country","poor"]]


# In[431]:


df = pd.read_csv(r'C:\Users\nghia\Projects\Github-Profile\Data1\worldbank_train_data.csv')
df_copy = df.copy()


# In[432]:


df.head()
#Observe the sample of the data


# In[433]:


df.info()
#Observe the different features. Recognize that the features
#our boolean is our label -> it determines if the exposure is poor or not
#we have 5 numerical values; should look into standardizing and scaling these values but also note ID is considered an int
#we should control the categorical objects and use some version of onehotencoding/label 


# In[407]:


df[['id']].head()
#example of numerical feature. we will standardize all numerical values except ID.


# In[313]:


'''num_attribs = list(df)
cat_atttribs =['wBXbHZmp']
num_pipeline = pipeline)[]
full_pipeline = columntransformer([
    ("num", num_pipeline,num_attribs),
    ("cat", OnehotEncoder(), cat_attribs)
])'''
#Work on finding and using easier methods to simplify preprocessing data in the future. 


# In[430]:


df_copy.shape
#recall that shape returns tuple


# In[435]:


unique_label = ["id"]
df_no_id = drop_feats(df.copy(), unique_label)


# In[438]:


df_no_id.info()


# In[444]:


#Standardize our features to bring our numerical features to similar scale
def standardize(df, numeric_only = True):
    numeric = df.select_dtypes(include=['int64', 'float64'])
    df[numeric.columns] = (numeric - numeric.mean()) / numeric.std()
    return df

standardized_df[['TiwRslOh']].head()


# In[447]:


standardized_df.info


# In[446]:


#OMtioXZZ,YFMZwKrU,poor,TiwRslOh,country,etc. These columns have numerical values
#After we drop. We will add back in to 
List_Numerical_Feats = ["OMtioXZZ","YFMZwKrU","TiwRslOh"]
#In the future, we should look to build a function that will scout these data type
#instead of manually looking at the file.
train_label = ["poor"]

def drop_feats(df,lst):
    return df.drop(columns = lst)


dropped_df = drop_feats(standardized_df, List_Numerical_Feats)
dropped_df_no_label = drop_feats(dropped_df,train_label)


print(dropped_df.shape)
print(dropped_df_no_label.shape)

#print(df.head())


# In[ ]:





# In[448]:



labelencoder = LabelEncoder()
# = labelencoder.fit_transform(dropped_values["KAJOWiiw"])
def labelencode(df):
    labelencoder = LabelEncoder()
    for i in list(df):
        df[i] = labelencoder.fit_transform(df[i])
    return df
new_dfA = labelencode(dropped_df_no_label)
#We changed the nominal values using labelencoder


# In[449]:


new_dfA.head()


# In[452]:


print(new_dfA.shape)
def add_back_feats(new_df, prior_df, lst):
    for i in lst: 
        new_df[i] = prior_df[i]
    return new_df

df_no_label = add_back_feats(new_dfA, standardized_df, List_Numerical_Feats)
df_no_label.shape
#Our function adds back in the numerical values we dropped except for the Label.
#note we added back our IDs so that our standardized function avoids scaling the IDs


# In[453]:


df_no_label.head()
#we should be missing our label and our unique IDs


# In[454]:


#add back in the unique IDs
new_df = add_back_feats(df_no_label, df, unique_label)


# In[455]:


new_df.head()
#We've added back in the unique Id without standardizing it. 


# In[462]:


new_df.dtypes
#notice how much we've changed the data types of each feature.


# In[463]:


def _encode(df):
    for i in list(df):
        df[i] = df[i].astype('category')
    return df

_encode(new_df)


# In[464]:


new_df.dtypes


# In[502]:


x = np.array(df_no_label)
#
y = np.array(df.poor)
x_train, x_test, y_train, y_test = train_test_split(df_no_label, y,test_size = .33)
#train_test_split already randomizes the train data
clf = RFC(max_depth = 15, min_samples_leaf = 1, min_samples_split = 2, n_estimators = 500)
#Random Forest Classifier

clf.fit(x_train,y_train)
#train_x, train_y


# In[503]:


df_no_label.shape
#randomized the order of the row and train maybe 4000 data as a start.
#create a samlpe for each train/test.


# In[504]:


prediction = clf.predict(x_test)
#predict test_x
print(prediction)
score = log_loss(y_test,prediction)
print(score)
#train_x, train_y, test_x, test_y = 
lin_scores = cross_val_score(clf,x_test,y_test,cv= 100)
print(lin_scores)


# In[ ]:


from sklearn.model_selection import GridSearchCV
random_grid = {'n_estimators': [200,400,600,700,800,1000],
               'max_features': ['auto'],
               'max_depth': [2,5,10,15,20,25,None],
               'min_samples_split': [2,4,10],
               'min_samples_leaf': [1,2,5],
               'bootstrap': [True]}

pprint(random_grid)
clf = RFC(max_depth = 15, min_samples_leaf = 1, min_samples_split = 2, n_estimators = 500)
rf_random = GridSearchCV(estimator = clf, param_grid = random_grid, cv = 3)
rf_random.fit(x_train,y_train)
rf_random.best_params_


# In[ ]:


x2 = np.array(standardized_df)
#
clf2 = RFC(n_estimators = 1000, max_leaf_nodes = 16, n_jobs = -1)
clf2.fit(x2,y)


# In[ ]:


prediction2 = clf.predict(standardized_df)
print(prediction2)
score2 = log_loss(y,prediction2)
print(score2)

lin_scores = cross_val_score(clf2,standardized_df,y,cv= 100, scoring = "neg_log_loss")
print((-lin_scores))


# In[325]:





# In[345]:


import lightgbm as lgb


# In[321]:


x3 = np.array(lgb_df_feats)
lgb_model = lgb.LGBMClassifier()
from sklearn.model_selection import RepeatedStratifiedKFold

cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
lgb_model.fit(standardized_df,y)
scores = cross_val_score(lgb_model, standardized_df,y,scoring = 'neg_log_loss', cv=cv,n_jobs =-1)


# In[322]:


print(-scores)


# In[346]:


standardized_df.dtypes


# In[355]:


from xgboost import XGBClassifier

#test for xgb model to see how it does against lgboost

def cat_encode(df):
    for i in list(df):
        df[i] = df[i].astype('int')
    return df
xgb_df = cat_encode(dropped_df_no_label)
xgb_df_feats = add_back_feats(lgb_df, df, List_Numerical_Feats)
xgb_df_feats.dtypes
xgb_model = XGBClassifier()
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
results = cross_val_score(xgb_model, )


# In[391]:


#add_back_feats(xgb_df_feats,df,unique_label)
df

