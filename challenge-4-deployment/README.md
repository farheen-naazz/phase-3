
# Challenge 4 - Deployment Recovery

Marks: 20

## Incident

The Inventory API container configuration has a port
mapping error.

The application listens inside the container on port 8000,
but users cannot access it through host port 8080.

Your task is to identify and correct the deployment issue.

## Files

- server.py
- Dockerfile
- compose.yaml
- evidence/deployment.log

## Step 1 - Investigate

Inspect server.py and identify the application listening port.

Inspect Dockerfile and identify the exposed port.

Inspect compose.yaml and identify the port mapping.

## Step 2 - Identify the problem

Understand the difference between:

Host port: The port accessed by users.

Container port: The port on which the application listens
inside the container.

## Step 3 - Fix the configuration

Correct compose.yaml without changing the application
listening port.

## Step 4 - Validate using GitHub Actions

Docker Desktop is NOT required.

1. Fork the official challenge repository.
2. Fix compose.yaml.
3. Commit and push your change.
4. Open your GitHub fork.
5. Navigate to Actions.
6. Open Phase 3 - Deployment Recovery.
7. Verify that the deployment smoke test passes.

GitHub Actions will build the Docker image, start the container,
test the health endpoint and clean up the container.

Expected endpoint:

http://localhost:8080/health

Expected response:

HTTP 200 OK

{"status":"ok"}

## Optional Local Validation

Participants with Docker installed can also run:

docker compose up --build -d

curl.exe -i http://localhost:8080/health

docker compose down

## Submission

Submit:

1. Application listening port.
2. Incorrect port mapping.
3. Corrected port mapping.
4. Root cause explanation.
5. Successful GitHub Actions run.
6. Fix commit hash.
