%global source0_hash a2d5cc66018b3a79cc406e3d52df06e09444d22e82f7e34e104fa39b6b095dd3
Name:           libphidget22
Version:        1.26.20260828
Release:        1%{?dist}
Summary:        Drivers and API for Phidget devices
License:        LGPL-3.0-or-later and BSD-2-Clause and BSD-3-Clause
URL:            https://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/libraries/linux/%{name}/%{name}-%{version}.tar.gz
Provides:       bundled(mos)
Provides:       libphidget = %{version}-%{release}
Obsoletes:      libphidget < 2.1.8.20140319-20
Requires:       udev
Requires:       avahi-compat-libdns_sd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  avahi-devel
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  udev
# /oreon:deps
%description
Phidgets are a set of "plug and play" building blocks for low cost USB 
sensing and control from your PC.  All the USB complexity is taken care 
of by the robust libphidget API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# These headers are supplied by the avahi-compat-libdns_sd-devel package
# We can get rid of the bundled ones
rm -rf src/ext/include/avahi-*

%build

autoreconf -fi
%configure --disable-silent-rules --disable-static --enable-zeroconf=avahi --disable-ldconfig --enable-jni
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p -m 0755 %{buildroot}%{_udevrulesdir}/
install -p -m 0644 plat/linux/udev/99-libphidget22.rules %{buildroot}%{_udevrulesdir}/
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libphidget22-devel -f %{oreon_filedir}/libphidget22-devel.list

%changelog

%autochangelog
