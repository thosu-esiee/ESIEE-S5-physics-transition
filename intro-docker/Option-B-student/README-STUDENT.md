# Option B — Energy and Carbon Dashboard (student kit)

The HTML, JavaScript, CSS, Flask API, SQL seed data and Python requirements are provided.
Do not change application code. Complete only the deployment files named below.

## Your tasks
1. Create `frontend/Dockerfile` (Nginx image with site and proxy configuration).
2. Complete `frontend/default.conf` (proxy `/api/` to the Flask service).
3. Create `backend/Dockerfile` (Python 3.13 slim, install requirements, launch Flask using `flask --app app run --host=0.0.0.0 --port=5000`).
4. Create `compose.yaml`: three services `web`, `api`, `mysql`, two networks `web_net` and
   internal `data_net`. Only web publishes `127.0.0.1:8080:80`. `api` belongs to both networks.
5. Configure database initialisation using `database/init.sql`, root/user passwords via secret
   files and named storage `mysql_data` mounted on `/var/lib/mysql`.
6. Add a MySQL readiness healthcheck and `depends_on: condition: service_healthy` for the API.

To create the demonstration secret files:

    cp secrets/mysql-root-password.example secrets/mysql-root-password.txt
    cp secrets/mysql-user-password.example secrets/mysql-user-password.txt

These sample values are **training-only**, not suitable for deployment. The `.gitignore`
excludes `*.txt` from `secrets/`.

After completing the missing files:

    docker compose config
    docker compose up -d --build

Dashboard: http://localhost:8080
API through the proxy: http://localhost:8080/api/measurements

Check published ports with `docker compose ps`, and network memberships with
`docker network inspect <project>_web_net` and `<project>_data_net`.

Important: a Docker internal network prevents ordinary external routing; Docker
host administrators may still have privileged ways to inspect containers.

For this teaching exercise, the Flask development server is sufficient. It is not intended for production.
