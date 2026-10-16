#!/bin/sh
set -e

# Run Alembic schema migrations on container initialization
echo "[JobPulse] Applying database schema migrations via Alembic..."
alembic upgrade head

# Execute container CMD (e.g. uvicorn server)
echo "[JobPulse] Starting server process..."
exec "$@"
