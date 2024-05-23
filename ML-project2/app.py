from flask import Flask , render_template,url_for,request
import joblib 
bow = joblib.load('bow.lb')
model = joblib.load('model.lb')


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict' , methods= ['GET','POST'])
def predict():
    if request.method == 'POST':
        message = request.form['email_message'] 
        ls = [message]
        x = bow.transform(ls) 

        pred = model.predict(x)[0]
        label = {'0':'ham','1':'spam'}
        

        return label[str(pred)]

if __name__ =="__main__":
    app.run(host='0.0.0.0',port=2525,debug=True)