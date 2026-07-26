%global source0_hash 57881348297c4412f86c410547cf76b4d8a236574dd2c6b7d6a2beebe7fc44e3

# Fedora spec file for phpMyAdmin
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

# nginx 1.6 with nginx-filesystem
%global with_nginx     1
# httpd 2.4 with httpd-filesystem
%global with_httpd     1

%global upstream_version 5.2.3
#global upstream_prever  rc1

Name: phpMyAdmin
Version: %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release: 2%{?dist}
Summary: A web interface for MySQL and MariaDB

# phpMyAdmin is GPL-2.0-or-later
# MIT (js/jquery/, js/jqplot, js/codemirror/, js/tracekit/)
# BSD 2-Clause (js/openlayers/)
# for PHP library see generated bundled list above
License: GPL-2.0-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause AND LGPL-3.0-or-later AND MPL-2.0 AND ISC
URL: https://www.phpmyadmin.net/
Source0: https://files.phpmyadmin.net/%{name}/%{upstream_version}%{?upstream_prever:-%upstream_prever}/%{name}-%{upstream_version}%{?upstream_prever:-%upstream_prever}-all-languages.tar.xz
Source1: https://files.phpmyadmin.net/%{name}/%{upstream_version}%{?upstream_prever:-%upstream_prever}/%{name}-%{upstream_version}%{?upstream_prever:-%upstream_prever}-all-languages.tar.xz.asc
Source2: phpMyAdmin.htaccess
Source3: phpMyAdmin.nginx
Source4: https://files.phpmyadmin.net/phpmyadmin.keyring
# List name / version / license of bundled libraries
Source5: phpMyAdmin-bundled.php

# Redirect to system certificates
Patch0:  phpMyAdmin-certs.patch

BuildArch: noarch
BuildRequires: gnupg2
# to run phpMyAdmin-bundled.php
BuildRequires: php(language) >= 7.2.5
BuildRequires: php-cli
BuildRequires: php-json
BuildRequires: composer-generators

Requires(post): coreutils sed
Requires:  webserver
%if %{with_nginx}
Requires:   nginx-filesystem
%endif
%if %{with_httpd}
Requires:  httpd-filesystem
Requires:  php(httpd)
Suggests:  httpd
%endif
# From composer.json, "require": {
#        "php": "^7.2.5 || ^8.0",
#        "ext-hash": "*",
#        "ext-iconv": "*",
#        "ext-json": "*",
#        "ext-mysqli": "*",
#        "ext-openssl": "*",
#        "ext-pcre": "*",
#        "ext-xml": "*",
#        "google/recaptcha": "^1.1",
#        "nikic/fast-route": "^1.3",
#        "phpmyadmin/motranslator": "^5.0",
#        "phpmyadmin/shapefile": "^2.0",
#        "phpmyadmin/sql-parser": "^5.5",
#        "phpmyadmin/twig-i18n-extension": "^3.0",
#        "phpseclib/phpseclib": "^2.0",
#        "symfony/config": "^4.4.9",
#        "symfony/dependency-injection": "^4.4.9",
#        "symfony/expression-language": "^4.4.9",
#        "symfony/polyfill-ctype": "^1.17.0",
#        "symfony/polyfill-mbstring": "^1.17.0",
#        "twig/twig": "^2.14.9 || ^3.3.5",
#        "williamdes/mariadb-mysql-kbs": "^1.2"
Requires:  php(language) >= 7.2.5
Requires:  php-iconv
Requires:  php-json
Requires:  php-mysqli
Requires:  php-openssl
Requires:  php-xml
Requires:  php-dom
Requires:  php-intl
Requires:  php-posix
# php-tidy required by tcpdf is not used (fixHTMLCode)
Requires:  php-ctype
Requires:  php-curl
Requires:  php-zlib
Requires:  php-bz2
Requires:  php-zip
Requires:  php-gd
Requires:  php-mbstring
# From phpcompatinfo reports for 4.8.0
#   notice: recode is optional (iconv or mbstring are preferred / used first)
Requires:  php-libxml
Requires:  php-simplexml
Requires:  php-xmlwriter
# System certificates
Requires:  %{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem

# Bundled JS library
Provides:  bundled(js-codemirror)
Provides:  bundled(js-jqplot) = 1.0.9
Provides:  bundled(js-jquery) = 3.2.1
Provides:  bundled(js-openlayers)
Provides:  bundled(js-tracekit)

# Allow lowercase in install command
Provides:  phpmyadmin   =  %{version}-%{release}

%description
phpMyAdmin is a tool written in PHP intended to handle the administration of
MySQL over the Web. Currently it can create and drop databases,
create/drop/alter tables, delete/edit/add fields, execute any SQL statement,
manage keys on fields, manage privileges,export data into various formats and
is available in 50 languages

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{?gpgverify:%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%setup -qn phpMyAdmin-%{upstream_version}%{?upstream_prever:-%upstream_prever}-all-languages
%patch -P0 -p1
rm -r vendor/composer/ca-bundle/res/

# Minimal configuration file
sed -e "/'blowfish_secret'/s@''@'MUSTBECHANGEDONINSTALL'@"  \
    -e "/'UploadDir'/s@''@'%{_localstatedir}/lib/%{name}/upload'@"  \
    -e "/'SaveDir'/s@''@'%{_localstatedir}/lib/%{name}/save'@" \
    config.sample.inc.php >CONFIG

# Setup vendor config file
sed -e "/'changeLogFile'/s@ROOT_PATH@'%{_pkgdocdir}/'@" \
    -e "/'licenseFile'/s@ROOT_PATH@'%{_pkgdocdir}/'@" \
    -e "/'configFile'/s@ROOT_PATH@'%{_sysconfdir}/%{name}/'@" \
    -e '/licenseFile/s:%_defaultdocdir:%_defaultlicensedir:' \
    -e "/versionSuffix/s/''/'-%{release}'/" \
    -e "/tempDir/s@ROOT.*tmp'@'%{_localstatedir}/lib/%{name}/temp'@" \
    -e "/cacheDir/s@ROOT.*cache'@'%{_localstatedir}/lib/%{name}/cache'@" \
    -i libraries/vendor_config.php

# For debug
grep '=>' libraries/vendor_config.php

%build
# Nothing to do

%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -ad ./* %{buildroot}/%{_datadir}/%{name}
install -Dpm 0640 CONFIG %{buildroot}/%{_sysconfdir}/%{name}/config.inc.php
# Apache
install -Dpm 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/phpMyAdmin.conf
# Nginx
%if %{with_nginx}
install -Dpm 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/nginx/default.d/phpMyAdmin.conf
%endif

mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}/{upload,save,config,temp}

rm -f %{buildroot}/%{_datadir}/%{name}/config.sample.inc.php
rm -f %{buildroot}/%{_datadir}/%{name}/*txt
rm -f %{buildroot}/%{_datadir}/%{name}/[CDLR]*
rm -f %{buildroot}/%{_datadir}/%{name}/libraries/.htaccess
rm -f %{buildroot}/%{_datadir}/%{name}/setup/lib/.htaccess
rm -f %{buildroot}/%{_datadir}/%{name}/setup/frames/.htaccess
rm -rf %{buildroot}%{_datadir}/%{name}/contrib
rm     %{buildroot}%{_datadir}/%{name}/composer.*
rm -rf %{buildroot}%{_datadir}/%{name}/tmp/
mv     %{buildroot}%{_datadir}/%{name}/libraries/cache %{buildroot}/%{_localstatedir}/lib/%{name}/cache

# JS libraries sources
#rm -r %%{buildroot}%%{_datadir}/%{name}/js/jquery/src
#rm -r %%{buildroot}%%{_datadir}/%{name}/js/openlayers/src

# documentation
rm -rf    %{buildroot}%{_datadir}/%{name}/examples/
rm -rf    %{buildroot}%{_datadir}/%{name}/doc/
mkdir -p  %{buildroot}%{_datadir}/%{name}/doc/
ln -s ../../doc/%{name}/html  %{buildroot}%{_datadir}/%{name}/doc/html

mv -f %{buildroot}%{_datadir}/%{name}/js/vendor/jquery/MIT-LICENSE.txt LICENSE-jquery
mv -f %{buildroot}%{_datadir}/%{name}/js/vendor/codemirror/LICENSE LICENSE-codemirror

%pretrans
# allow dir to link upgrade
if  [ -d %{_datadir}/%{name}/doc/html ]; then
  rm -rf %{_datadir}/%{name}/doc/html
fi

%post
# generate a 32 chars secret key for this install
SECRET=$(printf "%04x%04x%04x%04x%04x%04x%04x%04x" $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM)
sed -e "/'blowfish_secret'/s/MUSTBECHANGEDONINSTALL/$SECRET/" \
    -i %{_sysconfdir}/%{name}/config.inc.php

%files
%license LICENSE*
%doc ChangeLog README CONTRIBUTING.md config.sample.inc.php
%doc doc/html/
%doc examples/
%doc composer.json
%{_datadir}/%{name}
%attr(0750,root,apache) %dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/%{name}/config.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%if %{with_nginx}
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%endif
%dir %{_localstatedir}/lib/%{name}/
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/upload
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/save
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/config
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/temp
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/cache
     %attr(0640,apache,apache) %{_localstatedir}/lib/%{name}/cache/*

%changelog
%autochangelog
