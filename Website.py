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