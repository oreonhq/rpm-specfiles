%global source0_hash 8a7f8bf00c21ef5ad534e2804ed537f2fc6521a3932dd822c438e561a85a1bcd

%global udevdir %(pkg-config --variable=udevdir udev)

Name:           libratbag
Version:        0.18
Release:        5%{?gitdate:.%{gitdate}git%{gitversion}}%{?dist}
Summary:        Programmable input device library
License:        MIT
URL:            https://github.com/libratbag/libratbag
Source0:        https://github.com/libratbag/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# 0.18+ now installs into /usr/sbin, let's revert that
# for now until sure that's a permanent change
# https://github.com/libratbag/libratbag/issues/1672
Patch0001:      0001-Revert-build-install-ratbagd-into-sbindir.patch

BuildRequires:  git gcc gcc-c++
BuildRequires:  meson pkgconfig
BuildRequires:  libevdev-devel
BuildRequires:  libudev-devel
BuildRequires:  pkgconfig(udev) pkgconfig(glib-2.0) pkgconfig(json-glib-1.0)
BuildRequires:  check-devel
%ifarch %{valgrind_arches}
BuildRequires:  valgrind
%endif
BuildRequires:  systemd
BuildRequires:  python3 python3-devel python3-gobject
BuildRequires:  python3-lxml python3-evdev swig
BuildRequires:  libunistring-devel

%description
libratbag is a library that allows to configure programmable
mice.

%package        ratbagd
Summary:        DBus daemon to access programmable input devices
Obsoletes:      libratbag < 0.9.900
Requires:       python3-evdev python3-gobject

%description    ratbagd
The ratbagd package contains a dbus daemon to access and configure
programmable input devices, primarily gaming mice.

%package        -n liblur
Summary:        Logitech Unifying Receiver library

%description    -n liblur
The liblur package contains libraries and tools to access and
configure the Logitech Unifying Receivers. The functionality
are mainly listing, pairing and un-pairing Logitech devices
attached to a receiver.

%package        -n liblur-devel
Summary:        Development files for liblur
Requires:       liblur%{?_isa} = %{version}-%{release}

%description    -n liblur-devel
The liblur-devel package contains libraries and header files for
developing applications that use liblur.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git

# hack until rhbz#1409661 gets fixed
%{!?__global_cxxflags: %define __global_cxxflags %{optflags}}

%build
# s390x builds sometimes fails during the tests, let just disable those
%ifarch s390x
%meson -Dudev-dir=%{udevdir} -Ddocumentation=false -Dtests=false
%else
%meson -Dudev-dir=%{udevdir} -Ddocumentation=false
%endif
%meson_build

%check
%meson_test

%install
%meson_install

%ldconfig_scriptlets -n liblur

%files ratbagd
%license COPYING
%{_bindir}/ratbagctl
%{_bindir}/ratbagd
%dir %{_datadir}/libratbag
%{_datadir}/libratbag/*.device
%{_mandir}/man1/ratbagctl.1*
%{_mandir}/man8/ratbagd.8*
%{_datadir}/dbus-1/system.d/org.freedesktop.ratbag1.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.ratbag1.service
%{_unitdir}/ratbagd.service

%files -n liblur
%license COPYING
%{_libdir}/liblur.so.*
%{_bindir}/lur-command
%{_mandir}/man1/lur-command.1*

%files -n liblur-devel
%{_includedir}/liblur.h
%{_libdir}/liblur.so
%{_libdir}/pkgconfig/liblur.pc

%changelog
%autochangelog
