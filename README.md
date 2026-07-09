# auto-device-reverse-port

轻量级真机端口反向映射工具。插上 Android 或 Harmony 真机后，自动建立开发端口反向映射：

```bash
adb reverse tcp:8081 tcp:8081
hdc rport tcp:8081 tcp:8081
```

适合 React Native、Metro、Harmony 调试等需要设备访问电脑本地服务的场景。

## 安装

```bash
zsh install.sh
```

安装后会注册 macOS 用户级 `launchd` 任务，不需要 sudo。

## 使用

```bash
auto-device-reverse-port status
auto-device-reverse-port uninstall
auto-device-reverse-port run-once
```

`run-once` 表示只执行一次检测和端口映射，然后立即退出。它主要给 `launchd` 定时调用，也可以手动触发调试。

## 如何验证成功

先确认后台任务已经被 `launchd` 加载：

```bash
auto-device-reverse-port status
```

服务部分看到类似下面内容表示自动任务正常：

```text
服务:
  state = not running
  runs = 25
  last exit code = 0
  run interval = 3 seconds
```

字段含义：

- `state = not running`：正常。它不是常驻进程，而是每隔几秒执行一次短任务。
- `runs = 25`：已经自动执行过 25 次。
- `last exit code = 0`：最近一次执行成功。
- `run interval = 3 seconds`：当前每 3 秒检测一次。

再确认设备映射是否存在。Harmony 设备在 `status` 的 Harmony 映射里应看到：

```text
MJE0224B05005379    tcp:8081 tcp:8081    [Reverse]
```

也可以单独执行：

```bash
hdc fport ls
```

Android 设备在 `status` 的 Android 映射里应看到：

```text
设备ID tcp:8081 tcp:8081
```

也可以单独执行：

```bash
adb reverse --list
```

如果 `status` 里 `last exit code = 0`，并且对应平台的映射列表出现 `tcp:8081 tcp:8081`，就说明自动化成功。

## 配置

默认映射 `tcp:8081 -> tcp:8081`，默认每 3 秒检测一次。

```bash
DEVICE_REVERSE_LOCAL_PORT=8081 DEVICE_REVERSE_REMOTE_PORT=8081 zsh install.sh
DEVICE_REVERSE_INTERVAL=10 zsh install.sh
HDC_PATH=/path/to/hdc zsh install.sh
ADB_PATH=/path/to/adb zsh install.sh
```

`hdc` 默认查找顺序：

1. `HDC_PATH`
2. `PATH` 中的 `hdc`
3. `/Applications/DevEco-Studio.app/Contents/sdk/default/openharmony/toolchains/hdc`

`adb` 默认查找顺序：

1. `ADB_PATH`
2. `PATH` 中的 `adb`
3. `~/Library/Android/sdk/platform-tools/adb`

## 安装位置

```text
~/.local/bin/auto-device-reverse-port
~/.local/share/auto-device-reverse-port/auto-device-reverse-port.sh
~/Library/LaunchAgents/com.norcy.auto-device-reverse-port.plist
~/Library/Logs/auto-device-reverse-port/
```

## 卸载

```bash
zsh uninstall.sh
```
