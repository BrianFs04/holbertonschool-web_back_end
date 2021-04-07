#!/usr/bin/env python3
"""
SessionDBAuth module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta


class SessionDBAuth(SessionExpAuth):
    """SessionDBAuth class"""

    def create_session(self, user_id=None):
        """Create a session"""
        try:
            session_id = super().create_session(user_id)
        except Exception:
            return None

        session_dictionary = {
            'user_id': user_id,
            'session_id': session_id
        }

        session = UserSession(**session_dictionary)
        session.save()
        UserSession.save_to_file()

        return session_id

    def user_id_for_session_id(self, session_id=None):
        """User ID for Session ID"""
        if session_id is None:
            return None

        UserSession.load_from_file()

        session = UserSession.search({"session_id": session_id})

        if not session:
            return None

        created_time = session[0].created_at
        session_elapsed = timedelta(seconds=self.session_duration)

        if (created_time + session_elapsed) < datetime.now():
            return None

        return session[0].user_id

    def destroy_session(self, request=None):
        """Deletes the user session/logout"""
        if request is None:
            return False

        session_id = self.session_cookie(request)

        if not session_id:
            return False

        if not self.user_id_for_session_id(session_id):
            return False

        session = UserSession.search({"session_id": session_id})

        if not session:
            return False

        try:
            session[0].remove()
            UserSession.save_to_file()
        except Exception:
            return False

        return True
