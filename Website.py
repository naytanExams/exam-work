from flask import Flask, render_template, request, redirect, url_for, Flask
import psycopg2

app = Flask(__name__)
app.secret_key = "SECRET-KEY"


hostname = 'localhost'
database = 'postgres'
db_username = 'postgres'
db_password = 'postgres'
db_port = 5432


def check_user(username, password):
    conn=None
    cur=None

    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = db_username,
            password = db_password,
            port = db_port)
        
        cur = conn.cursor()
        
        cur.execute('SELECT * FROM "Account_Details" WHERE "Username" = %s and "Password" = %s', (username, password))

        in_db = cur.fetchone()

        return in_db
    except Exception as error:
        print(f"ERROR: {error}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()



def insert_user(first_name, last_name, email, address, postcode, username, password):
    conn=None
    cur=None

    try:
        conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = db_username,
            password = db_password,
            port = db_port)
        
        cur = conn.cursor()
        
        cur.execute('''INSERT INTO "User_Details" ("Forename", "Surname", "Email", "Address", "Post_code")
                       VALUES (%s, %s, %s, %s, %s) RETURNING "User_ID" ''', (first_name, last_name, email, address, postcode))

        user_ID = cur.fetchone()[0]

        cur.execute(''' INSERT INTO "Account_Details" ("Username", "Password", "User_ID")
                        VALUES (%s, %s, %s)''', (username, password, user_ID))

        conn.commit()
    except Exception as error:
        print(f"ERROR: {error}")
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()


@app.route('/')
def index():
    return render_template('Main.html')

@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        in_db = check_user(username, password)

        if in_db:
            return redirect(url_for('index'))
        else:
            render_template('login.html')


    return render_template('login.html')

@app.route('/singup', methods=['GET', 'POST'])
def signup():

    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        address = request.form.get('address')
        postcode = request.form.get('post_code')
        username = request.form.get('username')
        password = request.form.get('password')

        insert_user(first_name, last_name, email, address, postcode, username, password)

    return render_template('signup.html')


if __name__ == "__main__":
    app.run(debug=True)





from flask import Flask, render_template, request, redirect, url_for
import psycopg2

webapp = Flask(__name__)
webapp.secret_key = "CHANGE_THIS_SECRET"

DB_CONFIG = {
    "host": "localhost",
    "dbname": "postgres",
    "user": "postgres",
    "password": "postgres",
    "port": 5432
}

def validate_login(user, pwd):
    connection = cursor = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        query = '''SELECT * FROM "Account_Details" WHERE "Username" = %s AND "Password" = %s'''
        cursor.execute(query, (user, pwd))
        return cursor.fetchone()
    except Exception as err:
        print(f"Login error: {err}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def register_new_user(fname, lname, email, addr, pcode, uname, pwd):
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
            (uname, pwd, user_id)
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
        if validate_login(uname, pwd):
            return redirect(url_for('main_page'))
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
