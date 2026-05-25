# Secure Coding Review: network_sniffer.py

## 1. Static Analysis
- Tool Used: Bandit (v1.9.4)
- Result: No security vulnerabilities detected.

## 2. Manual Code Review
- The script captures and prints network packets using scapy.
- It prints raw payloads, which may expose sensitive data.
- Requires elevated privileges to run.

## 3. Security Findings & Recommendations

### Sensitive Data Exposure
- **Risk:** Raw payloads may contain credentials or private data.
- **Recommendation:** Filter or redact sensitive information before printing.

### Permissions
- **Risk:** Unrestricted use may allow unauthorized users to sniff traffic.
- **Recommendation:** Restrict script execution to trusted users only.

### Logging
- **Risk:** Logging raw packet data can leak sensitive info if logs are accessed.
- **Recommendation:** Avoid logging raw payloads in production.

### Exception Handling
- **Risk:** Unhandled exceptions may crash the script.
- **Recommendation:** Add try/except blocks around packet processing.

### Dependency Management
- **Risk:** Outdated libraries may have vulnerabilities.
- **Recommendation:** Keep scapy and Python up to date.

## 4. Remediation Steps
- Implement payload filtering/redaction.
- Add user permission checks if integrating into a larger system.
- Add error handling for robustness.



