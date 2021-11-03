import hashlib
import os
from dotenv import load_dotenv
load_dotenv()

HASH_KEY = os.getenv('HASH_KEY')


def create_hash(password: str):
    md5 = hashlib.md5(HASH_KEY.encode())
    md5.update(password.encode())
    return md5.hexdigest()
