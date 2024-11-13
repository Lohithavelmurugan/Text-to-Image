
from flask import Blueprint, render_template, redirect, url_for, session, flash
from forms import UploadForm
from werkzeug.utils import secure_filename
import os
import logging

extract_routes = Blueprint('extract_routes', __name__)

@extract_routes.route('/extract', methods=['GET', 'POST'])
def extract():
    form = UploadForm()
    if form.validate_on_submit():
        session['ocr_language'] = form.language.data
        session['image_paths'] = []
        upload_folder = os.path.join(os.getcwd(), 'uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
            logging.info(f'Created upload folder at {upload_folder}')
        for image_file in form.images.data:
            filename = secure_filename(image_file.filename)
            filepath = os.path.join(upload_folder, filename)
            image_file.save(filepath)
            session['image_paths'].append(filepath)
            logging.info(f'Image saved: {filepath}')
        functionality = session.get('functionality', 'extract')
        if functionality == 'translate':
            return redirect(url_for('translate_routes.translate'))
        elif functionality == 'ner':
            return redirect(url_for('ner_routes.ner'))
        elif functionality == 'all':
            return redirect(url_for('translate_routes.translate'))
        else:
            return redirect(url_for('main_routes.result'))
    return render_template('extract.html', form=form, title='Extract Text')
