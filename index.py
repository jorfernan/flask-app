#!/usr/bin/env python3
from flask import Flask, render_template
import sqlite3
from werkzeug.exceptions import abort

# Database File
DB_FILE = 'database.db'

app = Flask(__name__)

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