from  flask import  Blueprint,render_template,g,request,redirect,url_for,flash
from decorators import login_required
# from .forms import ShareForm,CommentForm,FeedbackForm,FeedbackcommentForm
# from models import ShareModel,ShareContentModel,FeedbackModel,FeedbackContentModel
from .forms import ShareForm,CommentForm
from models import ShareModel,ShareContentModel
from exts import db
from sqlalchemy import or_

bp = Blueprint("share",__name__,url_prefix="/")

@bp.route("/")
def index():
    shares = ShareModel.query.order_by(db.text("-create_time")).all()
    return render_template("index.html",shares = shares)

@bp.route("/share/public",methods=['GET','POST'])
@login_required
def public_share():
    # 判断是否登录，如果没有登录，跳转到登录页面
    if request.method =='GET':
        return render_template("public_share.html")
    else:
        form = ShareForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            share = ShareModel(title=title,content=content,author=g.user)
            db.session.add(share)
            db.session.commit()
            return redirect("/")
        else:
            flash("标题或内容格式错误！")
            return redirect(url_for("share.public_share"))

@bp.route("/share/<int:share_id>")
def share_detail(share_id):
    share = ShareModel.query.get(share_id)
    return render_template("detail.html", share=share)

@bp.route("/comment/<int:share_id>",methods=['POST'])
@login_required
def comment(share_id):
    form = CommentForm(request.form)
    if form.validate():
        content = form.content.data
        comment_model = ShareContentModel(content=content,author=g.user,share_id=share_id)
        db.session.add(comment_model)
        db.session.commit()
        return redirect(url_for("share.share_detail",share_id=share_id))
    else:
        flash("表单验证失败！")
        return redirect(url_for("share.share_detail",share_id=share_id))

@bp.route("/search")
def search():
    # /search?q=xxxx
    q = request.args.get("q")
    # filter_by:直接使用字段名称；filter：使用模型.字段名称
    shares = ShareModel.query.filter(or_(ShareModel.title.contains(q),ShareModel.content.contains(q))).order_by(db.text("create_time"))
    return render_template("index.html",shares=shares)




