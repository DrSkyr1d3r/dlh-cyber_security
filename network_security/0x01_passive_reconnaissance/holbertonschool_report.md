# Shodan Reconnaissance Report: holbertonschool.com


## Subdomains Identified in Shodan

| Subdomain | IP Address | Notes |
| --- | --- | --- |
| apply.holbertonschool.com | 35.180.145.93 | Holberton School admission portal |
| read.holbertonschool.com | 35.181.162.251 | Protected with Basic Authentication |

---

## IP Ranges / Infrastructure

The discovered hosts are hosted on Amazon AWS infrastructure in the `eu-west-3` region.

| IP Address | Hostname | Provider | Region | ASN |
| --- | --- | --- | --- | --- |
| 35.180.145.93 | apply.holbertonschool.com | Amazon EC2 | eu-west-3 | AS16509 |
| 35.181.162.251 | read.holbertonschool.com | Amazon EC2 | eu-west-3 | AS16509 |


---

## Technologies and Frameworks Summary

| Subdomain | Technologies / Frameworks |
| --- | --- |
| apply.holbertonschool.com | Nginx 1.20.0, Ruby, Ruby on Rails, jQuery, Slick, jsDelivr, Adobe Fonts, Typekit, Klaviyo, Google Tag Manager |
| read.holbertonschool.com | Nginx 1.20.0, Basic Authentication |

---

## Shodan Findings

### Entry 1 - 35.180.145.93

#### General Information

| Field | Value |
| --- | --- |
| Hostnames | ec2-35-180-145-93.eu-west-3.compute.amazonaws.com, apply.holbertonschool.com |
| Domains | amazonaws.com, holbertonschool.com |
| Cloud Provider | Amazon |
| Cloud Region | eu-west-3 |
| Cloud Service | EC2 |
| Country | France |
| City | Paris |
| Organization | Amazon Data Services France |
| ISP | Amazon.com, Inc. |
| ASN | AS16509 |
| Operating System | Not shown by Shodan |

#### Web Technologies

| Component | Technology |
| --- | --- |
| CDN | jsDelivr |
| Font Scripts | Adobe Fonts, Typekit |
| JavaScript Libraries | jQuery, Slick |
| Marketing Automation | Klaviyo |
| Programming Language | Ruby |
| Reverse Proxy | Nginx 1.20.0 |
| Tag Manager | Google Tag Manager |
| Web Framework | Ruby on Rails |
| Web Server | Nginx 1.20.0 |

#### Open Ports

| Port | Protocol | Service / Notes | Last Seen |
| --- | --- | --- | --- |
| 443 | TCP | HTTPS/SSL service visible in Shodan | 2026-05-27T09:28:26.720166 |

#### HTTP Response Summary

| Item | Value |
| --- | --- |
| Status | HTTP/1.1 200 OK |
| Server | nginx/1.20.0 |
| Content-Type | text/html; charset=utf-8 |
| Authentication | None visible |
| Security Headers | X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, X-Download-Options, X-Permitted-Cross-Domain-Policies, Referrer-Policy |
| Cookie / Session | `_holberton_session` with HttpOnly flag |
| Cache-Control | max-age=0, private, must-revalidate |
| Content-Security-Policy | Present but empty |
| Framework Clues | Ruby on Rails-style session cookie and runtime header |

#### SSL/TLS Information

| Field | Value |
| --- | --- |
| Certificate Version | 3 |
| Serial Number | 08:c2:0c:5f:f1:b5:b5:48:6e:51:3e:b3:54:3c:37:08 |
| Signature Algorithm | sha256WithRSAEncryption |
| Issuer | C=US, O=Amazon, CN=Amazon RSA 2048 M02 |
| Certificate Common Name | apply.holbertonschool.com |
| Subject Alternative Name | DNS:apply.holbertonschool.com |
| Valid From | Sep 5 00:00:00 2025 GMT |
| Valid Until | Oct 4 23:59:59 2026 GMT |
| Public Key Algorithm | RSA |
| Public Key Size | 2048 bit |
| Extended Key Usage | TLS Web Server Authentication |
| Supported TLS Versions | TLSv1.2 |

#### Vulnerabilities Reported by Shodan

| CVE | Score | Summary |
| --- | --- | --- |
| CVE-2025-23419 | 5.3 | Possible nginx TLS session resumption issue related to client certificate authentication bypass in some configurations |
| CVE-2023-44487 | 7.5 | HTTP/2 rapid reset denial-of-service issue |
| CVE-2021-23017 | 7.7 | nginx resolver vulnerability that may cause worker crash or other impact |
| CVE-2021-3618 | 7.4 | ALPACA TLS application-layer protocol confusion attack |

---

### Entry 2 - 35.181.162.251

#### General Information

| Field | Value |
| --- | --- |
| Hostnames | ec2-35-181-162-251.eu-west-3.compute.amazonaws.com, read.holbertonschool.com |
| Domains | amazonaws.com, holbertonschool.com |
| Cloud Provider | Amazon |
| Cloud Region | eu-west-3 |
| Cloud Service | EC2 |
| Country | France |
| City | Paris |
| Organization | Amazon Data Services France |
| ISP | Amazon.com, Inc. |
| ASN | AS16509 |
| Operating System | Not shown by Shodan |

#### Web Technologies

| Component | Technology |
| --- | --- |
| Reverse Proxy | Nginx 1.20.0 |
| Security | Basic Authentication |
| Web Server | Nginx 1.20.0 |

#### Open Ports

| Port | Protocol | Service / Notes | Last Seen |
| --- | --- | --- | --- |
| 80 | TCP | HTTP service requiring Basic Authentication | 2026-05-19T21:43:00.421972 |
| 443 | TCP | HTTPS service requiring Basic Authentication; SSL certificate visible | 2026-05-23T03:28:57.681785 |

#### HTTP Response Summary

| Item | Port 80 | Port 443 |
| --- | --- | --- |
| Status | HTTP/1.1 401 Unauthorized | HTTP/1.1 401 Unauthorized |
| Server | nginx/1.20.0 | nginx/1.20.0 |
| Content-Type | text/html; charset=utf-8 | text/html; charset=utf-8 |
| Authentication | Basic Authentication | Basic Authentication |
| WWW-Authenticate | Basic realm="Application" | Basic realm="Application" |
| Security Headers | X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, X-Download-Options, X-Permitted-Cross-Domain-Policies, Referrer-Policy | X-Frame-Options, X-XSS-Protection, X-Content-Type-Options, X-Download-Options, X-Permitted-Cross-Domain-Policies, Referrer-Policy |
| Cache-Control | no-cache | no-cache |
| Content-Security-Policy | Present but empty | Present but empty |

#### SSL/TLS Information

| Field | Value |
| --- | --- |
| Certificate Version | 3 |
| Serial Number | 0a:70:50:18:b6:16:cb:9b:0e:4e:7a:1c:33:b3:80:a0 |
| Signature Algorithm | sha256WithRSAEncryption |
| Issuer | C=US, O=Amazon, CN=Amazon RSA 2048 M04 |
| Certificate Common Name | read.holbertonschool.com |
| Subject Alternative Name | DNS:read.holbertonschool.com |
| Valid From | Sep 5 00:00:00 2025 GMT |
| Valid Until | Oct 4 23:59:59 2026 GMT |
| Public Key Algorithm | RSA |
| Public Key Size | 2048 bit |
| Extended Key Usage | TLS Web Server Authentication |

#### Vulnerabilities Reported by Shodan

| CVE | Score | Summary |
| --- | --- | --- |
| CVE-2025-23419 | 5.3 | Possible nginx TLS session resumption issue related to client certificate authentication bypass in some configurations |
| CVE-2023-44487 | 7.5 | HTTP/2 rapid reset denial-of-service issue |
| CVE-2021-23017 | 7.7 | nginx resolver vulnerability that may cause worker crash or other impact |
| CVE-2021-3618 | 7.4 | ALPACA TLS application-layer protocol confusion attack |

---
