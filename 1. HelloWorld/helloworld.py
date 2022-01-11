# flask는 폼(form), 데이터베이스(Database)를 처리하는 기능이 없다.
# flask는 필요시 확장 모듈을 통해 보완할 수 있다.

# flask run 명령어를 실행할 경우 에러발생 -
# FLASK_APP 환 경변수를 지정하지 않을 경우 app.py를 기본 애플리케이션으로 인식
# set FLASK_APP=helloworld를 추가로 명령어 입력해준다.
# 그래도 warning 발생
# flask는 서버를 실행할 때 아무런 설정을 하지 않는다면 기본 운영 환경으로 실행


from flask import Flask
# flask application을 생성하는 코드, __name__에는 모듈명이 담긴다. 여기는 helloworld
app = Flask(__name__)


@app.route('/')  # 특정 URL에 접속하면 바로 다음 줄에 이쓴 함수를 호출하는 플라스크의 데코레이터
def hello():
    return "Hello world!"


if __name__ == "__main__":
    app.run()
