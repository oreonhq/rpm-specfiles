%global source0_hash c81ce58d79b6e6edb8d89822a85471ef51cfa7d63ad812df6f470b5d14ff6e48
Summary:        SSL/TLS network protocol analyzer
Name:           ssldump
Version:        1.9
Release:        4%{?dist}
License:        BSD-4-Clause AND BSD-2-Clause
URL:            https://github.com/adulau/ssldump
Source0:        https://github.com/adulau/ssldump/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        HOWTO
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  json-c-devel
BuildRequires:  libnet-devel
BuildRequires:  libpcap-devel
BuildRequires:  openssl-devel
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
