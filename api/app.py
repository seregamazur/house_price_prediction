import os
import pickle

import pandas as pd
from flask import Flask, jsonify, request, render_template, redirect
from werkzeug.utils import secure_filename

from misc import normalize, prepare

UPLOAD_FOLDER = './uploads'
SECRET_KEY = '\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
ALLOWED_EXTENSIONS = {'csv'}
app = Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
model = pickle.load(open('./saved_model.pb', 'rb'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/csv-data", methods=["GET", "POST"])
def csv_data():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            data_df = pd.read_csv(file)
            try:
                id_df = data_df["Id"].values
                data_df.drop("Id", axis=1, inplace=True)
                d = xgb.DMatrix(normalize(data_df))
            except ValueError as e:
                return f"SERVER ERROR {e}", 400
            result = model.predict(d)

            context = {
                "results": zip(id_df, result),
            }
            return render_template("csv_data.html", context=context)
    else:
        return render_template("csv_data.html", context={})


@app.route('/api/predict', methods=['POST'])
def hello():
    data = request.json
    if not data:
        return jsonify({"err": "No data supplied"}), 400
    try:
        d = xgb.DMatrix(normalize(prepare(data)))
    except ValueError as e:
        return jsonify({"err": str(e)}), 400
    result = model.predict(d)
    return jsonify({"prediction": float(result[0])}), 200
