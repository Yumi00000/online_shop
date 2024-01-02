from flask import Blueprint, render_template, redirect, request, session

from db_requests import update_data_in_db, load_from_db, insert_data_in_db

user_blueprint = Blueprint('user', __name__)


@user_blueprint.get('/login')
def login_get():
    return render_template('login.html')


@user_blueprint.post('/login')
def login_post():
    login = request.form.get('login')
    password = request.form.get('password')
    user = load_from_db('*', 'User', {'login': login, 'password': password})
    if user:
        session['login'] = user[0][0]
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
    login = request.form.get('login')
    name = request.form.get('name')
    surname = request.form.get('surname')
    password = request.form.get('password')
    mobile_number = request.form.get('mobile_number')
    try:
        insert_data_in_db('User', {'login': login, 'name': name, 'surname': surname, 'password': password,
                                   'mobile_number': mobile_number})
        return redirect('/login')
    except:
        load_from_db('*', 'User', {'login': login})
        return render_template('register.html', login_exists=True)


@user_blueprint.route('/user', methods=['GET', 'POST'])
def user_profile():
    if request.method == 'POST':
        user_login = session.get('login')
        update_data_in_db('User',
                          {'login': user_login,
                           'name': request.form.get('name'),
                           'surname': request.form.get('surname'),
                           'password': request.form.get('password'),
                           'mobile_number': request.form.get('mobile_number')},
                          {'login': user_login})

        return redirect('/user')
    user_login = session.get('login')
    if session.get('login') == None:
        return redirect('/login')
    current_user = load_from_db('*', 'User', {'login': user_login})[0]
    return render_template('user_info.html', current_user=current_user)
