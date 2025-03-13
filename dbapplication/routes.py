from flask import render_template, request, redirect, url_for
from models import Person
from app import db

def register_routes(app, db):
    # @app.route('/', methods=['GET', 'POST'])
    # def index():
    #     if request.method == 'POST':
    #         name = request.form.get('name')
    #         age = request.form.get('age')
    #         job = request.form.get('job')

    #         if not name or not age or not job:
    #             return "All fields are required!", 400

    #         try:
    #             age = int(age)
    #         except ValueError:
    #             return "Age must be a number!", 400  

    #         person = Person(name=name, age=age, job=job)
    #         db.session.add(person)
    #         db.session.commit()

    #         return redirect(url_for('index'))  # Redirect to avoid resubmission

    #     people = Person.query.all()
    #     return render_template('index.html', people=people)

    # @app.route('/delete/<pid>', methods=['DELETE'])
    # def delete(pid):
    #     Person.query.filter(Person.pid == pid).delete()
        
    #     db.session.commit()
        
    #     people = Person.query.all()
    #     return render_template('index.html', people=people)
    
    # @app.route('/details/<pid>')
    # def details(pid):
    #     person = Person.query.filter(Person.pid == pid).first()
    #     return render_template('details.html', person=person)