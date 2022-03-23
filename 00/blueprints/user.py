from  flask import  Blueprint,render_template,request,redirect,url_for,jsonify,session,flash
from  exts import mail,db
from flask_mail import Message
from models import EmailCaptureModel,UserModel
import string
import random
from datetime import datetime
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash


bp = Blueprint("user",__name__,url_prefix="/user")

@bp.route("/login",methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email = email).first()
            if user and check_password_hash(user.password,password):
                session['user_id'] = user.id
                return redirect("/")
            else:
                flash("邮箱和密码不匹配！")
                return redirect(url_for("user.login"))
        else:
            flash("邮箱或密码格式错误！")
            return redirect(url_for("user.login"))

@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            capture = form.capture.data
            username = form.username.data
            password = form.password.data

            # md5("ljh") = sgsdfagfsjgjk
            hash_password = generate_password_hash(password)
            user = UserModel(email=email, username=username, password=hash_password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("user.login"))
        else:
            return redirect(url_for("user.register"))


@bp.route("/logout")
def logout():
    #清除session中所有的数据
    session.clear()
    return redirect(url_for('user.login'))


# mamcached/redis/数据库

@bp.route("/capture",methods=['POST'])
def get_capture():
    # GET POST
    email = request.form.get("email")
    letters = string.ascii_letters + string.digits
    random.sample(letters,4)
    capture = "".join(random.sample(letters,4))
    if email:
        message = Message(
            subject="Test",
            recipients=[email],
            body=f"【智能共享柜】：您的验证码是：{capture},请不要告诉任何人哦！"
        )
        mail.send(message)
        capture_model=  EmailCaptureModel.query.filter_by(email=email).first()
        if capture_model:
            capture_model.capture = capture
            capture_model.create_time = datetime.now()
            db.session.commit()
        else:
            capture_model = EmailCaptureModel(email = email,capture=capture)
            db.session.add(capture_model)
            db.session.commit()
        print("capture",capture)
        # code:200,成功的正常的请求
        return jsonify({"code":200})
    else:
        #code:400,客户端错误
        return jsonify({"code":400,"message":"请先传递邮箱！"})