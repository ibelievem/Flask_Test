# _*_ coding:utf-8 _*_
#@Author = zhoupengfei
#@Time = 2018/8/8 14:39
from flask import Flask #引入核心处理模块
from flask import Response, json, jsonify, request
#通过当前文件构建一个app应用 -- 当前文件就是web app程序的入口
app  = Flask(__name__)

#定义视图处理函数
@app.route("/")
def index():#默认get请求
    return "<h1>hello flask!</h1>"

@app.route("/login")
def login():
    return "<h2>用户已经登录</h2>"

@app.route("/regist")
def regist():
    return "<h2>用户已经注册成功</h2>"

@app.route("/test",methods=["POST"])
def test():

    name = request.form.get('name')
    pwss = request.form.get('pwss')
    #定义字典
    resalt = {
        "data": None,
        "msg": "返回成功",
        "code": 200}

    resalt['name'] = name
    resalt['pwss'] = pwss

    return json.dumps(resalt)

if __name__ == "__main__":

    #运行程序
    app.run(debug=True)

