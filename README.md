# Linux quickstart installer

This installer was developed to speed up setup process of any distro of linux. You can change few parameters in ```settings.txt```. Feel free to edit it or add your own programs or delete my programs. I created this installer for my needs of programming Arduino and Python but you can easily customise it.  

## Parameters which can be changed
* ```Name``` - your git name
* ```Email``` - your git email
* ```FolderName``` - name of folder which script creates for your git repositories
* ```distro_install``` - command in your distro and using your package manager to install program
* ```distro_uninstall``` -command in your distro and using your package manager to uninstall/purge program
* ```update``` - command in your distro to update packages
* ```upgrade``` - command in your distro to upgrade packages

## Programs installed by this installer
* ```Chromium```
* ```Curl ```
* ```sl ```
* ```neofetch ```
* ```Gimp ```
* ```Snap ```
* ```Arduino ```
* ```Git ```
* ```VLC ```
* ```Telegram desktop ```
* ```Kde connect ```
* ```xclip ```


### How to run script
1. Edit ```settings.txt``` for your distro options, package manager options and your git credentials
1. Make ```run.sh``` executable using terminal command in folder containing script with command ```chmod x run.sh```
1. Execute ```run.sh``` using terminal command in folder containing script with command ```./run.sh```
