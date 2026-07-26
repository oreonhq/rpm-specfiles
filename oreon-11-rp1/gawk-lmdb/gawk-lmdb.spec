%global source0_hash e3d0b899f2f56c0158404d105f1812fa8886bccd45adc3b9dd7da851005aa422

Name:             gawk-lmdb
Summary:          LMDB Lightning Memory-Mapped Database binding for gawk
Version:          1.1.3
Release:          7%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# rpmbuild finds the lmdb-libs dependency automatically
#Requires:        lmdb-libs
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    gawkextlib-devel
BuildRequires:    lmdb-devel
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
The %{name} module provides a gawk extension library implementing the
Lightning Memory-Mapped Database (LMDB) API.

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
%doc test/dict*.awk
%{_libdir}/gawk/lmdb.so
%{_mandir}/man3/*

# =============================================================================

%changelog
%autochangelog
