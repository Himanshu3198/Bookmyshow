from flask import Flask

from apps.Controller.userController import user_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)


@app.route('/homepage')
def index():
    return "this is welcome page for flask development"


if __name__ == '__main__':
    app.run(debug=True)
