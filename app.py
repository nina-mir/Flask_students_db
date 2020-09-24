import sqlite3

from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_student(student_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM students WHERE id = ?',
                        (student_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        
        fname = request.form['fname']
        lname = request.form['lname']
        student_id = request.form['id']
        pronouns = request.form['pronouns']
        mail_add = request.form['mail_add']
        email   = request.form['email']
        gpa     = request.form['gpa']


        if not (fname and lname and student_id) :
            flash('ID, first and last names are all required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO students (id, fname, lname, pronouns, mail_add, email, gpa) \
                        VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (student_id, fname, lname, pronouns, mail_add, email, gpa ))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        
        # fname = request.form['fname']
        # lname = request.form['lname']
        # student_id = request.form['id']

        # if not (fname and lname and student_id) :
        #     flash('ID, first and last names are all required!')
        # else:
        #     conn = get_db_connection()
        #     conn.execute('INSERT INTO students (id, fname, lname, pronouns, mail_add, email, gpa) \
        #                 VALUES (?, ?, ?, ?, ?, ?, ?)',
        #                 (student_id, fname, lname, pronouns, mail_add, email, gpa ))
        #     conn.commit()
        #     conn.close()
        return redirect(url_for('index'))

    return render_template('search.html')


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
