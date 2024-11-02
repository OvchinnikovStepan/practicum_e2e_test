import os

class Constants:
    try:
        login = os.getenv('AUTH_LOGIN')
        password = os.getenv('AUTH_PASSWORD')
        empty_login_error_msg=os.getenv('EMPTY_LOGIN_MSG')
    except KeyError:
        print("SMTH WASN'T FOUND")

        