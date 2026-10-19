%global source0_hash e2e8d95c40f9e9f10a7fbebb19c0f25ba88bab76fe521b945277ddd2397fcbe1
Name:           scanssh
Summary:        Fast SSH server and open proxy scanner
Version:        2.1.4
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://github.com/ofalk/scanssh/wiki
Source0:        https://github.com/ofalk/%{name}/archive/%{version}.tar.gz
Patch:          scanssh-2.1-hide.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libdnet-devel
BuildRequires:  libevent-devel
BuildRequires:  libpcap-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
