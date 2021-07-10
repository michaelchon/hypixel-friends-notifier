class PlayerSessionManager:
    def __init__(self):
        self.sessions = {}

    def is_session_changed(self, name, session):
        if name not in self.sessions or self.sessions[name]['online'] != session['online']:
            self.sessions[name] = session
            return True
        return False
