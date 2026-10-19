%global source0_hash d6b2a42378233aaff6188a0a5ff9fa0e959cb95742367e2cdfa2c6a023c7fe26
%bcond_without build_lib
Name:       ddcutil
Version:    3.0.2
Release:        1%{?dist}
Summary:        Query and update monitor settings
License:    GPL-2.0-or-later
URL:        http://www.ddcutil.com
Source0:        https://github.com/rockowitz/ddcutil/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
ExcludeArch:    s390 s390x
Requires:   hwdata
Requires:   i2c-tools
Recommends: /usr/bin/lsusb
Recommends: /usr/bin/modprobe
Recommends: pkg-config
Recommends: /usr/bin/lscpu
Recommends: /usr/bin/lsb_release
Recommends: xrandr
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libkmod)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xrandr)
# /oreon:deps
%description
Query and change monitor settings

ddcutil communicates with monitors implementing MCCS (Monitor Control Command
Set), using either the DDC/CI protocol on the I2C bus or as a Human Interface
Device on USB.  In general, anything that can be controlled using a monitor's
on-screen display can be controlled by this program.  Examples include
changing a monitor's input source and adjusting its brightness.

# libddcutil can be installed separately
%if %{with build_lib}
%package -n libddcutil
Summary:        Shared library to query and update monitor settings
%description -n libddcutil
Shared library version of ddcutil, exposing a C API.

%package -n libddcutil-devel
Summary:        Development files for libddcutil
License:        GPL-2.0-or-later AND BSD-3-Clause
Requires:       libddcutil%{?_isa} = %{version}-%{release}
Requires:       cmake-filesystem%{?_isa}
%description -n libddcutil-devel
Development files for libddcutil
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

NOCONFIGURE=1 ./autogen.sh
%configure \
%if %{with build_lib}
    --enable-lib=yes
%else
    --enable-lib=no
%endif
%make_build
%install
%make_install
%oreon_autofiles libddcutil usr/*/lib*.so.*
%oreon_autofiles libddcutil-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libddcutil -f %{oreon_filedir}/libddcutil.list
%files -n libddcutil-devel -f %{oreon_filedir}/libddcutil-devel.list

%changelog

%autochangelog
