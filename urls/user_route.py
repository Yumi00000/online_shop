from flask import Blueprint, render_template, redirect, request, session

from app import db
from models.user import User

user_blueprint = Blueprint('user', __name__)


@user_blueprint.get('/login')
def login_get():
    return render_template('login.html')


@user_blueprint.post('/login')
def login_post():
    login = request.form['login']
    password = request.form['password']
    user = db.session.query(User).filter_by(login=login, password=password).all()
    if user:
        session['login'] = user[0].login
        return redirect('/user')
    else:
        return render_template('login.html', login_failed=True)


@user_blueprint.get('/logout')
def logout():
    session.pop('login', None)
    return redirect('/login')


@user_blueprint.route('/register', methods=['GET'])
def get_register():
    return render_template('register.html')


@user_blueprint.route('/register', methods=['POST'])
def register():
    try:
        login = request.form.get('login')
        name = request.form.get('name')
        surname = request.form.get('surname')
        password = request.form.get('password')
        mobile_number = request.form.get('mobile_number')

        # Validate form data here if needed

        user = User(login=login, name=name, surname=surname, password=password, mobile_number=mobile_number)
        db.session.add(user)
        db.session.commit()

        return redirect('/login')

    except Exception as e:
        print(f"Error: {e}")
        db.session.rollback()
        return redirect('/register')


@user_blueprint.route('/user', methods=['GET', 'POST'])
def user_profile():
    user_login = session.get('login')

    if request.method == 'POST':
        user = db.session.query(User).filter_by(login=user_login).first()
        user.name = request.form['name']
        user.surname = request.form['surname']
        user.password = request.form['password']
        user.mobile_number = request.form['mobile_number']
        db.session.commit()

        return redirect('/user')

    if session.get('login') is None:
        return redirect('/login')

    current_user = db.session.query(User).filter_by(login=user_login).first()
    return render_template('user_info.html', current_user=current_user)