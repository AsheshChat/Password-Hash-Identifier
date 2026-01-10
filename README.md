# Password Hash Identifier (Student Project)

## Overview

This project is a Python-based password hash identifier created as a learning exercise to understand how different password hashing algorithms and formats can be identified based on their structure, prefixes, and length.

The tool analyzes a user-provided hash and attempts to determine its possible hash type(s) by checking common characteristics used by password hashing schemes, Unix/Linux systems, databases, and raw cryptographic hashes.

This project focuses on identification only and does not perform cracking or brute-forcing.

## Features

* Identifies common password hashing formats
* Supports modern and legacy hash schemes
* Categorizes hashes into:
   * Password hashing algorithms
   * Unix/Linux crypt formats
   * Database hashes
   * Raw cryptographic hashes
* Uses prefix, length, and character pattern analysis
* Simple command-line interface (CLI)

## Supported Hash Types

### Password Hashing Algorithms

* bcrypt
* Argon2
* PBKDF2
* scrypt

### Unix / Linux Hash Formats

* MD5-crypt
* bcrypt (Unix format)
* SHA-256-crypt
* SHA-512-crypt

### Database Hashes

* MySQL (< 4.1)
* MySQL (≥ 4.1)

### Raw Hash Algorithms (Heuristic-Based)

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512
* NTLM
* LM
* RIPEMD-160
* Whirlpool

Some outputs may return multiple possible hash types due to overlapping characteristics.

## How It Works (High Level)

1. The user enters a hash value via the command line.
2. The program removes whitespace and analyzes the hash.
3. The hash is checked in the following order:
   * Password hashing formats (bcrypt, Argon2, PBKDF2, scrypt)
   * Unix/Linux crypt formats
   * Database hash formats
   * Raw cryptographic hashes
4. Identification is based on:
   * Known prefixes (e.g., $2b$, $argon2, $6$)
   * Hash length
   * Hexadecimal character patterns
5. The program prints the most likely hash type(s) or returns Unknown if no match is found.

## Technologies Used

* Python 3
* Built-in libraries:
   * string

## Usage

### Running the Program
```bash
python3 hash_identifier.py
```

### Example
```
Welcome to the hash identifier program

Please enter the hash:
$2b$12$e9T9ZzR5p5xkZ7M1oR0yQe6m9B9z9UuG4s7nO9M3G0k9M3M9S


Detected password hash type(s): ['bcrypt']
```

## Identification Logic

* Prefix checks identify structured password hashes
* Length checks help differentiate hash families
* Hexadecimal validation ensures raw hash integrity
* Some hashes intentionally return multiple possibilities due to format overlap

## Limitations

* Cannot guarantee exact hash type for raw hashes
* No salt extraction or hash parsing beyond identification
* No hash cracking or verification
* Some hash formats share identical lengths
* Designed for learning, not forensic certainty

## What I Learned

* Common password hashing formats and structures
* Differences between password hashes and raw cryptographic hashes
* How Unix/Linux and database hashes are stored
* Practical pattern matching and validation in Python
* Ethical handling of password-related tools

## Future Improvements

* Add hash mode IDs (e.g., Hashcat reference)
* Support more database and application-specific hashes
* Improve detection confidence scoring
* Add file input support for batch identification
* Modularize detection logic for extensibility

## Ethical Disclaimer

This tool is intended only for educational and defensive security purposes.
It does not crack passwords and should only be used on hashes you are authorized to analyze.
