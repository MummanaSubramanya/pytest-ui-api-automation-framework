import string
import random
import time

from utils.constants import USER_PASSWORD

RANDOM_LENGTH = 3

def get_random_first_name():
    unqiue_value = generate_random_alphanumeric(RANDOM_LENGTH)
    return f'FN_{unqiue_value}'


def get_random_last_name():
    unqiue_value = generate_random_alphanumeric(RANDOM_LENGTH)
    return f'LN_{unqiue_value}'


def get_random_email():
    unqiue_value = generate_random_alphanumeric(RANDOM_LENGTH)
    return f'{unqiue_value}@gmail.com'

def get_password():
    return USER_PASSWORD

def generate_random_alphanumeric(length = 2):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    timestamp = time.strftime("%Y%m%d%H%M%S")
    unique_string = f"{random_string}{timestamp}"
    return unique_string