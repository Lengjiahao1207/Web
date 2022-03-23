from exts import db
from datetime import datetime

class EmailCaptureModel(db.Model):
    __tablename__="email_capture"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    email = db.Column(db.String(100),nullable=False,unique=True)
    capture = db.Column(db.String(10),nullable=False)
    creat_time = db.Column(db.DateTime,default=datetime.now)

class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False, unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now)

class ShareModel(db.Model):
    __tablename__ = "share"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    author = db.relationship("UserModel",backref="shares")

class ShareContentModel(db.Model):
    __tablename__ = "share_content"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    share_id = db.Column(db.Integer,db.ForeignKey("share.id"))
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    share = db.relationship("ShareModel",backref=db.backref("share_contents",order_by=create_time.desc()))
    author = db.relationship("UserModel",backref="share_contents")

class FeedbackModel(db.Model):
    __tablename__ = "feedback"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text,nullable=False)
    create_time = db.Column(db.DateTime,default=datetime.now)
    author_id = db.Column(db.Integer,db.ForeignKey("user.id"))

    author = db.relationship("UserModel",backref="feedbacks")
#
# class FeedbackContentModel(db.Model):
#     __tablename__ = "feedback_content"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     content = db.Column(db.Text, nullable=False)
#     create_time = db.Column(db.DateTime, default=datetime.now)
#     feedback_id = db.Column(db.Integer,db.ForeignKey("feedback.id"))
#     author_id = db.Column(db.Integer,db.ForeignKey("user.id"))
#
#     share = db.relationship("FeedbackModel",backref=db.backref("feedback_contents",order_by=create_time.desc()))
#     author = db.relationship("UserModel",backref="feedback_contents")

