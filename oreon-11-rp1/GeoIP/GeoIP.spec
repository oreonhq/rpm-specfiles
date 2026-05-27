%global source0_hash 1dfb748003c5e4b7fd56ba8c4cd786633d5d6f409547584f6910398389636f80

# Tests require network access so fail in koji; build using --with tests to run them yourself
%bcond_with tests

Name:		GeoIP
Version:	1.6.12
Release:	23%{?dist}
Summary:	Library for country/city/organization to IP address or hostname mapping
# Note: bundled GeoIP.dat data is CC-BY-SA-3.0 but we don't use or package it
License:	LGPL-2.1-or-later
URL:		http://www.maxmind.com/app/c
Source0:	https://github.com/maxmind/geoip-api-c/releases/download/v%{version}/GeoIP-%{version}.tar.gz
BuildRequires:	coreutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	sed
BuildRequires:	zlib-devel
Requires:	GeoIP-data

# For compatibility with original release of GeoIP in old distributions
%if 0%{?fedora} < 22 && 0%{?rhel} < 8
Requires:	geoipupdate
%endif

# Old name of GeoIP library package
Obsoletes:	geoip < %{version}-%{release}
Provides:	geoip = %{version}-%{release}

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

%build
%configure --disable-static --disable-dependency-tracking

# Kill bogus rpaths
sed -i -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
	-e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} INSTALL="install -p" install

# nix the stuff we don't need like .la files.
rm -f %{buildroot}%{_libdir}/*.la

%check
# Tests require network access so fail in koji; build using --with tests to run them yourself
%{?with_tests:LD_LIBRARY_PATH=%{buildroot}%{_libdir} make check}

%ldconfig_scriptlets

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog NEWS.md README.md
%{_bindir}/geoiplookup
%{_bindir}/geoiplookup6
%{_libdir}/libGeoIP.so.1
%{_libdir}/libGeoIP.so.1.*
%{_mandir}/man1/geoiplookup.1*
%{_mandir}/man1/geoiplookup6.1*

%files devel
%{_includedir}/GeoIP.h
%{_includedir}/GeoIPCity.h
%{_libdir}/libGeoIP.so
%{_libdir}/pkgconfig/geoip.pc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.12-23
- Prepare for Oreon 11 (RP1)
