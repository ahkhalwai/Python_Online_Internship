import os
from flask import Flask, render_template, request
from werkzeug import secure_filename
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/excelcsv')
def excelcsv():
    return render_template('excelcsv.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        df=pd.read_csv(f.filename)
        bf = df.sort_values (by=['Country'], ascending=True)
        bf.to_csv('Adat.csv')
        return bf.to_html()
    return render_template('excelcsv.html')

@app.route('/nrows', methods=['GET', 'POST'])
def nrows():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        df=pd.read_csv(f.filename,index_col=1)
        #bf = df.sort_values (by=['Country'], ascending=True)
        return df.to_html()
    return render_template('excelcsv.html')



@app.route('/decending', methods=['GET', 'POST'])
def decending():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        df=pd.read_csv(f.filename)
        bf = df.sort_values (by=['Country'], ascending=False)
        bf.to_csv('Ddat.csv')
        return bf.to_html()
    return render_template('excelcsv.html')

@app.route('/excelasc', methods=['GET', 'POST'])
def excelasc():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        df=pd.read_excel(f.filename)
        bf = df.sort_values (by=['Name'], ascending=True)
        bf.to_excel ('Adat.xlsx')
        return df.to_html()
    return render_template('excelcsv.html')


@app.route('/exceldec', methods=['GET', 'POST'])
def exceldec():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        df=pd.read_excel(f.filename)
        bf = df.sort_values (by=['Name'], ascending=False)
        bf.to_excel('Ddat.xlsx')
        return bf.to_html()
    return render_template('excelcsv.html')


if __name__=='__main__':
    app.run(debug=True)