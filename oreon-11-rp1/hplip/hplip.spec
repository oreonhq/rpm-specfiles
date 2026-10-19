%global source0_hash b9c61252754f35b4a237396ca8961e7b3e0c56db76d66a6712b7bf3e30e69463
%{?filter_setup:
%filter_provides_in %{python3_sitearch}/.*\.so$
%filter_setup
}
Summary:        HP Linux Imaging and Printing Project
Name: hplip
Version: 3.26.4
Release:        1%{?dist}
License: GPL-2.0-or-later AND MIT AND BSD-3-Clause-HP AND IJG AND GPL-2.0-only AND LGPL-2.1-or-later AND BSD-2-Clause AND LicenseRef-Public-Domain AND python-ldap
Url: https://developers.hp.com/hp-linux-imaging-and-printing
Source0:        https://downloads.sourceforge.net/project/hplip/hplip/%{version}/hplip-%{version}.tar.gz
Source1:        hpcups-update-ppds.sh
Source2:        copy-deviceids.py
Source3: %{name}.appdata.xml
Source4:        hp-laserjet_cp_1025nw.ppd.gz
Source5:        hp-laserjet_professional_p_1102w.ppd.gz
Source6:        hplip-repack.sh
Source7:        hp-plugin.in
Patch1:        hplip-pstotiff-is-rubbish.patch
Patch2:        hplip-strstr-const.patch
Patch3:        hplip-ui-optional.patch
Patch4:        hplip-no-asm.patch
Patch5:        hplip-deviceIDs-drv.patch
Patch6:        hplip-udev-rules.patch
Patch7:        hplip-retry-open.patch
Patch8:        hplip-snmp-quirks.patch
Patch9:        hplip-hpijs-marker-supply.patch
Patch10:        hplip-clear-old-state-reasons.patch
Patch11:        hplip-hpcups-sigpipe.patch
Patch12:        hplip-logdir.patch
Patch13:        hplip-bad-low-ink-warning.patch
Patch14:        hplip-deviceIDs-ppd.patch
Patch15:        hplip-ppd-ImageableArea.patch
Patch16:        hplip-scan-tmp.patch
Patch17:        hplip-log-stderr.patch
Patch18:        hplip-avahi-parsing.patch
Patch19:        hplip-dj990c-margin.patch
Patch20:        hplip-strncpy.patch
Patch21:        hplip-no-write-bytecode.patch
Patch22:        hplip-silence-ioerror.patch
Patch23:        hplip-sourceoption.patch
Patch24:        hplip-noernie.patch
Patch25:        hplip-appdata.patch
Patch26:        hplip-check-cups.patch
Patch27:        hplip-typo.patch
Patch28:        hplip-use-binary-str.patch
Patch29:        hplip-error-print.patch
Patch30:        hplip-hpfax-importerror-print.patch
Patch31:        hplip-wifisetup.patch
Patch32:        hplip-keyserver.patch
Patch33:        0026-Call-QMessageBox-constructors-of-PyQT5-with-the-corr.patch
Patch34:        0025-Remove-all-ImageProcessor-functionality-which-is-clo.patch
Patch35:        0027-Fixed-incomplete-removal-of-hp-toolbox-features-whic.patch
Patch36:        hplip-add-ppd-crash.patch
Patch37:        hplip-missing-links.patch
Patch38:        hplip-hplj-3052.patch
Patch39:        hplip-hpmud-string-parse.patch
Patch40:        hplip-m278-m281-needs-plugin.patch
Patch41:        hplip-hpcups-crash.patch
Patch42:        hplip-covscan.patch
Patch43:        hplip-logging-segfault.patch
Patch44:        hplip-systray-blockerror.patch
Patch45:        hplip-missing-drivers.patch
Patch46:        hplip-model-mismatch.patch
Patch47:        hplip-unicodeerror.patch
Patch48:        hplip-fix-Wreturn-type-warning.patch
Patch49:        hplip-configure-python.patch
Patch50:        hplip-dialog-infinite-loop.patch
Patch51:        hplip-find-driver.patch
Patch52:        hplip-clean-ldl.patch
Patch53:        hplip-revert-plugins.patch
Patch54:        hplip-hpsetup-noscanjets.patch
Patch55:        hplip-hpfirmware-timeout.patch
Patch56:        hplip-gpgdir-perms.patch
Patch57:        hplip-plugin-udevissues.patch
Patch58:        hplip-no-libhpmud-libm-warnings.patch
Patch59:        hplip-plugin-script.patch
Patch60:        hplip-pserror-c99.patch
Patch61:        hplip-scan-hpaio-include.patch
Patch62:        hplip-scan-orblite-c99.patch
Patch63:        hplip-pcardext-disable.patch
Patch64:        hplip-sclpml-strcasestr.patch
Patch65:        hplip-fix-parsing-lpstat.patch
Patch66:        hplip-plugin-curl.patch
Patch67:        hplip-use-raw-strings.patch
Patch68:        hplip-hpaio-gcc14.patch
Patch69:        hplip-locale-format.patch
Patch70:        hplip-gcc15-stdc23.patch
Patch71:        hplip-format-qdatetime.patch
Patch72:        hplip-no-urlopener.patch
Patch73:        hplip-scan-size.patch
Patch74:        hplip-plugin-stdout.patch
%if 0%{?fedora} || 0%{?rhel} <= 8 || (0%{?oreon} >= 11)
Patch1000:        hplip-fedora-gui.patch
%endif
%if 0%{?rhel} <= 8 || 0%{?fedora} || (0%{?oreon} >= 11)
%endif
%if 0%{?fedora} || 0%{?rhel} <= 8 || (0%{?oreon} >= 11)
Suggests: hplip-gui
%endif
Recommends: avahi-tools
Recommends: libsane-hpaio%{?_isa} = %{version}-%{release}
Recommends: python3-gobject
Requires: cups
Requires: curl
Requires: %{_bindir}/gpg
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: python3-dbus
%if 0%{?rhel} <= 8 || 0%{?fedora} || (0%{?oreon} >= 11)
Requires: python3-pillow
%endif
Requires: setup
Requires: systemd
Requires: tar
Requires: usbutils
Requires(post): coreutils
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cups
BuildRequires:  cups-devel
BuildRequires:  curl
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-core)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  python3-cups
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sane-backends-devel
BuildRequires:  systemd
# /oreon:deps
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

%if 0%{?rhel} <= 8 || 0%{?fedora} || (0%{?oreon} >= 11)
%package gui
Summary: HPLIP graphical tools
BuildRequires: libappstream-glib
Recommends: avahi-tools
Recommends: libsane-hpaio%{?_isa} = %{version}-%{release}
Recommends: pkgconf
Requires: %{name}%{?_isa} = %{version}-%{release}
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{SOURCE6} %{version} %{_sourcedir}
cd %{builddir}
tar -xf %{_sourcedir}/hplip-%{version}-repack.tar.gz
cd hplip-%{version}

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
%if 0%{?fedora} || 0%{?rhel} <= 8 || (0%{?oreon} >= 11)
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

sed -i 's|^AM_INIT_AUTOMAKE|AM_INIT_AUTOMAKE([foreign])|g' configure.in
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
mkdir -p %{buildroot}/run/hplip
mkdir -p %{buildroot}%{_sharedstatedir}/hp
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/hplip.conf <<EOF
d /run/hplip 0775 root lp -
EOF
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
rm -f %{buildroot}%{_sysconfdir}/xdg/autostart/hplip-systray.desktop
%if 0%{?rhel} > 8 || (0%{?oreon} >= 11)
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
%if 0%{?rhel} <= 8 || 0%{?fedora} || (0%{?oreon} >= 11)
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
sed -i -e '/^Encoding=/d' hplip.desktop
desktop-file-validate hplip.desktop
desktop-file-install                               \
        --dir %{buildroot}/%{_datadir}/applications              \
        --add-category System \
        --add-category Settings \
        --add-category HardwareSettings                        \
        hplip.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
sed -i 's/\/usr\/share\/icons\/Humanity\/devices\/48\/printer\.svg/hp_logo/' hp-uiscan.desktop
desktop-file-validate hp-uiscan.desktop
desktop-file-install \
          --dir %{buildroot}/%{_datadir}/applications \
          --add-category Graphics \
          --add-category Scanning \
          --add-category Application \
          hp-uiscan.desktop
%endif
install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/hpcups-update-ppds
%{__mkdir_p} %{buildroot}%{_sysconfdir}/sane.d/dll.d
echo hpaio > %{buildroot}%{_sysconfdir}/sane.d/dll.d/hpaio
find doc/images -type f -exec chmod 644 {} \;
%{__mkdir_p} %{buildroot}%{_datadir}/hplip/prnt/plugins
%oreon_autofiles libsane-hpaio usr/*/lib*.so.*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/*/lib*.so.*

%post

%{_bindir}/timeout 10m -k 15m %{_bindir}/hpcups-update-ppds &>/dev/null ||:
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n hplip-common -f %{oreon_filedir}/hplip-common.list
%files -n hplip-libs -f %{oreon_filedir}/hplip-libs.list
%files -n hplip-gui -f %{oreon_filedir}/hplip-gui.list
%files -n libsane-hpaio -f %{oreon_filedir}/libsane-hpaio.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.25.8-2
- Import
