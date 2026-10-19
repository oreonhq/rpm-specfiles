%global source0_hash 5d84dec684c27b97b921d2f3b73218cb773cf4ea915caee317ac8fc73cef8136
Name:           hidapi
Version:        0.15.0
Release:        1%{?dist}
Summary:        Library for communicating with USB and Bluetooth HID devices
License:        GPL-3.0-only OR BSD-3-Clause
URL:            https://github.com/libusb/hidapi
Source0:        https://github.com/libusb/%{name}/archive/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libudev-devel
BuildRequires:  libusb1-devel
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description

%package devel
Summary: Development files for hidapi
Requires: %{name}%{?_isa} = %{version}-%{release}
%description -n hidapi-devel
This package contains development files for hidapi which provides access to
USB and Bluetooth HID-class devices.

%package -n mingw32-hidapi
Summary:        Development files for hidapi
Obsoletes:      mingw32-hidapi-static < 0.11.2-6
%description -n mingw32-hidapi

%package -n mingw64-hidapi
Summary:        Development files for hidapi
Obsoletes:      mingw64-hidapi-static < 0.11.2-6
%description -n mingw64-hidapi

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{name}-%{version}
%oreon_prep
%build

%cmake
%cmake_build
%mingw_cmake
%mingw_make_build
%install
%cmake_install
%mingw_make_install
%mingw_debug_install_post
%oreon_autofiles mingw32-hidapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-hidapi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n hidapi-devel -f %{oreon_filedir}/hidapi-devel.list
%files -n mingw32-hidapi -f %{oreon_filedir}/mingw32-hidapi.list
%files -n mingw64-hidapi -f %{oreon_filedir}/mingw64-hidapi.list

%changelog

%autochangelog
