from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy  # 数据库管理插件
from flask_migrate import Migrate  # 数据库迁移管理插件
from flask_login import LoginManager  # 登录管理插件
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
# routes模块是在底部导入的，而不是在脚本的顶部。 最下面的导入是解决循环导入的问题，这是Flask应用程序的常见问题
from app import routes, models
