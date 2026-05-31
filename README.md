# conductor-sample-app

Sample application with **intentional** security and code quality issues.

This repo is a test target for [Conductor](https://github.com/sheshisheri-hi/AgenticConductor) multi-agent AI workflows. Conductor agents analyse the issues, plan fixes, and (in `integration` mode) create real branches and PRs against this repo.

> ⚠️ **These issues are intentional.** Do not use this code in production.

---

## Files and Issues

| File | Scanner | Issue |
|------|---------|-------|
| `snyk/requirements_vulnerable.txt` | Snyk | `requests==2.18.0` → CVE-2023-32681 (SSRF) |
| `snyk/app_with_dep_vuln.py` | Snyk | Flask app importing vulnerable `requests` |
| `sonar/auth_handler.py` | SonarQube | SQL injection + hardcoded credential |
| `blackduck/package_copyleft.py` | BlackDuck | `PyPDF2` GPL-3.0 license violation |
| `ado/buggy_calculator.py` | ADO defect | Off-by-one + division by zero |
| `ado/feature_stub.py` | ADO story | Unimplemented `paginate()` |

---

## How Conductor Uses This Repo

```bash
# Run Conductor in integration mode — real LLM + real GitHub PRs
./dev.sh sample snyk default integration
```

Conductor will:
1. Load the fixture JSON for the scenario (no real scanner token needed)
2. Run real LLM agents (Copilot `gpt-4.1`) to analyse and plan the fix
3. Create a branch `conductor/<run_id>/conductor-sample-app` in this repo
4. Commit the LLM-generated fix
5. Open a Pull Request — you can review and merge or close it

After testing, clean up branches and PRs with:
```bash
./dev.sh clean-integration   # deletes conductor/* branches + open PRs in test repos
```

---

## Environment Variables Required (integration mode)

```env
GITHUB_TOKEN=ghp_...             # needs repo + pull_request scope
GITHUB_ORG=sheshisheri-hi
CONDUCTOR_BRANCH_PREFIX=conductor
```
