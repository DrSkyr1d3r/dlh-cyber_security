# 1. Identify three STRIDE threats for the checkout process. For each threat, specify:
  - STRIDE category
  - Threat description
  - Potential impact
  - Suggested mitigation

## Spoofing:
### Description:
An attacker steals a user’s session token or credentials and impersonates the customer during checkout, placing orders or making purchases using the victim’s account.
### Impact:
Unauthorized purchases, financial loss for the customer, fraudulent orders, and loss of customer trust.
### Mitigation:
Multi-factor authentication (MFA), secure session management, HTTPS, session expiration, and re-authentication for high-value purchases.
## Tampering: 
### Description:
An attacker modifies the checkout request, such as changing the order total, item price, or payment status, and attempts to make the backend mark the order as paid without a valid Stripe payment confirmation.
### Impact:
The attacker could receive products without paying the correct amount, causing financial loss to the e-commerce platform.
### Mitigation:
Do not trust prices or payment status from the frontend. Recalculate totals on the backend, validate all inputs, use server-side order verification, verify Stripe payment/webhook signatures, and only mark an order as paid after confirmation from Stripe.
## Repudiation: 
### Description:
A user completes a purchase and later denies having made the transaction, claiming it was unauthorized and requesting a refund or chargeback.
### Impact:
Financial loss for the e-commerce platform, chargeback fees, fraud, and disputes with customers/payment providers.
### Mitigation:
Comprehensive audit logging, secure timestamps, order confirmation emails, payment transaction IDs, IP/device logging, and tamper-proof logs.
## Information Disclosure: 
### Description:
An attacker exploits an injection vulnerability during checkout to access sensitive information such as customer details, order history, delivery addresses, or payment-related records.
### Impact:
Exposure of sensitive customer data, privacy violations, reputational damage, and possible regulatory penalties.
### Mitigation:
Use parameterized queries, input validation, least-privilege database access, encrypt sensitive data, and sanitize error messages.
## Denial of Service: 
### Description:
An attacker floods the checkout endpoint with a large number of fake requests, exhausting server resources and preventing legitimate customers from completing purchases
### Impact:
Financial loss due to missed sales, reduced customer satisfaction, reputational damage, and customers moving to competing platforms.
### Mitigation:
Rate limiting, DDoS protection services, load balancing, traffic filtering, monitoring, and auto-scaling.
## Elevation of Privileages: 
### Description:
An attacker exploits a flaw in the checkout or order management API to gain administrative privileges, allowing them to modify orders, refunds, prices, or customer information
### Impact:
Exposure of sensitive data, unauthorized modification of orders, data exfiltration, financial loss, regulatory penalties, and loss of customer trust.
### Mitigation:
Principle of least privilege, role-based access control (RBAC), server-side authorization checks, regular security patching, and input validation.

# What trust boundaries exist in this system? Describe at least three.
## Browser / React Frontend → Backend API
This is a trust boundary because data moves from the user-controlled browser into the backend system. The frontend cannot be trusted because users can modify requests using browser developer tools, Burp Suite, or scripts. Therefore, the backend must validate all input, check authentication, and enforce authorization.
## Backend API → PostgreSQL Database
This is a trust boundary because data moves from the application layer into the protected database layer. The database stores sensitive information such as users, orders, and payment-related records. The backend should only send validated queries, use parameterized statements, and access the database with least-privilege permissions.
## Backend API → Stripe Payment Service
This is a trust boundary because the system communicates with an external third-party payment provider. Payment requests and responses leave the e-commerce system and cross into Stripe’s environment. Communication must use HTTPS, API authentication, and Stripe webhook/signature verification before marking payments as successful.
