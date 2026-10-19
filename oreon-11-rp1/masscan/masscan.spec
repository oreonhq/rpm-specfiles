%global source0_hash 0363e82c07e6ceee68a2da48acd0b2807391ead9a396cf9c70b53a2a901e3d5f
Name:           masscan
Version:        1.3.2
Release:        15%{?dist}
Summary:        This is an Internet-scale port scanner
License:        AGPL-3.0-only
URL:            https://github.com/robertdavidgraham/masscan
Source0:        https://github.com/robertdavidgraham/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       libpcap-devel
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
# /oreon:deps
%description
This is an Internet-scale port scanner. It can scan the entire 
Internet in under 6 minutes, transmitting 10 million packets 
per second, from a single machine.
It is a faster port scan that produces results similar to nmap,
the most famous port scanner. Internally, it operates more like
scanrand, unicornscan, and ZMap, using asynchronous transmission.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}
sed -i -e 's/CC =/CC ?=/g' Makefile
sed -i 's/\r$//' VULNINFO.md

%build

export CC=gcc
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_bindir}/
install -pm 0755 bin/masscan %{buildroot}%{_bindir}/%{name}
install -Dp -m 0644 doc/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
