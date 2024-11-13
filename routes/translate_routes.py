from flask import Blueprint, render_template, redirect, url_for, session
from forms import TranslateForm

translate_routes = Blueprint('translate_routes', __name__)

@translate_routes.route('/translate', methods=['GET', 'POST'])
def translate():
    form = TranslateForm()
    if form.validate_on_submit():
        session['target_language'] = form.target_language.data
        functionality = session.get('functionality', 'translate')
        if functionality == 'ner' or functionality == 'all':
            return redirect(url_for('ner_routes.ner'))
        else:
            return redirect(url_for('main_routes.result'))
    return render_template('translate.html', form=form, title='Translate Text')
