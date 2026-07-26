%global source0_hash 2062e74731568f44e026d532794a53633ea85bd6b45a78e341fed9b33cda3590

#
# Fedora spec file for roundcubemail
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%bcond_with  internet

# support for apache / nginx / php-fpm
%global with_phpfpm 1
%global upstream_version     1.7
%global upstream_prever      rc5

%global roundcubedir %{_datadir}/roundcubemail
%global _logdir /var/log  
Name: roundcubemail
Version:  %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:  1%{?dist}
Summary: Round Cube Webmail is a browser-based multilingual IMAP client

# Since 0.8 beta, the main code has been GPLv3+ with exceptions and
# skins CC-BY-SA.
# Plugins are a mix of GPLv3+ and GPLv2. The Enigma plugin contains a
# copy of php-Pear-Crypt-GPG (not yet packaged for Fedora), which is
# LGPLv2+. The jqueryui plugin contains the entire jQuery UI framework
# for the use of roundcube plugins: it is licensed as MIT or GPLv2.
# The program/js/tiny_mce directory contains an entire copy of TinyMCE
# which is LGPLv2+.
# https://github.com/pear/Crypt_GPG
# http://jqueryui.com/
# http://www.tinymce.com/
License: GPL-3.0-or-later AND GPL-2.0-only AND LGPL-2.0-or-later AND CC-BY-SA-3.0 AND MIT AND BSD-2-Clause AND BSD-3-Clause AND PHP-3.01
URL: http://www.roundcube.net
Source0: https://github.com/roundcube/roundcubemail/releases/download/%{upstream_version}%{?upstream_prever:-%{upstream_prever}}/roundcubemail-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}-complete.tar.gz
Source8: https://github.com/roundcube/roundcubemail/releases/download/%{upstream_version}%{?upstream_prever:-%{upstream_prever}}/roundcubemail-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}-complete.tar.gz.asc
Source9: https://roundcube.net/download/pubkey.asc

Source1: roundcubemail.httpd
Source3: roundcubemail.nginx
Source2: roundcubemail.logrotate
Source4: roundcubemail-README-rpm.txt
# Simple script to dump name, version and licenses of bundled libraries
Source5: roundcubemail-bundled.php

# Non-upstreamable: Adjusts config path to Fedora policy
Patch1: roundcubemail-1.7-confpath.patch

BuildArch: noarch
BuildRequires: gnupg2
BuildRequires: php(language) >= 8.1
# For test
BuildRequires: php-cli
BuildRequires: composer-generators

%if %{with_phpfpm}
Requires:  webserver
Requires:  nginx-filesystem
Requires:  httpd-filesystem
Requires:  php(httpd)
%else
Requires: httpd
Requires: mod_php
%endif
Requires: php(language) >= 8.1
Requires: php-ctype
Requires: php-curl
Requires: php-dom
Requires: php-fileinfo
Requires: php-gd
Requires: php-iconv
Requires: php-intl
Requires: php-json
Requires: php-ldap
Requires: php-libxml
Requires: php-mbstring
Requires: php-openssl
Requires: php-pdo
Requires: php-posix
Requires: php-simplexml
Requires: php-sockets
Requires: php-tokenizer
# mailcap for /etc/mime.types
Requires: mailcap
# EXIF images
Requires: php-exif
# ZIP download plugin
Requires: php-zip

# Optional deps
# Upload progress (shock!)
Suggests:   php-uploadprogress
# Crypto
Suggests:   php-sodium
# Spell check
Recommends: php-enchant
Suggests:   php-pspell
# Caching
Suggests:   php-apcu
Suggests:   php-memcache
Suggests:   php-memcached
Suggests:   php-redis
# Gearman support
Suggests:   php-gearman
# Authent
Suggests:   php-krb5
Suggests:   php-pam

# Bundled JS libraries
# see https://github.com/roundcube/roundcubemail/blob/master/jsdeps.json
# License Apache-2.0
Provides: bundled(js-lessjs) = 4.4.2
# License GPLv3
Provides: bundled(js-publickey) = 0e011cb1
# License LGPL
Provides: bundled(js-openpgp) = 5.0.0
Provides: bundled(js-tinymce) = 5.10.9
# License MIT
Provides: bundled(js-bootstrap) = 4.5.3
Provides: bundled(js-codemirror) = 5.58.3
Provides: bundled(js-jquery) = 3.7.1
# License Unkown
Provides: bundled(js-tinymce-langs) = 5.10.9

%description
RoundCube Webmail is a browser-based multilingual IMAP client
with an application-like user interface. It provides full
functionality you expect from an e-mail client, including MIME
support, address book, folder manipulation, message searching
and spell checking. RoundCube Webmail is written in PHP and 
requires a database: MySQL, PostgreSQL and SQLite are known to
work. The user interface is fully skinnable using XHTML and
CSS 2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{?gpgverify: %{gpgverify} --keyring=%{SOURCE9} --signature=%{SOURCE8} --data=%{SOURCE0}}

%setup -q -n roundcubemail-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}
%patch -P1 -p1 -b .rpm

%if %{with internet}
: JS bundled libraries
php %{SOURCE5} https://raw.githubusercontent.com/roundcube/roundcubemail/%{upstream_version}%{?upstream_prever:-%{upstream_prever}}/jsdeps.json
%endif

# fix permissions and remove any .htaccess files
find . -type f -print | xargs chmod a-x
find . -name \.htaccess -delete -print

# drop file from patch
find . -type f -name '*.orig' -o -name '*.rpm' -exec rm {} \; -print

# Wipe bbcode plugin from bundled TinyMCE to make doubleplus sure we cannot
# be vulnerable to CVE-2012-4230, unaddressed upstream
echo "CVE-2012-4230: removing tinymce bbcode plugin, check path if this fails."
test -d program/js/*mce/plugins/bbcode && rm -rf program/js/*mce/plugins/bbcode || exit 1

%build
# Nothing

%install
install -d %{buildroot}%{roundcubedir}
cp -pr * %{buildroot}%{roundcubedir}

# Apache with mod_php or php-fpm
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

%if %{with_phpfpm}
# Nginx with php-fpm
install -Dpm 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/nginx/default.d/%{name}.conf
%endif

mkdir -p %{buildroot}%{_sysconfdir}/roundcubemail
install -pDm644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/roundcubemail

# Log files
mkdir -p %{buildroot}/var/log/roundcubemail
# Temp files
mkdir -p %{buildroot}/var/lib/roundcubemail/temp
# GPG keys
mkdir -p %{buildroot}/var/lib/roundcubemail/enigma

cp -pr %SOURCE4 README-rpm.txt

# create empty files for ghost to not remove OLD config (0.9.x)
touch %{buildroot}%{_sysconfdir}/roundcubemail/db.inc.php
touch %{buildroot}%{_sysconfdir}/roundcubemail/main.inc.php
# create empty files for ghost for the NEW config
touch %{buildroot}%{_sysconfdir}/roundcubemail/config.inc.php

# keep any other config files too
mv %{buildroot}%{roundcubedir}/config/* %{buildroot}%{_sysconfdir}/roundcubemail/

# Also move plugins configuration file samples
pushd %{buildroot}%{roundcubedir}/plugins
for plug in $(ls); do
  if [ -f $plug/config.inc.php.dist ]; then
    mv $plug/config.inc.php.dist %{buildroot}%{_sysconfdir}/roundcubemail/$plug.inc.php.dist
  fi
  if [ -d $plug/tests ]; then
    rm -r $plug/tests
  fi
done
popd

# clean up the buildroot
rm -r %{buildroot}%{roundcubedir}/{config,logs,temp}
rm -r %{buildroot}%{roundcubedir}/README.md

%check
: Check our autoloader for needed classes
php -r '
require "%{buildroot}%{roundcubedir}/vendor/autoload.php";
$cl = [ "Auth_SASL", "Crypt_GPG", "Mail_mime", "Net_LDAP2", "Masterminds\\HTML5", "GuzzleHttp\\Client",
        "Net_LDAP3", "Net_Sieve", "Net_SMTP", "PEAR" , "BaconQrCode\\Writer", "RtfHtmlPhp\\Document" ];
$ret = 0;
foreach ($cl as $c) {
  if (class_exists($c)) {
    echo "$c ok\n";
  } else {
    echo("$c is missing\n");
    $ret = 1;
  }
}
exit($ret);
'

%pre
# Drop some old config options to ensure new defaults are used
if [ -f %{_sysconfdir}/%{name}/main.inc.php ]; then
  sed -e "/'temp_dir'/d" \
      -e "/'mime_types'/d" \
      -e "/'log_dir'/d" \
      -i %{_sysconfdir}/%{name}/main.inc.php
fi

%files
%license docs/LICENSE.md
%doc README.md
%doc docs
%{roundcubedir}
%dir %{_sysconfdir}/%{name}
# OLD config files from previous version
%ghost %attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/db.inc.php
%ghost %attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/main.inc.php
# NEW config file
%ghost %attr(0640,root,apache) %config(noreplace) %{_sysconfdir}/%{name}/config.inc.php
# Default upstream values, overwritten on update
%attr(0640,root,apache) %{_sysconfdir}/%{name}/mimetypes.php
%attr(0640,root,apache) %{_sysconfdir}/%{name}/defaults.inc.php
%attr(0640,root,apache) %{_sysconfdir}/%{name}/config.inc.php.sample
%attr(0640,root,apache) %{_sysconfdir}/%{name}/*.inc.php.dist
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%if %{with_phpfpm}
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%endif
%attr(0770,root,apache) %dir /var/log/roundcubemail
%attr(0770,root,apache) %dir /var/lib/roundcubemail
%attr(0770,root,apache) %dir /var/lib/roundcubemail/temp
%attr(0770,root,apache) %dir /var/lib/roundcubemail/enigma
%config(noreplace) %{_sysconfdir}/logrotate.d/roundcubemail

%changelog
%autochangelog
