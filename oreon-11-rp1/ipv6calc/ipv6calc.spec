%global source0_hash 6863540b173804e5b99cb2c1b14e600170ce9af0b462fcad41584c316d19a310
%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif
%if "%{?_without_shared:0}%{?!_without_shared:1}" == "1"
%define enable_shared 1
%endif
Summary:        IPv6/IPv4 address information, format change, filter and calculation utility
Name:		ipv6calc
Version:	4.4.0
Release:        1%{?dist}
URL:		https://www.deepspace6.net/projects/%{name}.html
License:	GPL-2.0-only
%if 0%{?gitcommit:1}
Source0:        https://github.com/pbiering/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Patch:		ipv6calc-4.4.0-9b6aebd3.patch
%endif
Requires:	unzip
Requires:	perl-BerkeleyDB perl-Net-IP
%if %{enable_shared}
Provides:	ipv6calc-libs = %{version}-%{release}
%else
Conflicts:	ipv6calc-libs
%endif
%{!?_httpd_apxs:    %{expand: %%global _httpd_apxs    %%{_sbindir}/apxs}}
%{!?_httpd_moddir:  %{expand: %%global _httpd_moddir  %%{_libdir}/httpd/modules}}
%{!?_httpd_confdir: %{expand: %%global _httpd_confdir %%{_sysconfdir}/httpd/conf.d}}
%if "%{?_without_ip2location:0}%{?!_without_ip2location:1}" == "1"
%define enable_ip2location 1
%endif
%if "%{?_without_mmdb:0}%{?!_without_mmdb:1}" == "1"
%define enable_mmdb 1
%endif
%if "%{?_without_external:0}%{?!_without_external:1}" == "1"
%define enable_external 1
%endif
%if "%{?_without_mod_ipv6calc:0}%{?!_without_mod_ipv6calc:1}" == "1"
%define enable_mod_ipv6calc 1
%endif
%define ip2location_db	%{_datadir}/IP2Location
%define geoip_db	%{_datadir}/GeoIP
%define dbip_db		%{_datadir}/DBIP
%define external_db	%{_datadir}/%{name}/db
%define require_db4 %(echo "%{dist}" | grep -Eq '^\.el(5|6)$' && echo 1 || echo 0)
%if %{require_db4}
Requires:      db4
%else
Requires:      libdb
%endif
%if %{enable_mmdb}
Recommends:    libmaxminddb
%endif
%if %{enable_ip2location}
Recommends:    IP2Location       >= 8.6.0
%endif
%define rpm_license_extra %(echo "%{_defaultlicensedir}" | grep -q defaultlicensedir && echo 0 || echo 1)
# oreon:deps
BuildRequires:  IP2Location-devel
BuildRequires:  automake
BuildRequires:  curl
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  libdb-devel
BuildRequires:  libmaxminddb-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Digest::SHA1)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  procps-ng
BuildRequires:  psmisc
# /oreon:deps
%description
ipv6calc is a small utility which formats and calculates IPv4/IPv6 addresses
in different ways.

Install this package, if you want to retrieve information about a particular
IPv4/IPv6/MAC address (-i ADDRESS) or make life easier in adding entries to
reverse IPv6 DNS zones (e.g. -a 2001:db8:1234::1/48).

In addition many format and type conversions are supported, see online help
and/or given URL for more.

Also this package contains additional programs
 - ipv6loganon: anonymize Apache web server logs
 - ipv6logconv: special Apache web server log converter
    (examples included for use with analog)
 - ipv6logstats: create statistics from list of IPv4/IPv6 addresses
    (examples included for use with gnu-plot)
 - mod_ipv6calc: Apache module for anonymization/information logging on-the-fly

Support for following databases
 - IP2Location(BIN)  %{?enable_ip2location:ENABLED}%{?!enable_ip2location:DISABLED}
		     default directory for downloaded db files: %{ip2location_db}
		     (requires also external library on system)

 - IP2Location(MMDB) %{?enable_mmdb:ENABLED}%{?!enable_mmdb:DISABLED}
		     default directory for downloaded db files: %{ip2location_db}
		     (requires also external library on system)

 - GeoIP(MMDB)	     %{?enable_mmdb:ENABLED}%{?!enable_mmdb:DISABLED}
		     default directory for downloaded db files: %{geoip_db}
		     (requires also external library on system)

 - db-ip.com(MMDB)   %{?enable_mmdb:ENABLED}%{?!enable_mmdb:DISABLED}
		     (once generated database files are found on system)
		     default directory for generated db files: %{dbip_db}

 - External	     %{?enable_external:ENABLED}%{?!enable_external:DISABLED}
		     default directory for generated db files: %{external_db}

Built %{?enable_shared:WITH}%{?!enable_shared:WITHOUT} shared-library

Available rpmbuild rebuild options:
  --without ip2location : disables IP2Location(BIN)
  --without mmdb : disables GeoIP, db-ip.com, IP2Location(MMDB)
  --without external
  --without shared
  --without mod_ipv6calc

%package ipv6calcweb
Summary:	IP address information web utility
Requires:	ipv6calc httpd
Requires:	perl(URI) perl(Digest::SHA1) perl(Digest::MD5) perl(HTML::Entities)
BuildRequires:	perl(URI) perl(Digest::SHA1) perl(Digest::MD5) perl(HTML::Entities)
%description ipv6calcweb
ipv6calcweb contains a CGI program and a configuration file for
displaying information of IP addresses on a web page using ipv6calc.

Check/adjust %{_sysconfdir}/httpd/conf.d/ipv6calcweb.conf
Default restricts access to localhost

%if %{enable_mod_ipv6calc}
%package mod_ipv6calc
Summary:	Apache module for ipv6calc
BuildRequires:	httpd-devel psmisc curl
Requires:	httpd >= 2.4.0
Requires:	httpd <= 2.4.99999
Requires:	ipv6calc = %{version}-%{release}
%if %{enable_shared}
Requires:	ipv6calc-libs = %{version}-%{release}
%endif
%description mod_ipv6calc
mod_ipv6calc contains an Apache module and a default configuration
file.

Features:
 - store anonymized IPv4/v6 address in environment variable
 - store CountryCode of IPv4/v6 address in environment variable
(environment variables can be used for custom log format)

Check/adjust %{_sysconfdir}/httpd/conf.d/ipv6calc.conf
By default the module is disabled.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup %{?gitcommit:-n %{name}-%{gitcommit}} -p1

autoreconf

%build

%configure \
	%{?enable_ip2location:--enable-ip2location} \
	%{?enable_ip2location:--with-ip2location-dynamic} \
	--with-ip2location-db=%{ip2location_db} \
	--with-geoip-db=%{geoip_db} \
	--with-dbip-db=%{dbip_db} \
	%{?enable_mmdb:--enable-mmdb --with-mmdb-dynamic} \
	%{?enable_external:--enable-external} \
	--with-external-db=%{external_db} \
	%{?enable_shared:--enable-shared} \
	%{?enable_mod_ipv6calc:--enable-mod_ipv6calc}
make clean
make %{?_smp_mflags} COPTS="$RPM_OPT_FLAGS"
%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -p %{buildroot}%{_docdir}/%{name}-%{version}
install -d %{buildroot}%{_datadir}/%{name}/examples
install -d %{buildroot}%{_datadir}/%{name}/examples/ipv6logconv
for file in examples/analog/*.{cfg,txt,tab,sh}; do
	install $file %{buildroot}%{_datadir}/%{name}/examples/ipv6logconv/
done
install -d %{buildroot}%{_datadir}/%{name}/examples/ipv6loganon
for file in ipv6loganon/README; do
	install $file %{buildroot}%{_datadir}/%{name}/examples/ipv6loganon/
done
install -d %{buildroot}%{_datadir}/%{name}/examples/ipv6logstats
for file in ipv6logstats/README ipv6logstats/example_* ipv6logstats/collect_ipv6logstats.pl; do
	install $file %{buildroot}%{_datadir}/%{name}/examples/ipv6logstats/
done
install -d %{buildroot}%{external_db}
install -d %{buildroot}%{external_db}/lisp
install -m 644 databases/registries/lisp/site-db %{buildroot}%{external_db}/lisp/
install -d %{buildroot}%{_datadir}/%{name}/selinux
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}%{_localstatedir}/www/ipv6calcweb/cgi-bin
install ipv6calcweb/ipv6calcweb.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -m 755 ipv6calcweb/ipv6calcweb.cgi %{buildroot}%{_localstatedir}/www/ipv6calcweb/cgi-bin/
install -m 644 ipv6calcweb/ipv6calcweb-databases-in-var.te %{buildroot}%{_datadir}/%{name}/selinux/
%if %{enable_mod_ipv6calc}
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}%{_localstatedir}/www/ipv6calc/cgi-bin
install mod_ipv6calc/ipv6calc.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -m 755 mod_ipv6calc/ipv6calc.cgi %{buildroot}%{_localstatedir}/www/ipv6calc/cgi-bin/
%endif
%clean
rm -rf %{buildroot}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%ifnarch ppc64
	make test
%endif
%post

if [ -x /usr/sbin/ldconfig ]; then
	/usr/sbin/ldconfig
elif [ -x /sbin/ldconfig ]; then
	/sbin/ldconfig
fi
%postun

if [ -x /usr/sbin/ldconfig ]; then
	/usr/sbin/ldconfig
elif [ -x /sbin/ldconfig ]; then
	/sbin/ldconfig
fi
%files -f %{oreon_filedir}/main.list
%files -n ipv6calc-ipv6calcweb -f %{oreon_filedir}/ipv6calc-ipv6calcweb.list
%files -n ipv6calc-mod_ipv6calc -f %{oreon_filedir}/ipv6calc-mod_ipv6calc.list

%changelog

%autochangelog
