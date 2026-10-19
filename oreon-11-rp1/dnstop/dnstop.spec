%global source0_hash 011f5f655857f6dfef8a4c7e9e571b8cc4142f479cf7aacd1148493b99c0bfab
%global commit aaf21ba3426b9cc612e7bc8c87ed5beb160e0cdc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global _hardened_build 1
Name:           dnstop
Version:        20140915
Release:        1%{?dist}
Summary:        Displays information about DNS traffic on your network
License:        BSD-3-Clause
URL:            http://dns.measurement-factory.com/tools/dnstop/
Source0:        https://github.com/measurement-factory/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
# /oreon:deps
%description
dnstop is a libpcap application (ala tcpdump) that displays various
tables of DNS traffic on your network.

dnstop supports both IPv4 and IPv6 addresses.

To help find especially undesirable DNS queries, dnstop provides a
number of filters.

dnstop can either read packets from the live capture device, or from a
tcpdump savefile.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build

%configure
%make_build
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
