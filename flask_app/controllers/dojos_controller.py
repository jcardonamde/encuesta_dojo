from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojos import Dojo

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/create/dojo_survey', methods=['POST'])
def data_form():
    if not Dojo.validate_fields(request.form):
        return redirect('/')
    data = {
        "name": request.form['name'],
        "ubication": request.form['ubication'],
        "language": request.form['language'],
        "comment": request.form['comment']
    }
    Dojo.save_survey(data)
    return redirect('/result')

@app.route('/result')
def results():
    return render_template("result.html", user = Dojo.get_temporal_survey())

@app.route('/back')
def back_home():
    session.clear()
    return redirect('/')
