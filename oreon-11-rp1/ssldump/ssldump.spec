%global source0_hash c81ce58d79b6e6edb8d89822a85471ef51cfa7d63ad812df6f470b5d14ff6e48

Summary:        SSL/TLS network protocol analyzer
Name:           ssldump
Version:        1.9
Release:        4%{?dist}
# pcap/{attrib.h,{logpkt,sys}.[ch]} are BSD-2-Clause, rest is BSD-4-Clause
License:        BSD-4-Clause AND BSD-2-Clause
URL:            https://github.com/adulau/ssldump
Source0:        https://github.com/adulau/ssldump/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        HOWTO
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  libpcap-devel
BuildRequires:  libnet-devel
BuildRequires:  json-c-devel

%description
The ssldump program is an SSL/TLS network protocol analyzer. It identifies
TCP connections on the chosen network interface and attempts to interpret
them as SSL/TLS traffic. When ssldump identifies SSL/TLS traffic, ssldump
decodes the records and displays them in a textual form to stdout. And if
provided with the appropriate keying material, ssldump will also decrypt
the connections and display the application data traffic. This program is
based on tcpdump, a network monitoring and data acquisition tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
install -p -m 0644 %{SOURCE1} .

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYRIGHT
%doc ChangeLog CREDITS HOWTO README README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
