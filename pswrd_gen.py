from random import choices
import string

def generate_password(len: int) -> str:
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choices(chars, k = len))
    return password
