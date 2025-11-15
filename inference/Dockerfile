FROM python:3.13-slim

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY . .

RUN uv sync

RUN uv venv

EXPOSE 8080

# gunicorn -b 0.0.0.0:5000 app:app
CMD ["uv", "run","gunicorn", "-b", "0.0.0.0:8080", "app:app"]