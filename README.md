# FILE-INTEGRITY-CHECKER

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*:  Sakshi Santosh Zurange

*INTERN ID*: CT12WNYF

*DOMAIN*: Cyber Security & Ethical Hacking

*DURATION*: 12 WEEKS

*MENTION*:  Neela Santhosh Kumar

Cybersecurity: File Integrity Monitoring
To implement a File Integrity Monitoring (FIM) tool that ensures the integrity of files by detecting unauthorized modifications, additions, or deletions. The goal is to enhance security by tracking changes in critical system files or sensitive data directories, thereby mitigating risks of tampering or data breaches.

1.Hash-Based Verification:
Use cryptographic hash functions (e.g., SHA-256) to compute and compare file hashes.
Ensure that even minor changes in a file are detected by analyzing differences in hash values.
Baseline Hash Creation:

2.Perform an initial scan of the target directory to create a baseline of file hashes.
Store these hashes securely in a file (e.g., JSON format) for future reference.
Integrity Check:

3.Continuously or periodically compare current file states with the baseline.
Identify and classify changes as:
Modified Files: Files with altered content.
New Files: Files added since the last scan.
Deleted Files: Files that existed in the baseline but are now missing.
Alerts and Logs:

4.Log detected changes for review and auditing.
Optionally, send alerts for critical changes (e.g., via email or system notification).

Purpose-
Detect Unauthorized Access: Identify potential tampering by malicious actors or accidental modifications.
Ensure Compliance: Meet regulatory requirements such as PCI DSS, HIPAA, or GDPR by implementing file integrity monitoring.
Protect Sensitive Data: Monitor directories containing sensitive or critical information.
Incident Response: Provide a mechanism for identifying and responding to unauthorized changes promptly.

Implementation Overview
Programming Language: Python.
Libraries Used:
os: To traverse directories and access files.
hashlib: To compute cryptographic hash values.
json: To store and retrieve baseline hash data.

Work Of that code:
Take the directory path as input.
Perform an initial scan to generate hash values for all files.
Save the hashes in a secure format for later comparison.
Periodically or on-demand, check the directory for changes.
Generate a report of new, modified, and deleted files.

Use Cases
1.System File Monitoring:
2.Monitor critical system files for tampering, ensuring OS integrity.
3.Web Server Monitoring:
4.Track changes in web server directories to detect unauthorized access or defacement.
5.Compliance Requirements:
6.Meet the requirements of standards like PCI DSS that mandate file integrity monitoring.
