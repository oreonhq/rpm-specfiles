%global source0_hash 7422009cc9494a3d219a7b9dfc583029479df9d95741f119639ce2e405e3a8f9
%global with_xrootd %{!?_without_xrootd:1}%{?_without_xrootd:0}
%global with_pylint 0
%global with_s3 1
%global with_gfal 1
%global with_xmlsec1 %{!?_without_xmlsec1:1}%{?_without_xmlsec1:0}
%global with_ldns 1
%global with_ldap_service 1
%global pkgdir arc
%global _bashcompdir %(pkg-config --variable=completionsdir bash-completion 2>/dev/null || echo %{_sysconfdir}/bash_completion.d)
Name:		nordugrid-arc
Version:	7.1.1
Release:        1%{?dist}
Summary:        Advanced Resource Connector Middleware
License:	Apache-2.0 AND MIT
URL:		https://www.nordugrid.org/
Source0:        https://download.nordugrid.org/packages/%{name}/releases/%{version}/src/%{name}-%{version}.tar.gz
Patch0:		0001-Handle-Python-multi-phase-initialization-support-in-.patch
Patch1:		0001-Fix-compilation-with-Python-3.15.patch
Obsoletes:	%{name}-arcproxyalt < 6.0.0
Obsoletes:	%{name}-java < 6.0.0
Obsoletes:	%{name}-egiis < 6.0.0
Obsoletes:	%{name}-acix-cache < 6.0.0
Obsoletes:	%{name}-acix-core < 7.0.0
Obsoletes:	%{name}-acix-scanner < 7.0.0
Obsoletes:	%{name}-acix-index < 7.0.0
Obsoletes:	%{name}-arex-python-lrms < 7.0.0
Obsoletes:	%{name}-gridftpd < 7.0.0
Obsoletes:	python2-%{name} < 7.0.0
Obsoletes:	%{name}-nordugridmap < 7.0.0
Obsoletes:	%{name}-gridmap-utils < 6.0.0
Obsoletes:	%{name}-plugins-gridftpjob < 7.0.0
Obsoletes:	%{name}-plugins-ldap < 7.0.0
%if ! %{with_ldap_service}
Obsoletes:	%{name}-infosys-ldap < %{version}-%{release}
Obsoletes:	%{name}-ldap-infosys < 6.0.0
Obsoletes:	%{name}-aris < 6.0.0
%endif
%if ! %{with_gfal}
Obsoletes:	%{name}-plugins-gfal < %{version}-%{release}
%endif
%if %{with_xmlsec1}
%endif
%if %{with_xrootd}
%endif
Requires:	hostname
Requires:	openssl
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gfal2-devel
BuildRequires:  glibmm24-devel
BuildRequires:  globus-common-devel
BuildRequires:  globus-ftp-client-devel
BuildRequires:  globus-ftp-control-devel
BuildRequires:  globus-gssapi-gsi-devel
BuildRequires:  help2man
BuildRequires:  ldns-devel
BuildRequires:  libs3-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  nss-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  perl(DBI)
BuildRequires:  perl(English)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  sqlite-devel
BuildRequires:  swig
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlsec1-devel
BuildRequires:  xmlsec1-openssl-devel
BuildRequires:  xrootd-client-devel
# /oreon:deps
%description
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC middleware is a software solution that uses distributed
computing technologies to enable sharing and federation of computing
resources across different administrative and application domains.
ARC is used to create distributed infrastructures of various scope and
complexity, from campus to national and global deployments.

%package client
Summary:	ARC command line clients
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
%description client
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This client package contains all the CLI tools that are needed to
operate with x509 proxies, submit and manage jobs and handle data
transfers.

%package hed
Summary:	ARC Hosting Environment Daemon
Requires:	%{name} = %{version}-%{release}
%{?systemd_requires}
%description hed
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC Hosting Environment Daemon (HED) is a Web Service container
for ARC services.

%package datadelivery-service
Summary:	ARC data delivery service
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-hed = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
Requires:	%{name}-arcctl-service = %{version}-%{release}
Requires:	logrotate
%{?systemd_requires}
%description datadelivery-service
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC data delivery service.

%package infosys-ldap
Summary:	ARC LDAP-based information services
BuildArch:	noarch
Requires:	openldap-servers
Requires:	bdii
Requires:	glue-schema >= 2.0.10
Requires:	%{name}-arcctl-service = %{version}-%{release}
Requires:	logrotate
Provides:	%{name}-ldap-infosys = %{version}-%{release}
Obsoletes:	%{name}-ldap-infosys < 6.0.0
Provides:	%{name}-aris = %{version}-%{release}
Obsoletes:	%{name}-aris < 6.0.0
%{?systemd_requires}
Requires(post):		policycoreutils-python-utils
Requires(postun):	policycoreutils-python-utils
%description infosys-ldap
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC information services relying on BDII and
LDAP technologies to publish ARC CE information according to various
LDAP schemas. Please note that the information collectors are part of
another package, the nordugrid-arc-arex.

%package monitor
Summary:	ARC LDAP monitor web application
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
Requires:	php
Requires:	php-gd
Requires:	php-ldap
Obsoletes:	%{name}-ldap-monitor < 6.0.0
Obsoletes:	%{name}-ws-monitor < 6.0.0
%description monitor
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the PHP web application that is used to set up a
web-based monitor which pulls information from the LDAP information
system and visualizes it.

%package arcctl
Summary:	ARC Control Tool
Requires:	%{name} = %{version}-%{release}
Requires:	python3-jwcrypto
%description arcctl
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC Control Tool with basic set of control
modules suitable for both server and client side.

%package arcctl-service
Summary:	ARC Control Tool - service control modules
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-arcctl = %{version}-%{release}
%description arcctl-service
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the service control modules for ARC Contol Tool
that allow working with server-side config and manage ARC services.

%package arex
Summary:	ARC Resource-coupled EXecution service
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-hed = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
Requires:	%{name}-arcctl = %{version}-%{release}
Requires:	%{name}-arcctl-service = %{version}-%{release}
Requires:	logrotate
Requires:	findutils
Requires:	procps
Provides:	%{name}-cache-service = %{version}-%{release}
Obsoletes:	%{name}-cache-service < 6.0.0
Provides:	%{name}-candypond = %{version}-%{release}
Obsoletes:	%{name}-candypond < 6.0.0
Requires(post):		%{name}-arcctl = %{version}-%{release}
Requires(preun):	%{name}-arcctl = %{version}-%{release}
Requires(post):		hostname
Requires(post):		openssl
%{?systemd_requires}
%description arex
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC Resource-coupled EXecution service (AREX) is the Computing
Element of the ARC middleware. AREX offers a full-featured middle
layer to manage computational tasks including interfacing to local
batch systems, taking care of complex environments such as data
staging, data caching, software environment provisioning, information
collection and exposure, accounting information gathering and
publishing.

%package arex-lrms-contrib
Summary:	ARC Resource-coupled EXecution service - contributed LRMS backends
BuildArch:	noarch
Requires:	%{name}-arex = %{version}-%{release}
Obsoletes:	%{name}-arex < 7.0.0
%description arex-lrms-contrib
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The AREX contributed LRMS backends package contains additional LRMS
support script contributed by the ARC user community.

%package community-rtes
Summary:	ARC community defined RTEs support
Requires:	%{name}-arex = %{version}-%{release}
Requires:	%{name}-arcctl = %{version}-%{release}
Requires:	gnupg2
Requires:	python3-dns
%description community-rtes
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

Community RTEs is the framework that allows deploying software packages
(tarballs, containers, etc) provided by trusted communities to ARC CE
using simple arcctl commands.
It is released as a technology preview.

%package plugins-needed
Summary:	ARC base plugins
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-plugins-arcrest = %{version}-%{release}
Obsoletes:	%{name}-plugins-arcrest < 7.0.0
%description plugins-needed
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC base plugins. This includes the Message Chain Components (MCCs)
and Data Manager Components (DMCs).

%package plugins-globus
Summary:	ARC Globus plugins (compat)
Requires:	%{name}-plugins-gridftp = %{version}-%{release}
Requires:	%{name}-plugins-lcas-lcmaps = %{version}-%{release}
%description plugins-globus
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC Globus plugins. This compat metapackage brings all Globus
dependent plugins at once, including: Data Manager Components (DMCs)
and LCAS/LCMAPS tools.

This package is meant to allow smooth transition and will be removed from
the upcoming releases.

%package plugins-globus-common
Summary:	ARC Globus plugins common libraries
Requires:	%{name} = %{version}-%{release}
%description plugins-globus-common
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC Globus plugins common libraries package includes the bundle of
necessary Globus libraries needed for all other globus-dependent ARC
components.

%package plugins-gridftp
Summary:	ARC Globus dependent DMCs
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-globus-common = %{version}-%{release}
%description plugins-gridftp
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC Globus GridFTP plugins. These allow access to data through the
gridftp protocol.

%package plugins-lcas-lcmaps
Summary:	ARC LCAS/LCMAPS plugins
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-globus-common = %{version}-%{release}
Requires:	globus-gssapi-gsi >= 12.2
%description plugins-lcas-lcmaps
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC LCAS/LCMAPS tools allow configuring ARC CE to use LCAS/LCMAPS
services for authorization and mapping.

%if %{with_xrootd}
%package plugins-xrootd
Summary:	ARC xrootd plugins
Requires:	%{name} = %{version}-%{release}
%description plugins-xrootd
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC xrootd plugins. These allow access to data through the xrootd
protocol.
%endif

%package plugins-gfal
Summary:	ARC GFAL2 plugins
Requires:	%{name} = %{version}-%{release}
%description plugins-gfal
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC plugins for GFAL2. This allows third-party transfer and adds
support for several extra transfer protocols (rfio, dcap, gsidcap).
Support for specific protocols is provided by separate 3rd-party GFAL2
plugin packages.

%package plugins-s3
Summary:	ARC S3 plugins
Requires:	%{name} = %{version}-%{release}
%description plugins-s3
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC plugins for S3. These allow access to data through the S3
protocol.

%package plugins-internal
Summary:	ARC internal plugin
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-arex = %{version}-%{release}
%description plugins-internal
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

The ARC internal plugin. A special interface aimed for restrictive HPC
sites, to be used with a local installation of the ARC Control Tower.

%package plugins-python
Summary:	ARC Python dependent plugin
Requires:	%{name} = %{version}-%{release}
Requires:	python%{python3_pkgversion}-%{name} = %{version}-%{release}
%description plugins-python
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

ARC plugins dependent on Python.

%package devel
Summary:	ARC development files
Requires:	%{name} = %{version}-%{release}
Requires:	glibmm24-devel
Requires:	libxml2-devel
Requires:	openssl-devel
%description devel
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

Header files and libraries needed to develop applications using ARC.

%package -n python%{python3_pkgversion}-%{name}
Summary:	ARC Python 3 wrapper
%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Requires:	%{name} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

Python 3 bindings for ARC.

%package test-utils
Summary:	ARC test tools
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-plugins-needed = %{version}-%{release}
Obsoletes:	%{name}-misc-utils < 6.0.0
%description test-utils
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains a few utilities useful to test various ARC
subsystems. The package is not required by users or sysadmins and it
is mainly for developers.

%package archery-manage
Summary:	ARCHERY administration tool
BuildArch:	noarch
Requires:	python3-dns
Requires:	python3-ldap
%description archery-manage
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the archery-manage utility for administration of
an ARCHERY DNS-embedded service endpoint registry.

%package wn
Summary:	ARC optional worker nodes components
%description wn
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the optional components that provide new job
management features on the worker nodes (WN).

%package -n python%{python3_pkgversion}-arcrest
Summary:	ARC REST client
%{?python_provide:%python_provide python%{python3_pkgversion}-arcrest}
BuildArch:	noarch
%description -n python%{python3_pkgversion}-arcrest
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the ARC REST client.

%package arc-exporter
Summary:	ARC Prometheus exporter service
BuildArch:	noarch
Requires:	python3-prometheus_client
%description arc-exporter
NorduGrid is a collaboration aiming at development, maintenance and
support of the middleware, known as the Advanced Resource
Connector (ARC).

This package contains the Prometheus arc-exporter which collects and
publishes metrics about jobs and datastaging on the ARC-CE.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

%build

autoreconf -v -f -i
%configure --disable-static \
     --enable-gfal \
     --enable-s3 \
     --with-python=python3 \
%if ! %{with_pylint}
     --disable-pylint \
%endif
%if ! %{with_xrootd}
     --disable-xrootd \
%endif
%if ! %{with_ldns}
     --disable-ldns \
%endif
     --enable-internal \
     --enable-systemd \
     --with-systemd-units-location=%{_unitdir} \
%if ! %{with_ldap_service}
     --disable-ldap-service \
%endif
     --disable-doc \
     --docdir=%{_pkgdocdir}
%make_build
%check

%make_build check
%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
install -p -m 644 debian/%{name}-arex.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-arex
install -p -m 644 debian/%{name}-infosys-ldap.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-infosys-ldap
install -p -m 644 debian/%{name}-datadelivery-service.logrotate \
    %{buildroot}%{_sysconfdir}/logrotate.d/%{name}-datadelivery-service
find %{buildroot} -type f -name \*.la -exec rm -fv '{}' ';'
find %{buildroot} -name libarcglobusutils.so -exec rm -fv '{}' ';'
rm -f %{buildroot}%{python3_sitelib}/pyarcrest-*.*-info/direct_url.json
mkdir -p %{buildroot}%{_localstatedir}/log/arc
mkdir -p %{buildroot}%{_localstatedir}/spool/arc
mkdir -p %{buildroot}%{_localstatedir}/spool/arc/ssm
mkdir -p %{buildroot}%{_localstatedir}/spool/arc/urs
mkdir -p %{buildroot}%{_sysconfdir}/arc.conf.d
%find_lang %{name}
rm -rf %{buildroot}%{_datadir}/%{pkgdir}/examples
make -C src/libs/data-staging/examples	DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/hed/libs/compute/examples	DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/hed/libs/data/examples	DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/hed/acc/PythonBroker	DESTDIR=$PWD/docdir/python pkgdatadir= install-exampleDATA
make -C python/examples			DESTDIR=$PWD/docdir/devel  pkgdatadir= install-exampleDATA
make -C src/tests/echo			DESTDIR=$PWD/docdir/hed	   pkgdatadir= install-exampleDATA
make -C src/hed				DESTDIR=$PWD/docdir/hed	   pkgdatadir= install-profileDATA
make -C src/clients DESTDIR=%{buildroot} install-exampleDATA
ln -s %{_datadir}/%{pkgdir}/examples/client.conf $PWD/docdir/client.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post hed

%systemd_post arched.service
%preun hed

%systemd_preun arched.service
%postun hed

%systemd_postun_with_restart arched.service
%post arex

%systemd_post arc-arex.service
%systemd_post arc-arex-ws.service
if [ $1 -eq 1 ]; then
  arcctl test-ca init
  arcctl test-ca hostcert
fi
%preun arex

%systemd_preun arc-arex.service
%systemd_preun arc-arex-ws.service
if [ $1 -eq 0 ]; then
  arcctl test-ca cleanup
fi
%postun arex

%systemd_postun_with_restart arc-arex.service
%systemd_postun_with_restart arc-arex-ws.service
%post datadelivery-service

%systemd_post arc-datadelivery-service.service
%preun datadelivery-service

%systemd_preun arc-datadelivery-service.service
%postun datadelivery-service

%systemd_postun_with_restart arc-datadelivery-service.service
%post infosys-ldap

%systemd_post arc-infosys-ldap.service
semanage port -a -t ldap_port_t -p tcp 2135 2>/dev/null || :
semanage fcontext -a -t slapd_etc_t "/var/run/arc/infosys/bdii-slapd\.conf" 2>/dev/null || :
semanage fcontext -a -t slapd_db_t "/var/lib/arc/bdii/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "/var/run/arc/bdii/db(/.*)?" 2>/dev/null || :
%preun infosys-ldap

%systemd_preun arc-infosys-ldap.service
%postun infosys-ldap

%systemd_postun_with_restart arc-infosys-ldap.service
if [ $1 -eq 0 ]; then
  semanage port -d -t ldap_port_t -p tcp 2135 2>/dev/null || :
  semanage fcontext -d -t slapd_etc_t "/var/run/arc/infosys/bdii-slapd\.conf" 2>/dev/null || :
  semanage fcontext -d -t slapd_db_t "/var/lib/arc/bdii/db(/.*)?" 2>/dev/null || :
  semanage fcontext -d -t slapd_var_run_t "/var/run/arc/bdii/db(/.*)?" 2>/dev/null || :
fi
%triggerun infosys-ldap -- bdii

systemctl try-restart arc-infosys-ldap.service > /dev/null 2>&1 || :
%triggerpostun infosys-ldap -- %{name}-ldap-infosys

semanage port -a -t ldap_port_t -p tcp 2135 2>/dev/null || :
semanage fcontext -a -t slapd_etc_t "/var/run/arc/infosys/bdii-slapd\.conf" 2>/dev/null || :
%triggerpostun infosys-ldap -- %{name}-aris

semanage fcontext -a -t slapd_db_t "/var/lib/arc/bdii/db(/.*)?" 2>/dev/null || :
semanage fcontext -a -t slapd_var_run_t "/var/run/arc/bdii/db(/.*)?" 2>/dev/null || :
%files -f %{oreon_filedir}/main.list
%files -n nordugrid-arc-client -f %{oreon_filedir}/nordugrid-arc-client.list
%files -n nordugrid-arc-hed -f %{oreon_filedir}/nordugrid-arc-hed.list
%files -n nordugrid-arc-datadelivery-service -f %{oreon_filedir}/nordugrid-arc-datadelivery-service.list
%files -n nordugrid-arc-infosys-ldap -f %{oreon_filedir}/nordugrid-arc-infosys-ldap.list
%files -n nordugrid-arc-monitor -f %{oreon_filedir}/nordugrid-arc-monitor.list
%files -n nordugrid-arc-arcctl -f %{oreon_filedir}/nordugrid-arc-arcctl.list
%files -n nordugrid-arc-arcctl-service -f %{oreon_filedir}/nordugrid-arc-arcctl-service.list
%files -n nordugrid-arc-arex -f %{oreon_filedir}/nordugrid-arc-arex.list
%files -n nordugrid-arc-arex-lrms-contrib -f %{oreon_filedir}/nordugrid-arc-arex-lrms-contrib.list
%files -n nordugrid-arc-community-rtes -f %{oreon_filedir}/nordugrid-arc-community-rtes.list
%files -n nordugrid-arc-plugins-needed -f %{oreon_filedir}/nordugrid-arc-plugins-needed.list
%files -n nordugrid-arc-plugins-globus -f %{oreon_filedir}/nordugrid-arc-plugins-globus.list
%files -n nordugrid-arc-plugins-globus-common -f %{oreon_filedir}/nordugrid-arc-plugins-globus-common.list
%files -n nordugrid-arc-plugins-gridftp -f %{oreon_filedir}/nordugrid-arc-plugins-gridftp.list
%files -n nordugrid-arc-plugins-lcas-lcmaps -f %{oreon_filedir}/nordugrid-arc-plugins-lcas-lcmaps.list
%files -n nordugrid-arc-plugins-xrootd -f %{oreon_filedir}/nordugrid-arc-plugins-xrootd.list
%files -n nordugrid-arc-plugins-gfal -f %{oreon_filedir}/nordugrid-arc-plugins-gfal.list
%files -n nordugrid-arc-plugins-s3 -f %{oreon_filedir}/nordugrid-arc-plugins-s3.list
%files -n nordugrid-arc-plugins-internal -f %{oreon_filedir}/nordugrid-arc-plugins-internal.list
%files -n nordugrid-arc-plugins-python -f %{oreon_filedir}/nordugrid-arc-plugins-python.list
%files -n nordugrid-arc-devel -f %{oreon_filedir}/nordugrid-arc-devel.list
%files -n python3-nordugrid-arc -f %{oreon_filedir}/python3-nordugrid-arc.list
%files -n nordugrid-arc-test-utils -f %{oreon_filedir}/nordugrid-arc-test-utils.list
%files -n nordugrid-arc-archery-manage -f %{oreon_filedir}/nordugrid-arc-archery-manage.list
%files -n nordugrid-arc-wn -f %{oreon_filedir}/nordugrid-arc-wn.list
%files -n python3-arcrest -f %{oreon_filedir}/python3-arcrest.list
%files -n nordugrid-arc-arc-exporter -f %{oreon_filedir}/nordugrid-arc-arc-exporter.list

%changelog

%autochangelog
