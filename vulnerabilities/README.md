# 0. CVE Purpose
## What is the purpose of CVE (Common Vulnerabilities and Exposures) in cybersecurity?
CVE is a database of security vulnerabilities and exposures. It’s crucial because it enables standardization, unique identification, and prioritization of vulnerabilities across different organizations.

## How does it contribute to vulnerability management and information sharing?
CVEs contribute by offering a shared language. Each vulnerability gets a unique ID. This ensures that organizations, vendors, and researchers all reference the same issue. In vulnerability management, security teams can track, assess, and prioritize fixes using CVE IDs. For information sharing, these IDs allow quick communication across tools and databases, so everyone’s on the same page and can coordinate responses efficiently. (Standardization, Identification and Prioritization)

# 1. Severity in CVE
## How does the severity of CVEs affect an organization’s prioritization of security measures?
The severity of the CVE are based on 3 metrics(Base metrics, temporal metrics and Environmental metrics). Higher severity means organizations address it first, while lower severity issues get lower priority.

## Provide examples of how different severity levels (low, medium, high, critical) influence response strategies.
Critical Priority - Immediate incident response, form a dedicated team, and patch systems ASAP—sometimes even taking systems offline briefly.
High Priority - Typically prioritized soon, maybe within days but without a full emergency team.
Medium Priority - schedule the patch in the next maintenance cycle
Low Priority - logged in a backlog and addressed when convenient, without urgency

# 2. CVE List
## Explain the process of assigning CVE IDs to vulnerabilities.
CVE Numbering Authorities (CNAs) assign CVE ids. When a vulnerability is identfied, CNA validate it and assign a CVE id. When no CNA covers the product, it goes to MITRE, who maintain the overall CVE system

## Who manages the CVE List, and what role do CVE Numbering Authorities (CNAs) play in this process?
The CVE list is managed by MITRE corporation. CNAs formally validate vulnerabilities and assign CVE IDs to those confirmed issues. 

# 3. CVEs Scores
## How can organizations use CVEs and CVSS scores effectively to enhance their cybersecurity posture?
Organizations leverage CVEs to identify known vulnerabilities in their systems. They uses CVSS score to guage severity, helping them priotize what to patch first. Thereby they efficiently reduce risk and strenghten overall security. 

## Discuss strategies for integrating CVE information into vulnerability management programs
Organization can integrate vulnerability management system with CVE databases. This ensures that when a new CVE emerges, they are quickly identified in the environment. They can then rank them by severity, assign them in ticketing systems and track remediation progress. These actions weave CVE data directly into the organization's vulnerability management workflow.

# 4. Calculate CVSS
## Calculate the CVSS base score for this vulnerability and determine its severity level
### CVSS Base Metrics
Attack Vector (AV): Network
Attack Complexity (AC): Low
Privileges Required (PR): None
User Interaction (UI): None
Scope (S): Unchanged
Confidentiality (C): High
Integrity (I): High
Availability (A): High
### Base metric Score
9.8 Critical
### Implications
The vulnerability is extremely seriousa and the severity is Critical. An attacker could remotely execute arbitrary code on the affected server, potentially leading to full system compromise, data theft, service disruption, or further attacks inside the organization’s network.
### Mitigation Strategy
Since the vulnerability is rated Critical, the organization should treat it as an urgent security risk. The affected systems should be identified immediately, and available patches or security updates should be applied as soon as possible. If patching cannot be done immediately, temporary mitigations such as disabling the vulnerable service. The organization should also monitor logs and alerts for signs of exploitation, prioritize incident response activities, and verify that remediation was successful through vulnerability scanning or retesting. Critical CVEs should be handled with the highest priority because they can have serious impacts on confidentiality, integrity, and availability.

# 5. CWE and CVE Difference
## What is CWE, and how does it differ from CVE?
Common Weakness Enumeration (CWE) categorizes the underlying software weaknesses. CVE on the otherhand track specific real world vulnerability that results from those weaknesses.

## Why are both important in cybersecurity?
CWE helps developers proactively avoid or fix the weaknesses before they turn into vulnerabilities. Meanwhile, CVE help security teams find, track and remediate vulnerabilities. Together, they offer both prevention and response.

# 6. Role of CWE
## Describe the role of CWE in secure software development practices.
CWE underpins secure software development. It acts as a guide for developers, highlighting common coding weaknesses. By referencing CWE, development teams can adopt secure coding practices, detect known weakness patterns and prevent vulnerabilites. 

## How can developers leverage CWE to improve code quality and security?
CWE gives developers a catalog of known weakness types. By referencing it during design, code review, and testing, developers can proactively identify and mitigate those weaknesses. This results in a secure code and reduces future vulnerabilities.
