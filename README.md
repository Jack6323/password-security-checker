# Password Security Auditor (Python)

## Overview
This project is a Python-based password security tool that evaluates the strength of a password using multiple security checks. It demonstrates foundational cyber security principles such as authentication security, password hygiene, and basic risk analysis.

---

## Purpose
The goal of this project is to simulate how real-world systems evaluate password strength and to provide users with clear, actionable feedback to improve password security.

This reflects real cyber security concerns such as:
- Weak password detection
- Brute-force attack resistance
- Password policy enforcement
- Secure authentication practices

---

## Features
- Checks password length (minimum 8 characters)
- Detects uppercase and lowercase characters
- Checks for numbers and special characters
- Identifies commonly used weak passwords
- Generates a password strength score
- Provides improvement suggestions

---

## Skills Demonstrated
- Python programming fundamentals
- Logical problem solving
- Cyber security awareness
- Authentication security principles
- Data validation and analysis

---

## How It Works
The program evaluates a password based on multiple security criteria:

- Length requirement
- Character diversity (uppercase, lowercase, numbers, symbols)
- Comparison against a list of commonly used weak passwords

A security score is generated and the password is classified as:
- Very strong
- Moderate
- Weak

The tool also outputs suggestions to help improve password strength.

---

## Example Output
```text
Enter your password: Test123!

--- Password Analysis ---
Moderate Password

Improve your password by adding:
- a special character (if missing)
- a number (if missing)
- an uppercase letter (if missing)
