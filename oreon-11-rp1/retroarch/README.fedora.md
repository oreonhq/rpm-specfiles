# RetroArch Fedora

## How to download and install more libretro cores

Network access disabled by default in RetroArch Fedora build due security reasons. Only free libretro cores available which packaged in official Fedora repo. To obtain more libretro cores you need to:

  1. Run in terminal:
     ```bash
     $ retroarch-enable-network-access.sh
     ```
  2. Now run RetroArch and go to: `Main Menu -> Load Core -> Download a Core`.

## How to reset all settings on defaults

To reset all settings on defaults and get back to system libretro cores remove user data dir:

```bash
$ rm -rf ~/.config/retroarch/
```
