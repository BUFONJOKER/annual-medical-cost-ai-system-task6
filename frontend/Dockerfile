FROM python:3.13-slim-bookworm

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

EXPOSE 8501

# Run the application.
ENTRYPOINT ["/app/.venv/bin/streamlit", "run","app.py", "--server.port=8501", "--server.address=0.0.0.0"]
