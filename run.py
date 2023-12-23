from flask import Flask
from flask_uploads import UploadSet, configure_uploads, ALL
#from app.models import db

app = Flask(__name__)
app.config.from_object('config.Config')

videos = UploadSet('videos', ALL)
configure_uploads(app, videos)

#db.init_app(app)