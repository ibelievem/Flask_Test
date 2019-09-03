# __author__: xws    
# time: 2019/8/30 23:10

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for
import functools


app=Flask(__name__,template_folder="templates",static_folder="static")

app.config.from_object("settings.DevelopmentConfig")


STUDENT_DICT={
    1:{"name":"张三","age":38,"gender":"男"},
    2:{"name":"李四","age":33,"gender":"女"},
    3:{"name":"王五","age":22,"gender":"男"},
}


# 类似于 django 的 process_request
@app.before_request
def xxxxxx():
    if request.path=="/login":
        # 通过继续执行
        return None
    if session.get("user"):
        return None
    # 中断执行
    return redirect("/login")


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    user=request.form.get("user")
    pwd=request.form.get("pwd")
    if user=="xws" and pwd=="123":
        session["user"]=user
        return redirect("/index")
    return render_template("login.html",error="用户名或者密码错误")


@app.route("/index")
def index():
    return render_template("index.html",stu_dic=STUDENT_DICT)


@app.route("/delete/<int:nid>")
def delete(nid):
    del STUDENT_DICT[nid]
    return redirect(url_for("index"))


@app.route("/detail/<int:nid>")
def detail(nid):
    info=STUDENT_DICT[nid]
    return render_template("detail.html",info=info)


if __name__ == '__main__':
    app.run()

