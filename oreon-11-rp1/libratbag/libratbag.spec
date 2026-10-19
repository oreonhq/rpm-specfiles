%global source0_hash 8a7f8bf00c21ef5ad534e2804ed537f2fc6521a3932dd822c438e561a85a1bcd
%global udevdir %(pkg-config --variable=udevdir udev)
Name:           libratbag
Version:        0.18
Release:        1%{?dist}
Summary:        Programmable input device library
License:        MIT
URL:            https://github.com/libratbag/libratbag
Source0:        https://github.com/libratbag/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0001:      0001-Revert-build-install-ratbagd-into-sbindir.patch
%ifarch %{valgrind_arches}
%endif
# oreon:deps
BuildRequires:  check-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  libevdev-devel
BuildRequires:  libudev-devel
BuildRequires:  libunistring-devel
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(udev)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python3-evdev
BuildRequires:  python3-gobject
BuildRequires:  python3-lxml
BuildRequires:  swig
BuildRequires:  systemd
# /oreon:deps
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
%oreon_autofiles liblur usr/*/lib*.so.*
%oreon_autofiles liblur-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libratbag-ratbagd -f %{oreon_filedir}/libratbag-ratbagd.list
%files -n liblur -f %{oreon_filedir}/liblur.list
%files -n liblur-devel -f %{oreon_filedir}/liblur-devel.list

%changelog

%autochangelog
