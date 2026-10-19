%global source0_hash 0c196016c281f685cb428011d4703360bca8a805f4efa777eb1bd29c8295d196
%global upstream_tag    8.7.0
%global rpm_version     8.7.0
%global soname 3
%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%global build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif
Name:		IP2Location
Summary:        Tools for mapping IP address to geolocation information
Version:	%{rpm_version}
Release:        3%{?dist}
License:	MIT
URL:		https://www.ip2location.com/
%if 0%{?gitcommit:1}
Source0:        https://github.com/chrislim2888/%{name}-C-Library/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        https://github.com/chrislim2888/%{name}-C-Library/archive/%{version}/%{name}-%{version}.tar.gz
%endif
Obsoletes:	libip2location < %{version}
Provides:	libip2location = %{version}
Requires:	%{name}-libs%{_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl-generators
# /oreon:deps
%description
ip2location command enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation and usage type from any IP
address or hostname. This library has been optimized for speed and memory
utilization. The library contains API to query all IP2Location LITE and
commercial binary databases.

Users can download the latest LITE database from IP2Location web site using e.g.
the included downloader.

%package 	libs
Summary:	C library for mapping IP address to geolocation information
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Recommends:	%{name}%{_isa} = %{version}-%{release}
%endif
%description libs
IP2Location C library enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation and usage type from any IP
address or hostname. This library has been optimized for speed and memory
utilization. The library contains API to query all IP2Location LITE and
commercial binary databases.

%package 	devel
Summary:	Development files for the IP2Location library
Requires:	%{name}%{_isa} = %{version}-%{release}
Obsoletes:	libip2location-devel < %{version}
Provides:	libip2location-devel = %{version}
%description 	devel
IP2Location C library enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation and usage type from any IP
address or hostname. This library has been optimized for speed and memory
utilization. The library contains API to query all IP2Location LITE and
commercial binary databases.

This package contains the development files for the IP2Location library.

%package 	data-sample
Summary:	Sample data files for the IP2Location library
Requires:	%{name} = %{version}-%{release}
Obsoletes:	ip2location-country < %{version}
Provides:	ip2location-country = %{version}
%description 	data-sample
IP2Location C library enables the user to get the country, region, city,
coordinates, ZIP code, time zone, ISP, domain name, connection type,
area code, weather info, mobile carrier, elevation, usage type, address
type and category from any IP address or hostname.
This library has been optimized for speed and memory utilization. The library
contains API to query all IP2Location LITE and commercial binary databases.

This package contains the sample data files for testing the library.

Latest lite databases can be downloaded from
	https://lite.ip2location.com

Further sample databases can be downloaded from
	https://www.ip2location.com/development-libraries/ip2location/c

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?gitcommit:1}
%setup -q -n IP2Location-C-Library-%{gitcommit}
%else
%setup -q -n IP2Location-C-Library-%{upstream_tag}
%endif

# remove a warning option which break configure on older gcc versions
# (at least gcc version 4.1.2 20080704)
perl -pi -e 's/-Wno-unused-result//' configure.ac

%build

autoreconf -fiv
%configure --disable-static
%make_build COPTS="$RPM_OPT_FLAGS"
make -C data convert
%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH make check
%install
%make_install
rm -f %{buildroot}%{_libdir}/*.*a
install -d %{buildroot}%{_datadir}/%{name}/tools
install -pm 0755 tools/download.pl %{buildroot}%{_datadir}/%{name}/tools
install -d %{buildroot}%{_datadir}/%{name}/
install -p data/IP-COUNTRY.BIN %{buildroot}%{_datadir}/%{name}/IP-COUNTRY-SAMPLE.BIN
install -p data/IPV6-COUNTRY.BIN %{buildroot}%{_datadir}/%{name}/IPV6-COUNTRY.SAMPLE.BIN
%oreon_autofiles IP2Location-libs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles IP2Location-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles IP2Location-data-sample usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n IP2Location-libs -f %{oreon_filedir}/IP2Location-libs.list
%files -n IP2Location-devel -f %{oreon_filedir}/IP2Location-devel.list
%files -n IP2Location-data-sample -f %{oreon_filedir}/IP2Location-data-sample.list

%changelog

%autochangelog
