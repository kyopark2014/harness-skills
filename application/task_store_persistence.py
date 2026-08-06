"""Local SQLite persistence helpers for the Harness UI task store."""

from __future__ import annotations

import logging
import os
import threading

logger = logging.getLogger("task_store_persistence")

_APPLICATION_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_WORKING_DIR = os.path.join(_APPLICATION_DIR, "data")

db_write_lock = threading.RLock()


def persistence_enabled() -> bool:
    """Harness UI uses local SQLite only (no S3 Files mount required)."""
    return False


def working_db_path() -> str:
    custom = os.environ.get("TASK_DB_WORKING_PATH", "").strip()
    if custom:
        return custom
    return os.path.join(_DEFAULT_WORKING_DIR, "tasks.db")


def persistent_db_path() -> str:
    return working_db_path()


def restore_tasks_db() -> None:
    """No-op for local-only mode."""
    return


def schedule_persist() -> None:
    """No-op for local-only mode."""
    return


def flush_persist() -> None:
    """No-op for local-only mode."""
    return
