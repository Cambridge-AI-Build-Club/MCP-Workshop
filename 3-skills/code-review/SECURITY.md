# Security Checklist

## Input Validation

### SQL Injection
```python
# Vulnerable
query = f"SELECT * FROM users WHERE id = {user_id}"

# Safe: Parameterized queries
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### Command Injection
```python
# Vulnerable
os.system(f"ls {user_input}")

# Safe: Use subprocess with list args
subprocess.run(["ls", user_input], check=True)
```

### Path Traversal
```python
# Vulnerable
with open(f"/data/{filename}") as f:
    return f.read()

# Safe: Validate path
import os
safe_path = os.path.normpath(os.path.join("/data", filename))
if not safe_path.startswith("/data/"):
    raise ValueError("Invalid path")
```

## Authentication & Authorization

### Check Every Request
- Verify user is authenticated
- Verify user has permission for this action
- Verify user owns the resource being accessed

### Token Security
- Use secure, random tokens (min 128 bits)
- Set appropriate expiration
- Invalidate on logout
- Use HttpOnly, Secure, SameSite cookies

### Password Storage
```python
# Never: Plain text or weak hash
password_hash = md5(password)

# Correct: Strong adaptive hash
from argon2 import PasswordHasher
ph = PasswordHasher()
hash = ph.hash(password)
```

## Data Exposure

### Sensitive Data in Logs
```python
# Bad
logger.info(f"User {user.email} logged in with {password}")

# Good
logger.info(f"User {user.id} logged in")
```

### API Responses
- Don't leak internal IDs unnecessarily
- Don't include stack traces in production
- Filter sensitive fields before serialization

### Error Messages
```python
# Bad: Information disclosure
raise Exception(f"Database error: {db_error.full_trace}")

# Good: Generic message
raise Exception("An error occurred. Please try again.")
```

## Cryptography

### Use Standard Libraries
- Don't implement custom crypto
- Use well-maintained libraries
- Keep dependencies updated

### Secure Defaults
- TLS 1.2+ for all connections
- Strong cipher suites
- Certificate validation enabled

## Quick Security Audit

| Category | Check | Risk |
|----------|-------|------|
| Input | All user input validated? | High |
| SQL | Parameterized queries used? | Critical |
| Auth | Every endpoint protected? | Critical |
| Secrets | No hardcoded credentials? | High |
| Logs | No sensitive data logged? | Medium |
| Errors | Generic error messages? | Medium |
| Deps | Known vulnerabilities? | Varies |
