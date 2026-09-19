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

# Apache configuration directory
%global apache_confdir %{_sysconfdir}/httpd/conf.d

# Apache User and Group
%global lm_apacheuser apache
%global lm_apachegroup apache

# Apache version
%global apache_version 2.4

%global lm_dnsdomain example.com

# SELinux
%global with_selinux 1
%global modulename lemonldap-ng
%global selinuxtype targeted

#global pre_release beta1

Name:           lemonldap-ng
Version:        2.22.2
Release:        %{?pre_release:0.}1%{?pre_release:.%{pre_release}}%{?dist}
Summary:        Web Single Sign On (SSO) and Access Management
# Lemonldap-ng itself is GPLv2+
# Qrious bundled javascript library is GPLv3+
# All other bundled javascript libraries are MIT
# Fontawesome bundled font is OFL
License:        GPL-2.0-or-later AND MIT AND GPL-3.0-or-later AND OFL-1.1-RFN
URL:            https://lemonldap-ng.org
Source0:        https://release.ow2.org/lemonldap/%{name}-%{version}%{?pre_release:~%{pre_release}}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  gnupg
BuildRequires:  which
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
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
BuildRequires:  perl(Apache::Session::Generate::MD5)
BuildRequires:  perl(APR::Table)
BuildRequires:  perl(Authen::PAM)
BuildRequires:  perl(Authen::Radius)
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(Cache::Memcached)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Config::IniFiles)
BuildRequires:  perl(constant)
BuildRequires:  perl(Convert::Base32)
BuildRequires:  perl(Convert::PEM)
BuildRequires:  perl(Crypt::JWT)
BuildRequires:  perl(Crypt::OpenSSL::RSA)
BuildRequires:  perl(Crypt::OpenSSL::X509)
BuildRequires:  perl(Crypt::Rijndael)
BuildRequires:  perl(Crypt::URandom)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Data::Password::zxcvbn)
BuildRequires:  perl(Date::Parse)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Email::Date::Format)
BuildRequires:  perl(Email::Sender::Simple)
BuildRequires:  perl(Email::Sender::Transport::SMTP)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FCGI::Client)
BuildRequires:  perl(feature)
BuildRequires:  perl(fields)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(GD::SecurityImage)
BuildRequires:  perl(GeoIP2::Database::Reader)
BuildRequires:  perl(GSSAPI)
BuildRequires:  perl(Hash::Merge::Simple)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::FormatText::WithLinks)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(HTTP::BrowserDetect)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(IO::Socket::INET)
BuildRequires:  perl(IO::Socket::Timeout)
BuildRequires:  perl(IO::String)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Log4perl)
BuildRequires:  perl(Log::Log4perl::MDC)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(mod_perl2)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Net::CIDR)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Control::PasswordPolicy)
BuildRequires:  perl(Net::LDAP::Extension::SetPassword)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Net::OpenID::Server)
BuildRequires:  perl(Net::SSLeay)
BuildRequires:  perl(parent)
BuildRequires:  perl(Plack::Middleware)
BuildRequires:  perl(Plack::Request)
BuildRequires:  perl(Plack::Runner)
BuildRequires:  perl(Plack::Util)
BuildRequires:  perl(Plack::Util::Accessor)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Redis)
BuildRequires:  perl(Regexp::Assemble)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Safe)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sentry::Raven)
BuildRequires:  perl(SOAP::Lite)
BuildRequires:  perl(SOAP::Transport::HTTP)
BuildRequires:  perl(strict)
BuildRequires:  perl(String::Random)
BuildRequires:  perl(Sys::Syslog)
BuildRequires:  perl(Text::Unidecode)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(URI::URL)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Web::ID)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(YAML)
# Runtime
BuildRequires:  perl(Apache::Session::Browseable)
BuildRequires:  perl(Apache::Session::Lock::File)
BuildRequires:  perl(Auth::Yubikey_WebClient)
BuildRequires:  perl(Authen::WebAuthn)
BuildRequires:  perl(CGI::Compile)
BuildRequires:  perl(CGI::Emulate::PSGI)
BuildRequires:  perl(Crypt::PK::ECC)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Email::Address)
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(English)
BuildRequires:  perl(FCGI::ProcManager)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Glib)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(IO::Pipe)
BuildRequires:  perl(Lasso)
BuildRequires:  perl(LWP::Protocol::https)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Net::Facebook::Oauth2)
BuildRequires:  perl(Net::MQTT::Simple)
BuildRequires:  perl(Net::MQTT::Simple::SSL)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(Net::OpenID::Consumer)
BuildRequires:  perl(Perl::Tidy)
BuildRequires:  perl(Plack::Handler::FCGI)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Storable)
BuildRequires:  perl(threads::shared)
BuildRequires:  perl(WWW::Form::UrlEncoded)
BuildRequires:  perl(XML::Simple)
# Tests
BuildRequires:  perl(Apache::Session::File)
BuildRequires:  perl(Cache::NullCache)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Email::Sender::Transport)
BuildRequires:  perl(Env)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Image::Magick)
BuildRequires:  perl(IO::Select)
BuildRequires:  perl(lib)
BuildRequires:  perl(locale)
BuildRequires:  perl(LWP::Protocol::PSGI)
BuildRequires:  perl(Plack::Builder)
BuildRequires:  perl(Plack::Response)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Time::Fake)

%{?el8:BuildRequires:  systemd}
%{!?el8:BuildRequires:  systemd-rpm-macros}
BuildRequires:  uglify-js

# Doc
BuildRequires:  python3-sphinx-bootstrap-theme
BuildRequires:  python3-sphinx

Requires: lemonldap-ng-common = %{version}-%{release}
Requires: lemonldap-ng-doc = %{version}-%{release}
Requires: lemonldap-ng-handler = %{version}-%{release}
Requires: lemonldap-ng-manager = %{version}-%{release}
Requires: lemonldap-ng-portal = %{version}-%{release}
Requires: lemonldap-ng-test = %{version}-%{release}

%if 0%{?with_selinux}
# This ensures that the *-selinux package and all it’s dependencies are not pulled
# into containers and other systems that do not use SELinux
Requires:        (%{name}-selinux = %{version}-%{release} if selinux-policy-%{selinuxtype})
%endif

# Setup requires filtering
%{?perl_default_filter}
%global __requires_exclude perl\\(Apache2::|perl\\(APR::Table\\)|perl\\(Protocol::WebSocket

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
# Yubikey
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
# Yubikey
Recommends:     perl(Auth::Yubikey_WebClient)
# Fido2
Recommends:     perl(Authen::WebAuthn)
# Password entropy
Recommends:     perl(Data::Password::zxcvbn)
# Location
Recommends:     perl(GeoIP2::Database::Reader)}
Recommends:     perl(HTTP::BrowserDetect)}
# SAML
Recommends:     perl(Glib)
Recommends:     perl(Lasso)
# Facebook
Recommends:     perl(Net::Facebook::Oauth2)
# OpenID
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
# SELinux policy (originally from selinux-policy-contrib)
# this policy module will override the production module
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

# UWSGI Application
mkdir -p %{buildroot}%{_sysconfdir}/uwsgi/apps-available
mkdir -p %{buildroot}%{lm_sharedir}/llng-server

# Install systemd presets for timers
mkdir -p %{buildroot}%{_presetdir}
install -p -m 0644 lemonldap-ng-handler/scripts/lemonldap-ng-handler.preset \
  %{buildroot}%{_presetdir}/10-lemonldap-ng-handler.preset
install -p -m 0644 lemonldap-ng-portal/scripts/lemonldap-ng-portal.preset \
  %{buildroot}%{_presetdir}/10-lemonldap-ng-portal.preset

# Install httpd conf files
# We use "z-lemonldap-ng-*" so that httpd read the files after "perl.conf"
mkdir -p %{buildroot}%{apache_confdir}
for i in handler manager portal api test; do {
    mv %{buildroot}%{lm_confdir}/$i-apache%{apache_version}.conf \
        %{buildroot}%{apache_confdir}/z-lemonldap-ng-$i.conf
}; done

# Install nginx conf files
mkdir -p %{buildroot}%{_sysconfdir}/nginx/conf.d/
mv %{buildroot}%{lm_confdir}/*nginx*.conf \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/
# Move lua and log configuration
mv %{buildroot}%{_sysconfdir}/nginx/conf.d/nginx-lua-headers.conf \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/nginx-lmlog.conf \
    %{buildroot}%{_sysconfdir}/nginx/
# Replace paths in main configuration files
sed -i 's:/etc/lemonldap-ng/nginx-lmlog.conf:/etc/nginx/nginx-lmlog.conf:' \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/handler-nginx.conf
sed -i 's:/etc/lemonldap-ng/nginx-lua-headers.conf:/etc/nginx/nginx-lua-headers.conf:' \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/test-nginx.conf

# Remove for_etc_hosts from %%{_sysconfdir}
mv %{buildroot}%{lm_confdir}/for_etc_hosts .

# Fix shebangs
sed -i -e 's,#!/usr/bin/env plackup,#!/usr/bin/plackup,' \
    %{buildroot}%{lm_sharedir}/manager/api/api.psgi \
    %{buildroot}%{lm_sharedir}/manager/htdocs/manager.psgi \
    %{buildroot}%{lm_examplesdir}/manager/manager.psgi
sed -i -e '1i#!/usr/bin/plackup' \
    %{buildroot}%{lm_examplesdir}/llngapp.psgi

# Install SELinux policy
%if 0%{?with_selinux}
install -D -m 0644 %{modulename}.pp.bz2 \
    %{buildroot}%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.bz2
%endif

# Fix man and perl modules permissions
%{_fixperms} %{buildroot}%{perl_vendorlib}/ %{buildroot}%{_mandir}/

%check
sed -i 's:^dirName.*:dirName = %{buildroot}%{lm_vardir}/conf:' \
    %{buildroot}%{lm_storagefile}
# Tests requiring network are disabled by default
# Use "--with network_tests" to execute them
%make_build test \
    %{?!_with_network_tests:SKIP_NETWORK_TESTS=1} \
    LLNG_DEFAULTCONFFILE=%{buildroot}%{lm_storagefile}
sed -i 's:^dirName.*:dirName = %{lm_vardir}/conf:' \
    %{buildroot}%{lm_storagefile}

%post common
# Upgrade from previous version
# See https://lemonldap-ng.org/documentation/1.0/upgrade
if [ $1 -gt 1 ] ; then
    if [ -e %{lm_confdir}/storage.conf \
         -o -e %{lm_confdir}/apply.conf \
         -o -e %{lm_confdir}/apps-list.xml ] ; then
        # Run migration script
        %{lm_bindir}/lmMigrateConfFiles2ini 2>&1 > /dev/null || :
        # Fix ownership
        chgrp %{lm_apachegroup} %{lm_storagefile} || :
    fi
fi
%systemd_post lemonldap-ng-rotateOidcKeys.timer

%preun common
# Upgrade from previous version
if [ $1 -eq 1 ] ; then
    # Remove old symlinks in Apache configuration
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
# SELinux contexts are saved so that only affected files can be
# relabeled after the policy module installation
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
# if with_selinux
%endif

%files

%files common
%doc changelog README.md AUTHORS CONTRIBUTING.md
%doc for_etc_hosts
%license COPYING LICENSE
%dir %{lm_confdir}
%config(noreplace) %attr(640,root,%{lm_apachegroup}) %{lm_storagefile}
%{_unitdir}/lemonldap-ng-rotateOidcKeys.service
%{_unitdir}/lemonldap-ng-rotateOidcKeys.timer
%{_mandir}/man1/convertConfig*
%{_mandir}/man1/convertSessions*
%{_mandir}/man1/convertToHashSessionStorage*
%{_mandir}/man1/encryptTotpSecrets*
%{_mandir}/man1/lemonldap-ng-sessions*
%{_mandir}/man1/rotateOidcKeys*
%dir %{_libexecdir}/%{name}
%dir %{lm_sbindir}
%dir %{lm_bindir}
%{lm_bindir}/convertConfig
%{lm_bindir}/convertSessions
%{lm_bindir}/convertToHashSessionStorage
%{lm_bindir}/encryptTotpSecrets
%{lm_bindir}/lemonldap-ng-sessions
%{lm_bindir}/importMetadata
%{lm_bindir}/lmMigrateConfFiles2ini
%{lm_bindir}/rotateOidcKeys
%dir %{lm_examplesdir}
%dir %{lm_sharedir}
%{lm_sharedir}/ressources/
%{_mandir}/man3/Lemonldap::NG::Common*.3pm.*
%dir %{perl_vendorlib}/Lemonldap
%dir %{perl_vendorlib}/Lemonldap/NG
%{perl_vendorlib}/Lemonldap/NG/Common.pm
%{perl_vendorlib}/Lemonldap/NG/Common/
%{perl_vendorlib}/auto/Lemonldap/NG/Common/
%dir %{lm_vardir}
%defattr(640,%{lm_apacheuser},%{lm_apachegroup},750)
%dir %{lm_vardir}/conf
%dir %{lm_vardir}/sessions
%dir %{lm_vardir}/sessions/lock
%dir %{lm_vardir}/psessions
%dir %{lm_vardir}/psessions/lock
%dir %{lm_vardir}/notifications
%dir %{lm_cachedir}
%config(noreplace) %{lm_vardir}/conf/lmConf-1.json

%files doc
%doc %{lm_sharedir}/doc
%doc changelog README.md AUTHORS CONTRIBUTING.md
%license COPYING LICENSE

%files handler
%{lm_bindir}/purgeLocalCache
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-handler.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/handler-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/nginx-lmlog.conf
%{_unitdir}/lemonldap-ng-handler.service
%{_unitdir}/lemonldap-ng-handler.timer
%{_presetdir}/10-lemonldap-ng-handler.preset
%{lm_sharedir}/handler
%{lm_examplesdir}/handler
%{lm_sharedir}/llng-server/
%{_mandir}/man3/Lemonldap::NG::Handler*.3pm.*
%{_mandir}/man3/Plack::Middleware::Auth::LemonldapNG.3pm.*
%{perl_vendorlib}/Lemonldap/NG/Handler.pm
%{perl_vendorlib}/Lemonldap/NG/Handler/
%{perl_vendorlib}/auto/Lemonldap/NG/Handler/
%{perl_vendorlib}/Plack/Middleware/Auth/LemonldapNG.pm

%files manager
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-manager.conf
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-api.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/manager-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/api-nginx.conf
%{lm_sharedir}/manager
%{lm_examplesdir}/manager
%{lm_bindir}/crowdsecBan
%{lm_bindir}/lmConfigEditor
%{lm_bindir}/lemonldap-ng-cli
%{lm_bindir}/llngDeleteSession
%{lm_bindir}/llngUserAttributes
%{_mandir}/man1/lemonldap-ng-cli*
%{_mandir}/man1/importMetadata*
%{_mandir}/man3/Lemonldap::NG::Manager*.3pm.*
%{perl_vendorlib}/Lemonldap/NG/Manager.pm
%{perl_vendorlib}/Lemonldap/NG/Manager/

%files portal
%{_mandir}/man1/downloadSamlMetadata*
%{_mandir}/man1/purgeCentralCache*
%{_mandir}/man1/purgePersistentSessions*
%{lm_sharedir}/portal
%{lm_bindir}/purgeCentralCache
%{lm_bindir}/downloadSamlMetadata
%{lm_bindir}/purgePersistentSessions
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-portal.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/portal-nginx.conf
%{_unitdir}/lemonldap-ng-portal.service
%{_unitdir}/lemonldap-ng-portal.timer
%{_presetdir}/10-lemonldap-ng-portal.preset
%{lm_examplesdir}/portal
%{_mandir}/man3/Lemonldap::NG::Portal*.3pm.*
%{perl_vendorlib}/Lemonldap/NG/Portal.pm
%{perl_vendorlib}/Lemonldap/NG/Portal/
%defattr(-,%{lm_apacheuser},%{lm_apachegroup},750)
%dir %{lm_vardir}/captcha

%files test
%{lm_sharedir}/test
%config(noreplace) %{apache_confdir}/z-lemonldap-ng-test.conf
%config(noreplace) %{_sysconfdir}/nginx/conf.d/test-nginx.conf
%config(noreplace) %{_sysconfdir}/nginx/nginx-lua-headers.conf

%files fastcgi-server
%{lm_sbindir}/llng-fastcgi-server
%config(noreplace) %{_sysconfdir}/default/llng-fastcgi-server
%{_unitdir}/llng-fastcgi-server.service
%{_tmpfilesdir}/llng-fastcgi-server.conf
%{lm_examplesdir}/llngapp.psgi
%{_mandir}/man8/llng-fastcgi-server.8p*
%defattr(755,%{lm_apacheuser},%{lm_apachegroup},755)
%dir %{_rundir}/llng-fastcgi-server

%files uwsgi-app
%config(noreplace) %{_sysconfdir}/uwsgi/apps-available/llng-server.yaml

%if 0%{?with_selinux}
%files selinux
%{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp.*
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%files -n perl-Lemonldap-NG-SSOaaS-Apache-Client
%{_mandir}/man3/Lemonldap::NG::SSOaaS::Apache*.3pm.*
%{perl_vendorlib}/Lemonldap/NG/SSOaaS/Apache/

%changelog
%autochangelog
