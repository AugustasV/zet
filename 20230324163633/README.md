# Linux Mint Bluetooth issue
Somehow often I have issue with my soundcore Space Q45 headphones that if I connect them via bluetooth, sound quallity is very poor, and if I try manually change audio mode to high fidelity, I was receiving this error message

`Failed to change profile to a2dp_sink`

after some search I found out fix that worked for me - reseting bluetooth Kernel module.

`sudo modprobe -r btusb && sleep 20 && sudo modprobe btusb`
