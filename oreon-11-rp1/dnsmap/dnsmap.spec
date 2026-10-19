%global source0_hash f52d6d49cbf9a60f601c919f99457f108d51ecd011c63e669d58f38d50ad853c
Name:           dnsmap
Version:        0.36
Release:        1%{?dist}
Summary:        Sub-domains bruteforcer
License:        GPL-2.0-or-later
URL:            https://github.com/resurrecting-open-source-projects/dnsmap
%global         gituser         resurrecting-open-source-projects
%global         gitname         dnsmap
%global         gitdate         20210226
%global         commit          2e3c23390a47cdf897367737db80f593475ed2a1
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
Source0:        https://github.com/%{gituser}/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
dnsmap is a small tool that perform brute-forcing of domains.
It can use a built-in list or an external dictionary file and
saves output to TXT/CSV format.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1
autoreconf -v -i

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
