class AIState:
    def __init__(self):
        self.cookies = {}  # Dictionary to store cookies

def store_cookie(ai_state, cookie_name, data):
    ai_state.cookies[cookie_name] = data

def get_cookie(ai_state, cookie_name):
    return ai_state.cookies.get(cookie_name, None)

def remove_cookie(ai_state, cookie_name):
    if cookie_name in ai_state.cookies:
        del ai_state.cookies[cookie_name]

def clear_all_cookies(ai_state):
    ai_state.cookies.clear()
