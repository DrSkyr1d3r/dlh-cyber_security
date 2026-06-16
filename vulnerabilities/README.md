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
