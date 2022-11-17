# flask-app
Realization of a Flask-app tutorial from digitalocean.com

# URL 
https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

# Creation of virtual envionment
python3 -m venv .flask-app

# Activation of virtual environment

# Linux
source .flask-app/bin/activate

# Windows
source .flask-app/Scripts/activate

# Installing requirements 
pip3 install -r requirements.txt

# Create the Database
python3 init_db.py

# RUNNING the APP: Execute this command
FLASK_APP=index.py flask run

# Create a secret password
echo "YOUR_PASSWORD">secret_key.txt
