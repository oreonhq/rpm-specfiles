text
lang en_US.UTF-8
keyboard us
timezone US/Eastern
selinux --enforcing
firewall --enabled --service=mdns
services --enabled=sshd,NetworkManager,chronyd
network --bootproto=dhcp --device=link --activate
rootpw --lock --iscrypted locked
shutdown

bootloader --timeout=1

zerombr
clearpart --all --initlabel --disklabel=msdos

# make sure that initial-setup runs and lets us do all the configuration bits
firstboot --reconfig

repo --name "packages" --url https://nowhere/

%packages
@core
@standard
@hardware-support

kernel
# on 32bit arm make sure we only install one kernel
-kernel-lpae
# remove this in %post
dracut-config-generic
-dracut-config-rescue
# install tools needed to manage and boot arm systems
@arm-tools
chrony
bcm283x-firmware
initial-setup
# Intel wireless firmware assumed never of use for disk images
-iwl*
-ipw*
-usb_modeswitch
-generic-release*

# make sure all the locales are available for inital-setup and anaconda to work
glibc-all-langpacks

%end
