%global source0_hash 1dfb748003c5e4b7fd56ba8c4cd786633d5d6f409547584f6910398389636f80
%bcond_with tests
Name:		GeoIP
Version:	1.6.12
Release:        23%{?dist}
Summary:        Library for country/city/organization to IP address or hostname mapping
License:	LGPL-2.1-or-later
URL:		http://www.maxmind.com/app/c
Source0:        https://github.com/maxmind/geoip-api-c/releases/download/v%{version}/GeoIP-%{version}.tar.gz
Requires:	GeoIP-data
%if 0%{?fedora} < 22 && 0%{?rhel} < 8 && 0%{?oreon} < 11
Requires:	geoipupdate
%endif
Obsoletes:	geoip < %{version}-%{release}
Provides:	geoip = %{version}-%{release}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed
BuildRequires:  zlib-devel
# /oreon:deps
%description
GeoIP is a C library that enables the user to find the country that any IP
address or hostname originates from.

It uses file based databases that can optionally be updated on a weekly basis
by installing the geoipupdate-cron (IPv4) and/or geoipupdate-cron6 (IPv6)
packages.

%package devel
Summary:	Development headers and libraries for GeoIP
Requires:	%{name} = %{version}-%{release}
Provides:	geoip-devel = %{version}-%{release}
Obsoletes:	geoip-devel < %{version}-%{release}
%description devel
Development headers and static libraries for building GeoIP-based applications.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

%configure --disable-static --disable-dependency-tracking
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} INSTALL="install -p" install
rm -f %{buildroot}%{_libdir}/*.la
%oreon_autofiles GeoIP-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{?with_tests:LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check}
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n GeoIP-devel -f %{oreon_filedir}/GeoIP-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.12-23
- Prepare for Oreon 11 (RP1)
