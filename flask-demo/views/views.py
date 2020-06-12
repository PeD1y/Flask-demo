from flask import request,redirect,render_template,flash,session,url_for
import requests
import json
from search_book import app

@app.route('/')
def home():
    return render_template('entries/home.html')

@app.route('/searchß')
def search():
    return render_template('entries/search.html')

@app.route('/add',methods=['GET','POST'])
def add():
    if request.method == 'POST':
        if request.form['keyword']:
            sbin =  request.form['keyword']
            data = (requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{sbin}")).json()
            context = {
                "name" : data["items"][0]["volumeInfo"]["title"],
                "writer" : data["items"][0]["volumeInfo"]["authors"][0],
                "publication" : data["items"][0]["volumeInfo"]["publishedDate"],
                "description" : data["items"][0]["volumeInfo"]["description"]
                }
            return render_template('entries/candidate.html',context=context)
        else:
            return  redirect(url_for('entries/add.html'))
    else:
        return render_template('entries/add.html')