#!/bin/bash

#INSTALL WINE
dpkg --add-architecture i386

wget -nc https://dl.winehq.org/wine-builds/Release.key
apt-key add Release.key
apt-add-repository https://dl.winehq.org/wine-builds/ubuntu/
apt update
apt install --install-recommends winehq-staging
apt install winetricks

#install lutris
ver=$(lsb_release -sr); if [ $ver != "18.04" -a $ver != "17.10" -a $ver != "17.04" -a $ver != "16.04" ]; then ver=18.04; fi
echo "deb http://download.opensuse.org/repositories/home:/strycore/xUbuntu_$ver/ ./" | sudo tee /etc/apt/sources.list.d/lutris.list
wget -q http://download.opensuse.org/repositories/home:/strycore/xUbuntu_$ver/Release.key -O- | sudo apt-key add -
apt update
apt install lutris

#install dxvk
apt install libvulkan1 libvulkan1:i386

#install gallium
add-apt-repository ppa:oibaf/graphics-drivers
apt update
apt upgrade
add-apt-repository ppa:commendsarnex/winedri3
apt update
apt install wine3.0
