%global source0_hash d2f01a9dc0cc01777844b6d27f0f836dad9a4b9a32a31c7bbde0762480262f25

Name:       libtelnet
Version:    0.23
Release:    13%{?dist}
Summary:    TELNET protocol parsing framework
License:    Unlicense-libtelnet
URL:        http://github.com/seanmiddleditch/libtelnet

Source0:    %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires: make

%description
Small library for parsing the TELNET protocol, responding to TELNET commands via
an event interface, and generating valid TELNET commands.

libtelnet includes support for the non-official MCCP, MCCP2, ZMP, and MSSP
protocols used by MUD servers and clients.

%package devel
Summary:    Header files for libtelnet
Requires:   %{name}%{?_isa} = %{version}-%{release}
Requires:   pkgconfig

%description devel
Header files for developing applications making use of %{name}.

%package utils
Summary:    TELNET utility programs from libtelnet

%description utils
Provides three utilities based on the libtelnet library.
  * telnet-proxy - a TELNET proxy and debugging daemon
  * telnet-client - simple TELNET client
  * telnet-chatd - no-features chat server for testing TELNET clients.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS
%{_libdir}/%{name}.so.2
%{_libdir}/%{name}.so.2.0.0

%files devel
%doc %{_datadir}/man/man1/*
%doc %{_datadir}/man/man3/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%files utils 
%{_bindir}/telnet-chatd
%{_bindir}/telnet-client
%{_bindir}/telnet-proxy

%changelog
%autochangelog
