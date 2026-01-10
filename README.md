# Password Hash Identifier (Phase 1)

A Python-based tool designed to identify common password hash formats through intelligent analysis of hash prefixes, lengths, and character patterns. This utility is built for security professionals, system administrators, and penetration testers who need to quickly identify hash types during defensive security operations.

## Features

- **Multi-Format Detection**: Identifies a wide range of hash formats across four major categories
- **Pattern Recognition**: Uses prefix matching, length analysis, and character pattern validation
- **Hierarchical Identification**: Implements a cascading detection system for optimal accuracy
- **Lightweight & Fast**: No external dependencies, pure Python implementation
- **Ethical Focus**: Designed for defensive security, incident response, and authorized security assessments

## Supported Hash Formats

### Password Hashing Algorithms
- **bcrypt** (`$2a$`, `$2b$`, `$2y$`)
- **Argon2** (`$argon2`)
- **PBKDF2** (`$pbkdf2`)
- **scrypt** (`$scrypt$`)

### Unix/Linux System Hashes
- **MD5-crypt** (`$1$`)
- **bcrypt (Unix)** (`$2y$`)
- **SHA-256-crypt** (`$5$`)
- **SHA-512-crypt** (`$6$`)

### Database Hashes
- **MySQL < 4.1** (16-character hex)
- **MySQL >= 4.1** (41-character, asterisk prefix)

### Raw Hash Algorithms
- **MD5** (32 hex characters, 128-bit)
- **NTLM/LM** (32 hex characters, uppercase detection)
- **SHA-1** (40 hex characters, 160-bit)
- **RIPEMD-160** (40 hex characters)
- **SHA-224** (56 hex characters)
- **SHA-256** (64 hex characters)
- **SHA-384** (96 hex characters)
- **SHA-512** (128 hex characters)
- **Whirlpool** (128 hex characters)

## Installation

No installation required! This is a standalone Python script with no external dependencies.

### Requirements
- Python 3.x

### Setup
```bash
# Clone or download the script
git clone <your-repository-url>
cd password-hash-identifier

# Or simply download the script file directly
wget <script-url> -O hash_identifier.py
```

## Usage

### Basic Usage
```bash
python hash_identifier.py
```

The program will prompt you to enter a hash:
```
Welcome to the hash identifier program

Please enter the hash: 
```

### Example Sessions

**Identifying a bcrypt hash:**
```
Please enter the hash: $2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy

Detected password hash type(s): ['bcrypt']
```

**Identifying a SHA-256 hash:**
```
Please enter the hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

Possible raw hash type(s): ['SHA-256']
```

**Identifying a MySQL hash:**
```
Please enter the hash: *2470C0C06DEE42FD1618BB99005ADCA2EC9D1E19

Detected database hash type(s): ['MySQL (>= 4.1)']
```

**Identifying a Unix SHA-512-crypt hash:**
```
Please enter the hash: $6$rounds=5000$usesomesillystringforsalt$D4IrlXatmP.KMy

Detected Unix/Linux hash type(s): ['SHA-512-crypt']
```

## How It Works

The tool employs a hierarchical detection strategy:

1. **Password Hash Detection**: First checks for modern password hashing schemes (bcrypt, Argon2, PBKDF2, scrypt) using prefix matching and minimum length validation.

2. **Unix/Linux Hash Detection**: Examines Unix crypt format hashes with their distinctive `$ID$` prefixes.

3. **Database Hash Detection**: Identifies database-specific hash formats, particularly MySQL variants.

4. **Raw Hash Detection**: Falls back to analyzing raw hash algorithms based on hexadecimal character validation and length-based bit calculation.

### Detection Logic

Each detection function performs:
- **Prefix Analysis**: Matches known hash format identifiers
- **Length Validation**: Ensures hash length matches expected format
- **Character Pattern**: Validates hexadecimal characters where applicable
- **Bit Calculation**: Computes hash bit-length for raw algorithm identification

## Security Considerations

### Intended Use Cases
✅ Password audit and security assessments  
✅ Incident response and forensic analysis  
✅ System administration and compliance checking  
✅ Security research and education  
✅ Authorized penetration testing  

### Ethical Guidelines
⚠️ **This tool is designed for defensive security purposes only**

- Only use on systems and data you own or have explicit authorization to test
- Do not use for unauthorized access attempts or malicious activities
- Respect privacy laws and regulations in your jurisdiction
- Follow responsible disclosure practices when identifying vulnerabilities

## Limitations

- **Collision Possibility**: Some hash lengths may match multiple algorithms (e.g., 32-character hex could be MD5 or NTLM)
- **No Hash Validation**: The tool identifies format patterns but doesn't validate if the hash is cryptographically valid
- **Prefix Dependency**: Relies on standard format prefixes; custom implementations may not be detected
- **No Salt Analysis**: Does not extract or analyze salt values from hashes

## Technical Details

### Function Breakdown

**`is_hex(s)`**  
Validates if a string contains only hexadecimal characters (0-9, a-f, A-F).

**`password_hash(h)`**  
Identifies modern password hashing algorithms using prefix and length analysis.

**`unix_hash(h)`**  
Detects Unix/Linux crypt format hashes with their distinctive prefixes.

**`database_hash(h)`**  
Recognizes database-specific hash formats, particularly MySQL variants.

**`raw_hash(h)`**  
Identifies raw cryptographic hash algorithms through length-based detection and hex validation.

### Detection Flow
```
Input Hash
    ↓
Password Hash Detection
    ↓ (if Unknown)
Unix Hash Detection
    ↓ (if Unknown)
Database Hash Detection
    ↓ (if Unknown)
Raw Hash Detection
    ↓
Result Output
```

## Future Enhancements (Phase 2+)

Potential improvements for future versions:
- Support for additional hash formats (SHA3, BLAKE2, etc.)
- Batch processing mode for multiple hashes
- JSON output format for integration with other tools
- Salt extraction and analysis
- Hash strength assessment
- GUI interface option
- Integration with hash cracking tools (for authorized use)

## Contributing

Contributions are welcome! Please ensure any additions:
- Maintain the ethical security focus
- Include appropriate detection tests
- Document new hash format specifications
- Follow the existing code structure


## Disclaimer

This tool is provided for educational and authorized security testing purposes only. Users are responsible for ensuring they have proper authorization before analyzing any hashes. The authors assume no liability for misuse of this tool.



**Version**: 1.0 (Phase 1)  
**Last Updated**: January 2026  
**Status**: Active Development
