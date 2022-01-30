from json.tool import main
import os
from flask import Flask,request,render_template,flash, redirect, url_for
from werkzeug.utils import secure_filename
import sys
sys.path.append('/home/a/GPT/RTVC')
import RTVC.demo_cli as RTC

 

 
 
 
UPLOAD_FOLDER = '/home/a/GPT/appUploads'
ALLOWED_EXTENSIONS = {"mp3","wav","m4a","flac"}
 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "a"
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT']= False
 
@app.route('/')
def home():
   return render_template("home.html")
 
def allowed_file(filename):
   return '.' in filename and \
          filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
@app.route('/upload', methods=['GET','POST'])
def upload_file():
   text1=""
  
   if request.method == 'POST':
       # check if the post request has the file part
      
       file = request.files['inputFile']
       text1 = request.form["prompt"]
       #print(text)
       # If the user does not select a file, the browser submits an
       # empty file without a filename.
       if file.filename == '':
           flash('No selected file')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           fullPath = "/home/a/GPT/appUploads" + filename
           print(fullPath)
           RTC.RTC(text1,fullPath)
           return redirect(url_for('upload_file', name=filename))
   print(text1 + "dsfdsfsdfdfsd")     
   return text1