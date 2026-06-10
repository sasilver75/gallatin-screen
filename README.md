# Gallatin Screen

Minimal Python project managed with `uv` and FastAPI.

## Setup

Create or refresh the local virtual environment and install locked dependencies:

```sh
uv sync
```

Activate the virtual environment if you want an interactive shell:

```sh
source .venv/bin/activate
```

## Run

Start the FastAPI development server:

```sh
uv run fastapi dev app/main.py --host 127.0.0.1 --port 8000
```

Then open:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/health`
