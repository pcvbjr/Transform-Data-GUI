from flask import Flask, request, redirect, send_file, render_template
from werkzeug.utils import secure_filename
import joblib
import pandas as pd
import os
from threading import Timer
import webbrowser

# create instance of Flask
app = Flask(__name__)

# setup folder to store uploaded files
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# download pipeline
# model = joblib.load('model.pkl')

def transform(file_path):
    """return transformed file at file_path"""
    data = pd.read_csv(file_path)
    # data['y'] = model.predict(data)
    data['y'] = data['x_0'] * data['x_1'] % 3
    return data

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('no file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('no filename')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('file saved successfully')
            
            def append_to_filename(filename, text):
                idx = filename.rfind('.')
                new_filename =filename[:idx] + text + filename[idx:]
                return new_filename
            
            data_transformed = transform(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            download_filename = append_to_filename(filename, '_TRANSFORMED')
            data_transformed.to_csv(os.path.join(app.config['UPLOAD_FOLDER'], download_filename), index=False)
            
            return redirect('/downloadfile/' + download_filename)
    
    return render_template('upload_file.html')

@app.route('/downloadfile/<filename>', methods=['GET'])
def download_file(filename):
    return render_template('download.html', value=filename)

@app.route('/return-files/<filename>')
def return_files_tut(filename):
    file_path = UPLOAD_FOLDER + filename
    return send_file(file_path, as_attachment=True)

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
#     Timer(1, webbrowser.open_new('http://127.0.0.1:5000')).start(); #automatically open page in browser
    app.run(host='0.0.0.0')