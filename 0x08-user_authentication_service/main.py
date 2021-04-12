#!/usr/bin/env python3
"""
End-to-end integration test
"""
import requests
URL = "http://localhost:5000"


def register_user(email: str, password: str) -> None:
    """Registers a user"""
    payload = {"email": email, "password": password}

    r = requests.post(f"{URL}/users", data=payload)
    assert r.status_code == 200, "register_user: fail"
    print(r.text)


def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password"""
    payload = {"email": email, "password": password}

    r = requests.post(f"{URL}/sessions", data=payload)
    assert r.status_code == 401, "log_in_wrong_password: fail"
    print(r.text)


def profile_unlogged() -> None:
    """Unlogged profile"""
    payload = {"session_id": ""}

    r = requests.get(f"{URL}/profile", data=payload)
    assert r.status_code == 403, "profile_unlogged: fail"
    print(r.text)


def log_in(email: str, password: str) -> str:
    """Log in it"""
    payload = {"email": email, "password": password}

    r = requests.post(f"{URL}/sessions", data=payload)
    assert r.status_code == 200, "log_in: fail"
    print(r.text)
    session_id = r.cookies.get("session_id")
    return session_id


def profile_logged(session_id: str) -> None:
    """Logged profile"""
    payload = {"session_id": session_id}

    r = requests.get(f"{URL}/profile", cookies=payload)
    assert r.status_code == 200, "profile_logged: fail"
    print(r.text)


def log_out(session_id: str) -> None:
    """Log out"""
    payload = {"session_id": session_id}

    r = requests.delete(f"{URL}/sessions", cookies=payload)
    assert r.status_code == 200, "log_out: fail"
    print(r.text)


def reset_password_token(email: str) -> str:
    """Reset password token"""
    payload = {"email": email}

    r = requests.post(f"{URL}/reset_password", data=payload)
    assert r.status_code == 200, "reset_password_token: fail"
    print(r.text)
    reset_token = r.json().get("reset_token")
    return reset_token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password"""
    payload = {"email": email, "reset_token": reset_token,
               "new_password": new_password}

    r = requests.put(f"{URL}/reset_password", data=payload)
    assert r.status_code == 200, "update_password: fail"
    print(r.text)


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
