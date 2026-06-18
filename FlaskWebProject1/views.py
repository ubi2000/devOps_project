"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from flask import jsonify
import mysql.connector
import os


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/version')
def version():
    return jsonify({
        "instance": os.environ.get('INSTANCE_NAME', 'unknown'),
        "version": "2.0"
    })
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/db-time')
def db_time():
    try:
        conn = mysql.connector.connect(
        host=os.environ.get('MYSQL_HOST', 'mysql-db'),
        user='root',
        password='password',
        database='mydb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT CURRENT_TIMESTAMP();")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({"mysql_time": str(result[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
        # saklndlk