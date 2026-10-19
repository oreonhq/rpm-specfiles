%global source0_hash 48cb144b2736160f57af9aaa75524244fa9a89c466c03cb9306d871d44e1ca29
%global lm_prefix %{_prefix}
%global lm_sharedir %{_datadir}/lemonldap-ng
%global lm_examplesdir %{_docdir}/lemonldap-ng/examples
%global lm_vardir %{_localstatedir}/lib/lemonldap-ng
%global lm_cachedir %{_localstatedir}/cache/lemonldap-ng
%global lm_confdir %{_sysconfdir}/lemonldap-ng
%global lm_storagefile %{lm_confdir}/lemonldap-ng.ini
%global lm_bindir %{_libexecdir}/%{name}/bin
%global lm_sbindir %{_libexecdir}/%{name}/sbin
%global apache_confdir %{_sysconfdir}/httpd/conf.d
%global lm_apacheuser apache
%global lm_apachegroup apache
%global apache_version 2.4
%global lm_dnsdomain example.com
%global with_selinux 1
%global modulename lemonldap-ng
%global selinuxtype targeted
Name:           lemonldap-ng
Version:        2.22.2
Release:        1%{?dist}
Summary:        Web Single Sign On (SSO) and Access Management
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later AND OFL-1.1-RFN
URL:            https://lemonldap-ng.org
Source0:        https://release.ow2.org/lemonldap/%{name}-%{version}.tar.gz
BuildArch:      noarch
%{?el8:BuildRequires:  systemd}
%{!?el8:BuildRequires:  systemd-rpm-macros}
Requires: lemonldap-ng-common = %{version}-%{release}
Requires: lemonldap-ng-doc = %{version}-%{release}
Requires: lemonldap-ng-handler = %{version}-%{release}
Requires: lemonldap-ng-manager = %{version}-%{release}
Requires: lemonldap-ng-portal = %{version}-%{release}
Requires: lemonldap-ng-test = %{version}-%{release}
%if 0%{?with_selinux}
Requires:        (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif
%{?perl_default_filter}
%global __requires_exclude perl\\(Apache2::|perl\\(APR::Table\\)|perl\\(Protocol::WebSocket
# oreon:deps
BuildRequires:  gnupg
BuildRequires:  make
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(Apache2::Connection)
BuildRequires:  perl(Apache2::Const)
BuildRequires:  perl(Apache2::Filter)
BuildRequires:  perl(Apache2::Log)
BuildRequires:  perl(Apache2::RequestIO)
BuildRequires:  perl(Apache2::RequestRec)
BuildRequires:  perl(Apache2::RequestUtil)
BuildRequires:  perl(Apache2::ServerRec)
BuildRequires:  perl(Apache2::ServerUtil)
BuildRequires:  perl(Apache::Session)
BuildRequires:  perl(Apache::Session::Browseable)
BuildRequires:  perl(Apache::Session::File)
BuildRequires:  perl(Apache::Session::Generate::MD5)
BuildRequires:  perl(Apache::Session::Lock::File)
BuildRequires:  perl(Auth::Yubikey_WebClient)
BuildRequires:  perl(Authen::PAM)
BuildRequires:  perl(Authen::Radius)
BuildRequires:  perl(Authen::WebAuthn)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(CGI::Compile)
BuildRequires:  perl(CGI::Emulate::PSGI)
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Cache::Memcached)
BuildRequires:  perl(Cache::NullCache)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(Convert::Base32)
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::JWT)
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(Crypt::OpenSSL::X509)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Password::zxcvbn)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(Email::Sender::Simple)
BuildRequires:  perl(Email::Sender::Transport)
BuildRequires:  perl(Email::Sender::Transport::SMTP)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(Env)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI::Client)
BuildRequires:  perl(FCGI::ProcManager)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(GD::SecurityImage)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(GeoIP2::Database::Reader)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Glib)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(HTTP::BrowserDetect)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::Timeout)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::Protocol::PSGI)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Lasso)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::MDC)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Net::CIDR)
BuildRequires:  perl(Net::Facebook::Oauth2)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Control::PasswordPolicy)
BuildRequires:  perl(Net::LDAP::Extension::SetPassword)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Net::MQTT::Simple)
BuildRequires:  perl(Net::MQTT::Simple::SSL)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(Net::OpenID::Consumer)
BuildRequires:  perl(Net::OpenID::Server)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Handler::FCGI)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Redis)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(SOAP::Transport::HTTP)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sentry::Raven)
BuildRequires:  perl(Storable)
BuildRequires:  perl(String::Random)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Time::Fake)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(WWW::Form::UrlEncoded)
BuildRequires:  perl(Web::ID)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Simple)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(feature)
BuildRequires:  perl(fields)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(mod_perl2)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(systemd)
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-bootstrap-theme
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  uglify-js
BuildRequires:  which
# /oreon:deps
%description
LemonLdap::NG is a modular Web-SSO based on Apache::Session modules. It
simplifies the build of a protected area with a few changes in the
application. It manages both authentication and authorization and provides
headers for accounting.
So you can have a full AAA protection for your web space as described below.

%package common
Summary:        LemonLDAP-NG configuration
Requires:       perl(Apache::Session::Browseable)
Requires:       perl(Cache::Cache)
Requires:       perl(IO::String)
Requires:       perl(String::Random)
Requires:       (httpd or nginx)
Requires:       httpd-filesystem
Requires:       nginx-filesystem
Requires:       (mod_fcgid if httpd)
Requires:       (perl(mod_perl2) if httpd)
Requires:       (perl(Apache2::ServerRec) if httpd)
Recommends:     perl(LWP::Protocol::https)
Recommends:     perl(Net::MQTT::Simple)
Recommends:     perl(Net::MQTT::Simple::SSL)
Obsoletes:      perl-Lemonldap-NG-Common < %{version}-%{release}
Provides:       perl-Lemonldap-NG-Common = %{version}-%{release}
Obsoletes:      lemonldap-ng-conf < %{version}-%{release}
Provides:       lemonldap-ng-conf = %{version}-%{release}
%description common
This package contains the main storage configuration.

%package doc
Summary:        LemonLDAP-NG documentation
Requires:       lemonldap-ng-common = %{version}-%{release}
%description doc
This package contains HTML documentation.

%package handler
Summary:        LemonLDAP-NG handler
Requires:       lemonldap-ng-common = %{version}-%{release}
Requires:       (perl(Apache2::Connection) if httpd)
Requires:       (perl(Apache2::Const) if httpd)
Requires:       (perl(Apache2::Filter) if httpd)
Requires:       (perl(Apache2::Log) if httpd)
Requires:       (perl(Apache2::RequestIO) if httpd)
Requires:       (perl(Apache2::RequestRec) if httpd)
Requires:       (perl(Apache2::RequestUtil) if httpd)
Requires:       (perl(Apache2::ServerUtil) if httpd)
Requires:       (perl(APR::Table) if httpd)
Obsoletes:      lemonldap-ng-nginx < %{version}-%{release}
Provides:       lemonldap-ng-nginx = %{version}-%{release}
Obsoletes:      perl-Lemonldap-NG-Handler < %{version}-%{release}
Provides:       perl-Lemonldap-NG-Handler = %{version}-%{release}
%description handler
This package deploys the Apache Handler.

%package manager
Summary:        LemonLDAP-NG administration interface
Requires:       lemonldap-ng-common = %{version}-%{release}
Provides:       bundled(fontawesome-fonts) = 4.7.0
Provides:       bundled(js-angular) = 1.7.9
Provides:       bundled(js-angular-animate) = 1.8.1
Provides:       bundled(js-angular-aria) = 1.8.1
Provides:       bundled(js-angular-bootstrap) = 2.5.0
Provides:       bundled(js-angular-cookies) = 1.8.1
Provides:       bundled(js-angular-ui-tree) = 2.22.6
Provides:       bundled(js-es5-shim) = 4.5.14
Provides:       bundled(js-filesaver) = 2.0.4
Recommends:     perl(Auth::Yubikey_WebClient)
Obsoletes:      lemonldap-ng-nginx < %{version}-%{release}
Provides:       lemonldap-ng-nginx = %{version}-%{release}
Obsoletes:      perl-Lemonldap-NG-Manager < %{version}-%{release}
Provides:       perl-Lemonldap-NG-Manager = %{version}-%{release}
Recommends:     lemonldap-ng-doc = %{version}-%{release}
%description manager
This package deploys the administration interface and sessions explorer.

%package portal
Summary:        LemonLDAP-NG authentication portal
Requires:       lemonldap-ng-common = %{version}-%{release}
Recommends:     perl(Auth::Yubikey_WebClient)
Recommends:     perl(Authen::WebAuthn)
Recommends:     perl(Data::Password::zxcvbn)
Recommends:     perl(GeoIP2::Database::Reader)}
Recommends:     perl(HTTP::BrowserDetect)}
Recommends:     perl(Glib)
Recommends:     perl(Lasso)
Recommends:     perl(Net::Facebook::Oauth2)
Recommends:     perl(Net::OAuth)
Recommends:     perl(Net::OpenID::Consumer)
Provides:       bundled(fontawesome-fonts) = 4.7.0
Provides:       bundled(js-bootstrap) = 4.6.2
Provides:       bundled(js-fingerprint2) = 2.1.4
Provides:       bundled(js-jquery) = 3.5.1
Provides:       bundled(js-jquery-ui) = 1.13.2
Provides:       bundled(js-jquery-cookie) = 1.4.1
Provides:       bundled(js-jssha) = 3.3.0
Provides:       bundled(js-qrious) = 4.0.2
Obsoletes:      lemonldap-ng-nginx < %{version}-%{release}
Provides:       lemonldap-ng-nginx = %{version}-%{release}
Obsoletes:      perl-Lemonldap-NG-Portal < %{version}-%{release}
Provides:       perl-Lemonldap-NG-Portal = %{version}-%{release}
%description portal
This package deploys the authentication portal.

%package test
Summary:        LemonLDAP-NG test applications
Requires:       lemonldap-ng-common = %{version}-%{release}
Obsoletes:      lemonldap-ng-nginx < %{version}-%{release}
Provides:       lemonldap-ng-nginx = %{version}-%{release}
%description test
This package deploys small test applications.

%package fastcgi-server
Summary:        LemonLDAP-NG FastCGI Server
Requires:       lemonldap-ng-common = %{version}-%{release}
Requires:       perl(FCGI::ProcManager)
Requires:       (mod_fcgid if httpd)
%description fastcgi-server
This package deploys files needed to start a FastCGI server.

%package uwsgi-app
Summary:        LemonLDAP-NG UWSGI Application
Requires:       uwsgi-plugin-psgi
%description uwsgi-app
LemonLDAP::NG uWSGI server provides a replacement to LemonLDAP::NG FastCGI
server, using uWSGI instead of Plack FCGI.

%if 0%{?with_selinux}
%package selinux
Summary:             LemonLDAP-NG SELinux policy
BuildArch:           noarch
Requires:            selinux-policy-%{selinuxtype}
Requires(post):      selinux-policy-%{selinuxtype}
BuildRequires:       selinux-policy-devel
%{?selinux_requires}
%description selinux
Custom SELinux policy module
%endif

%package -n perl-Lemonldap-NG-SSOaaS-Apache-Client
Summary:        Lemonldap-NG SSOaaS client for Apache
%description -n perl-Lemonldap-NG-SSOaaS-Apache-Client
This package permits one to enroll an Apache server
into Lemonldap::NG's SSOaaS service.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}%{?pre_release:~%{pre_release}}

%build

%make_build configure \
    STORAGECONFFILE=%{lm_storagefile} \
    DATADIR=%{lm_vardir} \
    CACHEDIR=%{lm_cachedir} \
    PERLOPTIONS="INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1"
%make_build
%if 0%{?with_selinux}
mkdir selinux
cp -p rpm/lemonldap-ng.fc selinux/
cp -p rpm/lemonldap-ng.te selinux/
make -f %{_datadir}/selinux/devel/Makefile %{modulename}.pp
bzip2 -9 %{modulename}.pp
%endif
%install
%make_install \
    PREFIX=%{lm_prefix} \
    BINDIR=%{lm_bindir} \
    SBINDIR=%{lm_sbindir} \
    FASTCGISOCKDIR=%{_rundir}/llng-fastcgi-server \
    DOCUMENTROOT=%{lm_sharedir} \
    EXAMPLESDIR=%{lm_examplesdir} \
    HANDLERDIR=%{lm_sharedir}/handler \
    MANAGERDIR=%{lm_sharedir}/manager \
    STORAGECONFFILE=%{lm_storagefile} \
    TOOLSDIR=%{lm_sharedir}/ressources \
    CONFDIR=%{lm_confdir} \
    DATADIR=%{lm_vardir} \
    CACHEDIR=%{lm_cachedir} \
    UNITDIR=%{_unitdir}/ \
    TMPFILESDIR=%{_tmpfilesdir}/ \
    ETCDEFAULTDIR=%{_sysconfdir}/default \
    MANDIR=%{_mandir}/ \
    DNSDOMAIN=%{lm_dnsdomain} \
    APACHEVERSION=%{apache_version} \
    APACHEUSER=%{lm_apacheuser} \
    APACHEGROUP=%{lm_apachegroup} \
    APACHELOGDIR=%{_localstatedir}/log/httpd \
    UWSGIYAMLDIR=%{_sysconfdir}/uwsgi/apps-available \
    LLNGAPPDIR=%{lm_sharedir}/llng-server \
    CHOWN=/usr/bin/true \
    CHGRP=/usr/bin/true \
    WITHRC=no \
    PROD=yes
mkdir -p %{buildroot}%{_sysconfdir}/uwsgi/apps-available
mkdir -p %{buildroot}%{lm_sharedir}/llng-server
mkdir -p %{buildroot}%{_presetdir}
install -p -m 0644 lemonldap-ng-handler/scripts/lemonldap-ng-handler.preset \
  %{buildroot}%{_presetdir}/10-lemonldap-ng-handler.preset
install -p -m 0644 lemonldap-ng-portal/scripts/lemonldap-ng-portal.preset \
  %{buildroot}%{_presetdir}/10-lemonldap-ng-portal.preset
mkdir -p %{buildroot}%{apache_confdir}
for i in handler manager portal api test; do {
    mv %{buildroot}%{lm_confdir}/$i-apache%{apache_version}.conf \
        %{buildroot}%{apache_confdir}/z-lemonldap-ng-$i.conf
}; done
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d/
mv %{buildroot}%{lm_confdir}/*nginx*.conf \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/
mv %{buildroot}%{_sysconfdir}/nginx/conf.d/nginx-lua-headers.conf \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/nginx-lmlog.conf \
    %{buildroot}%{_sysconfdir}/nginx/
sed -i 's:/etc/lemonldap-ng/nginx-lmlog.conf:/etc/nginx/nginx-lmlog.conf:' \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/handler-nginx.conf
sed -i 's:/etc/lemonldap-ng/nginx-lua-headers.conf:/etc/nginx/nginx-lua-headers.conf:' \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/test-nginx.conf
mv %{buildroot}%{lm_confdir}/for_etc_hosts .
sed -i -e 's,#!/usr/bin/env plackup,#!/usr/bin/plackup,' \
    %{buildroot}%{lm_sharedir}/manager/api/api.psgi \
    %{buildroot}%{lm_sharedir}/manager/htdocs/manager.psgi \
    %{buildroot}%{lm_examplesdir}/manager/manager.psgi
sed -i -e '1i#!/usr/bin/plackup' \
    %{buildroot}%{lm_examplesdir}/llngapp.psgi
%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 \
    %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%endif
%{_fixperms} %{buildroot}%{perl_vendorlib}/ %{buildroot}%{_mandir}/
%oreon_autofiles perl-Lemonldap-NG-SSOaaS-Apache-Client usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

sed -i 's:^dirName.*:dirName = %{buildroot}%{lm_vardir}/conf:' \
    %{buildroot}%{lm_storagefile}
%make_build test \
    %{?!_with_network_tests:SKIP_NETWORK_TESTS=1} \
    LLNG_DEFAULTCONFFILE=%{buildroot}%{lm_storagefile}
sed -i 's:^dirName.*:dirName = %{lm_vardir}/conf:' \
    %{buildroot}%{lm_storagefile}
%post common

if [ $1 -gt 1 ] ; then
    if [ -e %{lm_confdir}/storage.conf \
         -o -e %{lm_confdir}/apply.conf \
         -o -e %{lm_confdir}/apps-list.xml ] ; then
        %{lm_bindir}/lmMigrateConfFiles2ini 2>&1 > /dev/null || :
        chgrp %{lm_apachegroup} %{lm_storagefile} || :
    fi
fi
%systemd_post lemonldap-ng-rotateOidcKeys.timer
%preun common

if [ $1 -eq 1 ] ; then
    find %{apache_confdir} -name 'z-lemonldap-ng*.conf' \
        -type l -delete 2>&1 > /dev/null || :
fi
%systemd_preun lemonldap-ng-rotateOidcKeys.timer
%postun common

%systemd_postun lemonldap-ng-rotateOidcKeys.timer
%post fastcgi-server

%systemd_post llng-fastcgi-server.service
%preun fastcgi-server

%systemd_preun llng-fastcgi-server.service
%postun fastcgi-server

%systemd_postun_with_restart llng-fastcgi-server.service
%post portal

%systemd_post lemonldap-ng-portal.timer
systemctl start lemonldap-ng-portal.timer || :
%preun portal

%systemd_preun lemonldap-ng-portal.timer
%postun portal

%systemd_postun lemonldap-ng-portal.timer
%post handler

%systemd_post lemonldap-ng-handler.timer
systemctl start lemonldap-ng-handler.timer || :
%preun handler

%systemd_preun lemonldap-ng-handler.timer
%postun handler

%systemd_postun lemonldap-ng-handler.timer
%if 0%{?with_selinux}
%pre selinux

%selinux_relabel_pre -s %{selinuxtype}
%post selinux

%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%postun selinux

if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi
%posttrans selinux

%selinux_relabel_post -s %{selinuxtype}
%endif
%files -f %{oreon_filedir}/main.list
%files -n lemonldap-ng-common -f %{oreon_filedir}/lemonldap-ng-common.list
%files -n lemonldap-ng-doc -f %{oreon_filedir}/lemonldap-ng-doc.list
%files -n lemonldap-ng-handler -f %{oreon_filedir}/lemonldap-ng-handler.list
%files -n lemonldap-ng-manager -f %{oreon_filedir}/lemonldap-ng-manager.list
%files -n lemonldap-ng-portal -f %{oreon_filedir}/lemonldap-ng-portal.list
%files -n lemonldap-ng-test -f %{oreon_filedir}/lemonldap-ng-test.list
%files -n lemonldap-ng-fastcgi-server -f %{oreon_filedir}/lemonldap-ng-fastcgi-server.list
%files -n lemonldap-ng-uwsgi-app -f %{oreon_filedir}/lemonldap-ng-uwsgi-app.list
%files -n lemonldap-ng-selinux -f %{oreon_filedir}/lemonldap-ng-selinux.list
%files -n perl-Lemonldap-NG-SSOaaS-Apache-Client -f %{oreon_filedir}/perl-Lemonldap-NG-SSOaaS-Apache-Client.list

%changelog

%autochangelog
