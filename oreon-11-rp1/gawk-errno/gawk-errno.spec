%global source0_hash 95851395247868ebd8d2f934f160b57753ef28fdd4a547b4665166f4325675c4

Name:             gawk-errno
Summary:          Errno library for gawk
Version:          1.1.1
Release:          8%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    cpp

# Make sure the API version is compatible with our source code:
BuildRequires:    gawk(abi) >= 1.1
BuildRequires:    gawk(abi) < 5.0
BuildRequires: make

# At runtime, the ABI must be compatible with the compile-time version
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')

# This is the default as of Fedora 23:
%global _hardened_build 1

%description
The %{name} module is a gawk extension library containing some useful
functions for working with ERRNO values.

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

# Install NLS language files, if translations are present:
#%find_lang %{name}

# if translations are present: %files -f %{name}.lang
%files
%license COPYING
%doc NEWS
%{_libdir}/gawk/errno.so
%{_mandir}/man3/*

# =============================================================================

%changelog
%autochangelog
