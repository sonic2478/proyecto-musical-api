from werkzeug.security import check_password_hash
from flask_login import UserMixin
class User(UserMixin):
    def __init__(self,id,nombreu,correou,claveu,perfilu) -> None:
        self.id         = id
        self.nombreu    = nombreu
        self.correou    = correou
        self.claveu     = claveu
        self.perfilu    = perfilu
    
    @classmethod 
    def validar_clave(self,claveCifrada,claveu):
        return check_password_hash(claveCifrada,claveu)
