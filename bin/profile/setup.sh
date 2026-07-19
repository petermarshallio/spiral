#!/usr/bin/env bash
# One-time setup for the profiling harness: venv, deps, .env, Ollama models.
# Safe to re-run -- skips anything already done.
set -euo pipefail

cd "$(dirname "${BASH_SOURCE[0]}")"

if [ ! -d .venv ]; then
  echo "Creating virtualenv..."
  python3 -m venv .venv
fi

source .venv/bin/activate
echo "Installing Python dependencies..."
pip install --upgrade pip -q
pip install -r requirements.txt -q

if [ ! -f .env ]; then
  cp .env.example .env
fi

if ! grep -q '^ANTHROPIC_API_KEY=.\+' .env; then
  read -r -s -p "Enter your ANTHROPIC_API_KEY: " api_key
  echo
  if [ -z "$api_key" ]; then
    echo "No key entered -- leaving ANTHROPIC_API_KEY blank in .env. Edit it manually before running run.py."
  else
    # Portable in-place edit (macOS/BSD sed requires an explicit backup suffix).
    sed -i '' "s|^ANTHROPIC_API_KEY=.*|ANTHROPIC_API_KEY=${api_key}|" .env
    echo "Saved to .env"
  fi
else
  echo ".env already has an ANTHROPIC_API_KEY -- leaving it alone."
fi

OLLAMA_MODELS=(tinyllama llama2:7b mistral:7b llama3.1:8b qwen2.5:7b)

if command -v ollama >/dev/null 2>&1; then
  echo "Ollama found -- pulling local models used by models.yaml (${OLLAMA_MODELS[*]})..."
  for model in "${OLLAMA_MODELS[@]}"; do
    ollama pull "$model"
  done
else
  echo "Ollama not found on PATH -- skipping local model pulls."
  echo "Once it's installed, run: ${OLLAMA_MODELS[*]/#/ollama pull }"
fi

echo "Setup complete. Run: source .venv/bin/activate && python run.py"
