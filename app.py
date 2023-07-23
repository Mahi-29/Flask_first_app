# creating simple flask application.
from flask import Flask, redirect, url_for, render_template, Response, request

##create flask app

app =Flask(__name__)

@app.route("/")
def home():
    return "<p><h1>Hello World!</h1></p>"

@app.route('/welcome')
def welcome():
    return "welcome to flask tutorial"
@app.route('/index')
def index():
    return render_template('index.html') #this file is to be stored in the templates folder only

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and score is"+str(score)


@app.route('/fail/<int:score>')
def fail(score):
    return "The person is failed and score is "+str(score)

@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method == 'GET':
        return render_template('calculate.html',results=False)
    
    else:
        print(request.form)
        maths = float(request.form['Maths'])
        science = float(request.form['science'])
        english = float(request.form['english'])
        average_marks = (maths+science+english)/3
        result =""
        if average_marks >= 50:
            result = "success"
        else:
            result='fail'
        # return redirect(url_for(result,score=average_marks))
        return render_template('calculate.html',results=average_marks)




    

if __name__ == "__main__":
    app.run(debug=True,  host='0.0.0.0')
