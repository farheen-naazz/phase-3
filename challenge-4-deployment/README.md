# CHALLENGE 4 - DEPLOYMENT RECOVERY

Marks: 20

## INCIDENT

The inventory API container builds and starts successfully.

The application reports that it is listening on port 8000
inside the container.

However, users cannot access the application at:

http://localhost:8080/health

The deployment team reports that the container itself
is healthy, but the host cannot reach the API.

Investigate the deployment configuration.

## FILES

server.py
Dockerfile
compose.yaml
evidence/deployment.log

## STEP 1 - INSPECT THE APPLICATION

Open server.py.

Identify the address and port on which the application listens.

## STEP 2 - INSPECT THE DOCKERFILE

Check:
- EXPOSE instruction
- Application startup command
- Health check

## STEP 3 - INSPECT DOCKER COMPOSE

Open compose.yaml.

Investigate the ports configuration.

## STEP 4 - IDENTIFY THE ROOT CAUSE

Understand the difference between:
- Host port
- Container port

Correct the port mapping without changing the application listener.

## STEP 5 - DEPLOY THE APPLICATION

Run:

docker compose up --build -d

Verify:

curl.exe -i http://localhost:8080/health

Expected response:

HTTP/1.1 200 OK

{"status":"ok"}

## STEP 6 - CLEAN UP

Run:

docker compose down

## GITHUB ACTIONS

Push your corrected configuration to your fork.

Open GitHub Actions and verify the deployment smoke test.

## SUBMISSION

Submit:
1. Application listening port.
2. Incorrect deployment mapping.
3. Corrected mapping.
4. Successful HTTP health-check response.
5. Green deployment workflow evidence.
6. Commit hash of your fix.

## COMPLETION

FLAG: Not required.
The working deployment and successful smoke test are your proof.