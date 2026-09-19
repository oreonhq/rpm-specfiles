%global source0_hash 9ae39935cc5df1aebc805d7c7797c6cf42da5e74e3dfdc35b67ad237f8460f50

Name:             gawk-xml
Summary:          XML support for gawk
Version:          1.1.2
Release:          3%{?dist}
# Automatically converted from old format: GPL+ and GPLv3+ - review is highly recommended.
License:          GPL-1.0-or-later AND GPL-3.0-or-later

URL:              https://sourceforge.net/projects/gawkextlib
Source:           %{url}/files/%{name}-%{version}.tar.gz

Requires:         gawk
# rpmbuild finds the expat dependency automatically
#Requires:        expat
BuildRequires:    gawk-devel
BuildRequires:    gcc
BuildRequires:    gawkextlib-devel
BuildRequires:    expat-devel

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
%{name} provides the gawk XML extension module, as well as the xmlgawk script
and some gawk include libraries for enhanced XML processing.

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

# Install NLS language files:
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS
%doc *.xml
%{_infodir}/*.info*
%{_libdir}/gawk/xml.so
%{_bindir}/xmlgawk
%{_datadir}/awk/*
%{_mandir}/man1/*
%{_mandir}/man3/*

# =============================================================================

%changelog
%autochangelog
