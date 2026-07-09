# auto-device-reverse-port

使用 Android / Harmony 真机调试 React Native 时，自动执行 `adb reverse tcp:8081 tcp:8081` 或 `hdc rport tcp:8081 tcp:8081`，插上设备即可访问电脑上的 Metro 8081 服务。

## 安装

```bash
npx auto-device-reverse-port install
```

## 验证

```bash
npx auto-device-reverse-port status
```

输出中出现 `tcp:8081 tcp:8081` 即成功。

## 进阶配置

需要改端口或检测间隔时：

```bash
DEVICE_REVERSE_LOCAL_PORT=8081 DEVICE_REVERSE_REMOTE_PORT=8081 npx auto-device-reverse-port install
DEVICE_REVERSE_INTERVAL=10 npx auto-device-reverse-port install
```

## 卸载

```bash
npx auto-device-reverse-port uninstall
```
