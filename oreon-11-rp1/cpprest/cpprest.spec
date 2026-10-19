%global source0_hash 4b0d14e5bfe77ce419affd253366e861968ae6ef2c35ae293727c1415bd145c8
%global _lto_cflags %nil
%undefine __cmake_in_source_build
%define major 2
%define minor 10
Name:           cpprest
Version:        2.10.19
Release:        1%{?dist}
Summary:        C++ REST library
License:        MIT
Url:            https://github.com/Microsoft/cpprestsdk
Source0:        https://github.com/Microsoft/cpprestsdk/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         cpprest-2.10.17-disable-outside-and-failing-tests.patch
Patch2:         cpprest-2.10.9-disable-tests-long-timeouts.patch
Patch3:         cpprest-2.10.9-disable-test-extract_floating_point.patch
Patch4:         cpprest-2.10.16-revert_commit_cb7ca74.patch
Patch5:         cpprest-2.10.19-fix-boost-asio-errors.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  openssl-devel-engine
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  websocketpp-devel
# /oreon:deps
%description
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Also known as Casablanca.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       pkgconfig(openssl)
%description devel
The C++ REST SDK is a Microsoft project for cloud-based client-server
communication in native code using a modern asynchronous C++ API design. This
project aims to help C++ developers connect to and interact with services.

Development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cpprestsdk-%{version} -p1
# Remove bundled sources of websocketpp
rm -r Release/libs
# Remove file ThirdPartyNotices.txt, which is associated to websocketpp
rm ThirdPartyNotices.txt

%build

cd Release
export CXXFLAGS="%{optflags} -Wl,--as-needed"
%cmake -DCMAKE_BUILD_TYPE=Release -DWERROR=OFF -DCPPREST_EXCLUDE_BROTLI=OFF
%cmake_build
%install
cd Release
%cmake_install
%oreon_autofiles cpprest-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ifarch ppc64 s390x
%else
cd Release/%{_vpath_builddir}/Binaries
./test_runner *_test.so ||:
%endif
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n cpprest-devel -f %{oreon_filedir}/cpprest-devel.list

%changelog

%autochangelog
