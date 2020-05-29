source "settings.txt"
sudo $update
sudo $upgrade
sudo $distro_uninstall firefox -y
sudo $distro_install chromium-browser
sudo $distro_install libcanberra-gtk-module libcanberra-gtk3-module
sudo $distro_install curl
sudo $distro_install sl
sudo $distro_install neofetch -y
chromium http://gmail.com/
chromium http://facebook.com/
chromium http://youtube.com/
sudo $distro_install gimp -y
sudo $distro_install snap
sudo snap install --classic code
sudo snap install arduino
sudo $distro_install git -y
sudo $distro_install vlc -y
sudo $distro_install telegram-desktop -y
sudo $distro_install kdeconnect -y
sudo $distro_install xclip -y
chmod +x git_setup.sh
./git_setup.sh
