SESSION_TIMEOUT_MINUTES = 60

def session_expired(inactive_minutes):
    return inactive_minutes >= SESSION_TIMEOUT_MINUTES

def remaining_minutes(inactive_minutes):
    return max(0, SESSION_TIMEOUT_MINUTES - inactive_minutes)
