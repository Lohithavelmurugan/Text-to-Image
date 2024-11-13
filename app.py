

from flask import Flask
from config import Config
from routes import main_routes, extract_routes, translate_routes, ner_routes
import logging
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(main_routes)
app.register_blueprint(extract_routes)
app.register_blueprint(translate_routes)
app.register_blueprint(ner_routes)


if not os.path.exists('logs'):
    os.mkdir('logs')
file_handler = RotatingFileHandler('logs/flask_ocr_app.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    '%(asctime)s %(levelname)s [%(pathname)s:%(lineno)d] - %(message)s'
)
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)
app.logger.info('Flask OCR App startup')

if __name__ == '__main__':
    app.run(debug=True)
