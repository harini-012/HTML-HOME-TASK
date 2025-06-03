from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.method=="POST":
        data={"name":request.form.get("name"),
        "gender":request.form.get("gender"),
       "email":request.form.get("email"),
        "phoneno":request.form.get("number"),
        "file":request.files.get("photo").filename if request.files.get("photo") else "No photo updated",
        "position":request.form.get("position"),
        "exp":request.form.get("exp"),
        "cover":request.form.get("cover"),}
        return render_template("02.06reuslt.html",data=data)
    return render_template("02.06 HTML TASK.html")


if __name__=='__main__':
    app.run(debug=True)