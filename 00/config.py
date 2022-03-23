#数据库配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = '智能共享柜'
USERNAME = 'root'
PASSWORD = '1207'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = "2001120700ljh"

# 邮箱配置
# 该项目用的是QQ邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "2251943163@qq.com"
MAIL_PASSWORD = "sbqvmzhifqpudjge"
MAIL_DEFAULT_SENDER = "2251943163@qq.com"
