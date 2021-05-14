
# Creating the Necessary Files

Let’s say you are working for a company X and your role is a Machine Learning Engineer position. You have trained your model, saved it and you are ready to deploy it, so you decide to use Docker and Azure for this mission. 
First you must have your saved model, flask python code and one text. Your flask file which we called app.py is very important for deploying on docker. The requirements text file will include the dependencies important to run our Python application.

## Flask - app.py

Flask is a framework that allows you to build web applications. A web application can be a commercial website, blog, e-commerce system, or an application that generates predictions from data provided in real-time using trained models.

The following is the Python code we constructed using Flask. 'model.sav' is the model we trained and saved. It is a linear regression model that we trained based on the dataset of diabetes patients. We save this file as "app.py"

```
from flask import Flask, request
from sklearn import linear_model
import pickle
import os
import sys

app = Flask(__name__)


model = pickle.load(open("/src/model.sav",'rb'))


@app.route('/predict')

def predict():

    # get the prediction for unseen data
    new_record = -0.02560657
    predict_result = model.predict(new_record)


    # return the result back

    return 'Predicted result for observation ' + str(new_record) + ' is: ' + str(predict_result)


if __name__ == '__main__':

    app.run(debug=True,host='0.0.0.0',port=5000)

```

Next, we will construct the requirements text file. The requirements text file will include the dependencies important to run our Python application. We save this file as "requirements.txt".

```
Flask==0.10.1
sklearn==0.0
scikit-learn==0.23.1
pickle
```
## Next Step

In the next step, we will proceed to create the Docker file!


