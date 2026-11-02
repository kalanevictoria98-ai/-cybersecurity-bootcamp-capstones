import hashlib
import hmac
import base64
import struct
import time


# Base32 TOTP secret (20-byte secret encoded in base32).
TOTP_SECRET = "JBSWY3DPEHPK3PXP"  # Example base32 string


# ==============================
# Helper Functions
# ==============================

def hash_input(input_text: str) -> str:
    """
    Hash input using SHA-256 and return the hexadecimal result.
    """
    encoded_input = input_text.encode('utf-8')
    hashed = hashlib.sha256(encoded_input)
    return hashed.hexdigest()


STORED_PASSWORD_HASH = hash_input("MySecurePassword123")  # stored password
STORED_BIOMETRIC_HASH = hash_input("fingerprint-key-01")  # biometric key


def generate_totp(
    secret: str,
    interval: int = 30,
    digits: int = 6
) -> str:
    """
    Generate a Time-based One-Time Password (TOTP) using HMAC-SHA1.
    Do not modify this function. You will call it from verify_otp().
    """
    # Decode base32 secret
    key = base64.b32decode(secret, casefold=True)

    # Get current Unix time and compute the time step (counter)
    timestep = int(time.time() // interval)

    # Pack timestep into 8-byte big-endian
    msg = struct.pack(">Q", timestep)

    # HMAC-SHA1
    hmac_digest = hmac.new(key, msg, hashlib.sha1).digest()

    # Dynamic truncation
    offset = hmac_digest[-1] & 0x0F
    code = ((hmac_digest[offset] & 0x7F) << 24 |
            (hmac_digest[offset + 1] & 0xFF) << 16 |
            (hmac_digest[offset + 2] & 0xFF) << 8 |
            (hmac_digest[offset + 3] & 0xFF))

    # Reduce to the desired number of digits
    otp = code % (10 ** digits)
    return str(otp).zfill(digits)


# ==============================
# Verification Functions
# ==============================

def verify_password() -> bool:
    """
    Prompt for a password and verify it against STORED_PASSWORD_HASH.
    """
    password = input("Enter your password: ")
    hashed_input = hash_input(password)
    if hashed_input == STORED_PASSWORD_HASH:
        return True
    else:
        return False


def verify_otp() -> bool:
    """
    Generate a TOTP code using generate_totp() and
    verify user input against it.
    """
    # 1. Generate the current TOTP code
    current_code = generate_totp(TOTP_SECRET)

    # 2. Prompt the user for the TOTP
    user_code = input("Enter your 6-digit TOTP code: ").strip()

    # 3. Compare user input with generated code
    if user_code == current_code:
        return True
    else:
        return False


def verify_biometric() -> bool:
    """
    Simulate biometric check by hashing user input and comparing
    with STORED_BIOMETRIC_HASH.
    """
    bio_key = input("Enter your biometric key: ")
    hashed_bio = hash_input(bio_key)
    if hashed_bio == STORED_BIOMETRIC_HASH:
        return True
    else:
        print("Invalid biometric key. Please try again.")
        return False


# ==============================
# Main Authentication Flow
# ==============================

def main():
    """
    Main function to run the MFA system, requiring all three factors to pass.
    """
    print("Welcome to the MFA Authentication System")
    print("You must pass all three authentication factors.\n")

    # Step 1: Password verification
    if not verify_password():
        print("Authentication failed: Password verification failed.")
        return

    # Step 2: TOTP verification
    if not verify_otp():
        print("Authentication failed: TOTP verification failed.")
        return

    # Step 3: Biometric verification
    if not verify_biometric():
        print("Authentication failed: Biometric verification failed.")
        return

    # If all checks pass:
    print("Authentication successful! Access granted.")


if __name__ == "__main__":
    main()
