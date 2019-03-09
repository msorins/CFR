import base64

from Evaluators.KeywordsEvaluator import KeywordsEvaluator
from Evaluators.OnePage import OnePage
from Evaluators.SentenceLengthEvaluator import SentenceLengthEvaluator
from Utils.ReadPDF import ReadPDF
import json

import os
from flask import Flask, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from API.config import Config
from API.util import allowed_file
from flask_cors import CORS


# ==== FLASK SECTION =====
app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
app.secret_key = Config.SECRET

# ==== SUBMIT ROUTE ====
@app.route('/submit', methods=['POST', 'GET'])
def submit_resume():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return "no file"
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return "no selected file"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)

            # Get the PyPDFObject
            readUtils = ReadPDF()
            cv = readUtils.read(path)

            # Call all Evaluators
            evals = [OnePage(), SentenceLengthEvaluator(), KeywordsEvaluator()]
            feedbacks = []
            for eval in evals:
                crtFeedback = eval.evaluate(cv)
                feedbacks.extend(crtFeedback)

            # Return the feedback
            return json.dumps( [ob.__dict__ for ob in feedbacks])

# readUtils = ReadPDF()
# cv = readUtils.read('/Users/so/Desktop/Projects/CFR/Data/CV_MirceaSorinSebastian.pdf')
# onePageEval = OnePage()
# result = onePageEval.evaluate(cv)
# print(result)
#
