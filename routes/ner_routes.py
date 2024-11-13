from flask import Blueprint, render_template, redirect, url_for, session
from forms import NERForm

ner_routes = Blueprint('ner_routes', __name__)

@ner_routes.route('/ner', methods=['GET', 'POST'])
def ner():
    form = NERForm()
    if form.validate_on_submit():
        return redirect(url_for('main_routes.result'))
    return render_template('ner.html', form=form, title='Named Entity Recognition')
