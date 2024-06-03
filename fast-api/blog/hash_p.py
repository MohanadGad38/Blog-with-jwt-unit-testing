from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class hashing():
    def create_hash(password: str):
        hash_password = pwd_context.hash(password)
        return hash_password

    def verfiy(hash_password, password):
        return pwd_context.verify(password, hash_password)
