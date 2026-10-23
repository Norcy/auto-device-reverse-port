"""Exercise the shell entry point with fake devices; no real mappings are changed."""
import os
from pathlib import Path
import subprocess
import tempfile

script = Path(__file__).resolve().parent.parent / 'bin/auto-device-reverse-port'
if not script.exists():
    script = Path(__file__).with_name('auto-device-reverse-port')
with tempfile.TemporaryDirectory() as tmp:
    root = Path(tmp)
    calls = root / 'calls'
    adb = root / 'adb'
    adb.write_text('''#!/bin/zsh
if [[ "$1" == devices ]]; then
  printf 'List of devices attached\\nphone-a device\\nphone-b device\\noffline-phone offline\\n'
elif [[ "$1" == -s ]]; then
  echo "$*" >> "$TEST_CALLS"
  [[ "$2" != phone-a ]]
fi
''')
    hdc = root / 'hdc'
    hdc.write_text('''#!/bin/zsh
if [[ "$1" == list ]]; then
  echo harmony-a
else
  echo "hdc $*" >> "$TEST_CALLS"
  exit 1
fi
''')
    adb.chmod(0o755)
    hdc.chmod(0o755)
    env = {k: v for k, v in os.environ.items() if not k.startswith('DEVICE_REVERSE_')}
    env.update(ADB_PATH=str(adb), HDC_PATH=str(hdc), TEST_CALLS=str(calls))
    cases = [
        ({}, ['8081:8081', '8082:8082']),
        ({'DEVICE_REVERSE_PORTS': '9090,8082:8081'}, ['9090:9090', '8082:8081']),
        ({'DEVICE_REVERSE_LOCAL_PORT': '9090', 'DEVICE_REVERSE_REMOTE_PORT': '9091'}, ['9090:9091']),
        ({'DEVICE_REVERSE_PORTS': '8082', 'DEVICE_REVERSE_LOCAL_PORT': '9090'}, ['8082:8082']),
    ]
    for config, mappings in cases:
        calls.write_text('')
        result = subprocess.run(['zsh', str(script), 'run-once'], env=env | config, capture_output=True, text=True)
        assert result.returncode == 0, result.stderr
        expected = []
        for device in ['harmony-a', 'phone-a', 'phone-b']:
            for mapping in mappings:
                local, remote = mapping.split(':')
                prefix = f'hdc -t {device} rport' if device == 'harmony-a' else f'-s {device} reverse'
                expected.append(f'{prefix} tcp:{local} tcp:{remote}')
        assert calls.read_text().splitlines() == expected, calls.read_text()
    for invalid in ['0', '65536', 'abc', '8081,', ',8081', '8081,,8082', '80:90:100', '999999999999999999999']:
        result = subprocess.run(['zsh', str(script), 'run-once'], env=env | {'DEVICE_REVERSE_PORTS': invalid}, capture_output=True)
        assert result.returncode != 0, invalid
print('Passed: defaults, multiple ports/devices, custom mappings, legacy settings, precedence, failure isolation and invalid ports')
