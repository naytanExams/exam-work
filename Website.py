from flask import Flask, render_template, request, redirect, url_for
import psycopg2

webapp = Flask(__name__)
webapp.secret_key = "KEY-IS-SECRET"

DB_CONFIG = {
    "host": "localhost",
    "dbname": "ExamPaper2",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}

def validate_login(user, psw):
    connection = cursor = None
    try:
        connection = psycopg2.connect(**DB_CONFIG) # call kwargs of dbconfig
        cursor = connection.cursor()
        query = 0
        cursor.execute( '''SELECT * FROM "Account_Details" WHERE "Username" = %s AND "Password" = %s''', (user, psw))
        test = cursor.fetchone()
        print(test)
        return test
    except Exception as err:
        print(f"Login error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def register_new_user(fname, lname, email, addr, pcode, uname, psw):
    connection = cursor = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute(
            '''INSERT INTO "User_Details" ("Forename", "Surname", "Email", "Address", "Post_code") 
               VALUES (%s, %s, %s, %s, %s) RETURNING "User_ID"''',
            (fname, lname, email, addr, pcode)
        )
        user_id = cursor.fetchone()[0]
        cursor.execute(
            '''INSERT INTO "Account_Details" ("Username", "Password", "User_ID") 
               VALUES (%s, %s, %s)''',
            (uname, psw, user_id)
        )
        connection.commit()
    except Exception as err:
        print(f"Registration error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

@webapp.route('/')
def main_page():
    return render_template('Main.html')

@webapp.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        uname = request.form.get('username')
        pwd = request.form.get('password')
        test = validate_login(uname, pwd)
        print(test)
        if test:
            return redirect(url_for('main_page'))
        else:
            return render_template('login.html', error=True)
    return render_template('login.html')

@webapp.route('/signup', methods=['GET', 'POST'])
def signup_page():
    if request.method == 'POST':
        fname = request.form.get('first_name')
        lname = request.form.get('last_name')
        email = request.form.get('email')
        addr = request.form.get('address')
        pcode = request.form.get('post_code')
        uname = request.form.get('username')
        pwd = request.form.get('password')
        register_new_user(fname, lname, email, addr, pcode, uname, pwd)
        return redirect(url_for('login_page'))
    return render_template('signup.html')

if __name__ == '__main__':
    webapp.run(debug=True)
