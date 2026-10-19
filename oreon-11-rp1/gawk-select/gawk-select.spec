%global source0_hash 35fbaf4180851c9230dc2fa5272b669d77842ee4bfedbbdbb534e92219f99bcd
Name:             gawk-select
Summary:        Select I/O multiplexing library for gawk
Version:          1.1.4
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
BuildRequires:  cpp
BuildRequires:  gawk(abi)
BuildRequires:  gawk-devel
BuildRequires:  gawkextlib-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
The %{name} module provides a gawk extension library supporting I/O
multiplexing and signal trapping.

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
