# Kindle Lazybones

     .-.     _
    (   `. .' )
     `\  `  .'
       |   |
       |   |
       | 66|_
       |  ,__)
       |(,_|
       | | 
       | \_,
       |   |
       |   |
     .'     \
    (    ,   )
     '--' '-'

Remote controlling utilities for Kindle.

## Feature

  - Flip over Kindle with your smartphone.

## Issues

  - Currently only Kindle PaperWhite is supported, PW2/PW3 are not yet.
  - Kindle still goes to sleep after 10 minutes, a temporary solution is running the searchbox command `~ds` to disable screensaver, but only a restart can resume it. The other way is changing 10 minutes to longer by modifying `/etc/kdb/system/daemon/powerd/t1_timeout`, but it's readonly although I've run `mntroot rw`.
  - Button sizes won't be adjusted correctly when the orientation of Android smartphones changes (*from landscape to portrait or vice versa*), a temporary solution is refreshing the page. iOS devices don't have this problem.

## Project Architechture

  - kindle/  Server-side files for Kindle.

## User Guide

### Jailbreak Kindle

Jailbreaking Kindle allows you to access its operating system.

For how to do that, refer to [Kindle 5.6.5 越狱教程：支持所有 5.6.5 固件](http://kindlefere.com/post/307.html) in chinese or [5.6.5 Jailbreak (closed-kindle) -- released!](http://www.mobileread.com/forums/showthread.php?t=265675) in english.

### Install KUAL, MRPI and USBNetwork

KUAL is an application launcher for Kindle, MRPI is a package installer plugin for KUAL and USBNetwork is a package which provides SSH service for Kindle.

For how to do that, refer to [Kindle 5.6.5 越狱插件资源下载及详细安装步骤](http://kindlefere.com/post/311.html) in chinese or the following in english:

  - [KUAL: Kindle Unified Application Launcher (v 2.6)](http://www.mobileread.com/forums/showthread.php?t=203326)
  - [MobileRead Package Installer](http://www.mobileread.com/forums/showthread.php?t=251143)
  - [Kindle Touch/PW1/PW2 5.0.x - 5.4.4.2 JailBreak. Plus FW 5.x USBNetwork.](http://www.mobileread.com/forums/showthread.php?t=186645)

### Install Python

As this project is mainly written in Python, so refer to [FW 5.x ScreenSavers Hack](http://www.mobileread.com/forums/showthread.php?t=195474).

### Open Access to Port 8080

Lazybones communicates with remote controllers on port 8080, so add the following line to `/etc/sysconfig/iptables`:

> -A INPUT -p TCP --dport 8080 -j ACCEPT

### Install Lazybones

Put `kindle/` under `/opt/` and rename it to **lazybones**.

As Kindle uses Upstart to handle system startup jobs, run the following command to make Lazybones run automatically on OS startup:

```bash
cp /opt/lazybones/etc/upstart/lazybones.conf /etc/init/
```

### Usage

Restart Kindle, enable WIFI and it should works.

Type `;711` in the search box in Kindle and press Enter, this shows its WIFI infomation, find the IP address (*assuming that's 192.168.1.103*) and visit `http://192.168.1.103:8080` on your smartphone.