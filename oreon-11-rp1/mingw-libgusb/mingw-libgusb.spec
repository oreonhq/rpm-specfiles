%global source0_hash 9df5ef301d6a4b361002aa52cce1165a87a89744055879bdbab31e7e86f1e846
%{?mingw_package_header}
Name:           mingw-libgusb
Version:        0.4.9
Release:        1%{?dist}
Summary:        GLib wrapper around libusb1 for MinGW
License:        LGPL-2.1-or-later
URL:            https://github.com/hughsie/libgusb
Source0:        https://github.com/hughsie/libgusb/releases/download/%{version}/libgusb-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw64-libusbx
# /oreon:deps
%description
GUsb is a GObject wrapper for libusb1 that makes it easy to do
asynchronous control, bulk and interrupt transfers with proper
cancellation and integration into a mainloop.

This is the MinGW version of this library.

%package -n mingw32-libgusb
Summary:        MinGW library which allows easy access to USB devices
Requires:       pkgconfig
%description -n mingw32-libgusb
This package contains the header files and libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw32-libgusb-static
Summary:        MinGW static library which allows easy access to USB devices
Requires:       mingw32-libgusb = %{version}-%{release}
%description -n mingw32-libgusb-static
This package contains the static libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw64-libgusb
Summary:        MinGW library which allows easy access to USB devices
Requires:       pkgconfig
%description -n mingw64-libgusb
This package contains the header files and libraries needed to develop MinGW
applications that use libgusb.

%package -n mingw64-libgusb-static
Summary:        MinGW static library which allows easy access to USB devices
Requires:       mingw64-libgusb = %{version}-%{release}
%description -n mingw64-libgusb-static
This package contains the static libraries needed to develop MinGW
applications that use libgusb.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libgusb-%{version}

%build

%mingw_meson \
        --default-library=both \
        -Dvapi=false \
        -Dtests=false \
        -Dintrospection=false \
        -Ddocs=false
%mingw_ninja
%install
%mingw_ninja_install
%oreon_autofiles mingw32-libgusb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libgusb-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgusb usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgusb-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgusb -f %{oreon_filedir}/mingw32-libgusb.list
%files -n mingw32-libgusb-static -f %{oreon_filedir}/mingw32-libgusb-static.list
%files -n mingw64-libgusb -f %{oreon_filedir}/mingw64-libgusb.list
%files -n mingw64-libgusb-static -f %{oreon_filedir}/mingw64-libgusb-static.list

%changelog

%autochangelog
