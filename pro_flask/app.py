# __author__: xws    
# time: 2019/8/30 23:10

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session


# app=Flask(__name__,template_folder="templates",static_folder="static",static_url_path="static")
app=Flask(__name__,template_folder="templates",static_folder="static")
app.secret_key="eds3dsggd"


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        # return "Login"
        return render_template("login.html")

    # get 传递请求
    # request.args

    # post 传递请求
    user=request.form.get("user")
    pwd=request.form.get("pwd")

    if user=="xws" and pwd =="123":
        session["user"]=user
        return redirect("/index")

    return render_template("login.html",error="用户名或密码错误")
    # return render_template("login.html",**{"error":"用户名或密码错误"})


@app.route("/index")
def index():
    user=session.get("user")
    print(user)
    if not user:
        return redirect("/index")
    return render_template("/index.html")


if __name__ == '__main__':
    app.run()

