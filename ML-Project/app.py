from flask import Flask,render_template,url_for,request
import joblib
model = joblib.load("rfmodel.lb")

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/inputdata')
def inputdata():
    return render_template('input_data.html')


@app.route('/prediction' , methods=['GET','POST'])
def prediction():
    
    if request.method == 'POST':

        region = request.form['region']
        children = request.form['children']
        smoker = request.form['smoker']
        age = request.form['age']
        bmi = request.form['bmi']
        gender = request.form['gender']
        user_data = [region,children,smoker,age,bmi,gender]
        # model.predict(x_variable )
        return user_data



if __name__ == "__main__":
    app.run(debug=True)



