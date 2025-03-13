from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from app import db

# def register_routes(app, db):
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
    
def register_routes(app, db, bcrypt):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            hashed_password = bcrypt.generate_password_hash(password)
            
            user = User(username=username, password=hashed_password)
            
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            
            user = User.query.filter(User.username == username).first()
            
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
            else:
                return 'Failed'
            
             
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/secret')
    @login_required
    def secret():
        if current_user.role == 'admin':
            return 'My secret message!'
        else:
            return 'No permission'