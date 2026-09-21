%global source0_hash 410cf990e841bf6fe69668c201eb0235dcf2677544bcadbe4536f94cd4ff615f

Version: 22.1.0
Summary: Universal Plug and Play (UPnP) SDK
Name: libupnp
Release: 1%{?dist}
License: BSD-3-Clause AND ISC AND MIT
URL: https://github.com/pupnp/pupnp
Source: %{url}/archive/release-%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires:  openssl-devel


%description
The Universal Plug and Play (UPnP) SDK for Linux provides 
support for building UPnP-compliant control points, devices, 
and bridges on Linux.

%package devel
Summary: Include files needed for development with libupnp
Requires: libupnp%{?_isa} = %{version}-%{release}

%description devel
The libupnp-devel package contains the files necessary for development with
the UPnP SDK libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pupnp-release-%{version}


%build
%cmake -GNinja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -DUPNP_ENABLE_OPEN_SSL=ON
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets

%files
%license COPYING
%doc THANKS
%{_libdir}/libixml.so.*
%{_libdir}/libupnp.so.*

%files devel
%{_includedir}/upnp/
%{_libdir}/libixml.so
%{_libdir}/libupnp.so
%{_libdir}/pkgconfig/libupnp.pc

%changelog
%autochangelog

