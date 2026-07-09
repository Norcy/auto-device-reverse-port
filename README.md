# auto-device-reverse-port

使用 Android / Harmony 真机调试 React Native 时，无需再手动执行 `adb reverse` 或 `hdc rport`，自动把设备的开发端口连回电脑。

默认处理：

```bash
adb reverse tcp:8081 tcp:8081
hdc rport tcp:8081 tcp:8081
```

## 安装

```bash
npx auto-device-reverse-port install
```

安装后会注册 macOS 用户级后台任务，不需要 sudo。

## 验证

插上真机后执行：

```bash
auto-device-reverse-port status
```

看到这些信息就说明后台任务正常：

```text
服务:
  state = not running
  runs = 25
  last exit code = 0
  run interval = 3 seconds
```

说明：

- `state = not running` 是正常的，它不是常驻进程，而是定时执行一次就退出。
- `runs` 表示自动执行过多少次。
- `last exit code = 0` 表示最近一次执行成功。

继续看 `status` 里的映射列表。

Harmony 成功时会看到类似：

```text
MJE0224B05005379    tcp:8081 tcp:8081    [Reverse]
```

Android 成功时会看到类似：

```text
设备ID tcp:8081 tcp:8081
```

如果对应平台出现 `tcp:8081 tcp:8081`，就说明自动映射成功。

## 常用命令

```bash
auto-device-reverse-port status
auto-device-reverse-port uninstall
auto-device-reverse-port run-once
```

`run-once` 表示立即执行一次检测和映射，主要用于调试。

## 配置端口

默认映射 `8081 -> 8081`。需要改端口时：

```bash
DEVICE_REVERSE_LOCAL_PORT=8081 DEVICE_REVERSE_REMOTE_PORT=8081 npx auto-device-reverse-port install
```

想降低检测频率：

```bash
DEVICE_REVERSE_INTERVAL=10 npx auto-device-reverse-port install
```

没有安装 `adb` 或 `hdc` 时会直接跳过对应平台。

## 卸载

```bash
auto-device-reverse-port uninstall
```

这会删除后台任务、安装脚本副本、状态文件和日志。

