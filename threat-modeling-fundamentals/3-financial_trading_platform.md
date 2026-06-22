## 1. Which CIA component is most critical for this system and why? Can security requirements conflict with performance requirements?
All three CIA components are important, but the most critical component for this trading platform is **Availability**.
Trading is highly time-sensitive. If the system is down, users cannot buy or sell at the right time. This could cause major financial losses because trading decisions depend on real-time market conditions. The system also has a requirement of **99.99% uptime**, which shows that keeping the platform available is extremely important.
However, Regulatory requirements such as SEC and FINRA also place strong emphasis on maintaining the integrity and accuracy of financial transactions. Incorrect, manipulated, or unauthorized trades could lead to regulatory violations, financial penalties, legal consequences, and loss of trust in the trading platform. **Integrity** is also very important because trades, account balances, and automated trading rules must not be modified incorrectly or maliciously. If trade data is changed or processed incorrectly, users could lose money and the platform could face regulatory issues.
Yes, security requirements can conflict with performance requirements. For example, security checks, encryption, validation, logging, and regulatory controls can add extra processing time. Since the platform requires trades to happen in less than **100ms**, security controls must be designed carefully so they do not slow down trading too much.

## 2. Threat Model the "Automated Trading Rules" Feature
### Risk 1: Logic Flaws in Trading Rules
A logic flaw could cause the automated trading system to interpret a trading signal incorrectly. For example, the system could sell when it should buy, or buy when it should sell.

**Impact:** This could cause users to lose money because trades may be executed incorrectly.

**Mitigation:** Trading rules should be validated before being activated. The platform should also test rules carefully and make sure the rule logic is clear and correct before executing real trades.

### Risk 2: Race Conditions or Timing Issues
Since stock prices change in real time, the system may make a decision based on one market condition, but by the time the trade executes, the situation may have changed. If multiple actions happen at the same time, trades may be executed incorrectly or at the wrong time.

**Impact:** The user may sell or buy under the wrong market conditions and suffer financial loss.

**Mitigation:** The system should handle timing carefully, process trades in the correct order, and re-check important conditions before executing the trade.

### Risk 3: Unauthorized Modification of Automated Trading Rules
An attacker who gains unauthorized access could change the user's automated trading rules. This could cause the system to execute unwanted or harmful trades.

**Impact:** This could be catastrophic for the user, causing financial loss and loss of trust in the trading platform.

**Mitigation:** Rule changes should require strong authentication and additional verification. The system should also log rule changes and notify the user when automated trading rules are changed.

## 3. Defense-in-Depth Controls After User Account Compromise
If an attacker compromises a user account, the platform should still have additional controls to limit the damage.
### 1. Multi-Factor Authentication or Step-Up Verification
Sensitive actions such as changing automated trading rules, transferring funds, or making large trades should require extra verification.
### 2. Transaction Limits
The platform should limit how much money can be transferred or traded in a certain period. This reduces the damage if an attacker gets access to the account.
### 3. Anomaly Detection
The system should detect unusual behavior, such as sudden large trades, strange trading patterns, or activity from a new location.
### 4. Secure Session Management
The platform should manage sessions securely so that stolen or suspicious sessions can be expired or revoked.
### 5. Audit Trails
The platform should keep detailed logs of important actions such as trades, fund transfers, login activity, and automated rule changes. This helps investigate attacks and supports regulatory compliance.
