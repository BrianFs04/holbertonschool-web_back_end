#!/usr/bin/env python3
"""
SessionExpAuth module
"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class"""

    def __init__(self):
        """Constructor method"""
        self.session_duration = 0
        if int(getenv("SESSION_DURATION")):
            self.session_duration = int(getenv("SESSION_DURATION"))

    def create_session(self, user_id=None):
        """Create a session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        session_dictionary = {
            'user_id': user_id,
            'created_at': datetime.now()
        }

        self.user_id_by_session_id[session_id] = session_dictionary

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """User ID for Session ID"""
        if session_id is None:
            return None

        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None

        if self.session_duration <= 0:
            return session_dictionary.get("user_id")

        if "created_at" not in session_dictionary:
            return None

        created_time = session_dictionary.get("created_at")
        session_elapsed = timedelta(seconds=self.session_duration)

        if created_time + session_elapsed < datetime.now():
            return None
        else:
            return session_dictionary.get("user_id")
