restore:
    uv sync

lint:
    uv run ruff check

test:
    uv run pytest
