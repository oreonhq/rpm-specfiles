%global source0_hash d0a8b600fe1b4eaaf6277530e3cfc8f15b8ce4035f16af4a5eb5d4b123640cdd
%global rc %{nil}
Name:           srt
Version:        1.5.4
Release:        4%{?dist}
Summary:        Secure Reliable Transport protocol tools
License:        MPL-2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-build-Update-for-compatibility-with-CMake-4.x-3167.patch
Requires: srt-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  nettle-devel
# /oreon:deps
%description
Secure Reliable Transport (SRT) is an open source transport technology that
optimizes streaming performance across unpredictable networks, such as 
the Internet.

%package libs
Summary: Secure Reliable Transport protocol libraries
%description libs
Secure Reliable Transport protocol libraries

%package devel
Summary: Secure Reliable Transport protocol development libraries and headers
Requires: srt-libs%{?_isa} = %{version}-%{release}
%description devel
Secure Reliable Transport protocol development libraries and header files

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}%{rc}

%build

%cmake \
  -DENABLE_STATIC=OFF \
  -DENABLE_UNITTESTS=ON \
  -DENABLE_GETNAMEINFO=ON \
  -DENABLE_BONDING=ON \
  -DENABLE_PKTINFO=ON \
  -DUSE_ENCLIB=gnutls
%cmake_build
%install
%cmake_install
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest -j1 -E TestIPv6
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n srt-libs -f %{oreon_filedir}/srt-libs.list
%files -n srt-devel -f %{oreon_filedir}/srt-devel.list

%changelog

* Sun Apr 19 2026 Brandon Lester <blester@oreonhq.com> - 1.5.4-4
- import
