#!/bin/zsh
set -e

ROOT="${0:A:h}"
CLI_DIR="$HOME/.local/bin"
CLI_PATH="$CLI_DIR/auto-device-reverse-port"

mkdir -p "$CLI_DIR"
cp "$ROOT/bin/auto-device-reverse-port" "$CLI_PATH"
chmod +x "$CLI_PATH"
"$CLI_PATH" install

echo "CLI: $CLI_PATH"
