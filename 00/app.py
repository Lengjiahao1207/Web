from flask import Flask,session,g
from flask_cors import CORS
import config
from exts import db
from exts import mail
# from blueprints.share import bp as share_bp
from blueprints import share_bp
from blueprints import user_bp
# from blueprints import feedback_bp
from flask_migrate import Migrate
from models import UserModel

#实例化server，把当前这个python文件当做一个服务，__name__代表当前这个python文件
# server = flask.Flask(__name__)
# # r'/*' 是通配符，让本服务器所有的URL 都允许跨域请求
# CORS(server, resources=r'/*')

app = Flask(__name__)
# 绑定数据库
app.config.from_object(config)
# 初始化app

db.init_app(app)
mail.init_app(app)

migrate = Migrate(app,db)

app.register_blueprint(share_bp)
app.register_blueprint(user_bp)
# app.register_blueprint(feedback_bp)

@app.before_request
def before_request():
    user_id = session.get("user_id")
    if user_id:
        try:
            user = UserModel.query.get(user_id)
            # 给g（全局变量）绑顶一个叫做user的变量，它的值是user这个变量
            # setattr(g,"user",user)
            g.user = user
        except:
            g.user = None

#请求来了 -> before_request -> 视图函数 -> 视图函数中返回模板 -> context_processor

@app.context_processor
def context_processor():
    if hasattr(g,"user"):
        return {"user":g.user}
    else:
        return{}



if __name__ == '__main__':
    # 连同一网段，其他设备才可以访问该网站
    app.run(host='0.0.0.0',port=5000)
