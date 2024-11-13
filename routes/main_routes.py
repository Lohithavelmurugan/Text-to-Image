
from flask import Blueprint, render_template, redirect, url_for, session
from forms import FunctionalityForm
import logging

from flask import Blueprint, render_template, redirect, url_for, session, flash
from utils.ocr_utils import extract_text
from utils.nlp_utils import perform_ner
from utils.translation_utils import translate_text
import os
import logging

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/', methods=['GET', 'POST'])
def home():
    form = FunctionalityForm()
    if form.validate_on_submit():
        selected_functionality = form.functionality.data
        session['functionality'] = selected_functionality
        return redirect(url_for('extract_routes.extract'))
    return render_template('home.html', form=form, title='Home')

@main_routes.route('/result')
def result():
    texts = []
    image_paths = session.get('image_paths', [])
    ocr_language = session.get('ocr_language', 'eng')
    target_language = session.get('target_language', '')
    functionality = session.get('functionality', 'extract')

    if not image_paths:
        flash('No images uploaded. Please start again.', 'danger')
        return redirect(url_for('main_routes.home'))

    for filepath in image_paths:
        try:
            # Extract text
            text = extract_text(filepath, lang=ocr_language)
            if not text or "Error extracting text" in text:
                flash(f'Error extracting text from {os.path.basename(filepath)}.', 'danger')
                continue  # Skip to the next image

            translated_text = ''
            ner_text = text
            translation_error = None
            ner_error = None

            # Perform translation if selected
            if functionality in ['translate', 'all']:
                if target_language:
                    translated_text, translation_error = translate_text(text, target_language)
                    if translation_error:
                        flash(f'Error translating text from {os.path.basename(filepath)}: {translation_error}', 'danger')
                        # Use original text for NER if translation fails
                        ner_text = text
                    else:
                        ner_text = translated_text
                else:
                    translated_text = text

            # Perform NER if selected
            if functionality in ['ner', 'all']:
                ner_result = perform_ner(ner_text)
                entities = ner_result.get('entities', [])
                html = ner_result.get('html', '')
                ner_error = ner_result.get('error')
                if ner_error:
                    flash(f'Error performing NER on {os.path.basename(filepath)}: {ner_error}', 'danger')
            else:
                entities = []
                html = ''
                ner_error = None

            texts.append({
                'filename': os.path.basename(filepath),
                'text': text,
                'translated_text': translated_text,
                'entities': entities,
                'html': html,
                'translation_error': translation_error,
                'ner_error': ner_error
            })
        except Exception as e:
            logging.error(f'Error processing image {filepath}: {e}')
            flash(f'Error processing image {filepath}: {e}', 'danger')

    if not texts:
        flash('No valid texts were processed. Please try again with different images.', 'danger')
        return redirect(url_for('main_routes.home'))

    return render_template('result.html', texts=texts, functionality=functionality)