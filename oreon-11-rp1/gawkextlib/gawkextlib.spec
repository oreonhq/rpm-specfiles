%global source0_hash ecd06c1857f58530f73866dffb74a32f17d1194c045f351b5ab8acad4f77678c
Name:             gawkextlib
Summary:        Library providing common infrastructure for gawk extension libraries
Version:          1.0.4
Release:        1%{?dist}
License:          GPL-3.0-or-later
URL:              https://sourceforge.net/projects/gawkextlib
Source0:        https://sourceforge%{gawk_api_version}net/projects/%{name}/files/%{name}-%{version}%{gawk_api_version}tar%{gawk_api_version}gz
Requires:         gawk
%global gawk_api_version %(gawk 'BEGINFILE {if (ERRNO) nextfile} match($0, /#define gawk_api_(major|minor)_version[[:space:]]+([[:digit:]]+)/, f) {v[f[1]] = f[2]} END {print (v["major"] "." v["minor"])}' /usr/include/gawkapi.h)
Requires:         gawk(abi) >= %{gawk_api_version}
Requires:         gawk(abi) < %(echo %{gawk_api_version} | gawk -F. '{printf "%d.0\n", $1+1}')
%global _hardened_build 1
# oreon:deps
BuildRequires:  gawk(abi)
BuildRequires:  gawk-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
%{name} is a library providing common support infrastructure for gawk
extensions. This package provides 'libgawkextlib', which is used by various
gawk extension modules -- for example gawk-xml, gawk-pgsql, and more.

%package devel
Summary:          Header files and libraries for gawkextlib development
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         gawk-devel
%description devel
The %{name}-devel package contains the header files and libraries
needed to develop gawk extension modules that use %{name} facilities.

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
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gawkextlib-devel -f %{oreon_filedir}/gawkextlib-devel.list

%changelog

%autochangelog
