from flask import Flask

# hello_pybo는 URL 에서 /로 맵핑
# app.route('/') 애너테이션이 맵핑을 만들어 줌
# app.route와 같은 애너테이션으로 매핑되는 함수를 라우트 함수라고 한다.
# 지금까지 해온걸로는 URL을 추가할때마다 create_app에 추가해줘야한다.
# 블루프린트를 사용하면 라우트 함수를 구조적으로 관리가 가능하다.


def create_app():
    app = Flask(__name__)

    from .views import main_views
    app.register_blueprint(main_views.bp)  # 블루프린트 객체등록

    return app


if __name__ == "__main__":
    app.run()
