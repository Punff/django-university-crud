import db
import os
from http import cookies

def get_or_create_session_id():
    http_cookies_str = os.environ.get('HTTP_COOKIE', '')
    get_all_cookies_object = cookies.SimpleCookie(http_cookies_str)
    session_id = get_all_cookies_object.get("session_id").value if get_all_cookies_object.get("session_id") else None
    if session_id is None:
        session_id = db.create_session()
        cookies_object = cookies.SimpleCookie()
        cookies_object["session_id"] = session_id
        print(cookies_object.output())
    return session_id

def add_to_session(params):
    session_id = get_or_create_session_id()
    data = db.get_session(session_id)
    for subid in params.keys():
        data[subid] = params[subid]
    db.replace_session(session_id, data)
