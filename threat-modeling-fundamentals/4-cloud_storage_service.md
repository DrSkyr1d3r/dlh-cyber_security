# Threat Modeling – Cloud Storage Service
## 1. Map Out the Attack Surface
### 1. File Upload Endpoints (Highest Risk)
File upload endpoints represent the highest-risk attack surface. If file validation is not properly implemented, an attacker could upload malicious files, malware, or executable content that could compromise the system.
**Risk Level:** Critical
### 2. Public Link Generation and Sharing
Public sharing links could expose sensitive files if access controls are weak or if links are shared with unauthorized users.
**Risk Level:** High
### 3. API Endpoints
API endpoints provide access to core functionality such as uploads, downloads, sharing, and file management. Improper input validation, authentication, or authorization could allow attackers to abuse the service.
**Risk Level:** High
### 4. Authentication Flows
Authentication mechanisms are a common target for attackers attempting account takeover. Weak authentication could allow unauthorized access to stored files.
**Risk Level:** High
### 5. Admin Interfaces
Administrative interfaces are highly sensitive because they provide elevated privileges. Although they are generally less exposed than public-facing components, a successful compromise could result in full system control.
**Risk Level:** Medium

## 2. Why Storing Encryption Keys in the Database Is Problematic
Storing encryption keys in the same database as the encrypted files defeats much of the purpose of encryption. If an attacker compromises the database, they may gain access to both the encrypted files and the encryption keys required to decrypt them. This could lead to complete exposure of sensitive user data.

### STRIDE Threats Introduced
### Tampering
An attacker who gains access to the database could modify, replace, or delete encryption keys. This could prevent legitimate users from accessing their files or cause data corruption.
### Information Disclosure
If the database is breached, attackers may obtain both encrypted files and the associated encryption keys. This would allow them to decrypt sensitive information and access user data.
### Repudiation
Without proper logging and auditing, it may be difficult to determine who accessed, modified, or used encryption keys after a breach.
### Denial of Service
If encryption keys are deleted or corrupted, legitimate users may permanently lose access to their files.
### Elevation of Privilege
An attacker who gains elevated access to the database may gain access to encryption keys and decrypt information that should remain protected.

## 3. Risk Matrix

| Threat | Likelihood (1-5) | Impact (1-5) | Risk Score | Risk Level |
|----------|----------|----------|----------|----------|
| Malicious File Upload | 5 | 5 | 25 | Critical |
| Public Link Abuse / Data Exposure | 4 | 4 | 16 | High |
| API Endpoint Exploitation | 3 | 5 | 15 | High |
| Authentication Flow Compromise | 3 | 5 | 15 | High |
| Admin Interface Compromise | 1 | 5 | 5 | Low |

### Justification
#### Malicious File Upload
- **Likelihood: 5** – Upload functionality is directly exposed to users and is a common attack target.
- **Impact: 5** – Successful exploitation could allow malware execution, system compromise, or unauthorized access.
#### Public Link Abuse
- **Likelihood: 4** – Public links may be shared accidentally or discovered by unauthorized users.
- **Impact: 4** – Sensitive files may be exposed, but compromise is generally limited to the shared content.
#### API Endpoint Exploitation
- **Likelihood: 3** – Exploitation typically requires technical knowledge and vulnerability discovery.
- **Impact: 5** – Successful exploitation could affect core storage, sharing, and account functions.
#### Authentication Flow Compromise
- **Likelihood: 3** – Authentication systems are common attack targets but are usually protected by multiple security controls.
- **Impact: 5** – Account compromise may expose all files owned by the victim.
#### Admin Interface Compromise
- **Likelihood: 1** – Administrative interfaces are generally restricted and not publicly accessible.
- **Impact: 5** – A successful compromise could result in complete control of the storage platform.
