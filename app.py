import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.jpeg' '.png', '.gif']
app.config['UPLOAD_PATH'] = 'images'
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    # To display any uploaded images
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)


@app.route('/', methods=["POST"])
def upload_img():
    image = request.files['file']
    filename = secure_filename(image.filename)
    #if user didn't upload any image
    if filename == '':
        flash('No image selected')
    else:
        file_ext = os.path.splitext(filename)[1]
        #if images in not in the accepted format
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            flash('Wrong image Extension, we accept .png, .jpeg, .jpg , .gif')
        else:
            image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            flash('Image successfully uploaded')

    return redirect(url_for('index'))


@app.route('/images/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)

if __name__ == '__main__':
    app.run(debug=True)
