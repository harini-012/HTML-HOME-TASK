from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=["GET","POST"])
def form():
    if request.method =='POST':
        data={"name":request.form.get('name'),
        "email":request.form.get('email'),
        "mobile":request.form.get('number'),
        }
        return render_template("19.03result.html",data=data)
    return render_template("19.03.html")
if __name__=='__main__':
    app.run(debug=True)