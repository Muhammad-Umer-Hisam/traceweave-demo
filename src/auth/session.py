SESSION_TIMEOUT_MINUTES = 60

def session_expired(inactive_minutes):
    return inactive_minutes >= SESSION_TIMEOUT_MINUTES
