%global source0_hash none

# we don't want to provide private python extension libs
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}

Summary: HP Linux Imaging and Printing Project
Name: hplip
Version: 3.25.8
Release: 2%{?dist}
# most files (base/*, *, ui*/...) - GPL2+
# prnt/hpijs/ jpeg related files - IJG
# prnt/* - BSD-3-Clause-HP - it is modified a little, asked here https://gitlab.com/fedora/legal/fedora-license-data/-/issues/267
# base/exif.py - BSD-2-Clause - reported as https://gitlab.com/fedora/legal/fedora-license-data/-/issues/268
# base/ldif.py - python-ldap - reported https://gitlab.com/fedora/legal/fedora-license-data/-/issues/269
# io/*, scan/* - MIT
# protocol/discovery/* - LGPL-2.1-or-later
# protocol/* - GPL2only
# scan/sane/sane.h - Public Domain
License: GPL-2.0-or-later AND MIT AND BSD-3-Clause-HP AND IJG AND GPL-2.0-only AND LGPL-2.1-or-later AND BSD-2-Clause AND LicenseRef-Public-Domain AND python-ldap

Url: https://developers.hp.com/hp-linux-imaging-and-printing
# Original source tarball
# Source0: http://downloads.sourceforge.net/sourceforge/hplip/hplip-%%{version}.tar.gz
#
# Repacked source tarball without redundant files - always repack
# the original tarball once a new version arrives by:
#
# ./hplip-repack.sh <version>
#

Source0: hplip-%{version}-repack.tar.gz
Source1: hpcups-update-ppds.sh
Source2: copy-deviceids.py
Source3: %{name}.appdata.xml
Source4: hp-laserjet_cp_1025nw.ppd.gz
Source5: hp-laserjet_professional_p_1102w.ppd.gz
Source6: hplip-repack.sh
Source7: hp-plugin.in

Patch1: hplip-pstotiff-is-rubbish.patch
Patch2: hplip-strstr-const.patch
Patch3: hplip-ui-optional.patch
Patch4: hplip-no-asm.patch
Patch5: hplip-deviceIDs-drv.patch
Patch6: hplip-udev-rules.patch
Patch7: hplip-retry-open.patch
Patch8: hplip-snmp-quirks.patch
Patch9: hplip-hpijs-marker-supply.patch
Patch10: hplip-clear-old-state-reasons.patch
Patch11: hplip-hpcups-sigpipe.patch
Patch12: hplip-logdir.patch
Patch13: hplip-bad-low-ink-warning.patch
Patch14: hplip-deviceIDs-ppd.patch
Patch15: hplip-ppd-ImageableArea.patch
Patch16: hplip-scan-tmp.patch
Patch17: hplip-log-stderr.patch
Patch18: hplip-avahi-parsing.patch
Patch19: hplip-dj990c-margin.patch
Patch20: hplip-strncpy.patch
Patch21: hplip-no-write-bytecode.patch
Patch22: hplip-silence-ioerror.patch
Patch23: hplip-sourceoption.patch
Patch24: hplip-noernie.patch
Patch25: hplip-appdata.patch
Patch26: hplip-check-cups.patch
Patch27: hplip-typo.patch
# python3 - recent HP release removed encoding/decoding to utf-8 in fax/pmlfax.py -
# that results in text string going into translate function in base/utils.py, which
# expects binary string because of parameters. Remove this patch if base/utils.py
# code gets fixed.
Patch28: hplip-use-binary-str.patch
# m278-m281 doesn't work correctly again
Patch29: hplip-error-print.patch
Patch30: hplip-hpfax-importerror-print.patch
Patch31: hplip-wifisetup.patch
# pgp.mit.edu keyserver got bad connection, so we need to have pool of keyservers
# to choose (Bz#1641100, launchpad#1799212)
# F42+ update: HP has new key, and currently only on Ubuntu keyserver - so this patch now
# only adjust terminal output, we will see if connection problems reappear
Patch32: hplip-keyserver.patch
# QMessagebox call was copy-pasted from Qt4 version, but Qt5 has different arguments,
# This patch solves most of them
Patch33: 0026-Call-QMessageBox-constructors-of-PyQT5-with-the-corr.patch
# HP upstream introduced new binary blob, which is not open-source, so it violates
# FPG by two ways - shipping binary blob and non open source code - so it needs to be removed.
# Patch is taken from Debian.
Patch34: 0025-Remove-all-ImageProcessor-functionality-which-is-clo.patch
# In hplip-3.18.10 some parts of UI code was commented out, which leaved hp-toolbox
# unusable (crashed on the start). The patch removes usages of variables, which were
# commented out.
# The patch is taken from Debian.
Patch35: 0027-Fixed-incomplete-removal-of-hp-toolbox-features-whic.patch
# hp-setup crashed when user wanted to define a path to PPD file. It was due
# byte + string variables incompatibility and it is fixed by decoding the 
# bytes-like variable
# part of https://bugzilla.redhat.com/show_bug.cgi?id=1666076
# reported upstream https://bugs.launchpad.net/hplip/+bug/1814272
Patch36: hplip-add-ppd-crash.patch
# external scripts, which are downloaded and run by hp-plugin, try to create links
# in non-existing dirs. These scripts ignore errors, so plugin is installed fine
# but then internal hp-plugin can check for plugin state, where links are checked too.
# It results in corrupted plugin state, which breaks printer installation by GUI hp-setup.
# Temporary workaround is to ignore these bad links and real fix should come from HP,
# because their external scripts try to create links in non-existing dirs.
# Bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=1671513
# Reported upstream: https://bugs.launchpad.net/hplip/+bug/1814574
Patch37: hplip-missing-links.patch
# change in 3.18.9 in scanext.c caused broken scanning for HP LaserJet 3052. Since I cannot figure
# it out what author wanted by the change (it sets option number 9 to true, but different handles
# have different options, so I'm not sure what author wanted to set).
# Remove the change for now, it works for user and me.
Patch38: hplip-hplj-3052.patch
# hpmud parses mdns txt record badly
# upstream tickets: https://bugs.launchpad.net/hplip/+bug/1797501
#                   https://bugs.launchpad.net/hplip/+bug/1817214
#                   https://bugs.launchpad.net/hplip/+bug/1821932
# with no response from upstream
# Patch taken from Debian https://lists.debian.org/debian-printing/2018/11/msg00049.html
Patch39: hplip-hpmud-string-parse.patch
# Part of https://bugzilla.redhat.com/show_bug.cgi?id=1694663
# It was found out that specific device needs plugin for scanning
# Reported upstream as https://bugs.launchpad.net/hplip/+bug/1822762
Patch40: hplip-m278-m281-needs-plugin.patch
# hpcups crashes when a printer needs a plugin and does not have one installed
# it crashes in destructor, because pointer is not initialized
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1695716
# reported upstream 
Patch41: hplip-hpcups-crash.patch
# Fixing the issues found by coverity scan
# reported upstream https://bugs.launchpad.net/hplip/+bug/1808145
Patch42: hplip-covscan.patch
# Segfault during logging to syslog because argument are switched
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1727162
# upstream https://bugs.launchpad.net/hplip/+bug/1837846
Patch43: hplip-logging-segfault.patch
# Traceback in hp-systray when there are no resource
# wanted to report upstream, but launchpad ends with timeout error
# bugzilla https://bugzilla.redhat.com/show_bug.cgi?id=1738321
Patch44: hplip-systray-blockerror.patch
# several printers were removed in 3.19.1, but actually someone still uses them
# reported upstream https://bugs.launchpad.net/hplip/+bug/1843592
# bugzillas 1742949, 1740132, 1739855
Patch45: hplip-missing-drivers.patch
# laserjet 2200 and other devices have different device id than HP expects...
# https://bugzilla.redhat.com/show_bug.cgi?id=1772698
# reported upstream https://bugs.launchpad.net/hplip/+bug/1853002
Patch46: hplip-model-mismatch.patch
# sixext has problems with python3 strings (bz#1573430)
# reported https://bugs.launchpad.net/bugs/1480152
Patch47: hplip-unicodeerror.patch
# error with new gcc, already reported in upstream as
# https://bugs.launchpad.net/hplip/+bug/1836735
Patch48: hplip-fix-Wreturn-type-warning.patch
# upstream check for python clears OS build system
# CFLAGS
# https://bugs.launchpad.net/hplip/+bug/1879445
Patch49: hplip-configure-python.patch
# taken from hplip upstream report - toolbox uses deprecated method
# setMargin(), which generates an exception, resulting in a infinite loop
# of request on cupsd
# https://bugs.launchpad.net/hplip/+bug/1880275
Patch50: hplip-dialog-infinite-loop.patch
# searching algorithm did not expect '-' in model name and thought it is a new PDL
# it resulted in incorrect PPD match, so e.g. hpijs driver was used instead of hpcups
# bug: https://bugzilla.redhat.com/show_bug.cgi?id=1590014
# reported upstream: https://bugs.launchpad.net/hplip/+bug/1881587
Patch51: hplip-find-driver.patch
# hp-clean didn't work for Photosmart C1410 because it was comparing
# string length with buffer size for string object, which is different,
# causing cleaning to fail - the fix is to make the object bytes-like,
# then buffer size is the same as the length.
# Thanks to Stefan Assmann we were able to fix level 1 cleaning
# for the device, but there can be similar issues with other devices
# bug https://bugzilla.redhat.com/show_bug.cgi?id=1833308
# reported upstream https://bugs.launchpad.net/hplip/+bug/1882193
Patch52: hplip-clean-ldl.patch
# 3.20.6 turned off requirement for most devices which needed it
# - it will cause malfunction of printing and scanning for them
# https://bugs.launchpad.net/hplip/+bug/1883898
Patch53: hplip-revert-plugins.patch
# if an user tries to install scanner via hp-setup (printer/fax utility)
# it fails further down - break out earlier with a message
# reported upstream as https://bugs.launchpad.net/hplip/+bug/1916114
Patch54: hplip-hpsetup-noscanjets.patch
# 1963114 - patch for hplip firmware load timeout fix
# reported upstream https://bugs.launchpad.net/hplip/+bug/1922404
Patch55: hplip-hpfirmware-timeout.patch
# 1985251 - Incorrect permission for gpg directory
# reported upstream https://bugs.launchpad.net/hplip/+bug/1938442
Patch56: hplip-gpgdir-perms.patch
# 1987141 - hp-plugin installs malformed udev files
# reported upstream https://bugs.launchpad.net/hplip/+bug/1847477
Patch57: hplip-plugin-udevissues.patch
# 2080235 - Misleading errors about missing shared libraries when scanning
# downstream patch to prevent errors:
# - when loading libhpmud.so - unversioned .so files belong into devel packages,
#   but dlopen() in hplip was set to load the unversioned .so - so to remove rpmlint
#   error (when libhpmud.so is in non-devel package) and prevent runtime dependency on -devel
#   package (if libhpmud.so had been moved to -devel) the dlopen on unversioned .so file was
#   removed
# - /lib64/libm.so is not symlink but ld script, which cannot be used in dlopen()
Patch58: hplip-no-libhpmud-libm-warnings.patch
Patch59: hplip-plugin-script.patch
# C99 compatibility fixes by fweimer - use explicit int
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch60: hplip-pserror-c99.patch
# C99 compatibility patch by fweimer - several undefined functions in hpaio
# backend are declared in orblite.h
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch61: hplip-scan-hpaio-include.patch
# C99 compatibility patch by fweimer - undefined _DBG() and dynamic linking funcs in orblite.c
# - _DBG() looks like typo and new header is added for funcs
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch62: hplip-scan-orblite-c99.patch
# C99 compatibility patch by fweimer:
# PyString_AsStringAndSize is removed in Python3, remove its compilation for now
# in case there is a request for compiling it again, there is a possible solution
# for the function py3 alternative https://opendev.org/openstack/pyeclib/commit/19c8313986
# - disabling removes hp-unload and /usr/share/hplip/pcard as well
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch63: hplip-pcardext-disable.patch
# undefined strcasestr() in sclpml.c - build with _GNU_SOURCE
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
Patch64: hplip-sclpml-strcasestr.patch
# 2192131 - parseQueues() doesn't get device uri from 'lpstat -v', because parsing pattern changed
# https://bugs.launchpad.net/hplip/+bug/2027972
Patch65: hplip-fix-parsing-lpstat.patch
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
# Remove this once internal openstack handles IPv6 better - test by pinging IPv6 in OpenStack,
# it should not hang.
Patch66: hplip-plugin-curl.patch
# fix SyntaxWarning from python3.12
# https://bugs.launchpad.net/hplip/+bug/2029480
Patch67: hplip-use-raw-strings.patch
# FTBFS GCC 14
# https://bugs.launchpad.net/hplip/+bug/2048780
Patch68: hplip-hpaio-gcc14.patch
# format is no longer method in locale module
# https://bugs.launchpad.net/hplip/+bug/2045507
Patch69: hplip-locale-format.patch
# function prototype did not specify argument's data types
# https://bugs.launchpad.net/hplip/+bug/2096650
Patch70: hplip-gcc15-stdc23.patch
# status history table shows unformatted QDateTime values
# https://bugs.launchpad.net/hplip/+bug/1956547
Patch71: hplip-format-qdatetime.patch
# Python 3.14 removed urlopener
# https://bugs.launchpad.net/hplip/+bug/2115046
Patch72: hplip-no-urlopener.patch
# hp-scan command failed to run and gives an error (fedora#2395809)
# https://bugs.launchpad.net/hplip/+bug/2124268
Patch73: hplip-scan-size.patch
# 3.25.8 brings new implementation for calling commands in subprocess,
# but again directs I/O into pipes, which does not work for TUI plugin
# installation. Additionally it tracebacks if stdout/stderr is None
# https://bugs.launchpad.net/hplip/+bug/2110101
Patch74: hplip-plugin-stdout.patch

%if 0%{?fedora} || 0%{?rhel} <= 8 || 0%{?oreon}
# mention hplip-gui if you want to have GUI
Patch1000: hplip-fedora-gui.patch
%endif


# uses automatic creation of configure
BuildRequires: autoconf
# uses automatic creation of Makefile
BuildRequires: automake
# Make sure we get postscriptdriver tags - need cups and python3-cups.
BuildRequires: cups
# uses functions from CUPS in filters, backends and libraries defining them
BuildRequires: cups-devel
%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
# needed for desktop file validation in spec file
BuildRequires: desktop-file-utils
%endif
# gcc and gcc-c++ are no longer in buildroot by default
# gcc is needed for compilation of HPAIO scanning backend, HP implementation of
# IPP and MDNS protocols, hpps driver, hp backend, hpip (image processing
# library), multipoint transport driver hpmud
BuildRequires: gcc
# gcc-c++ is needed for hpijs, hpcups drivers
BuildRequires: gcc-c++
# support for JPEG file formats in hp-scan
BuildRequires: libjpeg-devel
# uses libtool for autorconf
BuildRequires: libtool
# implements support for USB devices
BuildRequires: libusb1-devel
# uses make
BuildRequires: make
# SLP device discovery is based on SNMP
BuildRequires: net-snmp-devel
# wasn't able to find out why, but SO libraries in hplip-libs require them...
BuildRequires: openssl-devel
# supports mDNS device discovery via Avahi
BuildRequires: pkgconfig(avahi-client)
BuildRequires: pkgconfig(avahi-core)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: python3-cups
# implements C Python extensions like hpmudext, cupsext, scanext
BuildRequires: python3-devel
# distutils are removed in Python3.12, use setuptools
BuildRequires: python3-setuptools
# SANE backend hpaio uses function from SANE API
BuildRequires: sane-backends-devel
# macros: %%{_tmpfilesdir}, %%{_udevrulesdir}
BuildRequires: systemd

%if 0%{?fedora} || 0%{?rhel} <= 8 || 0%{?oreon}
Suggests: hplip-gui
%endif
# uses avahi-browse for discovering IPP-over-USB printers
Recommends: avahi-tools
# 1733449 - Scanner on an HP AIO printer is not detected unless libsane-hpaio is installed
Recommends: libsane-hpaio%{?_isa} = %{version}-%{release}
# downloaded plugin requires python3-gobject to work even via CLI...
# but make it weak dependency, so users which don't need the plugin and have servers
# can remove the python3-gobject which is used by desktop apps
Recommends: python3-gobject

Requires: cups
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
Requires: curl
# set require directly to /usr/bin/gpg, because gnupg2 and gnupg ships it,
# but gnupg will be deprecated in the future
Requires: %{_bindir}/gpg
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python3-dbus
%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
Requires: python3-pillow
%endif
# user+group lp
Requires: setup
# /usr/lib/udev/rules.d
Requires: systemd
# 1788643 - Fedora minimal does not ship tar by default
Requires: tar
# require usbutils, hp-diagnose_queues needs lsusb
Requires: usbutils

# require coreutils, because timeout binary is needed in post scriptlet,
# because hpcups-update-ppds script can freeze in certain situation and
# stop the update
Requires(post): coreutils

%description
The Hewlett-Packard Linux Imaging and Printing Project provides
drivers for HP printers and multi-function peripherals.

%package common
Summary: Files needed by the HPLIP printer and scanner drivers

%description common
Files needed by the HPLIP printer and scanner drivers.

%package libs
Summary: HPLIP libraries
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: python3

%description libs
Libraries needed by HPLIP.

%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
%package gui
Summary: HPLIP graphical tools
BuildRequires: libappstream-glib

# for avahi-browse - looks for devices on local network
Recommends: avahi-tools
Recommends: libsane-hpaio%{?_isa} = %{version}-%{release}
# for hp-check
Recommends: pkgconf

Requires: %{name}%{?_isa} = %{version}-%{release}
# hpssd.py
Requires: python3-gobject
Requires: python3-reportlab
Requires: python3-qt5

%description gui
HPLIP graphical tools.
%endif

%package -n libsane-hpaio
Summary: SANE driver for scanners in HP's multi-function devices

Requires: sane-backends
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n libsane-hpaio
SANE driver for scanners in HP's multi-function devices (from HPOJ).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

# The pstotiff filter is rubbish so replace it (launchpad #528394).
%patch -P 1 -p1 -b .pstotiff-is-rubbish

# Fix compilation.
%patch -P 2 -p1 -b .strstr-const

# Make utils.checkPyQtImport() look for the gui sub-package (bug #243273).
%patch -P 3 -p1 -b .ui-optional

# Make sure to avoid handwritten asm.
%patch -P 4 -p1 -b .no-asm

# Corrected several IEEE 1284 Device IDs using foomatic data.
# Color LaserJet 2500 series (bug #659040)
# LaserJet 4100 Series/2100 Series (bug #659039)
%patch -P 5 -p1 -b .deviceIDs-drv
chmod +x %{SOURCE2}
mv prnt/drv/hpijs.drv.in{,.deviceIDs-drv-hpijs}
%{SOURCE2} prnt/drv/hpcups.drv.in \
           prnt/drv/hpijs.drv.in.deviceIDs-drv-hpijs \
           > prnt/drv/hpijs.drv.in

# Move udev rules from /etc/ to /usr/lib/ (bug #748208).
%patch -P 6 -p1 -b .udev-rules

# Retry when connecting to device fails (bug #532112).
%patch -P 7 -p1 -b .retry-open

# Mark SNMP quirks in PPD for HP OfficeJet Pro 8500 (bug #581825).
%patch -P 8 -p1 -b .snmp-quirks

# Fixed bogus low ink warnings from hpijs driver (bug #643643).
%patch -P 9 -p1 -b .hpijs-marker-supply

# Clear old printer-state-reasons we used to manage (bug #510926).
%patch -P 10 -p1 -b .clear-old-state-reasons

# Avoid busy loop in hpcups when backend has exited (bug #525944).
%patch -P 11 -p1 -b .hpcups-sigpipe

# CUPS filters should use TMPDIR when available (bug #865603).
%patch -P 12 -p1 -b .logdir

# Fixed Device ID parsing code in hpijs's dj9xxvip.c (bug #510926).
%patch -P 13 -p1 -b .bad-low-ink-warning

# Add Device ID for
# HP LaserJet Color M451dn (bug #1159380)
for ppd_file in $(grep '^diff' %{PATCH14} | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done
%patch -P 14 -p1 -b .deviceIDs-ppd
for ppd_file in $(grep '^diff' %{PATCH14} | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done

# Fix ImageableArea for Laserjet 8150/9000 (bug #596298).
for ppd_file in $(grep '^diff' %{PATCH15} | cut -d " " -f 4);
do
  gunzip ${ppd_file#*/}.gz
done
%patch -P 15 -p1 -b .ImageableArea
for ppd_file in $(grep '^diff' %{PATCH15} | cut -d " " -f 4);
do
  gzip -n ${ppd_file#*/}
done

# Scan to /var/tmp instead of /tmp (bug #1076954).
%patch -P 16 -p1 -b .scan-tmp

# Treat logging before importing of logger module (bug #984699).
%patch -P 17 -p1 -b .log-stderr

# Fix parsing of avahi-daemon output (bug #1096939).
%patch -P 18 -p1 -b .parsing

# Fixed left/right margins for HP DeskJet 990C (LP #1405212).
%patch -P 19 -p1 -b .dj990c-margin

# Fixed uses of strncpy throughout.
%patch -P 20 -p1 -b .strncpy

# Don't try to write bytecode cache for hpfax backend (bug #1192761)
# or hp-config_usb_printer (bug #1266903)
# or hpps filter (bug #1241548).
%patch -P 21 -p1 -b .no-write-bytecode

# Ignore IOError when logging output (bug #712537).
%patch -P 22 -p1 -b .silence-ioerror

# [abrt] hplip: hp-scan:663:<module>:NameError: name 'source_option' is not defined (bug #1341304)
%patch -P 23 -p1 -b .sourceoption

# hplip license problem (bug #1364711)
%patch -P 24 -p1 -b .no-ernie

# hplip appdata
%patch -P 25 -p1 -b .appdata

# hp-check shows 'CUPS incompatible or not running' even if CUPS is running (bug #1456467)
%patch -P 26 -p1 -b .check-cups

# hp-firmware:NameError: name 'INTERACTIVE_MODE4' is not defined (bug #1533869)
%patch -P 27 -p1 -b .typo

%patch -P 28 -p1 -b .use-binary-str

# TypeError: 'Error' object does not support indexing (bug #1564770)
# upstream bug: https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/1718129
# in python2 it was possible to acces Exception message by index [0].
# in python3 this is no longer possible and it causes TypeError.
%patch -P 29 -p1 -b .error-print-fix

# TypeError: not all arguments converted during string formatting (bug #1566938)
# upstream bug: https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/616450
# bug caused by more arguments than argument specifiers in formatted string
%patch -P 30 -p1 -b .hpfax-import-error-print

# 'WifiSetupDialog' object has no attribute 'wifiobj' (bug #1626877)
# upstream bug: https://bugs.launchpad.net/hplip/+bug/1752060
# bug caused by typo in wifisetupdialog wifiObj property call
%patch -P 31 -p1 -b .wifisetup-bad-call-fix

# have pool of keyservers to choose
%patch -P 32 -p1 -b .keyserver

# TypeError: argument 5 has unexpected type 'StandardButtons' (bug #1594602)
# upstream bug: https://bugs.launchpad.net/ubuntu/+source/hplip/+bug/1745383
# bug caused by typo in QMessageBox constructor call
# this patch fixes more of those typos - some fixed by tkorbar, some taken from ubuntu fix
%patch -P 33 -p1 -b .qmsgbox-typos-fix

# removal of non open source code, taken from ubuntu
%patch -P 34 -p1 -b .libimageprocessor-removal

%{_bindir}/rm prnt/hpcups/libImageProcessor-x86*

%patch -P 35 -p1 -b .toolbox-crash
# part of https://bugzilla.redhat.com/show_bug.cgi?id=1666076
%patch -P 36 -p1 -b .add-ppd-crash
# 1671513 - after 'successful' plugin installation it is not installed
%patch -P 37 -p1 -b .missing-links
# 1684434 - Scanning broken for HP LaserJet 3052
%patch -P 38 -p1 -b .hp-laserjet-3052-broken-scanning
# 1694663 - Cannot scan with M281fdw LaserJet - failed: Error during device I/O (part 1)
%patch -P 39 -p1 -b .hpmud-string-parse
# 1694663 - Cannot scan with M281fdw LaserJet - failed: Error during device I/O (part 2)
%patch -P 40 -p1 -b .m278-m281-needs-plugin
# 1695716 - hpcups crashes in Compressor destructor
%patch -P 41 -p1 -b .hpcups-crash
# fixing issues found by coverity scan
%patch -P 42 -p1 -b .covscan
# segfault during logging (1727162)
%patch -P 43 -p1 -b .logging-segfault
# 1738321 - [abrt] hp-systray:BlockingIOError: [Errno 11] Resource temporarily unavailable
%patch -P 44 -p1 -b .systray-blockerror
# 1742949, 1740132, 1739855 - missing drivers
%patch -P 45 -p1 -b .missing-drivers
# 1772698 - Can't setup printer (HP LJ 2200): no attributes found in model.dat
%patch -P 46 -p1 -b .model-mismatch
# 1573430 - sixext.py:to_string_utf8:UnicodeDecodeError: 'utf-8' codec can't decode bytes
%patch -P 47 -p1 -b .unicodeerror
%patch -P 48 -p1 -b .Wreturn-fix
%patch -P 49 -p1 -b .configure-python
%patch -P 50 -p1 -b .dialog-infinite-loop
# 1590014 - hplip PPD search doesn't expect '-' in device name
%patch -P 51 -p1 -b .find-driver
# 1833308 - hp-clean cannot clean HP PSC1410 - Device I/O error
%patch -P 52 -p1 -b .clean-ldl
%patch -P 53 -p1 -b .revert-plugins
# if an user tries to install scanner via hp-setup (printer/fax utility)
# it fails further down - break out earlier with a message
%patch -P 54 -p1 -b .hpsetup-noscanjets
# 1963114 - patch for hplip firmware load timeout fix
%patch -P 55 -p1 -b .hpfirmware-timeout
# 1985251 - Incorrect permission for gpg directory
%patch -P 56 -p1 -b .gpgdir-perms
# 1987141 - hp-plugin installs malformed udev files
%patch -P 57 -p1 -b .hpplugin-udevperms
# 2080235 - Misleading errors about missing shared libraries when scanning
%patch -P 58 -p1 -b .no-libm-libhpmud-warn
%patch -P 59 -p1 -b .plugin-patch
# C99 compatibility fixes by fweimer - use explicit int
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
%patch -P 60 -p1 -b .pserror-int
# C99 compatibility patch by fweimer - several undefined functions in hpaio
# backend are declared in orblite.h
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
%patch -P 61 -p1 -b .hpaio-orblite-defs
# C99 compatibility patch by fweimer - undefined _DBG() and dynamic linking funcs in orblite.c
# - _DBG() looks like typo and new header is added for funcs
# Submitted upstream: <https://bugs.launchpad.net/hplip/+bug/1997875>
%patch -P 62 -p1 -b .orblite-undefs
# C99 compatibility patch by fweimer - python2 PyString_AsStringAndSize in python3 code
# gives undefined reference - removed for now with dependent hp-unload
%patch -P 63 -p1 -b .pcardext-disable
# C99 compatibility patch by fweimer - undefined strcasestr() in sclpml.c - build with _GNU_SOURCE
%patch -P 64 -p1 -b .sclpml-strcasestr
# 2192131 - parseQueues() doesn't get device uri from 'lpstat -v', because parsing pattern changed
# https://bugs.launchpad.net/hplip/+bug/2027972
%patch -P 65 -p1 -b .lpstat-parse
# switch to curl by downstream patch from wget to workaround openstack dropping IPv6
# which causes great delays...
%patch -P 66 -p1 -b .curl-switch
# fix warnings
# upstream https://bugs.launchpad.net/hplip/+bug/2029480
%patch -P 67 -p1 -b .raw-strings
# FTBFS GCC 14
# https://bugs.launchpad.net/hplip/+bug/2048780
%patch -P 68 -p1 -b .hpaio-gcc14
# format is no longer method in locale module
# https://bugs.launchpad.net/hplip/+bug/2045507
%patch -P 69 -p1 -b .locale-format
# https://bugs.launchpad.net/hplip/+bug/2096650
%patch -P 70 -p1 -b .gcc-strc23
# https://bugs.launchpad.net/hplip/+bug/1956547
%patch -P 71 -p1 -b .format-qdatetime
# https://bugs.launchpad.net/hplip/+bug/2115046
%patch -P 72 -p1 -b .no-urlopener
# https://bugs.launchpad.net/hplip/+bug/2124268
%patch -P 73 -p1 -b .scan-size
# https://bugs.launchpad.net/hplip/+bug/2110101
%patch -P 74 -p1 -b .plugin-stdout

# Fedora specific patches now, don't put a generic patches under it
%if 0%{?fedora} || 0%{?rhel} <= 8 || 0%{?oreon}
# mention hplip-gui should be installed if you want GUI
%patch -P 1000 -p1 -b .fedora-gui
%endif


sed -i.duplex-constraints \
    -e 's,\(UIConstraints.* \*Duplex\),//\1,' \
    prnt/drv/hpcups.drv.in

# Change shebang /usr/bin/env python -> /usr/bin/python3 (bug #618351).
find -name '*.py' -print0 | xargs -0 \
    sed -i.env-python -e 's,^#!/usr/bin/env python,#!%{__python3},'
sed -i.env-python -e 's,^#!/usr/bin/env python,#!%{__python3},' \
    prnt/filters/hpps \
    fax/filters/pstotiff

cp -p %{SOURCE4} %{SOURCE5} ppd/hpcups

# 2129849 - move hp-plugin script into srcdir
cp -p %{SOURCE7} .


%build
# Work-around Makefile.am imperfections.
sed -i 's|^AM_INIT_AUTOMAKE|AM_INIT_AUTOMAKE([foreign])|g' configure.in
# Upstream uses old libtool, which causes problems (due to libhpmud requiring
# libhpdiscovery) when we try to remove rpath from it.
# Regenerating all autotools files works-around these rpath issues.
autoreconf --verbose --force --install

%configure \
        --enable-fax-build \
        --enable-foomatic-drv-install \
        --enable-gui-build \
        --enable-hpcups-install \
        --enable-hpijs-install \
        --enable-pp-build \
        --enable-qt5 \
        --enable-scan-build \
        --disable-foomatic-rip-hplip-install \
        --disable-imageProcessor-build \
        --disable-policykit \
        --disable-qt4 \
        --with-mimedir=%{_datadir}/cups/mime PYTHON=%{__python3}

%make_build


%install
mkdir -p %{buildroot}%{_bindir}
%make_install PYTHON=%{__python3}

# Create /run/hplip & /var/lib/hp
mkdir -p %{buildroot}/run/hplip
mkdir -p %{buildroot}%{_sharedstatedir}/hp

# install /usr/lib/tmpfiles.d/hplip.conf (bug #1015831)
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/hplip.conf <<EOF
# See tmpfiles.d(5) for details

d /run/hplip 0775 root lp -
EOF


# Remove unpackaged files
rm -rf  %{buildroot}%{_sysconfdir}/sane.d \
        %{buildroot}%{_docdir} \
        %{buildroot}%{_datadir}/hal/fdi \
        %{buildroot}%{_datadir}/hplip/pkservice.py \
        %{buildroot}%{_bindir}/hp-pkservice

rm -rf  %{buildroot}%{_datadir}/hplip/locatedriver* \
        %{buildroot}%{_datadir}/hplip/dat2drv*

rm -f   %{buildroot}%{_bindir}/hp-logcapture \
        %{buildroot}%{_bindir}/hp-doctor \
        %{buildroot}%{_bindir}/hp-pqdiag \
        %{buildroot}%{_datadir}/hplip/logcapture.py \
        %{buildroot}%{_datadir}/hplip/doctor.py \
        %{buildroot}%{_datadir}/hplip/pqdiag.py

rm -f   %{buildroot}%{_bindir}/foomatic-rip \
        %{buildroot}%{_libdir}/cups/filter/foomatic-rip \
        %{buildroot}%{_libdir}/*.la \
        %{buildroot}%{python3_sitearch}/*.la \
        %{buildroot}%{_libdir}/libhpip.so \
        %{buildroot}%{_libdir}/libhpmud.so \
        %{buildroot}%{_libdir}/libhpipp.so \
        %{buildroot}%{_libdir}/libhpdiscovery.so \
        %{buildroot}%{_libdir}/sane/*.la \
        %{buildroot}%{_datadir}/cups/model/foomatic-ppds \
        %{buildroot}%{_datadir}/applications/hplip.desktop \
        %{buildroot}%{_datadir}/ppd/HP/*.ppd

rm -f %{buildroot}%{_datadir}/hplip/hpaio.desc

rm -rf %{buildroot}%{_datadir}/hplip/install.* \
       %{buildroot}%{_datadir}/hplip/uninstall.* \
       %{buildroot}%{_bindir}/hp-uninstall \
       %{buildroot}%{_datadir}/hplip/upgrade.* \
       %{buildroot}%{_bindir}/hp-upgrade \
       %{buildroot}%{_datadir}/hplip/hplip-install

rm -f %{buildroot}%{_datadir}/hplip/hpijs.drv.in.template

rm -f %{buildroot}%{_datadir}/cups/mime/pstotiff.types \
      %{buildroot}%{_datadir}/hplip/fax/pstotiff*

rm -f %{buildroot}%{_datadir}/hplip/hplip-install

rm -f %{buildroot}%{_unitdir}/hplip-printer@.service

rm -f %{buildroot}%{_datadir}/ipp-usb/quirks/HPLIP.conf

rm -rf %{buildroot}%{_bindir}/hp-unload \
       %{buildroot}%{_datadir}/%{name}/pcard

# The systray applet doesn't work properly (displays icon as a
# window), so don't ship the launcher yet.
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop

%if 0%{?rhel} > 8 || 0%{?oreon}
rm -rf %{buildroot}%{_bindir}/hp-check \
       %{buildroot}%{_bindir}/hp-devicesettings \
       %{buildroot}%{_bindir}/hp-diagnose_plugin \
       %{buildroot}%{_bindir}/hp-faxsetup \
       %{buildroot}%{_bindir}/hp-linefeedcal \
       %{buildroot}%{_bindir}/hp-makecopies \
       %{buildroot}%{_bindir}/hp-print \
       %{buildroot}%{_bindir}/hp-printsettings \
       %{buildroot}%{_bindir}/hp-systray \
       %{buildroot}%{_bindir}/hp-scan \
       %{buildroot}%{_bindir}/hp-toolbox \
       %{buildroot}%{_bindir}/hp-uiscan \
       %{buildroot}%{_bindir}/hp-wificonfig \
       %{buildroot}%{_datadir}/applications/*.desktop \
       %{buildroot}%{_datadir}/metainfo/hplip.appdata.xml \
       %{buildroot}%{_datadir}/icons/hicolor/*/apps/* \
       %{buildroot}%{_datadir}/hplip/base/imageprocessing.py* \
       %{buildroot}%{_datadir}/hplip/check.py* \
       %{buildroot}%{_datadir}/hplip/devicesettings.py* \
       %{buildroot}%{_datadir}/hplip/diagnose_plugin.py* \
       %{buildroot}%{_datadir}/hplip/faxsetup.py* \
       %{buildroot}%{_datadir}/hplip/linefeedcal.py* \
       %{buildroot}%{_datadir}/hplip/makecopies.py* \
       %{buildroot}%{_datadir}/hplip/print.py* \
       %{buildroot}%{_datadir}/hplip/printsettings.py* \
       %{buildroot}%{_datadir}/hplip/systray.py* \
       %{buildroot}%{_datadir}/hplip/scan.py* \
       %{buildroot}%{_datadir}/hplip/toolbox.py* \
       %{buildroot}%{_datadir}/hplip/uiscan.py* \
       %{buildroot}%{_datadir}/hplip/wificonfig.py* \
       %{buildroot}%{_datadir}/hplip/data/images \
       %{buildroot}%{_datadir}/hplip/scan \
       %{buildroot}%{_datadir}/hplip/ui5 \
       %{buildroot}%{_docdir}/hplip/hpscan.html \
       doc/hpscan.html
%endif

install -p -m755 hp-plugin %{buildroot}%{_bindir}/hp-plugin-download

%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
mkdir -p %{buildroot}%{_datadir}/metainfo
cp %{SOURCE3} %{buildroot}%{_datadir}/metainfo/

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{16x16,32x32,64x64}/apps
install -p -m644 %{buildroot}%{_datadir}/hplip/data/images/16x16/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/hp_logo.png
install -p -m644 %{buildroot}%{_datadir}/hplip/data/images/32x32/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/hp_logo.png
install -p -m644 %{buildroot}%{_datadir}/hplip/data/images/64x64/hp_logo.png \
   %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/hp_logo.png

mkdir -p %{buildroot}%{_datadir}/applications
sed -i -e '/^Categories=/d' hplip.desktop
# Encoding key is deprecated
sed -i -e '/^Encoding=/d' hplip.desktop
desktop-file-validate hplip.desktop

desktop-file-install                               \
        --dir %{buildroot}/%{_datadir}/applications              \
        --add-category System \
        --add-category Settings \
        --add-category HardwareSettings                        \
        hplip.desktop

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

# install hp-uiscan desktop file
sed -i 's/\/usr\/share\/icons\/Humanity\/devices\/48\/printer\.svg/hp_logo/' hp-uiscan.desktop

desktop-file-validate hp-uiscan.desktop

desktop-file-install \
          --dir %{buildroot}/%{_datadir}/applications \
          --add-category Graphics \
          --add-category Scanning \
          --add-category Application \
          hp-uiscan.desktop
%endif

# Regenerate hpcups PPDs on upgrade if necessary (bug #579355).
install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/hpcups-update-ppds

%{__mkdir_p} %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio

# Images in docdir should not be executable (bug #440552).
find doc/images -type f -exec chmod 644 {} \;

# Create an empty plugins directory to make sure it gets the right
# SELinux file context (bug #564551).
%{__mkdir_p} %{buildroot}%{_datadir}/hplip/prnt/plugins

%post
# timeout is to prevent possible freeze during update
%{_bindir}/timeout 10m -k 15m %{_bindir}/hpcups-update-ppds &>/dev/null ||:

%ldconfig_scriptlets libs


%files
%doc COPYING doc/*
# ex-hpijs
%{_bindir}/hpijs
# ex-hpijs
%{_bindir}/hpcups-update-ppds
%{_bindir}/hp-align
%{_bindir}/hp-clean
%{_bindir}/hp-colorcal
%{_bindir}/hp-config_usb_printer
%{_bindir}/hp-diagnose_queues
%{_bindir}/hp-fab
%{_bindir}/hp-firmware
%{_bindir}/hp-info
%{_bindir}/hp-levels
%{_bindir}/hp-makeuri
%{_bindir}/hp-plugin
%{_bindir}/hp-plugin-download
%{_bindir}/hp-probe
%{_bindir}/hp-query
%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
%{_bindir}/hp-scan
%endif
%{_bindir}/hp-sendfax
%{_bindir}/hp-setup
%{_bindir}/hp-testpage
%{_bindir}/hp-timedate
%{_cups_serverbin}/backend/hp
%{_cups_serverbin}/backend/hpfax
# ex-hpijs
%{_cups_serverbin}/filter/hpcdmfax
%{_cups_serverbin}/filter/hpcups
%{_cups_serverbin}/filter/hpcupsfax
%{_cups_serverbin}/filter/hpps
%{_cups_serverbin}/filter/pstotiff
# ex-hpijs
%{_datadir}/cups/drv/*
%{_datadir}/cups/mime/pstotiff.convs
# Files
%{_datadir}/hplip/align.py*
%{_datadir}/hplip/check-plugin.py*
%{_datadir}/hplip/clean.py*
%{_datadir}/hplip/colorcal.py*
%{_datadir}/hplip/config_usb_printer.py*
%{_datadir}/hplip/diagnose_queues.py*
%{_datadir}/hplip/fab.py*
%{_datadir}/hplip/fax
%{_datadir}/hplip/firmware.py*
%{_datadir}/hplip/hpdio.py*
%{_datadir}/hplip/hplip_clean.sh
%{_datadir}/hplip/hpssd*
%{_datadir}/hplip/info.py*
%{_datadir}/hplip/__init__.py*
%{_datadir}/hplip/levels.py*
%{_datadir}/hplip/makeuri.py*
%{_datadir}/hplip/plugin.py*
%{_datadir}/hplip/probe.py*
%{_datadir}/hplip/query.py*
%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
%{_datadir}/hplip/scan.py*
%endif
%{_datadir}/hplip/sendfax.py*
%{_datadir}/hplip/setup.py*
%{_datadir}/hplip/testpage.py*
%{_datadir}/hplip/timedate.py*
%{_datadir}/hplip/unload.py*
# Directories
%{_datadir}/hplip/base
%{_datadir}/hplip/copier
%{_datadir}/hplip/data/ldl
%{_datadir}/hplip/data/localization
%{_datadir}/hplip/data/pcl
%{_datadir}/hplip/data/ps
%{_datadir}/hplip/installer
%{_datadir}/hplip/prnt
%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
%{_datadir}/hplip/scan
%endif
%{_datadir}/ppd
%{_sharedstatedir}/hp
%dir %attr(0775,root,lp) /run/hplip
%{_tmpfilesdir}/hplip.conf
%{_udevrulesdir}/56-hpmud.rules

%files common
%license COPYING
%dir %{_sysconfdir}/hp
%config(noreplace) %{_sysconfdir}/hp/hplip.conf
%dir %{_datadir}/hplip
%dir %{_datadir}/hplip/data
%{_datadir}/hplip/data/models

%files libs
%{_libdir}/libhpip.so.0
%{_libdir}/libhpip.so.0.0.1
%{_libdir}/libhpipp.so.0
%{_libdir}/libhpipp.so.0.0.1
%{_libdir}/libhpdiscovery.so.0
%{_libdir}/libhpdiscovery.so.0.0.1
%{_libdir}/libhpmud.so.0
%{_libdir}/libhpmud.so.0.0.6
# Python extension
%{python3_sitearch}/*

%if 0%{?rhel} <= 8 || 0%{?fedora} || 0%{?oreon}
%files gui
%{_bindir}/hp-check
%{_bindir}/hp-devicesettings
%{_bindir}/hp-diagnose_plugin
%{_bindir}/hp-faxsetup
%{_bindir}/hp-linefeedcal
%{_bindir}/hp-makecopies
%{_bindir}/hp-print
%{_bindir}/hp-printsettings
%{_bindir}/hp-systray
%{_bindir}/hp-toolbox
%{_bindir}/hp-uiscan
%{_bindir}/hp-wificonfig
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/hplip.appdata.xml
# Files
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/hplip/check.py*
%{_datadir}/hplip/devicesettings.py*
%{_datadir}/hplip/diagnose_plugin.py*
%{_datadir}/hplip/faxsetup.py*
%{_datadir}/hplip/linefeedcal.py*
%{_datadir}/hplip/makecopies.py*
%{_datadir}/hplip/print.py*
%{_datadir}/hplip/printsettings.py*
%{_datadir}/hplip/systray.py*
%{_datadir}/hplip/toolbox.py*
%{_datadir}/hplip/uiscan.py*
%{_datadir}/hplip/wificonfig.py*
# Directories
%{_datadir}/hplip/data/images
%{_datadir}/hplip/ui5
%endif

%files -n libsane-hpaio
%{_libdir}/sane/libsane-*.so
%{_libdir}/sane/libsane-*.so.1
%{_libdir}/sane/libsane-*.so.1.0.0
%config(noreplace) %{_sysconfdir}/sane.d/dll.d/hpaio

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.25.8-2
- Import
