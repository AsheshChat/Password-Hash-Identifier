import string

def is_hex(s):
    return all(c in string.hexdigits for c in s)

def password_hash(h):
    h = h.strip()
    l = len(h)

    checks = {
        "bcrypt": lambda: h.startswith(("$2a$", "$2b$", "$2y$")) and l == 60,
        "Argon2": lambda: h.startswith("$argon2") and l >= 90,
        "PBKDF2": lambda: h.startswith("$pbkdf2") and l >= 50,
        "scrypt": lambda: h.startswith("$scrypt$") and l >= 60,
    }

    for hash_type, check in checks.items():
        if check():
            return [hash_type]
    return ["Unknown"]

def unix_hash(h):
    h = h.strip()
    l = len(h)

    checks = {
        "MD5-crypt": lambda: h.startswith("$1$") and l >= 30,
        "bcrypt (Unix)": lambda: h.startswith("$2y$") and l == 60,
        "SHA-256-crypt": lambda: h.startswith("$5$") and l >= 50,
        "SHA-512-crypt": lambda: h.startswith("$6$") and l >= 80,
    }

    for hash_type, check in checks.items():
        if check():
            return [hash_type]
    return ["Unknown"]

def database_hash(h):
    h = h.strip()
    l = len(h)

    checks = {
        "MySQL (< 4.1)": lambda: l == 16 and is_hex(h),
        "MySQL (>= 4.1)": lambda: l == 41 and h.startswith("*") and
is_hex(h[1:]),
    }

    for hash_type, check in checks.items():
        if check():
            return [hash_type]
    return ["Unknown"]

def raw_hash(h):
    h = h.strip()
    length = len(h)
    bits = length * 4

    if not is_hex(h):
        return ["Unknown"]

    hash_types = {
        32: lambda: ["NTLM", "LM"] if h.isupper() else ["MD5", "NTLM"],
        40: lambda: ["SHA-1", "RIPEMD-160"],
        56: lambda: ["SHA-224"],
        64: lambda: ["SHA-256"],
        96: lambda: ["SHA-384"],
        128: lambda: ["SHA-512", "Whirlpool"],
    }

    if length in hash_types:
        return hash_types[length]()
    return ["Unknown"]

print("Welcome to the hash identifier program\n")
user_hash = input("Please enter the hash: ").strip()

pw = password_hash(user_hash)
if pw != ["Unknown"]:
    print("\nDetected password hash type(s):", pw)
    exit()

ux = unix_hash(user_hash)
if ux != ["Unknown"]:
    print("\nDetected Unix/Linux hash type(s):", ux)
    exit()

db = database_hash(user_hash)
if db != ["Unknown"]:
    print("\nDetected database hash type(s):", db)
    exit()

raw = raw_hash(user_hash)
print("\nPossible raw hash type(s):", raw)
