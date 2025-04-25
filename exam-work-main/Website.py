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
            return redirect(url_for('homepage'))
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


@webapp.route('/homepage')
def homepage():
    return render_template('homepage.html')


@webapp.route('/carbon_calculator', methods=['GET', 'POST'])
def carbon_calculator():
    if request.method == 'POST':
        appliance_ratings = [request.form.get(f'appliance{i}') for i in range(1, 13)]
        # Placeholder: calculation will be added later
        average_rating = "Coming soon"
        estimated_cost = "Coming soon"
        return render_template('carbon_calculator.html',
                               appliance_ratings=appliance_ratings,
                               average_rating=average_rating,
                               estimated_cost=estimated_cost)
    return render_template('carbon_calculator.html')


@webapp.route('/schedules')
def schedules():
    return render_template('schedules.html')

@webapp.route('/consultations', methods=['GET', 'POST'])
def consultations():
    connection = cursor = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if request.method == 'POST':
            consult_date = request.form.get('consult_date')
            topic = request.form.get('topic')
            phone = request.form.get('phone')
            address = request.form.get('address')

            cursor.execute('''
                INSERT INTO "Consultations" ("Consult_Date", "Topic", "Phone", "Address")
                VALUES (%s, %s, %s, %s)
            ''', (consult_date, topic, phone, address))

            connection.commit()
            return redirect(url_for('consultations'))

        cursor.execute('''
            SELECT "Consult_Date", "Topic", "Phone", "Address"
            FROM "Consultations"
            ORDER BY "Consult_Date" ASC
        ''')
        consultations = cursor.fetchall()
        return render_template('consultations.html', consultations=consultations)

    except Exception as err:
        print(f"Consultations page error: {err}")
        return "Error occurred"

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()



@webapp.route('/installations', methods=['GET', 'POST'])
def installations():
    connection = cursor = None
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()

        if request.method == 'POST':
            install_date = request.form.get('install_date')
            product = request.form.get('product')
            phone = request.form.get('phone')
            address = request.form.get('address')

            cursor.execute('''
                INSERT INTO "Installations" ("Install_Date", "Product", "Phone", "Address")
                VALUES (%s, %s, %s, %s)
            ''', (install_date, product, phone, address))

            connection.commit()
            return redirect(url_for('installations'))

        cursor.execute('''
            SELECT "Install_Date", "Product", "Phone", "Address"
            FROM "Installations"
            ORDER BY "Install_Date" ASC
        ''')
        bookings = cursor.fetchall()
        return render_template('installations.html', bookings=bookings)

    except Exception as err:
        print(f"Installations page error: {err}")
        return "Error occurred"

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()










if __name__ == '__main__':
    webapp.run(debug=True)
