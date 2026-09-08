## Overview

Traceable AST (Active Security Testing) continuously tests your APIs for vulnerabilities. This GitHub Action provides a streamlined way to run AST scans, generate reports, and gate pipelines based on scan results.

## Actions

v2 provides dedicated actions — each with minimal inputs and an `additional_cli_options` escape hatch for advanced CLI flags.

| Action | Path | Description |
|---|---|---|
| **code-scan** | `Traceableai/ast-action/code-scan@v2` | Discover APIs from source (`code apis`, Docker) |
| **scan** | `Traceableai/ast-action/scan@v2` | Run a local scan (`initAndRun`) |
| **queue-scan** | `Traceableai/ast-action/queue-scan@v2` | Queue a scan on remote runners |
| **report** | `Traceableai/ast-action/report@v2` | Generate and publish a detailed report |
| **gate** | `Traceableai/ast-action/gate@v2` | Pass/fail the pipeline based on scan evaluation |

### CLI Binary Management

The CLI binary is downloaded once per job and reused across all actions:
- First action to run downloads the CLI to `${GITHUB_WORKSPACE}/traceable`
- Subsequent actions detect the existing binary and skip the download
- `cli_version` (default: `latest`) is accepted on every action but only the first action's value takes effect
- **code-scan** does not use the CLI binary — it runs `traceableai/traceable-cli:latest` (Joern is bundled there)

---

## Inputs

### code-scan

Requires Docker on the runner (GitHub-hosted runners have it). Runs `traceableai/traceable-cli` → `code apis`.

| Input | Required | Default | Description |
|---|---|---|---|
| `code_path` | no | `.` | Path to source code (relative to repository root) |
| `code_languages` | no | — | Comma-separated languages (`java`, `python`, `javascript`, `csharp`). Omit to auto-detect |
| `memory_limit` | no | — | Percentage of available memory for Joern (1–100). CLI default is 80 |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

### scan

| Input | Required | Default | Description |
|---|---|---|---|
| `scan_name` | no* | — | Name of the scan |
| `scan_id` | no* | — | ID of the scan config |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

\* At least one of `scan_name` or `scan_id` must be provided.

### queue-scan

| Input | Required | Default | Description |
|---|---|---|---|
| `scan_name` | no* | — | Name of the scan |
| `scan_id` | no* | — | ID of the scan config |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `runner_ids` | no | — | Comma-separated runner IDs (defaults to `any_runner`) |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

\* At least one of `scan_name` or `scan_id` must be provided.

### report

| Input | Required | Default | Description |
|---|---|---|---|
| `id` | no | — | Scan run ID (if omitted, auto-resolved from `.traceable` folder) |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `output_format` | no | `md` | Report format |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

### gate

| Input | Required | Default | Description |
|---|---|---|---|
| `id` | no | — | Scan run ID (if omitted, auto-resolved from `.traceable` folder) |
| `client_scan_token` | yes | — | Access token from platform |
| `traceable_server` | yes | — | Platform URL |
| `cli_version` | no | `latest` | CLI version |
| `additional_cli_options` | no | `''` | Extra CLI flags appended to the command |

> **Note:** Any file paths passed via `additional_cli_options` should be relative to the repository root, since that's the working directory on the runner.

---

## Usage Examples

### Code scan then AST scan

Create the scan once in the UI. CI refreshes the OpenAPI spec, then triggers that scan by name.

```yaml
name: Traceable Code Scan & AST
on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Discover APIs from source
        uses: Traceableai/ast-action/code-scan@v2
        with:
          code_path: .
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}

      - name: Queue AST scan
        uses: Traceableai/ast-action/queue-scan@v2
        with:
          scan_name: 'my-scan'
          client_scan_token: ${{ secrets.CLIENT_SCAN_TOKEN }}
          traceable_server: ${{ secrets.TRACEABLE_SERVER }}
          additional_cli_options: '--target-url https://staging-api.example.com'

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
