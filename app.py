import os

from flask import Flask, render_template, request
from ImageDetect import ImageDetect

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        if request.files['image']:
            cmd = request.form['cmd']
            file = request.files['image']
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            obj = ImageDetect(filename)
            if cmd == 'face':
                obj.detect_faces(filename)
                return render_template("index.html", filename=filename)
            if cmd == 'eye':
                obj.detect_eyes(filename)
                return render_template("index.html", filename=filename)
            if cmd == 'text':
                text = obj.detect_text()
                return render_template("index.html", text=text)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)