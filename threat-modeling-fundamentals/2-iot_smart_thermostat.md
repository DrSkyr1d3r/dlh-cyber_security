## 1. Identify IoT-Specific Threats That Don't Typically Apply to Web Applications
### 1. Physical Device Tampering
An attacker with physical access to the thermostat could open the device and manipulate its hardware, access internal components, or install malicious firmware.
### 2. Weak or Default Credentials
Many IoT devices ship with default usernames and passwords. If these credentials are not changed, an attacker can easily gain access to the device.
### 3. Unencrypted Communications
If communications between the thermostat, mobile app, and cloud services are not encrypted, an attacker could intercept temperature data, device status information, and user commands.
### 4. Firmware Vulnerabilities
Vulnerabilities in the device firmware could allow an attacker to gain control of the thermostat, modify settings, or execute malicious code on the device.
### 5. Compromise Through Always-On Connectivity
Because IoT devices are continuously connected to the network, an attacker who compromises the thermostat could use it as an entry point into the home network and monitor or attack other connected devices.

## 2. What Happens If an Attacker Gains Physical Access to the Device?
### Attack Chain
1. The attacker gains physical access to the thermostat.
2. The device is opened and internal components are exposed.
3. The attacker accesses debug ports or device memory.
4. Sensitive information such as credentials, encryption keys, or configuration data is extracted.
5. Malicious firmware is installed on the device.
6. The attacker gains persistent access and control over the thermostat.
### Potential Impacts
- Loss of privacy through monitoring of device activity.
- Unauthorized control of heating and cooling systems.
- Theft of sensitive information stored on the device.
- Use of the compromised thermostat as a foothold to attack other devices on the home network.
- Long-term persistence through malicious firmware modifications.

## 3. Design Security Controls for the OTA (Over-The-Air) Update Process
### 1. Encrypted Update Channel
Firmware updates should be transmitted through encrypted channels such as TLS to prevent attackers from intercepting or modifying updates in transit.
### 2. Code Signing and Digital Signatures
All firmware updates should be digitally signed. The device must verify the signature before installing the update to ensure it comes from a trusted source.
### 3. Secure Boot
The device should verify the integrity and authenticity of firmware during startup and only execute trusted firmware images.
### 4. Rollback Protection
The device should support rollback to a known good version if an update fails or introduces security issues.
### 5. Firmware Integrity Verification
The device should verify checksums or cryptographic hashes before installation to ensure the update has not been altered or corrupted.
### Essential Security Requirements
- Encryption of update communications.
- Verification of firmware authenticity using digital signatures.
- Secure boot to prevent execution of malicious firmware.
- Integrity verification before installation.
- Safe rollback mechanisms for recovery from failed or vulnerable updates.
