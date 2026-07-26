%global source0_hash f40fadf9e1dc56a8c177fac5ad7b8e3346964a80d3b268b97bc1af4b20022004

Name:           scanssh
Summary:        Fast SSH server and open proxy scanner
Version:        2.1.4
Release:        %autorelease
License:        BSD-3-Clause
URL:            https://github.com/ofalk/scanssh/wiki
Source:         https://github.com/ofalk/%{name}/archive/%{version}.tar.gz
Patch:          scanssh-2.1-hide.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libdnet-devel
BuildRequires:  libevent-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make

%description
ScanSSH supports scanning a list of addresses and networks for open proxies,
SSH protocol servers, Web and SMTP servers. Where possible ScanSSH, displays
the version number of the running services. ScanSSH protocol scanner supports
random selection of IP addresses from large network ranges and is useful for
gathering statistics on the deployment of SSH protocol servers in a company
or the Internet as whole.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -ivf

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%{_bindir}/scanssh
%{_mandir}/man1/scanssh.1*

%changelog
%autochangelog
