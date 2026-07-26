%global source0_hash c55345e7fc0b303fae5b96030da0b77a1a84392b2423e9ef8abea565a47fe8f2

%global forgeurl https://github.com/libimobiledevice/libideviceactivation
%global commit ecc10ef8048c6591b936c5ca1b0971157087e6b2
%global date 20240529
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}

Name:           libideviceactivation
Version:        1.1.1^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Library to handle the activation process of iOS devices

License:        LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            https://www.libimobiledevice.org/
Source:         %{forgeurl}/archive/%{commit}/%{name}-%{commit}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

BuildRequires:  libcurl-devel
BuildRequires:  libimobiledevice-devel
BuildRequires:  libplist-devel
BuildRequires:  libxml2-devel

%description
This project provides an interface to activate and deactivate iOS devices by
talking to Apple's webservice.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and libraries for %{name}.

%package        utils
Summary:        Utilities for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    utils
This package provides a command-line utility to active and deactivate iOS
devices leveraging %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{commit}

%if %{defined commit}
echo %{version} > .tarball-version
%endif

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
%make_build

%install
%make_install

%files
%license COPYING COPYING.LESSER
%doc AUTHORS NEWS README.md
%{_libdir}/libideviceactivation-1.0.so.2{,.*}

%files utils
%{_bindir}/ideviceactivation
%{_mandir}/man1/ideviceactivation.1*

%files devel
%{_libdir}/libideviceactivation-1.0.so
%{_libdir}/pkgconfig/libideviceactivation-1.0.pc
%{_includedir}/libideviceactivation.h

%changelog
%autochangelog
