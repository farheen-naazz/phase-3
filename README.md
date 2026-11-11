# RELEASE RUSH
## Phase 3 — Testing & Deployment Recovery

**Total Marks: 35**

This phase contains two practical troubleshooting challenges.

- Challenge 3 — Automated Testing: 15 marks.
- Challenge 4 — Deployment Recovery: 20 marks.

Your team must investigate and resolve both incidents.

---

### CHALLENGE 3 — AUTOMATED TESTING

**15 MARKS**

#### INCIDENT

The Inventory application is producing incorrect customer pricing results.

The automated test suite reports failures.

Your team must investigate the supplied application code and test reports, identify the underlying problem and restore the expected application behavior.

**Challenge directory:** `challenge-3-testing/`

#### YOUR TASKS

1. Investigate the application implementation.
2. Analyse the supplied automated test cases.
3. Identify the cause of the incorrect results.
4. Implement a correction.
5. Preserve the original application functionality.
6. Run the complete supplied test suite.
7. Provide evidence that the tests pass.

---

### CHALLENGE 4 — DEPLOYMENT RECOVERY

**20 MARKS**

#### INCIDENT

The Inventory API deployment pipeline is unable to validate application accessibility through the configured host port.

The container may start successfully, but the deployment health check is unsuccessful.

Your team must investigate the application, container configuration and deployment manifests to restore accessibility.

**Challenge directory:** `challenge-4-deployment/`

#### YOUR TASKS

1. Investigate the application server configuration.
2. Inspect the Dockerfile.
3. Examine the Docker Compose configuration.
4. Identify the deployment issue.
5. Implement the required correction.
6. Preserve the existing application functionality.
7. Trigger the hosted deployment workflow.
8. Verify that the health endpoint responds successfully.

---

### PARTICIPANT SETUP

**Step 1 — Clone the official repository**

https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-3-Testing-Deployment

```bash
git clone https://github.com/sammjoshuaa07-ui/ReleaseRush-Phase-3-Testing-Deployment.git
cd ReleaseRush-Phase-3-Testing-Deployment
```

**Step 2 — Create your team's repository**

The team leader must create a new, empty GitHub repository.

Suggested name:

`RR-TEAM-ID-Phase-3-Testing-Deployment`

Do not initialize the repository with a README, Gitignore or license.

**Step 3 — Configure your remotes**

```bash
git remote rename origin source
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Verify:

```bash
git remote -v
```

- `origin` = your team's repository.
- `source` = official event repository.

**Step 4 — Push the starter code**

```bash
git push -u origin main
```

Work only in your team's copy.

---

### SOFTWARE REQUIREMENTS

- Git installed.
- Python 3.10 or newer.
- VS Code or another code editor.
- Stable internet connection.
- Modern web browser.
- Docker Desktop is optional.

Deployment validation is performed using GitHub Actions. You do not need Docker Desktop installed locally.

---

### VALIDATION

For Challenge 3, run the supplied tests from inside `challenge-3-testing`.

Windows:

```powershell
py -m unittest discover -s tests -v
```

Other systems:

```bash
python -m unittest discover -s tests -v
```

For Challenge 4, use the supplied GitHub Actions deployment workflow.

Open your team's repository and inspect the latest deployment workflow run.

Verify that:

- The container image builds successfully.
- The application starts successfully.
- The health check succeeds.
- The health endpoint returns HTTP 200.
- The deployment workflow completes successfully.

The deployment health endpoint is:

`http://127.0.0.1:8080/health`

---

### COMMIT AND PUSH YOUR SOLUTIONS

From the repository root, check your changes:

```bash
git status
```

Stage your changes:

```bash
git add .
```

Commit:

```bash
git commit -m "fix: resolve testing and deployment incidents"
```

Push to your team's repository:

```bash
git push origin main
```

Never push to the official repository or the `source` remote.

---

### SUBMISSION REQUIREMENTS

Submit:

1. Team ID and member names.
2. Your team's repository URL.
3. Challenge 3 root cause.
4. Description of the testing correction.
5. Automated test evidence.
6. Challenge 4 root cause.
7. Description of the deployment correction.
8. Successful deployment workflow link.
9. Health endpoint validation evidence.
10. Final commit hash.
11. Completed `SUBMISSION_TEMPLATE.md`.
12. Both challenge flags.

### RULES

- Teams of 2–3 members.
- Internet search is permitted.
- Discussion only within your own team.
- Do not modify tests to hide failures.
- Do not remove health checks.
- Do not delete required configuration files.
- Preserve existing application functionality.
- Do not push to the official event repository or the `source` remote.
- All solutions must be pushed to your own repository.

**Good luck!**
