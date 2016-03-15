from flask import Flask

UPLOAD_FOLDER = 'puppies/static/images/'

app = Flask(__name__)
app.config.from_object('config')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from puppies import views

if __name__ == "__main__":
    app.run()
