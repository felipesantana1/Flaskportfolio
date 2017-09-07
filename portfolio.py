from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')

def myPort():
    return render_template('myPort.html') 
                                          
# app = Flask(__name__)                     
                                          
@app.route('/webPage')

def webPage():
  return render_template('aWebPage.html')

@app.route('/aboutMe')

def aboutMe():
  return render_template('aboutMe.html')
app.run(debug=True)