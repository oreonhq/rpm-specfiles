%global source0_hash 811f19ed3df60f75070c07fc0eb5f767574e5b6dc2f12a679df04df381a43d88

Summary:        Generic library for real-time communications
Name:           libre
Version:        4.6.0
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/baresip/re
Source0:        https://github.com/baresip/re/archive/v%{version}/re-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  openssl-devel
%else
# https://github.com/baresip/re/pull/1371
BuildRequires:  openssl3-devel
# https://github.com/baresip/re/pull/1374
BuildRequires:  gcc-toolset-12
%endif
BuildRequires:  zlib-devel
# Cover multiple third party repositories
Obsoletes:      libre0 < 0.6.1-2
Provides:       libre0 = %{version}-%{release}
Provides:       libre0%{?_isa} = %{version}-%{release}
Obsoletes:      re < 0.6.1-2
Provides:       re = %{version}-%{release}
Provides:       re%{?_isa} = %{version}-%{release}
# librem was merged into libre 3.0.0
Obsoletes:      librem < 3.0.0-1
Provides:       librem = %{version}-%{release}
Provides:       librem%{?_isa} = %{version}-%{release}

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
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires:       openssl-devel
%else
Requires:       openssl3-devel
%endif
Requires:       zlib-devel
# Cover multiple third party repositories
Obsoletes:      libre0-devel < 0.6.1-2
Provides:       libre0-devel = %{version}-%{release}
Provides:       libre0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      re-devel < 0.6.1-2
Provides:       re-devel = %{version}-%{release}
Provides:       re-devel%{?_isa} = %{version}-%{release}
# librem was merged into libre 3.0.0
Obsoletes:      librem-devel < 3.0.0-1
Provides:       librem-devel = %{version}-%{release}
Provides:       librem-devel%{?_isa} = %{version}-%{release}

%description devel
The libre-devel package includes header files and libraries necessary for
developing programs which use the re C library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n re-%{version}

%build
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

%cmake \
%if 0%{?rhel} == 8
  -DOPENSSL_ROOT_DIR:PATH="%{_includedir}/openssl3;%{_libdir}/openssl3"
%endif

%cmake_build

%install
%cmake_install

# Remove static library
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%check
%if 0%{?rhel} == 8
. /opt/rh/gcc-toolset-12/enable
%endif

%cmake_build --target retest
%{__cmake_builddir}/test/retest -d test/data/ -v -r

%ldconfig_scriptlets

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_libdir}/%{name}.so.41*

%files devel
%{_libdir}/%{name}.so
%{_includedir}/re/
%{_libdir}/cmake/%{name}/
%{_libdir}/cmake/re/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
