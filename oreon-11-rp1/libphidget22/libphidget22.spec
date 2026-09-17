%global source0_hash ff63a08e2ba82b7fa027de6d4a4f34f4e7cc00152d28f37d6dbe29547e38ec89

Name:           libphidget22
Version:        1.23.20250925
Release:        2%{?dist}
Summary:        Drivers and API for Phidget devices

# libphidget is LGPL-3.0-or-later
# Bundled mos is BSD 2/3 Clause
License:        LGPL-3.0-or-later and BSD-2-Clause and BSD-3-Clause
URL:            https://www.phidgets.com
Source0:        https://www.phidgets.com/downloads/phidget22/libraries/linux/%{name}/%{name}-%{version}.tar.gz

Provides:       bundled(mos)
Provides:       libphidget = %{version}-%{release}
# Last build was libphidget-2.1.8.20140319-19.fc36
Obsoletes:      libphidget < 2.1.8.20140319-20

BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  avahi-devel
BuildRequires:  avahi-compat-libdns_sd-devel
BuildRequires:  libusb1-devel
BuildRequires:  make
BuildRequires:  gawk
BuildRequires:  udev

Requires:       udev
Requires:       avahi-compat-libdns_sd

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

%files
%doc AUTHORS README
%license COPYING
%{_libdir}/*.so.*
%{_udevrulesdir}/99-libphidget22.rules

%files devel
%{_includedir}/mos/
%{_includedir}/phidget22.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
