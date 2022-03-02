#!/bin/sh

# Key Configuration


# Screen Configuration
brightnessctl -s set 180

# System Icons
# udiskie -t &
nm-applet &
# volumeicon &
# cbatticon -u 5 &
# set wallpaper
nitrogen --restore &

flameshot &
picom &
