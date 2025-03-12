from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("11.03.html")
@app.route("/submit",methods=["POST"])
def submit():
    name=request.form.get("name")
    rno=request.form.get("rno")
    
    comments=request.form.get("comment")
   
    return f"Received Name:{name},Roll No:{rno},Comments:{comments}.Your response has been recorded."
if __name__=="__main__":
    app.run(debug=True)
    