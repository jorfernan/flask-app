#!/usr/bin/env python3
from flask import Flask, render_template, request,url_for,flash,redirect
import sqlite3
from werkzeug.exceptions import abort

# Database File
DB_FILE = 'database.db'
#Location of password
SECRET_KEY_FILE = "secret_key.txt"

with open(SECRET_KEY_FILE,"r") as secret_file_key:
    key = secret_file_key.read().strip()

app = Flask(__name__)
app.config['SECRET_KEY'] = key


""" Function that establish a connection to the database file"""
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

"""Function that gets an specific post taking its id as an argument"""
def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',(post_id,)).fetchone()
    conn.close()
    # Checking for results, if not returns a 404
    if post is None:
        abort(404)
    return post
    

@app.route('/')
def index():
    # Get all posts from database file
    conn = get_db_connection() # Creating conection
    posts = conn.execute('SELECT * FROM posts').fetchall() # Executin query
    conn.close() # Closing connection
    return render_template("index.html",posts=posts)

#Route for specific post request
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)


# Function that displays a form template
@app.route('/create', methods = ('GET','POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
            
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))