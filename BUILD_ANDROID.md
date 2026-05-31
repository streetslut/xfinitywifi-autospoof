# Building Xfinity WiFi AutoSpoof Android APK

This guide explains how to build the Android APK from this repository.

## Prerequisites

### On Linux/macOS/WSL:

1. **Install Java Development Kit (JDK)**
   ```bash
   # macOS with Homebrew
   brew install openjdk@11
   
   # Ubuntu/Debian
   sudo apt-get install openjdk-11-jdk
   
   # Set JAVA_HOME
   export JAVA_HOME=/path/to/jdk
   ```

2. **Install Android SDK**
   - Download from: https://developer.android.com/studio
   - Or use command-line tools

3. **Install Python 3.9+**
   ```bash
   python3 --version
   ```

4. **Install Buildozer**
   ```bash
   pip install buildozer cython
   ```

## Build Steps

### 1. Clone/Navigate to Repository
```bash
cd xfinitywifi-autospoof
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Build APK

**Debug APK (recommended for testing):**
```bash
buildozer android debug
```

**Release APK (for distribution):**
```bash
buildozer android release
```

### 4. Locate Built APK
- **Debug:** `bin/xfinitywifi-1.0-debug.apk`
- **Release:** `bin/xfinitywifi-1.0-release.apk`

## Troubleshooting

### Issue: "buildozer: command not found"
```bash
pip install --upgrade buildozer
```

### Issue: Android SDK not found
```bash
buildozer android debug -- --ndk-version 23b --sdk-version 31
```

### Issue: Build hangs during NDK download
- Buildozer will auto-download NDK and SDK on first run (~500MB)
- This may take 10-30 minutes depending on connection
- Be patient and don't interrupt the process

### Issue: Java version mismatch
```bash
export JAVA_HOME=/path/to/jdk11
```

## Installation on Device

### Via USB Debugging:
```bash
adb install bin/xfinitywifi-1.0-debug.apk
```

### Manually:
1. Transfer APK to your Android device
2. Open file manager
3. Tap the APK file to install
4. Accept permissions

## Permissions Required

The app requires the following Android permissions:
- `INTERNET` - To access Xfinity portal
- `ACCESS_NETWORK_STATE` - To check network status
- `CHANGE_NETWORK_STATE` - To manage WiFi connections
- `ACCESS_WIFI_STATE` - To read WiFi info
- `CHANGE_WIFI_STATE` - To modify WiFi settings

## Features

✅ GUI interface for easy use
✅ Random MAC address generation
✅ Automatic credential generation
✅ Connection status monitoring
✅ Logs for debugging

## Legal Notice

This tool is for educational purposes only. Unauthorized access to computer networks is illegal. Ensure you have proper authorization before using this application.

---

For more information on Buildozer, visit: https://buildozer.readthedocs.io/
