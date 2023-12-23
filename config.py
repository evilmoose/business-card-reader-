import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'your_secret_key'
    UPLOADED_VIDEOS_DEST = os.path.join(BASE_DIR, 'static/uploads')
    ALLOWED_EXTENSIONS = set(['mp4', 'avi', 'mov', 'mkv'])
