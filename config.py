

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    UPLOAD_FOLDER = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 

    # Google Cloud Translation API Configuration
    # Ensure this environment variable is set
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
