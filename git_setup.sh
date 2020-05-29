source "settings.txt"
git config --global user.name $Name
git config --global user.email $Email
mkdir ~/$FolderName
ssh-keygen -t rsa -b 4096 -C $Email
chromium http://github.com/ </dev/null >/dev/null 2>&1 & disown
clear
echo "Key copied to your clipboard:"
echo ""
cat /home/$USER/.ssh/id_rsa.pub
cat /home/$USER/.ssh/id_rsa.pub | xclip -i -selection clipboard
echo ""

