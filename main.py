from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)
app.static_folder = 'static'

#connect to Mongo database
client = MongoClient('mongodb://localhost:27017')
db = client['flaskdb']
collection = db['form']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'username': request.form['username'],
            'email': request.form['email'],
            'pass': request.form['pass'],
        }
        
        collection.insert_one(data)
        
        return redirect(url_for('about'))
    
if __name__ == '__main__':
    app.run(debug=True)
    