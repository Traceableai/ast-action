## Overview
In the cloud-native world, API security is an important concern as most microservices are exposed externally to users and to other internal services via APIs. Traceable AST complements the API Catalog in using the DNA to build intelligently targeted scans for detecting vulnerabilities at the API layer. It also helps close the loop of exploits found in production by running security scans in pre-prod environments. It helps in finding vulnerabilities in the early stages of SDLC, giving developers and Product security engineers more time and context to prioritize mitigation of vulnerabilities and build secure APIs. 

Traceable’s GitHub action can be used to continuously test your software builds for active vulnerabilities and get comprehensive reports which will help in deciding if a build should pass or not based on new or existing vulnerabilities exposed by the new code. It runs AST scans on triggers and maps scan results which include a list of vulnerabilities with severities based on CVSS and CWE scores to help categorize issues correctly and get a comprehensive understanding of risks added by new code added in the relevant builds. 

## What does Traceable xAST Github action provide?
- Extensive security testing coverage for microservices and APIs.
- Generate tests from live functional traffic for targeted security testing based on actual payloads
- Insertion into DevSecOps with Scan initiation and Vulnerability Management from scan findings.
- Inserts security seamlessly into existing functional tests in the same pipeline with full automation. 
- Risk-based prioritization using asset inventory, threat intel, and predictive modeling.
- Make a decision around passing or failing the build based on security issues introduced in it. 

## Getting started with Traceable AST action
### Understanding the inputs

| **Input**               | **Description**                                                    |
| ------------------- |--------------------------------------------------------------------|
| step\_name          | Scan action: init/ run/ init and run/ stop.                        |
| scan\_name          | Name of the scan                                                   |
| client\_scan\_token | Access token from platform                                         |
| cli\_version        | Version of CLI you want to use for AST. Current one is 1.0.0-rc.3. |
| traffic\_env        | Environment from where AST should observe traffic.                 |
| plugins             | List of plugins you want to run the AST scan for.                  |
| include\_url\_regex | Include URL patterns to test.                                      |
| exclude\_url\_regex | exclude URL patterns from scan.                                    |
| target\_url         | Target URL for the tests.                                          |
| traceable\_server   | URL for traceable server, not applicable for SaaS customers.       |
| idle\_timeout       | Scan timeout for a scan when it goes in IDLE state.                |
| scan\_timeout       | Scan timeout in general.                                           |
| reference\_env      | Reference environment from where AST should pick up the API specs. |
| max\_retries        | Max retries for the scan after failure.                            |


### Sample GitHub Action workflow
1. Here are the sample GitHub actions workflows which shows how you can configure the AST GitHub action. 
```
name: Test Traceable AST Init Action And Traceable AST Run Action
on:
  push:
    branches:
      - main
  pull_request:

jobs:
  AstScan:
    runs-on: ubuntu-20.04
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Init scan action
        uses: Traceableai/ast-action@main
        with:
          step_name: 'init'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traffic_env: 'crapi-demo-1'
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}
      - name: Run a loop as functional test (This is sample)
        run: |
          for ((i=1;i<=100;i++)); 
          do 
             echo $i
          done
      - name: Run scan action
        uses: Traceableai/ast-action@main
        with:
          step_name: 'run'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traffic_env: 'crapi-demo-1'
          cli_version: '1.0.0-rc.3'
      
      - name: Stop Scan
        if: always()
        uses: Traceableai/ast-action@main
        with:
          step_name: 'stop'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN_DEMO }}
          traffic_env: 'crapi-demo1'
          traceable_server: ${{ secrets.TRACEABLE_SERVER_DEMO }}
```

```
name: Test Traceable AST Init And Run Action
on:
  push:
    branches:
      - main
  pull_request:

jobs:
  InitAndRunAstScan:
    runs-on: ubuntu-20.04
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      - name: Init and run scan action
        uses: Traceableai/ast-action@main
        with:
          step_name: 'init and run'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN_DEMO }}
          cli_version: '1.0.0-rc.3'
          traffic_env: 'crapi-demo1'
          traceable_server: ${{ secrets.TRACEABLE_SERVER_DEMO }}
      - name: Stop Scan
        if: always()
        uses: Traceableai/ast-action@main
        with:
          step_name: 'stop'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN_DEMO }}
          traffic_env: 'crapi-demo1'
          traceable_server: ${{ secrets.TRACEABLE_SERVER_DEMO }}
          
  functionalTest: // (This is a sample functional test that runs in parallel to scans)
    runs-on: ubuntu-20.04
    steps:
      - name: Run a loop as functional test
        run: |
          for ((i=1;i<=100;i++)); 
          do 
             echo $i
          done

```
2. As you can see in the above workflow, we have initiated the scan with initiate scan action step which takes client_scan_token, traffic_env, and traceable_server as input. 
3. In the next step we are executing functional tests and then running the scan in the step after that which take client_scan_token,traffic_env, and cli_version as input. 



