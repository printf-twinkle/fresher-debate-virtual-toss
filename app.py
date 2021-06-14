from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        stu1=""
        stu2=""
        stu1_first_name = request.form["stu11"]
        stu1_second_name = request.form["stu12"]
        stu2_first_name = request.form["stu21"]
        stu2_second_name = request.form["stu22"]
        stu1=stu1_first_name+stu1_second_name
        stu2=stu2_first_name+stu2_second_name
        print(stu1_first_name,stu1_second_name,stu2_first_name,stu2_second_name)
        return redirect(url_for("toss",stu1=stu1,stu2=stu2))
    return render_template("home.html")

@app.route('/toss/<stu1>/<stu2>')
def toss(stu1,stu2):
    return render_template("toss.html",stu1=stu1,stu2=stu2)

if __name__=='__main__':
    app.run(debug=True)