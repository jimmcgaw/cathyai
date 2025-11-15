FROM python:3.13-slim

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync

EXPOSE 8000

# uv run gunicorn -b 0.0.0.0:8000 -k uvicorn.workers.UvicornWorker main:app
CMD ["uv", "run","uvicorn", "main:app", "--reload"]