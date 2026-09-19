%global source0_hash 15c4e32b6c55ff105bafe03e8c91c7ca1b2eda31bf9a7127326bb87887ee18fe

%global _hardened_build 1
#global snapshot 0
%global OWNER schweikert
%global PROJECT fping
%global commit 06f9481ef3cf79c2aa973718366fb13927777689
%global commitdate 20251231
%global gittag v5.5
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: fping
Version: 5.5%{?snapshot:^%{commitdate}git%{shortcommit}}
Release: 1%{?dist}
Summary: Scriptable, parallelized ping-like utility
License: BSD-4.3TAHOE
URL: https://www.fping.org/
%if 0%{?snapshot}
Source0: https://github.com/%{OWNER}/%{PROJECT}/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires: autoconf automake
%else
Source0: https://fping.org/dist/%{name}-%{version}.tar.gz
%endif

BuildRequires: gcc
BuildRequires: make

%if "%{_sbindir}" == "%{_bindir}"
# We rely on filesystem to create the compat symlinks for us
Requires: filesystem(unmerged-sbin-symlinks)
Provides: /usr/sbin/fping
%endif

%description
fping is a ping-like program which can determine the accessibility of
multiple hosts using ICMP echo requests. fping is designed for parallelized
monitoring of large numbers of systems, and is developed with ease of
use in scripting in mind.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?snapshot}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1
%endif

%build
%if 0%{?snapshot}
./autogen.sh
%endif
%configure
%make_build

%install
%make_install

%files
%doc CHANGELOG.md
%license COPYING
%attr(0755,root,root) %caps(cap_net_raw=ep) %{_sbindir}/fping
%{_mandir}/man8/*

%changelog
%autochangelog
