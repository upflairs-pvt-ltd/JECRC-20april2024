from flask import Flask,render_template,url_for,request
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
        return "hii i am good"



if __name__ == "__main__":
    app.run(debug=True)



