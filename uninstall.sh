#!/bin/sh
set -e

CLI_PATH="$HOME/.local/bin/auto-device-reverse-port"
if [ -x "$CLI_PATH" ]; then
  "$CLI_PATH" uninstall
fi
rm -f "$CLI_PATH"
echo "已移除 auto-device-reverse-port"
