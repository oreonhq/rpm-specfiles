%global source0_hash f485ca48b3f20a61b83cf4d16adfa5cc67fdea3ebfea01e4af4027fd429a9ea2

Name:             gawk-json
Summary:          JSON encoder/decoder for gawk
Version:          2.0.1
Release:          7%{?dist}
License:          GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk >= 5.0.0
BuildRequires:    gawk-devel >= 5.0.0
BuildRequires:    gcc-c++
BuildRequires:    rapidjson-devel

# Make sure the API version is compatible with our source code:
BuildRequires:    gawk(abi) >= 2.0
BuildRequires:    gawk(abi) < 5.0
BuildRequires: make

# At runtime, the ABI must be compatible with the compile-time version
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')

# This is the default as of Fedora 23:
%global _hardened_build 1

%description
The %{name} module provides a gawk extension library that uses RapidJSON to
implement functions mapping between gawk associative arrays and JSON.

# =============================================================================

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%configure
%make_build

%check
make check

%install
%make_install

# Install NLS language files, if and when translations are added:
#%find_lang %{name}

#%files -f %{name}.lang
%files
%license COPYING
%doc NEWS
%doc test/*.awk
%{_libdir}/gawk/json.so
%{_mandir}/man3/*

# =============================================================================

%changelog
%autochangelog
