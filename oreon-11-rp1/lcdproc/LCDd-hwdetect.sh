#!/bin/bash

lcd_device=""
extra_lcd_devices=""
lcd_driver=""
input_name=""

add_device () {
  if [ -z "$lcd_device" ]; then
    lcd_device="$1"
    lcd_driver="$2"
    input_name="$3"
  elif [ "$1" != "$lcd_device" ]; then
    extra_lcd_devices="$extra_lcd_devices $1"
  fi
}

if [ -f /etc/lcdproc/LCDd.conf ]; then
   echo "/etc/lcdproc/LCDd.conf already exists"
   echo "If you want LCDd-hwdetect to create a new config move it out of the way"
   exit 1
fi

# USB devices where we use raw USB access (through libusb)
if [ -d /sys/bus/hid/devices ]; then
  for i in $(cat /sys/bus/usb/devices/*/modalias); do
    case "$i" in
      usb:v0403pC630d*)
        add_device "lcd2usb" "hd44780"
        ;;
    esac
  done
fi

# HID devices
if [ -d /sys/bus/hid/devices ]; then
  pushd /sys/bus/hid/devices > /dev/null
    for i in $(ls); do
      case "$i" in
        # Logitech MX5000 connected through its receiver in USB HID proxy mode
        0003:046D:B305.*)
          add_device "mx5000" "mx5000" "Logitech Wireless Keyboard PID:b305"
          ;;
        # Logitech MX5000 connected over bluetooth
        0005:046D:B305.*)
          add_device "mx5000" "mx5000" "Logitech MX5000 Keyboard"
          ;;
        # Logitech MX5500 connected through its receiver in USB HID proxy mode
        # Note the MX5500's LCD menu buttons are not accessible by the host
        0003:046D:B30B.*)
          add_device "mx5500" "mx5000"
          ;;
        # Logitech MX5500 connected over bluetooth, no usable LCD menu btns
        0005:046D:B30B.*)
          add_device "mx5500" "mx5000"
          ;;
        # Logitech G15
        0003:046D:C222.*)
          add_device "g15"    "g15" "Logitech Gaming Keyboard Gaming Keys"
          ;;
        # Logitech G15 v2
        0003:046D:C227.*)
          add_device "g15-v2" "g15" "Logitech Gaming Keyboard Gaming Keys"
          ;;
        # Logitech G510 without a headset plugged in, without USB audio intf.
        0003:046D:C22D.*)
          add_device "g510"   "g15" "Logitech Gaming Keyboard Gaming Keys"
          ;;
        # Logitech G510 with a headset plugged, with extra USB audio intf.
        0003:046D:C22E.*)
          add_device "g510"   "g15" "Logitech Gaming Keyboard Gaming Keys"
          ;;
        # Logitech Z10 speakers
        0003:046D:0A07.*)
          add_device "z-10"   "g15" "Logitech Z-10 LCD Menu Keys"
          ;;
      esac
    done
  popd > /dev/null
fi

if [ -z "$lcd_device" ]; then
  echo "No known LCD devices detected"
  exit 1
fi

echo "Detected $lcd_device LCD device"
if [ -n "$extra_lcd_devices" ]; then
  echo "Detected extra LCD devices:$extra_lcd_devices"
  echo "Multiple devices are not supported, these extra LCD devices will be ignored"
fi

# Write LCDd.conf for the found device, also:
# Disable the server screen in the rotation of screens
# Disable the annoying blinking heartbeat by default
# Disable title scrolling (set the speed to 0) most keyboard LCDs have
#  a low refresh rate making the scrolling look terrible
cat /etc/lcdproc/LCDd.conf.example | \
  sed -e "s/^Driver=curses/Driver=$lcd_driver/" \
      -e "s/#ServerScreen=no/ServerScreen=no/" \
      -e "s/#Heartbeat=open/Heartbeat=off/" \
      -e "s/#TitleSpeed=10/TitleSpeed=0/" > \
  /etc/lcdproc/LCDd.conf

# Add input-device config if specified
# Also set prev / next screen to up/down since non of the supported devices
# has enough buttons to create mappings for both left and right
# And uncomment the LeftKey and RightKey assignments so that they work
# when they are available
if [ "$input_name" ]; then
  sed -i -e "s|Driver=$lcd_driver|Driver=$lcd_driver\nDriver=linux_input|" \
         -e "s|PrevScreenKey=Left|PrevScreenKey=Up|" \
         -e "s|NextScreenKey=Right|NextScreenKey=Down|" \
         -e "s|# Device=/dev/input/event0|Device=\"$input_name\"|" \
         -e "s|#LeftKey=Left|LeftKey=Left|" \
         -e "s|#RightKey=Right|RightKey=Right|" \
    /etc/lcdproc/LCDd.conf
fi

# Device specific config bits
case "$lcd_device" in
  "lcd2usb")
    # This assume a 16x2 display as the lcd2usb board is typically sold with
    # this display on aliexpress / banggood.   There are only 2 buttons making
    # menu navigation impossible. We map button 1 to toggling auto-rotate on/off
    # and button 2 to manually switching to the next screen
    sed -i -e 's/ConnectionType=4bit/ConnectionType=lcd2usb/' \
           -e 's/Keypad=no/Keypad=yes/' \
           -e 's/#Contrast=0/Contrast=600/' \
           -e 's/Size=20x4/Size=16x2/g' \
           -e 's/KeyMatrix_4_1=Enter/# Button config for lcd2usb, not enough buttons for menu navigation/' \
           -e 's/KeyMatrix_4_2=Up/# so we only do screen rotation control/' \
           -e 's/KeyMatrix_4_3=Down/KeyDirect_1=Enter/' \
           -e 's/KeyMatrix_4_4=Escape/KeyDirect_2=Right/' \
      /etc/lcdproc/LCDd.conf
    ;;
  "g15"|"g15-2"|"g510"|"z-10")
    sed -i -e "s/# specify a non-default key map/# Keymap for the G15's 5 LCD-menu buttons/" \
           -e 's/#key=1,Escape/key=0x2b8,Escape/' \
           -e 's/#key=28,Enter/key=0x2b9,Left/' \
           -e 's/#key=96,Enter/key=0x2ba,Up/' \
           -e 's/#key=105,Left/key=0x2bb,Down/' \
           -e 's/#key=106,Right/key=0x2bc,Enter/' \
           -e 's/#key=103,Up//' \
           -e 's/#key=108,Down//' \
      /etc/lcdproc/LCDd.conf
    ;;
  "mx5000")
    sed -i -e "s/# specify a non-default key map/# Keymap for the MX5000's 4 LCD-menu buttons/" \
           -e 's/#key=1,Escape/key=0x2b8,Escape/' \
           -e 's/#key=28,Enter/key=0x2b9,Up/' \
           -e 's/#key=96,Enter/key=0x2ba,Down/' \
           -e 's/#key=105,Left/key=0x2bb,Enter/' \
           -e 's/#key=106,Right//' \
           -e 's/#key=103,Up//' \
           -e 's/#key=108,Down//' \
      /etc/lcdproc/LCDd.conf
    ;;
esac

echo "Wrote /etc/lcdproc/LCDd.conf for $lcd_device using $lcd_driver driver"

# If there is no lcdproc.conf, generate one from the example file
if [ -f /etc/lcdproc/lcdproc.conf ]; then
  exit 0
fi
  
install -p -m 644 /etc/lcdproc/lcdproc.conf.example /etc/lcdproc/lcdproc.conf

# Device specific config bits
case "$lcd_device" in
  "mx5000"|"mx5500")
    # The mx5000 and mx5500 do not do vertical-bars, disable load screen 
    sed -i -e '73s/Active=True/Active=false/' \
      /etc/lcdproc/lcdproc.conf
    ;;
esac

echo "Wrote /etc/lcdproc/lcdproc.conf"
