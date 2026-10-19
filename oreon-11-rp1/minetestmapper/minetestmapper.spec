%global source0_hash ea17fc113f44b13b85916c44f3fb98ecd8257236842eb12fac70927c6f9c6b07
%global         forgeurl https://github.com/minetest/minetestmapper
%global         tag      20260808
Version:        %{tag}
%forgemeta
Name:           minetestmapper
Release:        1%{?dist}
Summary:        Generates a overview image of a minetest map
License:        BSD-2-Clause
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
Suggests:       minetest
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(hiredis)
BuildRequires:  pkgconfig(leveldb)
BuildRequires:  pkgconfig(libpq)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
Generates a overview image of a minetest map. This is a port of
minetestmapper.py to C++, that is both faster and provides more
details than the deprecated Python script.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%cmake -DENABLE_LEVELDB=1 -DENABLE_REDIS=1 -DENABLE_POSTGRESQL=1
%cmake_build
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/minetest
cp -a colors.txt %{buildroot}%{_datadir}/minetest/
rm -rf %{buildroot}%{_pkgdocdir}/COPYING
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
