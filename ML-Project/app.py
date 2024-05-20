from flask import Flask,render_template,url_for,request,jsonify
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
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        age = int(request.form['age'])
        bmi = int(request.form['bmi'])
        gender = int(request.form['gender'])
        region_northeast = 0
        region_northwest = 0
        region_southeast = 0
        region_southwest = 0
        if region == "ne":
            region_northeast = 1
        elif region == "nw":
            region_northwest = 1
        elif region == "se":
            region_southeast = 1
        else:
            region_southwest = 1
        user_data = [[age,gender,bmi,children,smoker,
                region_northeast,region_northwest,
                region_southeast,region_southwest]]

        pred = model.predict(user_data)[0]
        return jsonify(pred)



if __name__ == "__main__":
    app.run(debug=True)



