
import hashlib

def hash_password(password):
    # Encode the password string to bytes
    password_bytes = password.encode('utf-8')
    
    # Use SHA-256 hash function
    hashed_bytes = hashlib.sha256(password_bytes).digest()
    
    # Convert the hashed bytes to a hexadecimal string
    hashed_password = hashed_bytes.hex()
    return hashed_password