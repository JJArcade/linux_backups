#!/usr/bin/env bash

echo "doing update and upgrade"
apt-get update
apt-get upgrade

#Set up defaults
echo "installing zsh"
apt-get install zsh

echo "installing python dev"
apt-get update
apt-get install -y python3-dev python3-pip

echo "installing build essential"
apt-get install -y build-essential

#echo "installing Git"
#apt-get install -y git

echo "installing i3 and openbox"
apt-get install -y i3 openbox

echo "installing rxvt-unicode"
apt-get install -y rxvt-unicode

echo "installing vim"
apt-get install -y vim

echo "installing xbindkeys and feh"
apt-get install -y xbindkeys feh

echo "installing weechat"
apt-get install -y weechat

echo "installing conky"
apt-get install -y conky

echo "isntalling sqlite3"
apt-get install -y sqlite3

#echo "installing scilab-cli"
#apt-get install scilab-cli

#more complicated installs
echo "setting up vim"
cp -rf ./.vimrc ~/
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

echo "installing nvm"
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash

#64 bit installs
test=$(uname -m)
echo "$test"
if [ $test = "x86_64" ]
then
  #install atom
  echo "installing atom"
  curl -sL https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add -
  sh -c 'echo "deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main" > /etc/apt/sources.list.d/atom.list'
  apt-get update
  apt-get install atom

  echo "installing Gnome"
  apt-get install gnome
fi
