# Copy shortcut in GCP console
As Ctrl+shift+c was triggering devtools appearing everytime I wanted to copy text from GCP console for lab, had to look for workaround.
First, `sudo apt install autokey-gtk` . Then, launch AutoKey, create a new script, set the Hotkey to be Ctrl+Shift+C, 
the window filter to be `chromium-browser.Chromium-browser` , and the script contents to be `keyboard.send_keys('<ctrl>+c')` .

Once the script is saved, pressing Ctrl+Shift+C in Chromium will copy to the system clipboard instead of displaying the dev tools.

Source: [Change shortcut](https://askubuntu.com/questions/604434/chrome-disable-or-change-keyboard-shortcut-ctrlshiftc-developer-tools-console)
