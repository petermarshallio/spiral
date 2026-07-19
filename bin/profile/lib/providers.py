"""Chat-completion clients for the profiling harness.

Both providers expose the same interface -- send(messages, system) -> Reply
-- so run.py doesn't need to know which one it's talking to.
"""

from __future__ import annotations

from typing import NamedTuple

import anthropic
import requests

DEFAULT_MAX_TOKENS = 4096
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
OLLAMA_TIMEOUT_SECONDS = 600


class Reply(NamedTuple):
    text: str
    truncated: bool
    input_tokens: int
    output_tokens: int


class OllamaUnavailableError(RuntimeError):
    """The Ollama service itself can't be reached."""


class OllamaModelNotFoundError(RuntimeError):
    """The service is up, but the requested model tag isn't pulled locally."""


class AnthropicProvider:
    def __init__(self, model: str):
        self.model = model
        self._client = anthropic.Anthropic()

    def send(self, messages: list[dict], system: str) -> Reply:
        response = self._client.messages.create(
            model=self.model,
            max_tokens=DEFAULT_MAX_TOKENS,
            system=system,
            messages=messages,
        )
        text = "".join(block.text for block in response.content if block.type == "text")
        return Reply(
            text=text,
            truncated=response.stop_reason == "max_tokens",
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
        )


class OllamaProvider:
    def __init__(self, model: str):
        self.model = model

    def send(self, messages: list[dict], system: str) -> Reply:
        payload_messages = [{"role": "system", "content": system}, *messages]
        try:
            response = requests.post(
                OLLAMA_CHAT_URL,
                json={"model": self.model, "messages": payload_messages, "stream": False},
                timeout=OLLAMA_TIMEOUT_SECONDS,
            )
        except requests.exceptions.ConnectionError as exc:
            raise OllamaUnavailableError(
                f"Can't reach Ollama at {OLLAMA_CHAT_URL} -- is it running? Try: ollama serve"
            ) from exc

        if response.status_code == 404:
            detail = ""
            if response.content:
                try:
                    detail = f" ({response.json().get('error', response.text)})"
                except ValueError:
                    detail = f" ({response.text})"
            raise OllamaModelNotFoundError(
                f"'{self.model}' isn't pulled -- try: ollama pull {self.model}{detail}"
            )
        response.raise_for_status()

        data = response.json()
        return Reply(
            text=data["message"]["content"],
            truncated=data.get("done_reason") == "length",
            input_tokens=data.get("prompt_eval_count", 0),
            output_tokens=data.get("eval_count", 0),
        )


def get_provider(provider: str, model: str) -> AnthropicProvider | OllamaProvider:
    if provider == "anthropic":
        return AnthropicProvider(model)
    if provider == "ollama":
        return OllamaProvider(model)
    raise ValueError(f"Unknown provider: {provider!r}")
