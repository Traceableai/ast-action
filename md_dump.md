# Scan Details 👀

- Name: testMD
- ID: 23dc4ad4-81a8-448f-8d34-920982f1fff7
- Created at: 2023-05-04 11:59:28
- Environment: ast_load2
- State: Completed

# Vulnerabilities 💀

| Plugin Category             | Plugin Subcategory                      | Vulnerabilities Found 🎯 | Executed/Generated Tests 🏁 | Severity ⚠ |
| --------------------------- | --------------------------------------- | ----------------------- | -------------------------- | ---------- |
| Cat-1                       | subcat-1                                | 2                       | 10/20                      | CRITICAL ️ |
| cat-2                       | subcat-2                                | 5                       | 12/15                      | MEDIUM 🟠   |
| cat-3                       | subcat-3                                | 11                      | 51/51                      | HIGH 🔴     |
| Access Control              | Session Fixation                        | 0                       | 0/0                        | -🟡         |
| Sql Injection               | Error Based SQL Injection               | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Token Expiry                        | 0                       | 0/0                        | -🟡         |
| Authorization               | Broken Function Level Authorization     | 0                       | 0/0                        | -🟡         |
| Server Side Request Forgery | Server Side Request Forgery Blind       | 0                       | 0/0                        | -🟡         |
| Insecure Design             | HTTPS Content Available via HTTP        | 0                       | 0/0                        | -🟡         |
| Authorization               | Broken Object Level Authorization       | 0                       | 0/0                        | -🟡         |
| Insecure Design             | HTTP Redirect                           | 0                       | 0/0                        | -🟡         |
| Security Headers            | HSTS Header Misconfiguration            | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Insecure HTTP Method                    | 0                       | 0/0                        | -🟡         |
| Cross Site Scripting        | Reflected Cross Site Scripting          | 0                       | 0/0                        | -🟡         |
| Security Headers            | Referrer Policy Header Misconfiguration | 0                       | 0/0                        | -🟡         |
| Remote Code Execution       | Java Log4Shell                          | 0                       | 0/0                        | -🟡         |
| Insecure Design             | SOAP Action Spoofing                    | 0                       | 0/0                        | -🟡         |
| Business Logic              | Mass Assignment                         | 0                       | 0/0                        | -🟡         |
| Improper Asset Management   | Default Landing Page                    | 0                       | 0/0                        | -🟡         |
| Access Control              | Rate Limiting                           | 0                       | 0/0                        | -🟡         |
| Business Logic              | Parameter Tampering                     | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Invalid Signature                   | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT JKU Misuse                          | 0                       | 0/0                        | -🟡         |
| Json Web Token              | JWT Algorithm Confusion                 | 0                       | 0/0                        | -🟡         |
| Authentication              | Unauthenticated Access                  | 0                       | 0/0                        | -🟡         |
| Insecure Design             | Username and Password Enumeration       | 0                       | 0/0                        | -🟡         |
| Insecure Design             | GET for POST                            | 0                       | 0/0                        | -🟡         |
| Cross Site Scripting        | Stored Cross Site Scripting             | 0                       | 0/0                        | -🟡         |

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

![Logo](https://lp.traceable.ai/rs/803-DME-599/images/logo-horizontal-white-background.png)
