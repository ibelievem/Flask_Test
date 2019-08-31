# __author__: xws    
# time: 2019/8/30 23:10

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import url_for


app=Flask(__name__,template_folder="templates",static_folder="static")


# flask 中所有的默认配置文件
# print(app.config)

# app.config["DEBUG"]=True
# 引入配置文件
app.config.from_object("settings.DevelopmentConfig")


@app.route("/index/<int:nid>",methods=["GET","POST"])
# endpoint="n1" 代指 /index，若不定义 endpoint，则默认值为 函数名 index
def index(nid):
    print(url_for("index",nid=777))
    return "Index"



if __name__ == '__main__':
    app.run()

