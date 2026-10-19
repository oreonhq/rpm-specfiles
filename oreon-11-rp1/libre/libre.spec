%global source0_hash 2a8cbf13719618d879464617512a80fe2c13fe63cd5461cf01a195fbe46b3ca4
Summary:        Generic library for real-time communications
Name:           libre
Version:        4.11.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/baresip/re
Source0:        https://github.com/baresip/re/archive/v%{version}/re-%{version}.tar.gz
Obsoletes:      libre0 < 0.6.1-2
Provides:       libre0 = %{version}-%{release}
Provides:       libre0%{?_isa} = %{version}-%{release}
Obsoletes:      re < 0.6.1-2
Provides:       re = %{version}-%{release}
Provides:       re%{?_isa} = %{version}-%{release}
Obsoletes:      librem < 3.0.0-1
Provides:       librem = %{version}-%{release}
Provides:       librem%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-toolset-12
BuildRequires:  openssl3-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Libre is a generic library for real-time communications with async I/O
support. Features are a SIP stack (RFC 3261), SDP, RTP and RTCP, SRTP and
SRTCP (Secure RTP), DNS client, STUN/TURN/ICE stack, BFCP, HTTP stack with
client/server, Websockets, Jitter buffer, async I/O (poll, epoll, select,
kqueue), UDP/TCP/TLS/DTLS transport, JSON parser and Real Time Messaging
Protocol (RTMP).

%package devel
Summary:        Development files for the re library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       openssl3-devel
Requires:       zlib-devel
Obsoletes:      libre0-devel < 0.6.1-2
Provides:       libre0-devel = %{version}-%{release}
Provides:       libre0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      re-devel < 0.6.1-2
Provides:       re-devel = %{version}-%{release}
Provides:       re-devel%{?_isa} = %{version}-%{release}
Obsoletes:      librem-devel < 3.0.0-1
Provides:       librem-devel = %{version}-%{release}
Provides:       librem-devel%{?_isa} = %{version}-%{release}
%description devel
The libre-devel package includes header files and libraries necessary for
developing programs which use the re C library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir re-%{version}
%oreon_prep
%build

%cmake \
%cmake_build
%install
%cmake_install
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build --target retest
%{__cmake_builddir}/test/retest -d test/data/ -v -r
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n libre-devel -f %{oreon_filedir}/libre-devel.list

%changelog

%autochangelog
