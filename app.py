import numpy as np
import pickle
from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)
# read model
with open("model/model_numpy.pkl", "rb") as model_file:
    model_numpy = pickle.load(model_file)
LABEL = ['Iris Setosa', "Iris Versicolor", "Iris Virginica"]

@app.route("/")
def iris():
        return render_template("index.html")
     
@app.route("/predict", methods=['POST'])   
def predict():
    # getting input with name  in HTML form dan ubah dalam bentuk float
       sepal_length = float(request.form.get("sepal_length")) 
       sepal_width = float(request.form.get("sepal_width"))
       petal_length = float(request.form.get("petal_length"))
       petal_width = float(request.form.get("petal_width"))
       # Print the text in terminal for verification 
        # print(sepal_length)
       new_data = [[sepal_length, sepal_width, petal_length, petal_width]]
       result = model_numpy.predict(new_data)
       result = LABEL[result[0]]
    
       return render_template("index.html", prediction_result=result, sepal_length=sepal_length,sepal_width=sepal_width,petal_length=petal_length,petal_width=petal_width) 

if __name__ == "__main__":
    app.run(debug=True) 