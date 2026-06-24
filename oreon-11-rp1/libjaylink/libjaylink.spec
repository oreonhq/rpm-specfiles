%global source0_hash none

Name:           libjaylink
Version:        0.3.0
Release:        10%{?dist}
Summary:        Library for SEGGER J-Link and compatible devices

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.zapb.de/libjaylink/libjaylink
Source0:        https://gitlab.zapb.de/%{name}/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires: make

%description
libjaylink is a shared library written in C to access SEGGER J-Link
and compatible devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup


%build
./autogen.sh
%configure --disable-static
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%__mkdir -p $RPM_BUILD_ROOT/usr/lib/udev/rules.d/
%__sed -e 's/MODE="664", GROUP="plugdev"/TAG+="uaccess"/g' contrib/99-libjaylink.rules > $RPM_BUILD_ROOT/usr/lib/udev/rules.d/60-libjaylink.rules

%ldconfig_scriptlets

%files
%license COPYING
%doc README.md NEWS
%{_libdir}/*.so.*
%{_prefix}/lib/udev/rules.d/*

%files devel
%doc HACKING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
%autochangelog

