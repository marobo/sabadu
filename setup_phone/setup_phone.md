# Android ADB Install / Uninstall App Examples


#### Use ADB to Install Many Android Applications Only Run one time command.

1. All android applications or apk files we need to put all inside one folder called `setup_phone` folder or whatever you wan.

2. Create a sh file called `setup_phone.sh` then copy and pate the source bellow to `setup_phone.sh` file and change example app to app name you wan to installing.

   ```
   #!/bin/sh -e
   echo 'Installing example app...'
   adb install -r example_app.apk
   
   echo 'Installing example app...'
   adb install -r example_app.apk
   
   echo 'Installing example app...'
   adb install -r example_app.apk
   
   echo 'Installing example app...'
   adb install -r example_app.apk
   ```

3. Connecting your device phone to PC

4. In command run `adb devices` to make sure you are enable USB debugging mode then the command must showing your devices serial like down here:

   ```
   List of devices attached
   5200e09ab4dd2517	device
   ```

   If not showing you need to enable USB debugging on the phone itself on your devices, for how to enable USB debugging please visit this [enable USB debugging](https://stackoverflow.com/questions/4756451/how-to-install-an-apk-file-on-an-android-phone)

5. Run sh file with `./setup_phone.sh`  then every apps should installing on your mobile.

6. For more information and documents about Android ADB Install / Uninstall App Examples please visit this [document](https://www.dev2qa.com/android-adb-install-uninstall-app-examples/). Thanks You... Ony.