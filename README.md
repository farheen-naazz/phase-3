# RELEASE RUSH
# PHASE 3 - TESTING & DEPLOYMENT RECOVERY

Total Marks: 35

This phase contains two practical troubleshooting challenges.

## CHALLENGE 3 - AUTOMATED TESTING (15 MARKS)

The inventory application calculates customer discounts incorrectly.

Investigate the application code and failed automated tests.
Correct the implementation without weakening or deleting tests.

Directory:
challenge-3-testing/

## CHALLENGE 4 - DEPLOYMENT RECOVERY (20 MARKS)

The inventory API container starts successfully, but the
application cannot be accessed through the host port.

Investigate the application listener, Dockerfile and
Docker Compose configuration.

Directory:
challenge-4-deployment/

## PARTICIPANT REQUIREMENTS

- Git installed
- Python 3.10+
- VS Code or another code editor
- Docker Desktop is optional.
- Deployment validation is performed using GitHub Actions.
- Internet access for GitHub Actions

If Docker is unavailable locally, use the supplied GitHub Actions
deployment workflow on your team's fork.

## WORKFLOW

1. Fork this repository.
2. Clone your team's fork.
3. Investigate both incidents.
4. Fix the application and deployment configuration.
5. Run the automated tests.
6. Verify the deployment health endpoint.
7. Push your fixes to your own fork.
8. Demonstrate successful GitHub Actions runs.
9. Submit the completed submission template.

## IMPORTANT RULES

- Teams of 2â€“3 members.
- Internet searching is permitted.
- Do not modify tests just to hide failures.
- Do not remove health checks.
- Do not push directly to the official event repository.
- Preserve existing application functionality.