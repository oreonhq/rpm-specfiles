%global source0_hash 451f323764f37ea6057e0ade60a0473938232ab2a92b97ffdc8c4860a8c76cfc
Name: ipcalc
Version: 1.0.3
Release:        1%{?dist}
Summary:        IP network address calculator
License: GPL-2.0-or-later
URL: https://gitlab.com/ipcalc/ipcalc
Source0:        https://gitlab.com/ipcalc/ipcalc/-/archive/%{version}/ipcalc-%{version}.tar.gz
Recommends:    libmaxminddb, geolite2-city, geolite2-country
Conflicts: initscripts < 9.63
Obsoletes:  ipcalculator < 0.41-20
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libmaxminddb-devel
BuildRequires:  meson
BuildRequires:  rubygem-ronn-ng
# /oreon:deps
%description
ipcalc provides a simple way to calculate IP information for a host
or network. Depending on the options specified, it may be used to provide
IP network information in human readable format, in a format suitable for
parsing in scripts, generate random private addresses, resolve an IP address,
or check the validity of an address.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Duse_maxminddb=enabled -Duse_runtime_linking=enabled
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.3-1
- Prepare for Oreon 11 (RP1)
