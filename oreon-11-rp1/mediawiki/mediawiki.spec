%global source0_hash eeaa82f1c7030c0bbff4bbb8b0e09e625603640f59c034a7400a859dfbe612bf

Summary: A wiki engine
Name: mediawiki
Version: 1.44.3
Release: 3%{?dist}
License: GPL-2.0-or-later
URL: https://www.mediawiki.org/
Source0: https://releases.wikimedia.org/mediawiki/1.44/%{name}-%{version}.tar.gz
Source1: https://releases.wikimedia.org/mediawiki/1.44/%{name}-%{version}.tar.gz.sig
Source2: mediawiki.conf
Source3: README.RPM
Source4: mw-createinstance.in
Source5: mw-updateallinstances.in

BuildArch: noarch

BuildRequires: djvulibre
BuildRequires: perl-generators
BuildRequires: php-cli
BuildRequires: php-gd
BuildRequires: php-intl
BuildRequires: php-pdo
#BuildRequires: php-phpunit-PHPUnit
BuildRequires: php-theseer-autoload
BuildRequires: php-composer(liuggio/statsd-php-client) >= 1.0.18
BuildRequires: php-composer(oojs/oojs-ui) >= 0.51.2
BuildRequires: php-composer(psr/log) >= 1.1.4
BuildRequires: php-composer(wikimedia/assert) >= 0.5.1
BuildRequires: php-composer(wikimedia/cdb) >= 3.0.0
BuildRequires: php-composer(wikimedia/utfnormal) >= 4.0.0
BuildRequires: php-composer(zordius/lightncandy) >= 1.2.6
BuildRequires: php-pear(Mail) >= 2.0.0
BuildRequires: php-pear(Mail_Mime) >= 1.10.12
BuildRequires: php-pear(Net_SMTP) >= 1.12.1
BuildRequires: php-pear(Net_Socket) >= 1.2.2
BuildRequires: python3-devel

Requires: httpd-filesystem
Requires: php(httpd)
Requires: php(language) >= 8.1.0
Requires: php-gd
Requires: php-xml
Requires: diffutils
Recommends: ImageMagick
Requires: php-composer(liuggio/statsd-php-client) >= 1.0.18
Requires: php-composer(oojs/oojs-ui) >= 0.51.2
Requires: php-composer(psr/log) >= 1.1.4
Requires: php-composer(wikimedia/assert) >= 0.5.1
Requires: php-composer(wikimedia/cdb) >= 3.0.0
Requires: php-composer(wikimedia/utfnormal) >= 4.0.0
Requires: php-composer(zordius/lightncandy) >= 1.2.6
Requires: php-pear(Mail) >= 2.0.0
Requires: php-pear(Mail_Mime) >= 1.10.12
Requires: php-pear(Net_SMTP) >= 1.12.1
Requires: php-pear(Net_Socket) >= 1.2.2

# Update script call command-line php
Requires(post): php-cli

Obsoletes: php-mediawiki-at-ease <= 1.1.0
Obsoletes: php-wikimedia-ip-set <= 3.1.0
Obsoletes: php-wikimedia-avro <= 1.9.0

Provides: bundled(php-bacon-bacon-qr-code) = 3.0.1
Provides: bundled(php-christian-riesen-base32) = 1.6.0
Provides: bundled(php-composer-semver) = 3.4.3
Provides: bundled(php-dasprid-enum) = 1.0.6
Provides: bundled(php-endroid-qr-code) = 5.1.0
Provides: bundled(php-firebase-php-jwt) = 6.10.0
Provides: bundled(php-guzzlehttp-guzzle) = 7.9.3
Provides: bundled(php-guzzlehttp-promises) = 2.0.4
Provides: bundled(php-guzzlehttp-psr7) = 2.7.0
Provides: bundled(php-jakobo-hotp-php) = 2.0.0
Provides: bundled(php-justinrainbow-json-schema) = 5.3.0
Provides: bundled(php-mck89-peast) = 1.17.0
Provides: bundled(php-monolog-monolog) = 2.9.3
Provides: bundled(php-pear-console_getopt) = 1.4.3
Provides: bundled(php-pear-Net_URL2) = 2.2.3
Provides: bundled(php-pear-pear-core-minimal) = 1.10.16
Provides: bundled(php-pear-pear_exception) = 1.0.2
Provides: bundled(php-psr-container) = 1.1.2
Provides: bundled(php-psr-http-client) = 1.0.3
Provides: bundled(php-psr-http-factory) = 1.1.0
Provides: bundled(php-psr-http-message) = 1.1
Provides: bundled(php-ralouphie-getallheaders) = 3.0.3
Provides: bundled(php-symfony-deprecation-contracts) = 2.5.4
Provides: bundled(php-symfony-polyfill-php82) = 1.32.0
Provides: bundled(php-symfony-polyfill-php83) = 1.32.0
Provides: bundled(php-symfony-polyfill-php84) = 1.32.0
Provides: bundled(php-symfony-polyfill-php85) = 1.33.0
Provides: bundled(php-symfony-yaml) = 5.4.45
Provides: bundled(php-wikimedia-at-ease) = 3.0.0
Provides: bundled(php-wikimedia-common-passwords) = 0.5.1
Provides: bundled(php-wikimedia-composer-merge-plugin) = 2.1.0
Provides: bundled(php-wikimedia-equivset) = 1.7.1
Provides: bundled(php-wikimedia-base-convert) = 2.0.2
Provides: bundled(php-wikimedia-bcp-47-code) = 2.0.1
Provides: bundled(php-wikimedia-cldr-plural-rule-parser) = 3.0.0
Provides: bundled(php-wikimedia-composer-merge-plugin) = 2.1.0
Provides: bundled(php-wikimedia-css-sanitizer) = 5.5.0
Provides: bundled(php-wikimedia-cssjanus) = 2.3.0
Provides: bundled(php-wikimedia-html-formatter) = 4.1.0
Provides: bundled(php-wikimedia-ip-utils) = 5.0.0
Provides: bundled(php-wikimedia-json-codec) = 3.0.3
Provides: bundled(php-wikimedia-langconv) = 0.4.2
Provides: bundled(php-wikimedia-less.php) = 5.1.2
Provides: bundled(php-wikimedia-minify) = 2.9.0
Provides: bundled(php-wikimedia-normalized-exception) = 2.1.1
Provides: bundled(php-wikimedia-object-factory) = 5.0.1
Provides: bundled(php-wikimedia-parsoid) = 0.21.1
Provides: bundled(php-wikimedia-php-session-serializer) = 3.0.1
Provides: bundled(php-wikimedia-purtle) = 2.0.0
Provides: bundled(php-wikimedia-relpath) = 4.0.2
Provides: bundled(php-wikimedia-remex-html) = 4.1.2
Provides: bundled(php-wikimedia-request-timeout) = 2.0.2
Provides: bundled(php-wikimedia-running-stat) = 2.1.0
Provides: bundled(php-wikimedia-scoped-callback) = 5.0.0
Provides: bundled(php-wikimedia-services) = 4.0.0
Provides: bundled(php-wikimedia-shellbox) = 4.2.0
Provides: bundled(php-wikimedia-timestamp) = 4.2.0
Provides: bundled(php-wikimedia-wait-condition-loop) = 2.0.2
Provides: bundled(php-wikimedia-wrappedstring) = 4.0.1
Provides: bundled(php-wikimedia-xmp-reader) = 0.10.2
Provides: bundled(php-wikimedia-zest-css) = 3.0.2

%description
MediaWiki is the software used for Wikipedia and the other Wikimedia
Foundation websites. Compared to other wikis, it has an excellent
range of features and support for high-traffic websites using multiple
servers

This package supports wiki farms. Read the instructions for creating wiki
instances under %{_pkgdocdir}/README.RPM.
Remember to remove the config dir after completing the configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Remove extension as it ships a bundled lua binary
rm -rf extensions/Scribunto
# Remove bundled PHP libraries in order to use system versions
rm -rf vendor/composer/*php
rm -rf vendor/composer/*json
rm -rf vendor/composer/LICENSE
rm -rf vendor/liuggio
rm -rf vendor/oojs
#rm -rf vendor/oyejorge
rm -rf vendor/pear/mail
rm -rf vendor/pear/mail_mime
rm -rf vendor/pear/mail_mime-decode
rm -rf vendor/psr/log
rm -rf vendor/wikimedia/assert
rm -rf vendor/wikimedia/avro
rm -rf vendor/wikimedia/cdb
rm -rf vendor/wikimedia/composer-merge-plugin
rm -rf vendor/wikimedia/ip-set
rm -rf vendor/wikimedia/utfnormal
rm -rf vendor/zordius
ln -s %{_datadir}/php/Liuggio vendor/liuggio-shared
ln -s %{_datadir}/php/OOUI vendor/oojs-shared
#ln -s %%{_datadir}/php/lessphp vendor/oyejorge-shared
ln -s %{_datadir}/pear/Mail vendor/pear/mail-shared
ln -s %{_datadir}/php/Psr vendor/psr-shared
ln -s %{_datadir}/php/Wikimedia vendor/wikimedia/assert-shared
ln -s %{_datadir}/php/avro vendor/wikimedia/avro-shared
ln -s %{_datadir}/php/Cdb vendor/wikimedia/cdb-shared
ln -s %{_datadir}/php/IPSet vendor/wikimedia/ip-set-shared
ln -s %{_datadir}/php/UtfNormal vendor/wikimedia/utfnormal-shared
ln -s %{_datadir}/php/zordius vendor/zordius-shared
# Fix up Python shebangs
%py3_shebang_fix \
  maintenance/language/zhtable/Makefile.py \
  extensions/ConfirmEdit/captcha.py \
  extensions/SyntaxHighlight_GeSHi/pygments/create_pygmentize_bundle

%build
%{_bindir}/php -d memory_limit=1G %{_bindir}/phpab --follow --tolerant --output vendor/autoload.php vendor
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/at-ease/src/AtEase.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/base-convert/src/Functions.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/html-formatter/src/HtmlFormatter.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/php-session-serializer/src/PhpSessionSerializer.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/timestamp/src/defines.php';" >> vendor/autoload.php
echo "require dirname(dirname(__FILE__)) . '/vendor/wikimedia/relpath/src/RelPath.php';" >> vendor/autoload.php

%install
# move away the documentation to the final folder.
cp -p %{SOURCE3} .

# now copy the rest to the buildroot.
mkdir -p %{buildroot}%{_datadir}/mediawiki
cp -a * %{buildroot}%{_datadir}/mediawiki/

# remove unneeded parts
rm -fr %{buildroot}%{_datadir}/mediawiki/{t,test,tests}
rm -fr %{buildroot}%{_datadir}/mediawiki/includes/zhtable
find %{buildroot}%{_datadir}/mediawiki/ \
  \( -name .htaccess -or -name \*.cmi \) \
  | xargs -r rm
rm -fr %{buildroot}%{_datadir}/mediawiki/maintenance/hhvm/

# fix permissions
find %{buildroot}%{_datadir}/mediawiki -name \*.pl | xargs -r chmod +x
chmod +x %{buildroot}%{_datadir}/mediawiki/maintenance/storage/make-blobs
chmod +x %{buildroot}%{_datadir}/mediawiki/extensions/ConfirmEdit/captcha.py

# remove version control/patch files
find %{buildroot} -name .svnignore | xargs -r rm
find %{buildroot} -name \*.commoncode | xargs -r rm
find %{buildroot} -name .gitreview | xargs -r rm
find %{buildroot} -name .jshintignore | xargs -r rm
find %{buildroot} -name .jshintrc | xargs -r rm

# placeholder for a default instance
mkdir -p %{buildroot}/var/www/wiki

mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -p -m 0644 %{SOURCE2} \
  %{buildroot}%{_sysconfdir}/httpd/conf.d/mediawiki.conf

# tools for keeping mediawiki instances current
mkdir -p %{buildroot}%{_sbindir}
sed -e's,@datadir@,%{_datadir},g' -e's,@sysconfdir@,%{_sysconfdir},g' \
  < %{SOURCE4} > %{buildroot}%{_sbindir}/mw-createinstance
sed -e's,@datadir@,%{_datadir},g' -e's,@sysconfdir@,%{_sysconfdir},g' \
  < %{SOURCE5} > %{buildroot}%{_sbindir}/mw-updateallinstances
chmod 0755 %{buildroot}%{_sbindir}/mw-*
mkdir %{buildroot}%{_sysconfdir}/mediawiki
echo /var/www/wiki > %{buildroot}%{_sysconfdir}/mediawiki/instances

%check
php maintenance/install.php \
    --dbtype sqlite \
    --dbname mediawiki-test \
    --dbpath /tmp \
    --pass test123456 \
    Test test
cd tests/phpunit
# Database tests currently fail on the 1.26 release series
# https://phabricator.wikimedia.org/T122301
# KafkaHandlerTest tests now fail in 1.26.3
#make database
# Some tests now fail on the 1.27 release series.
#FLAGS="--exclude-group Broken,ParserFuzz,Destructive,Database,Stub,default" make phpunit

%post
%{_sbindir}/mw-updateallinstances >> /var/log/mediawiki-updates.log 2>&1 || :

%files
%doc FAQ HISTORY README.md README.RPM RELEASE-NOTES-1.44 UPGRADE CREDITS docs
%license COPYING
%{_datadir}/mediawiki
/var/www/wiki
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mediawiki.conf
%dir %{_sysconfdir}/mediawiki
%config(noreplace) %{_sysconfdir}/mediawiki/instances
%{_sbindir}/mw-createinstance
%{_sbindir}/mw-updateallinstances

%changelog
%autochangelog
