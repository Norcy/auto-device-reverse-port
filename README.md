# auto-device-reverse-port

使用 Android / Harmony 真机调试 React Native 时，自动为连接的设备配置 `adb reverse` 或 `hdc rport`。默认同时转发 **8081、8082**，支持多个 React Native 项目使用不同的 Metro 端口。每隔 5 秒重新检查并补上转发，设备重连后也会恢复。

## 安装

```bash
npx auto-device-reverse-port install
```

## 验证

```bash
npx auto-device-reverse-port status
```

输出中每台设备都出现 `tcp:8081 tcp:8081`、`tcp:8082 tcp:8082` 即成功。

升级后需要重新执行 `install`，后台服务才会使用新版脚本和配置。

## 进阶配置

支持逗号分隔的端口，或用 `设备端口:电脑端口` 指定映射。显式设置后会替换默认端口：

```bash
DEVICE_REVERSE_PORTS=8081,8082,8083 npx auto-device-reverse-port install
DEVICE_REVERSE_PORTS=8082:8081 npx auto-device-reverse-port install
```

旧版单端口配置仍然有效；同时设置时，`DEVICE_REVERSE_PORTS` 优先。需要改端口或检测间隔时：

```bash
DEVICE_REVERSE_LOCAL_PORT=8081 DEVICE_REVERSE_REMOTE_PORT=8081 npx auto-device-reverse-port install
DEVICE_REVERSE_INTERVAL=10 npx auto-device-reverse-port install
```

ADB 设备刚接入时会默认重试 3 次、每次间隔 1 秒，避免 ADB 服务启动或设备状态切换期间漏掉端口映射。可按需调整：

```bash
DEVICE_REVERSE_ADB_DISCOVERY_RETRIES=5 DEVICE_REVERSE_ADB_DISCOVERY_DELAY=1 npx auto-device-reverse-port install
```

## 卸载

```bash
npx auto-device-reverse-port uninstall
```
