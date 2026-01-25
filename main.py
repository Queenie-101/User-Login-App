from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
#routing-display the home page first
@app.route('/',methods=['GET','POST'])
#function to login
def login():
    if request.method=='POST':
        #username and password
        username=request.form['username']
        password=request.form['password']
        #redirect the user
        return redirect(url_for('success',name=username,passw=password))
    return render_template('home.html')
#dashboard function
@app.route('/success/<name>/<passw>')
def success(name,passw):
    return render_template('dashboard.html',name=name,passw=passw)
#logout function
@app.route('/logout')
def logout():
    return redirect(url_for('login'))
if __name__=='__main__':
    app.run(debug=True)