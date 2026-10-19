%global source0_hash 26bdcf2cebd7310c6f598850606b037ef0c515fe6608ebc54d22c50c4c32b35f
%bcond_with deprecated
Name:    bluez
Version: 5.87
Release:        1%{?dist}
Summary:        Bluetooth utilities
License: GPL-2.0-or-later
URL:     http://www.bluez.org/
Source0:        https://www.kernel.org/pub/linux/bluetooth/%{name}-%{version}.tar.xz
Requires: dbus >= 1.6
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cups-devel
BuildRequires:  dbus-devel
BuildRequires:  glib2-devel
BuildRequires:  json-c-devel
BuildRequires:  libell-devel
BuildRequires:  libical-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  python3-docutils
BuildRequires:  python3-pygments
BuildRequires:  readline-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
Utilities for use in Bluetooth applications:
	- avinfo
	- bluemoon
	- bluetoothctl
	- bluetoothd
	- btattach
	- btmon
	- hex2hcd
	- mpris-proxy

The BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package cups
Summary: CUPS printer backend for Bluetooth printers
Requires: bluez%{?_isa} = %{version}-%{release}
Requires: cups
%description cups
This package contains the CUPS backend

%if %{with deprecated}
%package deprecated
Summary: Deprecated Bluetooth applications
Requires: bluez%{?_isa} = %{version}-%{release}
Obsoletes: bluez < 5.55-2
%description deprecated
Bluetooth applications that have bee deprecated by upstream. They have been
replaced by functionality in the core bluetoothctl and will eventually
be dropped by upstream. Utilities include:
	- ciptool
	- gatttool
	- hciattach
	- hciconfig
	- hcidump
	- hcitool
	- meshctl
	- rfcomm
	- sdptool
%endif

%package libs
Summary: Libraries for use in Bluetooth applications
%description libs
Libraries for use in Bluetooth applications.

%package libs-devel
Summary: Development libraries for Bluetooth applications
Requires: bluez-libs%{?_isa} = %{version}-%{release}
%description libs-devel
bluez-libs-devel contains development libraries and headers for
use in Bluetooth applications.

%package hid2hci
Summary: Put HID proxying bluetooth HCI's into HCI mode
Requires: bluez%{?_isa} = %{version}-%{release}
%description hid2hci
Most allinone PC's and bluetooth keyboard / mouse sets which include a
bluetooth dongle, ship with a so called HID proxying bluetooth HCI.
The HID proxying makes the keyboard / mouse show up as regular USB HID
devices (after connecting using the connect button on the device + keyboard),
which makes them work without requiring any manual configuration.

The bluez-hid2hci package contains the hid2hci utility and udev rules to
automatically switch supported Bluetooth devices into regular HCI mode.

Install this package if you want to use the bluetooth function of the HCI
with other bluetooth devices like for example a mobile phone.

Note that after installing this package you will first need to pair your
bluetooth keyboard and mouse with the bluetooth adapter before you can use
them again. Since you cannot use your bluetooth keyboard and mouse until
they are paired, this will require the use of a regular (wired) USB keyboard
and mouse.

%package mesh
Summary: Bluetooth mesh
Requires: bluez%{?_isa} = %{version}-%{release}
Requires: bluez-libs%{?_isa} = %{version}-%{release}
%description mesh
Services for bluetooth mesh

%package obexd
Summary: Object Exchange daemon for sharing content
Requires: bluez%{?_isa} = %{version}-%{release}
Requires: bluez-libs%{?_isa} = %{version}-%{release}
%description obexd
Object Exchange daemon for sharing files, contacts etc over bluetooth

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure --enable-tools --enable-library \
           --enable-external-ell --disable-optimization \
%if %{with deprecated}
           --enable-deprecated \
%endif
           --enable-sixaxis --enable-cups --enable-nfc --enable-mesh \
           --enable-hid2hci --enable-testing --enable-experimental \
           --enable-bap --enable-bass --enable-mcp --enable-micp \
           --enable-csip --enable-vcp \
           --with-systemdsystemunitdir=%{_unitdir} \
           --with-systemduserunitdir=%{_userunitdir}
%{make_build}
%install
%{make_install}
%if %{with deprecated}
install -m0755 attrib/gatttool $RPM_BUILD_ROOT%{_bindir}
%endif
install -m0755 tools/avinfo $RPM_BUILD_ROOT%{_bindir}
install -m0755 tools/btmgmt $RPM_BUILD_ROOT%{_bindir}
install -m0644 doc/btmgmt.1 $RPM_BUILD_ROOT%{_mandir}/man1/
find $RPM_BUILD_ROOT -name '*.la' -delete
if test -d ${RPM_BUILD_ROOT}/usr/lib64/cups ; then
	install -D -m0755 ${RPM_BUILD_ROOT}/usr/lib64/cups/backend/bluetooth ${RPM_BUILD_ROOT}%_cups_serverbin/backend/bluetooth
	rm -rf ${RPM_BUILD_ROOT}%{_libdir}/cups
fi
rm -f ${RPM_BUILD_ROOT}/%{_sysconfdir}/udev/*.rules ${RPM_BUILD_ROOT}/usr/lib/udev/rules.d/*.rules
install -D -p -m0644 tools/hid2hci.rules ${RPM_BUILD_ROOT}/%{_udevrulesdir}/97-hid2hci.rules
install -d -m0755 $RPM_BUILD_ROOT/%{_localstatedir}/lib/bluetooth
install -d -m0755 $RPM_BUILD_ROOT/%{_localstatedir}/lib/bluetooth/mesh
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/bluetooth/
install -D -p -m0644 src/main.conf ${RPM_BUILD_ROOT}/etc/bluetooth/main.conf
install -D -p -m0644 mesh/mesh-main.conf ${RPM_BUILD_ROOT}/etc/bluetooth/mesh-main.conf
install -D -p -m0644 profiles/input/input.conf ${RPM_BUILD_ROOT}/etc/bluetooth/input.conf
install -D -p -m0644 profiles/network/network.conf ${RPM_BUILD_ROOT}/etc/bluetooth/network.conf
install emulator/btvirt ${RPM_BUILD_ROOT}/%{_libexecdir}/bluetooth/
%ldconfig_scriptlets libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post bluetooth.service
%preun

%systemd_preun bluetooth.service
%postun

%systemd_postun_with_restart bluetooth.service
%post hid2hci

/sbin/udevadm trigger --subsystem-match=usb
%post mesh

%systemd_user_post bluetooth-mesh.service
%preun mesh

%systemd_user_preun bluetooth-mesh.service
%post obexd

%systemd_user_post obex.service
%preun obexd

%systemd_user_preun obex.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
