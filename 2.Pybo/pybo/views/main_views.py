from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list'))
    #question : 등록된 블루프린트 이름
    #_list : 블루프린트에 등록된 함수 
    #url_for : 라우트가 설정된 함수명으로 URL을 찾아준다.

