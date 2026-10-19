%global source0_hash 1c462f2630f62bbfc14f3248358abd7d7646b964e5514473a1059f69b1f11109
Name:             gawk-redis
Summary:        Redis client library for gawk
Version:          1.7.8
Release:        1%{?dist}
License:          GPL-3.0-or-later
URL:              https://sourceforge.net/projects/gawkextlib
Source0:        https://sourceforge%{gawk_api_version}net/projects/gawkextlib/files/%{name}-%{version}%{gawk_api_version}tar%{gawk_api_version}gz
Requires:         gawk
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')
%global _hardened_build 1
# oreon:deps
BuildRequires:  gawk(abi)
BuildRequires:  gawk-devel
BuildRequires:  gcc
BuildRequires:  hiredis-devel
BuildRequires:  make
# /oreon:deps
%description
The %{name} module provides a gawk extension library for accessing Redis
database servers using the hiredis C library API.

# =============================================================================

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%check

make check
%install
%make_install
rm -f %{buildroot}%{_infodir}/dir
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
