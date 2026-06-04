%global source0_hash none

%global rc %{nil}

Name:           srt
Version:        1.5.4
Release:        4%{?dist}
Summary:        Secure Reliable Transport protocol tools

License:        MPL-2.0
URL:            https://www.srtalliance.org
Source0:        https://github.com/Haivision/srt/archive/refs/tags/v%{version}%{rc}/%{name}-%{version}%{rc}.tar.gz

# https://github.com/Haivision/srt/commit/0def1b1a1094fc57752f241250e9a1aed71bbffd
Patch0:         0001-build-Update-for-compatibility-with-CMake-4.x-3167.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gmock-devel
BuildRequires:  gnutls-devel
BuildRequires:  gtest-devel
BuildRequires:  make
BuildRequires:  nettle-devel

Requires: srt-libs%{?_isa} = %{version}-%{release}


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
# remove old upstream temporary compatibility pc
rm -f %{buildroot}/%{_libdir}/pkgconfig/haisrt.pc


%check
# tests do not work in parallel as of 1.5.4 rc0
# - TestIPv6 are known broken due to v4_v6 mapping differnces between platforms
#   https://github.com/Haivision/srt/issues/1972#
%ctest -j1 -E TestIPv6


%ldconfig_scriptlets libs


%files
%license LICENSE
%doc README.md docs
%{_bindir}/srt-ffplay
%{_bindir}/srt-file-transmit
%{_bindir}/srt-live-transmit
%{_bindir}/srt-tunnel

%files libs
%license LICENSE
%{_libdir}/libsrt.so.1.5*

%files devel
%doc examples
%{_includedir}/srt
%{_libdir}/libsrt.so
%{_libdir}/pkgconfig/srt.pc


%changelog
* Sun Apr 19 2026 Brandon Lester <blester@oreonhq.com> - 1.5.4-4
- import
