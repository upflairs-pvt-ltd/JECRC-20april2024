from flask import Flask , render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict' , methods= ['GET','POST'])
def predict():
    if request.method == 'POST':
        message = request.form['email_message']  
        return message

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=2525,debug=True)