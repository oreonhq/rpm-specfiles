%global source0_hash 6863540b173804e5b99cb2c1b14e600170ce9af0b462fcad41584c316d19a310

### supports following defines during RPM build:
#
### specific git commit on upstream (EXAMPLE)
## build SRPMS
# fedpkg srpm --define "gitcommit 8046fa240a35be86e5c3500abf897bf42cb59037" -- --undefine=_disable_source_fetch
#
## build RPMS local
# fedpkg local --define "gitcommit 8046fa240a35be86e5c3500abf897bf42cb59037" -- --undefine=_disable_source_fetch
#
## rebuild SRPMS on a different system using
# rpmbuild --rebuild -D "gitcommit 8046fa240a35be86e5c3500abf897bf42cb59037" ipv6calc-<VERSION>-<RELEASE>.YYYYMMDDgitSHORTHASH.DIST.src.rpm

%if 0%{?gitcommit:1}
%global shortcommit %(c=%{gitcommit}; echo ${c:0:7})
%define build_timestamp %(date +"%Y%m%d")
%global gittag .%{build_timestamp}git%{shortcommit}
%endif

# shared library support (deselectable)
%if "%{?_without_shared:0}%{?!_without_shared:1}" == "1"
%define enable_shared 1
%endif

Summary:	IPv6/IPv4 address information, format change, filter and calculation utility
Name:		ipv6calc
Version:	4.4.0
Release:	2%{?gittag}%{?dist}
URL:		https://www.deepspace6.net/projects/%{name}.html
License:	GPL-2.0-only
%if 0%{?gitcommit:1}
Source:		https://github.com/pbiering/%{name}/archive/%{gitcommit}/%{name}-%{gitcommit}.tar.gz
%else
Source:		https://github.com/pbiering/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:		ipv6calc-4.4.0-9b6aebd3.patch
%endif
BuildRequires:	automake make
BuildRequires:	gcc
BuildRequires:	openssl-devel
BuildRequires:	perl-generators
BuildRequires:	perl(Digest::MD5), perl(Digest::SHA), perl(URI::Escape)
BuildRequires:	perl(strict), perl(warnings)
BuildRequires:	procps-ng
Requires:	unzip
Requires:	perl-BerkeleyDB perl-Net-IP
%if %{enable_shared}
Provides:	ipv6calc-libs = %{version}-%{release}
%else
Conflicts:	ipv6calc-libs
%endif

# mod_ipv6calc related
%{!?_httpd_apxs:    %{expand: %%global _httpd_apxs    %%{_sbindir}/apxs}}
%{!?_httpd_moddir:  %{expand: %%global _httpd_moddir  %%{_libdir}/httpd/modules}}
%{!?_httpd_confdir: %{expand: %%global _httpd_confdir %%{_sysconfdir}/httpd/conf.d}}

# database support (deselectable)
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

# database locations
%define ip2location_db	%{_datadir}/IP2Location
%define geoip_db	%{_datadir}/GeoIP
%define dbip_db		%{_datadir}/DBIP
%define external_db	%{_datadir}/%{name}/db

# Berkeley DB selector
%define require_db4 %(echo "%{dist}" | grep -Eq '^\.el(5|6)$' && echo 1 || echo 0)
%if %{require_db4}
BuildRequires: db4-devel
Requires:      db4
%else
BuildRequires: libdb-devel
Requires:      libdb
%endif

%if %{enable_mmdb}
BuildRequires: libmaxminddb-devel
Recommends:    libmaxminddb

%if 0%{?fedora} >= 39
BuildRequires: geolite2-country
BuildRequires: geolite2-city
BuildRequires: geolite2-asn
Recommends:    geolite2-country
Recommends:    geolite2-city
Recommends:    geolite2-asn
%endif

%if 0%{?rhel} >= 8
BuildRequires: geolite2-country
BuildRequires: geolite2-city
Recommends:    geolite2-country
Recommends:    geolite2-city
%endif

%endif

%if %{enable_ip2location}
BuildRequires: IP2Location-devel >= 8.6.0
Recommends:    IP2Location       >= 8.6.0
%endif

# RPM license macro detector
%define rpm_license_extra %(echo "%{_defaultlicensedir}" | grep -q defaultlicensedir && echo 0 || echo 1)

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

## Install examples and helper files
install -d -p %{buildroot}%{_docdir}/%{name}-%{version}

## examples
install -d %{buildroot}%{_datadir}/%{name}/examples

# ipv6logconv
install -d %{buildroot}%{_datadir}/%{name}/examples/ipv6logconv
for file in examples/analog/*.{cfg,txt,tab,sh}; do
	install $file %{buildroot}%{_datadir}/%{name}/examples/ipv6logconv/
done

# ipv6loganon
install -d %{buildroot}%{_datadir}/%{name}/examples/ipv6loganon
for file in ipv6loganon/README; do
	install $file %{buildroot}%{_datadir}/%{name}/examples/ipv6loganon/
done

# ipv6logstats
install -d %{buildroot}%{_datadir}/%{name}/examples/ipv6logstats
for file in ipv6logstats/README ipv6logstats/example_* ipv6logstats/collect_ipv6logstats.pl; do
	install $file %{buildroot}%{_datadir}/%{name}/examples/ipv6logstats/
done

# db directory
install -d %{buildroot}%{external_db}
install -d %{buildroot}%{external_db}/lisp
install -m 644 databases/registries/lisp/site-db %{buildroot}%{external_db}/lisp/

# selinux
install -d %{buildroot}%{_datadir}/%{name}/selinux

# ipv6calcweb
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}%{_localstatedir}/www/ipv6calcweb/cgi-bin

install ipv6calcweb/ipv6calcweb.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -m 755 ipv6calcweb/ipv6calcweb.cgi %{buildroot}%{_localstatedir}/www/ipv6calcweb/cgi-bin/
install -m 644 ipv6calcweb/ipv6calcweb-databases-in-var.te %{buildroot}%{_datadir}/%{name}/selinux/

%if %{enable_mod_ipv6calc}
# mod_ipv6calc
install -d %{buildroot}%{_sysconfdir}/httpd/conf.d
install -d %{buildroot}%{_localstatedir}/www/ipv6calc/cgi-bin
install mod_ipv6calc/ipv6calc.conf %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -m 755 mod_ipv6calc/ipv6calc.cgi %{buildroot}%{_localstatedir}/www/ipv6calc/cgi-bin/
%endif

%clean
rm -rf %{buildroot}

%check
%ifnarch ppc64
	make test
%endif

%files
%if %{rpm_license_extra}
%doc ChangeLog README README.* CREDITS TODO USAGE doc/ipv6calc.lyx doc/ipv6calc.html doc/ipv6calc.xml
%license COPYING LICENSE
%else
%doc ChangeLog README README.* CREDITS TODO USAGE doc/ipv6calc.lyx doc/ipv6calc.html doc/ipv6calc.xml COPYING LICENSE
%endif

%defattr(644,root,root,755)

# binaries
%attr(755,-,-) %{_bindir}/*

# man pages
%{_mandir}/man8/*

# tools
%attr(755,-,-) %{_datadir}/%{name}/tools/*

# selinux
%attr(644,-,-) %{_datadir}/%{name}/selinux/*

# shared library
%{?enable_shared:%attr(755,-,-) %{_libdir}/libipv6calc*}

# database directory
%{external_db}

# examples
%attr(755,-,-) %{_datadir}/%{name}/examples/*/*.pl
%attr(755,-,-) %{_datadir}/%{name}/examples/*/*.sh
%{_datadir}/%{name}/examples/ipv6loganon/
%{_datadir}/%{name}/examples/ipv6logconv/
%{_datadir}/%{name}/examples/ipv6logstats/

%files ipv6calcweb
%if %{rpm_license_extra}
%doc ipv6calcweb/README ipv6calcweb/USAGE
%license COPYING LICENSE
%else
%doc ipv6calcweb/README ipv6calcweb/USAGE COPYING LICENSE
%endif

%defattr(644,root,root,755)

%attr(755,-,-) %{_localstatedir}/www/ipv6calcweb/cgi-bin/ipv6calcweb.cgi
%config(noreplace) %{_sysconfdir}/httpd/conf.d/ipv6calcweb.conf

%files mod_ipv6calc
%if %{rpm_license_extra}
%doc mod_ipv6calc/README.md
%license COPYING LICENSE
%else
%doc mod_ipv6calc/README.md COPYING LICENSE
%endif

%defattr(644,root,root,755)

%config(noreplace) %{_httpd_confdir}/ipv6calc.conf
%attr(755,-,-) %{_httpd_moddir}/mod_ipv6calc.so

%attr(755,-,-) %{_localstatedir}/www/ipv6calc/cgi-bin/ipv6calc.cgi

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

%changelog
%autochangelog
