    # Swiftter - FastAPI starter package

This is a minimal FastAPI skeleton named **Swiftter** ready to upload to GitHub and deploy to a VPS.

## What's included
- FastAPI app with `/health`, `/generate` and `/token` stubs
- Dockerfile and docker-compose.yml (API + nginx)
- Nginx config for reverse proxy and Let's Encrypt ACME challenge
- Example deploy script (deploy/deploy.sh)
- `.env.example` and requirements.txt

## Quick local test
1. Copy `.env.example` to `.env` and adjust values.
2. Build and run locally:

```bash
docker compose up --build
```

3. Visit `http://localhost:8000/health`

## Upload to GitHub (browser)
1. Zip this folder (or upload folder via GitHub -> Add file -> Upload files).
2. Create repo `Swiftter` on GitHub (private/public as you prefer).
3. Upload the zip or push via git.

## Simple GitHub upload via browser
- Create new repository named `Swiftter`.
- On the new repo page, click **Add file → Upload files** and drag the contents of this project (not the outer Swiftter folder). Commit.

## Next steps
- Add GitHub Actions CI (I've included an example in .github/workflows if you want it)
- Add secrets: `DOCKER_REGISTRY`, `DOCKER_USERNAME`, `DOCKER_PASSWORD`, `SSH_PRIVATE_KEY`, `SSH_HOST`, `JWT_SECRET`, `DATABASE_URL`, `MODEL_SERVER_URL`, `BASE44_WEBHOOK_SECRET`
- Replace dev secrets before production

## Deploy to VPS
- Copy files to server (or use CI to deploy using SSH and the deploy script)
- Ensure port 80/443 open and install docker/docker-compose
- Use certbot with webroot (`/var/www/static`) to obtain certificates

