# Scan Details 👀

- Name: testMD
- ID: f97776e8-7d16-4875-84fe-43e1ded0b6ea
- Created at: 2023-05-04 15:03:14
- Environment: ast_load2
- State: Completed

# Vulnerabilities 💀

| Plugin Category             | Plugin Subcategory                      | Vulnerabilities Found 🎯 | Executed/Generated Tests 🏁 | Severity ⚠ |
| --------------------------- | --------------------------------------- | ----------------------- | -------------------------- | ---------- |
| Cat-1                       | subcat-1                                | 2                       | 10/20                      | CRITICAL ☣ |
| cat-2                       | subcat-2                                | 5                       | 12/15                      | MEDIUM 🟠   |
| cat-3                       | subcat-3                                | 11                      | 51/51                      | HIGH 🔴     |
| Sql Injection               | Error Based SQL Injection               | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Token Expiry                        | 0                       | 0/0                        | -🟡         |
| Insecure Design             | XSLT Injection                          | 0                       | 0/0                        | -🟡         |
| Remote Code Execution       | OS Command Injection                    | 0                       | 0/0                        | -🟡         |
| Authorization               | Broken Function Level Authorization     | 0                       | 0/0                        | -🟡         |
| Server Side Request Forgery | Server Side Request Forgery Blind       | 0                       | 0/0                        | -🟡         |
| Remote Code Execution       | Buffer Overflow                         | 0                       | 0/0                        | -🟡         |
| NoSql Injection             | Blind NoSQL Injection                   | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Missing Audience Claim              | 0                       | 0/0                        | -🟡         |
| Sql Injection               | Blind SQL Injection                     | 0                       | 0/0                        | -🟡         |
| Data Exposure               | Excessive Data Exposure                 | 0                       | 0/0                        | -🟡         |
| Insecure Design             | HTTPS Content Available via HTTP        | 0                       | 0/0                        | -🟡         |
| Authorization               | Broken Object Level Authorization       | 0                       | 0/0                        | -🟡         |
| Insecure Design             | HTTP Redirect                           | 0                       | 0/0                        | -🟡         |
| Security Headers            | HSTS Header Misconfiguration            | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Anti-CSRF Tokens Check                  | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Insecure HTTP Method                    | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Weak Algorithm                      | 0                       | 0/0                        | -🟡         |
| Access Control              | Remote File Inclusion                   | 0                       | 0/0                        | -🟡         |
| Cross Site Scripting        | Reflected Cross Site Scripting          | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Regex DOS                               | 0                       | 0/0                        | -🟡         |
| Security Headers            | Referrer Policy Header Misconfiguration | 0                       | 0/0                        | -🟡         |
| Authentication              | Weak Password                           | 0                       | 0/0                        | -🟡         |
| Remote Code Execution       | Java Log4Shell                          | 0                       | 0/0                        | -🟡         |
| Remote Code Execution       | Integer Overflow Error                  | 0                       | 0/0                        | -🟡         |
| Business Logic              | Mass Assignment                         | 0                       | 0/0                        | -🟡         |
| Improper Asset Management   | Default Landing Page                    | 0                       | 0/0                        | -🟡         |
| Access Control              | Rate Limiting                           | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Weak Encryption                     | 0                       | 0/0                        | -🟡         |
| Business Logic              | Parameter Tampering                     | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Invalid Signature                   | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT JKU Misuse                          | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Algorithm Confusion                 | 0                       | 0/0                        | -🟡         |
| Authentication              | Unauthenticated Access                  | 0                       | 0/0                        | -🟡         |
| Improper Asset Management   | Multiple Versions of API                | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Username and Password Enumeration       | 0                       | 0/0                        | -🟡         |
| Insecure Design             | XPath Injection                         | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Cloud Metadata Potentially Exposed      | 0                       | 0/0                        | -🟡         |
| Insecure Design             | GET for POST                            | 0                       | 0/0                        | -🟡         |
| Cross Site Scripting        | Stored Cross Site Scripting             | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Weak HMAC Secret                    | 0                       | 0/0                        | -🟡         |

# Scan Evaluation 🔎

result: Fail ❌

## Failed rules 🚫

| Asset Type | Asset Selection | Vulnerability Selection | Severity ⚠ | Operator  | Threshold 🛑 | Actual Count 📌 |
| ---------- | --------------- | ----------------------- | ---------- | --------- | ----------- | -------------- |
| ENDPOINT   | Any             | New                     | CRITICAL ️ | LESS_THAN | 3           | 3              |

# Response Summary per API

| API 👣 | Requests |
| ----- | -------- |
| api-1 | 5        |
| api-2 | 14       |
| api-3 | 20       |

# Response Summary per Plugin

| Plugin | Requests |
| ------ | -------- |
| TLS    | 10       |
| Jwt    | 31       |

## This is doc2

| heading-1 | heading-2 |
| --------- | --------- |
| val-1     | val-2     |
| val-3     | val-4     |
