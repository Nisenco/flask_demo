import os
import db_setting


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = db_setting.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置每页显示的条数
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es']
    # ADMINS = 'SUCCESSW2M@163.com'
    # todo 增加邮箱配置 未完成
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('SUCCESSW2M@163.com')
    MAIL_PASSWORD = os.environ.get('W2308090624M')
    ADMINS = ['2308090624@qq.com']
