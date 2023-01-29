from handle_uploaded_file import HandleUploadedFile

import os
from flask import Flask, flash, request, redirect, url_for
from flask_restful import Resource, Api, reqparse
from werkzeug.utils import secure_filename
from PyPDF2 import PdfReader

app = Flask(__name__)
api = Api(app)


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    its_extension = filename.rsplit('.', 1)[1].lower()
    return '.' in filename and its_extension in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['PUT'])
def upload_file():
    if request.method == 'PUT':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('download_file', name=filename))
            return filename
    return "success"


@app.route('/get', methods=['GET'])
def get_result():
    if request.method == 'GET':
        uploaded_file_path = 'uploads/' + os.listdir("uploads")[0]

        # with open(uploaded_file_path, 'rb') as f:
        file_name = os.listdir("uploads")[0]
        uploaded_file = HandleUploadedFile(uploaded_file_path)
        print(uploaded_file)
        # pdf_file = PdfReader(f)
        return {"f": file_name}


####DONT FORGET TO REMOVE DEBUG=TRUE##################################################################################
if __name__ == '__main__':
    app.run(debug=True)
