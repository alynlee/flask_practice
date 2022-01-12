from pybo import db


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # primary_key: 기본키 지정, 중복을 허용하지 않음
    # flasks는 기본키로 지정하고 데이터타입이 db.Integer이면 자동으로 값이 증가하는 특성이 있음
    subject = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)  # 빈값을 허용 nullable


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey(
        'question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
