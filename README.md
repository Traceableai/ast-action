## Overview

Traceable AST (Active Security Testing) continuously tests your APIs for vulnerabilities. This GitHub Action provides a streamlined way to run AST scans, generate reports, and gate pipelines based on scan results.

## Actions

v2 provides four dedicated actions — each with minimal inputs and an `additional_cli_options` escape hatch for advanced CLI flags.

| Action | Path | Description |
|---|---|---|
| **scan** | `Traceableai/ast-action/scan@v2` | Run a local scan (`initAndRun`) |
| **queue-scan** | `Traceableai/ast-action/queue-scan@v2` | Queue a scan on remote runners |
| **report** | `Traceableai/ast-action/report@v2` | Generate and publish a detailed report |
| **gate** | `Traceableai/ast-action/gate@v2` | Pass/fail the pipeline based on scan evaluation |

### CLI Binary Management

The CLI binary is downloaded once per job and reused across all actions:
- First action to run downloads the CLI to `${GITHUB_WORKSPACE}/traceable`
- Subsequent actions detect the existing binary and skip the download
- `cli_version` (default: `latest`) is accepted on every action but only the first action's value takes effect

---

## Inputs

### scan

| Input | Required | Default | Description |
|---|---|---|---|
| `scan_name` | yes | — | Name of the scan |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

### queue-scan

| Input | Required | Default | Description |
|---|---|---|---|
| `scan_name` | yes | — | Name of the scan |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `runner_ids` | no | — | Comma-separated runner IDs (defaults to `any_runner`) |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

### report

| Input | Required | Default | Description |
|---|---|---|---|
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `output_format` | no | `md` | Report format |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

### gate

| Input | Required | Default | Description |
|---|---|---|---|
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

---

## Usage Examples

### Local scan with report and gate

```yaml
name: Traceable AST Scan
on:
  push:
    branches: [main]
  pull_request:

jobs:
  ast-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run AST scan
        uses: Traceableai/ast-action/scan@v2
        with:
          scan_name: 'my-scan'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}

      - name: Publish report
        uses: Traceableai/ast-action/report@v2
        with:
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}

      - name: Gate pipeline
        uses: Traceableai/ast-action/gate@v2
        with:
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}
```

### Queued scan with remote runners

```yaml
name: Traceable AST Queued Scan
on:
  push:
    branches: [main]
  pull_request:

jobs:
  ast-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Queue AST scan
        uses: Traceableai/ast-action/queue-scan@v2
        with:
          scan_name: 'my-scan'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}
          runner_ids: 'runner-1,runner-2'

      - name: Publish report
        uses: Traceableai/ast-action/report@v2
        with:
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}

      - name: Gate pipeline
        uses: Traceableai/ast-action/gate@v2
        with:
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}
```

### Using additional CLI options

```yaml
- name: Run AST scan with advanced flags
  uses: Traceableai/ast-action/scan@v2
  with:
    scan_name: 'my-scan'
    client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
    traceable_server: ${{ secrets.TRACEABLE_SERVER }}
    additional_cli_options: '--idle-timeout 15 --scan-timeout 600 --target-url https://api.example.com'
```
