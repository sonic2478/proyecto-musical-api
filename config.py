class Config: 
    SECRET_KEY='fdfzdzdfszsdfghdsfghsdfzuyggh'

class DevelopmentConfig(Config):
    DEBUG           = True
    MYSQL_HOST      = 'localhost' 
    MYSQL_USER      = 'root'
    MYSQL_PASSWORD  = ''
    MYSQL_DB        = 'musical'

config = {
    'development': DevelopmentConfig
}