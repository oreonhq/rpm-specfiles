%global source0_hash 167a44121a332e71c51608e08c741c3d3b462f06eba06d4b4882b268cd944f36

%global basever 0.8.2
%global commit b9aeec6eaf3d5610503439b4fae3581d9aff08e8
%global shortcommit %{sub %{commit} 1 7}
%global snapdate 20220525

Name:    websocketpp
Summary: C++ WebSocket Protocol Library
Version: %{basever}%{?snapdate:^git%{snapdate}.%{shortcommit}}
Release: 1%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Url:     https://www.zaphoyd.com/websocketpp
%if %{defined snapdate}
Source0: https://github.com/zaphoyd/websocketpp/archive/%{commit}/%{name}-%{commit}.tar.gz
%else
Source0: https://github.com/zaphoyd/websocketpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%endif
Source1: websocketpp.pc
BuildArch: noarch

# put cmake files in share/cmake instead of lib/cmake
Patch1: websocketpp-0.8.3-cmake_noarch.patch

# Switch from ExactVersion to AnyNewerVersion to improve compatibility
# https://cmake.org/cmake/help/v3.0/module/CMakePackageConfigHelpers.html
# Fixes build failure of tomahawk, which uses "find_package(websocketpp 0.2.99 REQUIRED)"
# PR submitted upstream: https://github.com/zaphoyd/websocketpp/pull/740
# Disable check for same 32/64bit-ness in websocketpp-configVersion.cmake by setting CMAKE_SIZEOF_VOID_P
# PR submitted upstream: https://github.com/zaphoyd/websocketpp/pull/770
Patch2: websocketpp-0.8.1-cmake-configversion-compatibility-anynewerversion.patch

# Disable the following tests, which fail occasionally: test_transport, test_transport_asio_timers
Patch3: websocketpp-0.7.0-disable-test_transport-test_transport_asio_timers.patch

# Compatibility fixes for Boost 1.87
# https://github.com/zaphoyd/websocketpp/pull/1164
# Patch from PR at commit ee8cf42, 2025-04-09
Patch4: websocketpp-0.8.2-compatibility_fixes_for_boost_1.87.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
# needed for tests mostly
BuildRequires:  pkgconfig(openssl)
BuildRequires:  openssl-devel-engine
BuildRequires:  zlib-devel

%description
WebSocket++ is an open source (BSD license) header only C++ library
that implements RFC6455 The WebSocket Protocol. It allows integrating
WebSocket client and server functionality into C++ programs. It uses
interchangeable network transport modules including one based on C++
iostreams and one based on Boost Asio.

%package devel
Summary:  C++ WebSocket Protocol Library
Requires: boost-devel
%description devel
WebSocket++ is an open source (BSD license) header only C++ library
that implements RFC6455 The WebSocket Protocol. It allows integrating
WebSocket client and server functionality into C++ programs. It uses
interchangeable network transport modules including one based on C++
iostreams and one based on Boost Asio.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{defined snapdate}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build
%cmake -DBUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/pkgconfig
install -p -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pkgconfig/websocketpp.pc

## unpackaged files
rm -rfv %{buildroot}%{_includedir}/test_connection/

%check
%ctest

%files devel
%doc changelog.md readme.md roadmap.md
%license COPYING
%{_includedir}/websocketpp/
%dir %{_datadir}/cmake/
%{_datadir}/cmake/websocketpp/
%{_datadir}/pkgconfig/websocketpp.pc

%changelog
%autochangelog
