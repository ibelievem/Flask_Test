# __author__: xws    
# time: 2019/8/30 23:10

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session


app=Flask(__name__,template_folder="templates",static_folder="static")


# flask 中所有的默认配置文件
print(app.config)

# app.config["DEBUG"]=True
app.config.from_object("settings.DevelopmentConfig")






if __name__ == '__main__':
    app.run()

