#!/bin/sh
set -e

CLI_DIR="$HOME/.local/bin"
CLI_PATH="$CLI_DIR/auto-device-reverse-port"
BIN_URL="${AUTO_DEVICE_REVERSE_PORT_BIN_URL:-}"

mkdir -p "$CLI_DIR"

if [ -n "$BIN_URL" ]; then
  curl -fsSL "$BIN_URL" -o "$CLI_PATH"
else
  SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
  cp "$SCRIPT_DIR/bin/auto-device-reverse-port" "$CLI_PATH"
fi

chmod +x "$CLI_PATH"
"$CLI_PATH" install

echo "CLI: $CLI_PATH"
