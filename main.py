from flask import Flask,render_template,request,redirect,url_for,session
app=Flask(__name__)
#secret key
app.secret_key="secretkey"
#temporary storage for users
users={}
#routing-display the home page first
@app.route('/',methods=['GET','POST'])
#function to login
def login():
    if request.method=='POST':
        #username and password
        username=request.form['username']
        password=request.form['password']
        if username in users and users[username]==password:
            session['username']=username#add the user to session
            #redirect the user  
            return redirect(url_for('success',name=username,passw=password))
        else:
            return "Invalid username or password. Please try again."
    return render_template('home.html')
#dashboard function
@app.route('/success/<name>/<passw>')
def success(name,passw):
    return render_template('dashboard.html',name=name,passw=passw)
#logout function
@app.route('/logout')
def logout():
    return redirect(url_for('login'))
#sign up function
@app.route('/signuo',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        #get the username and password
        username=request.form['username']
        password=request.form['password']
        if username in users:
            return "Username already exists. Please choose a different username."
        else:
            #store them in the users dictionary
            users[username]=password
            #redirect to the login page
            return redirect(url_for('login'))
    return render_template('signup.html')
if __name__=='__main__':
    app.run(debug=True)