from  flask import  Blueprint,render_template,g,request,redirect,url_for,flash
from decorators import login_required
from .forms import FeedbackForm
from models import FeedbackModel
from exts import db
from sqlalchemy import or_

bp = Blueprint("feedback",__name__,url_prefix="/")


# @bp.route("/")
# def index():
#     shares = FeedbackModel.query.order_by(db.text("-create_time")).all()
#     return render_template("index.html",feedbacks = feedbacks)


@bp.route("/feedback/public",methods=['GET','POST'])
@login_required
def public_feedback():
    # 判断是否登录，如果没有登录，跳转到登录页面
    if request.method =='GET':
        return render_template("public_feedback.html")
    else:
        form = FeedbackForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            share = FeedbackModel(title=title,content=content,author=g.user)
            db.session.add(share)
            db.session.commit()
            return redirect("/")
        else:
            flash("标题或内容格式错误！")
            return redirect(url_for("feedback.public_feedback"))

@bp.route("/feedback/<int:feedback_id>")
def feedback_detail(feedback_id):
    feedback = FeedbackModel.query.get(feedback_id)
    return render_template("public_feedback.html", feedback=feedback)

# @bp.route("/feedbackcomment/<int:feedback_id>",methods=['POST'])
# @login_required
# def feedbackcomment(feedback_id):
#     form = FeedbackcommentForm(request.form)
#     if form.validate():
#         content = form.content.data
#         feedbackcomment_model = FeedbackContentModel(content=content,author=g.user,share_id=feedback_id)
#         db.session.add(feedbackcomment_model)
#         db.session.commit()
#         return redirect(url_for("feedback.feedback_detail",share_id=feedback_id))
#     else:
#         flash("表单验证失败！")
#         return redirect(url_for("feedback.feedback_detail",share_id=feedback_id))