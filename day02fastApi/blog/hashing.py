from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash():
    @staticmethod
    def bcrypt(password: str) :
        password = password[:72] if len(password) > 72 else password
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword

    def verify(hashed_password, plain_password):
        return pwd_cxt.verify(plain_password, hashed_password)