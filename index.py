#!/usr/bin/env python3
from flask import Flask, render_template
import sqlite3

# Database File
DB_FILE = 'database.db'

app = Flask(__name__)

""" Function that establish a connection to the database file"""
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    # Get all posts from database file
    conn = get_db_connection() # Creating conection
    posts = conn.execute('SELECT * FROM posts').fetchall() # Executin query
    conn.close() # Closing connection
    return render_template("index.html")
