%global source0_hash 478b22124c6ff4901826fbe8f6cc91b26000bb7499d737493cd4cbc1b734c2e2
Name:             gawk-json
Summary:        JSON encoder/decoder for gawk
Version:          2.1.0
Release:        1%{?dist}
License:          GPL-3.0-or-later
URL:              https://sourceforge.net/projects/gawkextlib
Source0:        https://sourceforge%{gawk_api_version}net/projects/gawkextlib/files/%{name}-%{version}%{gawk_api_version}tar%{gawk_api_version}gz
Requires:         gawk >= 5.0.0
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')
%global _hardened_build 1
# oreon:deps
BuildRequires:  gawk(abi)
BuildRequires:  gawk-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  rapidjson-devel
# /oreon:deps
%description
The %{name} module provides a gawk extension library that uses RapidJSON to
implement functions mapping between gawk associative arrays and JSON.

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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
