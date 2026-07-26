#! /usr/bin/bash

# Free/Freeworld/Non-Free version
RETROARCH=retroarch

pkill --signal TERM $RETROARCH
pkill --signal KILL $RETROARCH
$RETROARCH &
sleep 1 &&
pkill --signal TERM $RETROARCH
pkill --signal KILL $RETROARCH
pushd ~/.config/retroarch/
sed -e 's|menu_show_online_updater = "false"|menu_show_online_updater = "true"|' \
    -e 's|menu_show_core_updater = "false"|menu_show_core_updater = "true"|'     \
    -e 's|libretro_directory = "/usr/lib64/libretro/"| "~/.config/retroarch/cores"|' \
    -i $RETROARCH.cfg
popd

echo "To reset all settings on defaults and get back to system libretro cores remove user data dir:

 $ rm -rf ~/.config/retroarch/"
