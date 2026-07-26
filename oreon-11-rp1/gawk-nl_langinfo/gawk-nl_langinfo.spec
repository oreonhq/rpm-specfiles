%global source0_hash 3d8a208b9e180be5ff287bd41002cdf38ee859083a0b4e7315c1568f05054b28

Name:             gawk-nl_langinfo
Summary:          Gawk library providing nl_langinfo access
Version:          1.1.0
Release:          23%{?dist}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:          GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
BuildRequires:    gawk-devel
BuildRequires:    gcc

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
The %{name} module contains the gawk nl_langinfo shared library
extension. It provides access to the nl_langinfo(3) C library function.

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
%{_libdir}/gawk/nl_langinfo.so
%{_mandir}/man3/*

# =============================================================================

%changelog
%autochangelog
