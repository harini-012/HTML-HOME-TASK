from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("11.06HTML TASK(1).html.html")
@app.route("/submit",methods=['POST'])
def submit():
    data={
    "name":request.form.get('fname'),
    "password":request.form.get('pwd'),
    
    }
    
    if not data["name"]:
        return f"Name Should not be Empty"
    elif len(data["password"])<6:
        return f"Password must have atleast 6 characters"
    else:
        return render_template("11.06HTML TASK result.html",data=data)
if __name__=='__main__':
    app.run(debug=True)