sdubby - Set of systemd-boot shims that don't fit anywhere else in the distro
===========================================================

This package largly exists to replace some of the grub specific
functionality in the grubby package, while providing rpm ownership
points in the /boot/efi directories for config files created
both by anaconda and this package. It also provides a utility
for updating the loader entries files during (and possibly)
after install.

Version and Modification Information
====================================
1.0 Initial version being used with the proposed anaconda changes.

Licence Information
===================
GPLv2, See the COPYING file.

Contact
=======
jeremy.linton@arm.com
