import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from config import Config
from util import allowed_file

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.secret_key = Config.SECRET

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/submit', methods=['POST', 'GET'])
def submit_resume():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

            return path
    # return my_cool_function(f'./{Config.UPLOAD_FOLDER}/{filename}')
