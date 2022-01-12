from flask import Flask

# 애플리케이션 팩토리
# create_app 말고 다른걸 사용시 정상 동작하지 않음, create_app은 플라스크 내부에 정의된 함수명


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello_pybo():
        return "Hello Pybo!"

    return app


if __name__ == "__main__":
    app.run()
