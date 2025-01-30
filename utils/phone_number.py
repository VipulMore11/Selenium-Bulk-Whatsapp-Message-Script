import re

def is_phone_valid(phone_number):
    INDIAN_PHONE_REGEX = r"^\+91\d{10}$" 

    return bool(re.match(INDIAN_PHONE_REGEX, phone_number))