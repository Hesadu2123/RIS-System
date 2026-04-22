[app]
# ඇප් එකේ නම
title = IRIS System
# පැකේජ් එකේ නම
package.name = irisapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# අවශ්‍ය කරන ලයිබ්‍රරි (මේවා ඉතා වැදගත්)
requirements = python3,kivy==2.3.0,opencv4android,numpy

orientation = portrait
fullscreen = 1

# Android සඳහා අවශ්‍ය දේවල්
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.permissions = CAMERA
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
