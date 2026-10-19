%global source0_hash 592b867902fb59ced63fa10f1be2921ff703d231d35f30350288a60a12ca5b8e
Name:           libusbauth-configparser
Version:        1.0.5
Summary:        Library for USB Firewall including flex/bison parser
URL:            https://github.com/kochstefan/usbauth-all/tree/master/libusbauth-configparser
Source0:        https://github.com/kochstefan/usbauth-all/archive/v%{version}.tar.gz
Release:        1%{?dist}
License:        LicenseRef-Callaway-LGPLv2
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pkgconfig(libudev)
# /oreon:deps
%description
Library to read usbauth config file into data structures

%package devel
Summary:        Development part of library for USB Firewall including flex/bison parser
Requires:       libusbauth-configparser%{?_isa} = %{version}-%{release}
%description devel
Development part of library to read usbauth config file into data structures

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir usbauth-all-%{version}
%oreon_prep
%build

pushd %{name}/
autoreconf -f -i
%configure
%make_build
popd
%install
pushd %{name}/
%make_install
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libusbauth-configparser-devel -f %{oreon_filedir}/libusbauth-configparser-devel.list

%changelog

%autochangelog
