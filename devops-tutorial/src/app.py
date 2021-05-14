#!/usr/bin/env python
# coding: utf-8

# In[12]:


from flask import Flask, request
from sklearn import linear_model
import pickle
import os
import sys

app = Flask(__name__)


# In[13]:


model = pickle.load(open("/Users/patricianaccachian/Desktop/devops-tutroial/model.sav",'rb'))


# In[14]:


@app.route('/predict')

def predict():

    # get the prediction for unseen data
    new_record = -0.02560657
    predict_result = model.predict(new_record)


    # return the result back

    return 'Predicted result for observation ' + str(new_record) + ' is: ' + str(predict_result)


# In[15]:


if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=5000)


# In[11]:





# In[ ]:




