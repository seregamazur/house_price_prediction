import numpy as np
import pandas as pd
from flask import Flask, request, render_template, redirect
from tensorflow import keras

from normalization import normalized_test_data

UPLOAD_FOLDER = './uploads'
SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

extra_data = pd.read_csv("../data/train.csv")
model = keras.models.load_model('../data/regression_model')


def is_valid_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/csv", methods=["GET", "POST"])
def get_csv():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and is_valid_file(file.filename):
            data_df = pd.read_csv(file)
            id_df = data_df["Id"].values
            try:
                test_data = np.array(normalized_test_data(data_df))
            except ValueError as e:
                return f"SERVER ERROR {e}", 400
            result = model.predict(test_data)
            context = {
                "results": zip(id_df, result),
            }
            return render_template("csv_data.html", context=context)
    else:
        return render_template("csv_data.html", context={})
