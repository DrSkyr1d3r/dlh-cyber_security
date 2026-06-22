## 1. Which asset is most critical in this system? Explain your reasoning using the CIA Triad.
The most critical asset in this system is the patient's medical records and personal health information (PHI).
### Confidentiality
Patient medical records contain highly sensitive information and must only be accessible to authorized healthcare providers and the patient. Unauthorized disclosure could violate privacy regulations such as HIPAA and result in significant harm to the patient.
### Integrity
Medical records must remain accurate and untampered. If an attacker modifies a patient's medical history, prescriptions, allergies, or diagnoses, healthcare providers could make incorrect treatment decisions that may endanger the patient's health.
### Availability
Patient records must be available whenever needed, especially during emergencies. Healthcare providers rely on timely access to accurate medical information to diagnose and treat patients effectively.

## 2. Apply STRIDE to the "Message Healthcare Providers" Feature
### Spoofing Identity
An attacker could steal a patient's session token or credentials and impersonate them to send messages to healthcare providers, potentially requesting unauthorized prescriptions or medical advice.
### Tampering with Data
An attacker could intercept and modify messages exchanged between patients and healthcare providers, altering medical information or treatment requests.
### Repudiation
A patient or healthcare provider could deny sending or receiving a message, leading to disputes regarding medical advice or treatment decisions.
### Information Disclosure
An attacker could gain unauthorized access to private messages containing sensitive medical information, exposing patient health records and violating privacy regulations.
### Denial of Service
An attacker could flood the messaging system with requests, preventing patients from contacting healthcare providers when needed.
### Elevation of Privilege
An attacker could exploit a vulnerability to gain higher privileges and access or modify messages and patient records belonging to other users.

## 3. Security Controls to Protect Patient Data (Prioritized)
### 1. Multi-Factor Authentication (MFA)
Authentication should be the highest priority because it prevents unauthorized users from accessing patient accounts even if credentials are compromised.
### 2. Encryption of Sensitive Data
All sensitive patient information should be encrypted both at rest and in transit to protect confidentiality and reduce the impact of data breaches.
### 3. Access Control and Least Privilege
Users should only have access to the information necessary for their role. This limits the damage that can occur if an account is compromised.
### 4. Audit Logging and Monitoring
Comprehensive logging and monitoring provide accountability, support investigations, and help detect suspicious activity or security incidents.
### 5. Input Validation and Secure Coding Practices
All user inputs should be validated and sanitized to prevent common attacks such as SQL injection and cross-site scripting (XSS), helping protect both patient data and system integrity.
