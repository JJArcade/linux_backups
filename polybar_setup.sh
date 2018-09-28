#!/bin/bash

#dependicies
apt update
apt install libcairo2-dev
apt install libxcb1-dev
apt install python-dev
apt install python-xcbgen
apt install xcb-proto
apt install libxcb-image0-dev
apt install libxcb-icccm4-dev
apt install libxcb-ewmh-dev
apt install libxcb-render-util0
apt install libxcb-randr0-dev
apt install libcurl4-gnutls-dev
apt install libiw-dev
apt install libpulse-dev
apt install libxcb-util-dev


#polybar main
git clone --branch 3.2 --recursive https://github.com/jaagr/polybar ~/Documents/polybar-git
echo "You'll have to run build.sh from ~/Documents/polybar-git manually to finish install of polybar"
