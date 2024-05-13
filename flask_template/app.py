from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('sign.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/userdata')
def userdata():
    return render_template('user_data.html')


@app.route('/submitdata',methods=['GET','POST'])
def submitdata():
    if request.method == "POST":
        profession = request.form['profession']
        name = request.form['name'] 
        email = request.form['email'] 
        password = request.form['password'] 
        user_data = {"user_profession":profession,
        "user_name":name,"user_email":email,
        "user_password":password}

        return user_data


    

if __name__ =="__main__":
    app.run(host="0.0.0.0",port=2525,debug=True)