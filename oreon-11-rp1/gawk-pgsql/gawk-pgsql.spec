%global source0_hash a258385265ce254c967cf47ad9288a65f5b5d40c626911dfab78fac3e344f170

Name:             gawk-pgsql
Summary:          PostgreSQL client library for gawk
Version:          1.1.2
Release:          8%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# rpmbuild finds the postgresql-libs dependency automatically
#Requires:        postgresql-libs
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    gawkextlib-devel
BuildRequires:    libpq-devel

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
The gawk-pgsql module provides a gawk extension library for accessing
PostgreSQL database servers using the libpq C library API.

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

# The */dir file is not necessary for info pages to work correctly...
rm -f %{buildroot}%{_infodir}/dir

# Install NLS language files, if translations are present:
#%find_lang %{name}

# if translations are present: %files -f %{name}.lang
%files
%license COPYING
%doc NEWS
%doc *.awk test/*.awk
%{_infodir}/*.info*
%{_libdir}/gawk/pgsql.so

# =============================================================================

%changelog
%autochangelog
