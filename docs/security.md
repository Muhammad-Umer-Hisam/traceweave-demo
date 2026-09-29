# Session security

Users are logged out after **30 minutes of inactivity**.

The timeout is defined by `SESSION_TIMEOUT_MINUTES` in `src/auth/session.py`. The `session_expired` function checks the elapsed inactive time against this limit. 
