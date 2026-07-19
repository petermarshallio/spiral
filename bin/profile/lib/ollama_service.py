"""Owns the local Ollama background service's lifecycle for the harness.

Starts `ollama serve` on demand, the first time it's actually needed, and
shuts down only the instance this process started -- never one that was
already running before the harness launched.
"""

from __future__ import annotations

import logging
import shutil
import subprocess
import time

import requests

OLLAMA_VERSION_URL = "http://localhost:11434/api/version"
STARTUP_TIMEOUT_SECONDS = 15
STARTUP_POLL_INTERVAL_SECONDS = 0.5
SHUTDOWN_TIMEOUT_SECONDS = 10

log = logging.getLogger("uriam")


class OllamaBinaryMissingError(RuntimeError):
    pass


def is_running() -> bool:
    try:
        requests.get(OLLAMA_VERSION_URL, timeout=2)
        return True
    except requests.exceptions.RequestException:
        return False


class OllamaService:
    """Tracks whether *this* process started Ollama, so shutdown() only stops what it started."""

    def __init__(self):
        self._process: subprocess.Popen | None = None

    def ensure_running(self) -> None:
        if is_running():
            return
        if shutil.which("ollama") is None:
            raise OllamaBinaryMissingError(
                "ollama isn't on PATH -- install it from ollama.com/download or `brew install ollama`."
            )
        log.info("Ollama isn't running -- starting it...")
        self._process = subprocess.Popen(
            ["ollama", "serve"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        deadline = time.monotonic() + STARTUP_TIMEOUT_SECONDS
        while time.monotonic() < deadline:
            if is_running():
                log.info("Ollama is up.")
                return
            time.sleep(STARTUP_POLL_INTERVAL_SECONDS)
        raise RuntimeError("Started `ollama serve` but it never became reachable within 15s.")

    def shutdown(self) -> None:
        if self._process is None:
            return
        log.info("Shutting down the Ollama service this run started...")
        self._process.terminate()
        try:
            self._process.wait(timeout=SHUTDOWN_TIMEOUT_SECONDS)
        except subprocess.TimeoutExpired:
            self._process.kill()
            self._process.wait(timeout=5)
        self._process = None
        log.info("Ollama service stopped.")

    @property
    def started_by_us(self) -> bool:
        return self._process is not None
