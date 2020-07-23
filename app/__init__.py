import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy  # 数据库管理插件
from flask_migrate import Migrate  # 数据库迁移管理插件
from flask_login import LoginManager  # 登录管理插件
from flask_mail import Mail  # 实际的邮件发送而言，Flask有一个名为Flask-Mail的流行插件，可以使任务变得非常简单
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# from flask_babel import Babel


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'auth.login'
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
# babel = Babel(app)

from app.errors import bp as errors_bp

app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp

app.register_blueprint(auth_bp, url_prefix='/auth')

from app.main import bp as main_bp

app.register_blueprint(main_bp, url_prefix='/main')
# @babel.localeselector
# def get_locale():
#     return request.accept_languages.best_match(app.config['LANGUAGES'])


if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')
# routes模块是在底部导入的，而不是在脚本的顶部。 最下面的导入是解决循环导入的问题，这是Flask应用程序的常见问题
from app import models
