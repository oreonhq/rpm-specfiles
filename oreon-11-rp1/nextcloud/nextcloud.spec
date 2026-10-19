%global source0_hash d8c165e764a7a4de82eb3dec510d66e19f2d82218572604af9c15d99a98a29a0
%global distro epel
Name:           nextcloud
Version:        35.0.0
Release:        1%{?dist}
Summary:        Private file sync and share server
License:        AGPL-3.0-or-later AND LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD AND Apache-2.0 AND WTFPL AND LicenseRef-Callaway-CC-BY-SA AND GPL-3.0-or-later AND Adobe-2006
URL:            http://nextcloud.com
Source0:        https://download.nextcloud.com/server/releases/%{name}-%{version}.tar.bz2
Source1:        %{name}-config.php
Source2:       %{name}-systemd-timer.service
Source3:       %{name}-systemd-timer.timer
Source100:      %{name}-httpd.conf
Source101:      %{name}-access-httpd.conf.avail
Source102:      %{name}-auth-any.inc
Source103:      %{name}-auth-local.inc
Source104:      %{name}-auth-none.inc
Source105:      %{name}-defaults.inc
Source200:      %{name}-default-nginx.conf
Source201:      %{name}-conf-nginx.conf
Source202:      %{name}-php-fpm.conf
Source203:      %{name}-php.ini
Source300:      %{name}-README.fedora
Source301:      %{name}-mysql.txt
Source302:      %{name}-postgresql.txt
Source303:      %{name}-MIGRATION.fedora
Patch0:         0000-disable-update-version-check.patch
Patch1:         nextcloud-integritycheck-exclusion.patch
BuildArch:      noarch
Requires:       %{name}-webserver = %{version}-%{release}
Requires:       %{name}-database = %{version}-%{release}
Requires:       php-bcmath
Requires:       php-cli
Requires:       php-curl
Requires:       php-dom
Requires:       php-exif
Requires:       php-fileinfo
Requires:       php-filter
Requires:       php-gd
Requires:       php-gmp
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-pdo
Requires:       php-pecl-apcu
Requires:       php-pecl-imagick
Requires:       php-pecl-memcached
Requires:       (php-pecl-redis6 or php-pecl-redis5)
Requires:       php-process
Requires:       php-session
Requires:       php-simplexml
Requires:       php-smbclient
Requires:       php-spl
Recommends:     php-sodium
Requires:       php-opcache
Requires:       php-xmlwriter
Requires:       php-zip
%{?systemd_requires}
Requires:       %{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
Provides:       bundled(jquery-ui-multiselect) = 1.13
Provides:       bundled(zxcvbn) = 4.4.2
# oreon:deps
BuildRequires:  composer-generators
BuildRequires:  php(language)
BuildRequires:  php-pear
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
NextCloud gives you universal access to your files through a web interface or
WebDAV. It also provides a platform to easily view & sync your contacts,
calendars and bookmarks across all your devices and enables basic editing right
on the web. NextCloud is extendable via a simple but powerful API for
applications and plugins.

%package httpd
Summary:        Httpd integration for NextCloud
Provides:       %{name}-webserver = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       php-fpm httpd
%description httpd
%{summary}.

%package nginx
Summary:        Nginx integration for NextCloud
Provides:       %{name}-webserver = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       php-fpm nginx
%description nginx
%{summary}.

%package mysql
Summary:        MySQL database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       php-mysqlnd
%description mysql
This package ensures the necessary dependencies are in place for NextCloud to
work with MySQL / MariaDB databases. It does not require a MySQL / MariaDB
server to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable a MySQL / MariaDB server package. See README.mysql for
more details.

%package postgresql
Summary:        PostgreSQL database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
Requires:       php-pgsql
%description postgresql
This package ensures the necessary dependencies are in place for NextCloud to
work with a PostgreSQL database. It does not require the PostgreSQL server
package to be installed, as you may well wish to use a remote database
server.

If you want the database to be on the same system as NextCloud itself, you must
also install and enable the PostgreSQL server package. See README.postgresql
for more details.

%package sqlite
Summary:        SQLite 3 database support for NextCloud
Provides:       %{name}-database = %{version}-%{release}
Requires:       %{name} = %{version}-%{release}
%description sqlite
This package ensures the necessary dependencies are in place for NextCloud to
work with an SQLite 3 database stored on the local system.

%prep

%autosetup -n %{name} -p1

# Fix php shebang in occ
sed -ri 's\^#!/usr/bin/env php$\#!%{_bindir}/php\' occ

# patch backup files and .git stuff
find . -name \*.orig    -type f -delete -print
find . -name .gitignore -type f -delete -print
find . -name .github    -type d -prune -exec rm -r {} \; -print

# fix CLI upgrade advise on splash screen
sed -i -e 's#\./\(occ upgrade\)#sudo -u apache php /usr/share/nextcloud/\1#' core/templates/update.admin.php

# prepare package doc
cp %{SOURCE300} README.%{distro}
cp %{SOURCE301} README.mysql
cp %{SOURCE302} README.postgresql
cp %{SOURCE303} MIGRATION.%{distro}

# point the reader to the correct README filename
sed -i 's/distro/%{distro}/g' README.%{distro}

# Locate license files and put them sensibly in place
# get rid of all composer licenses
find -wholename "*/composer/LICENSE" -exec mv {} composer-LICENSE \;

# Deal with licenses automatically
find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' \) | { while read a ; do mv "$a" $(echo $a | sed "s_^./__" | tr "/ " "__" )-LICENSE ; done ; }
find . -mindepth 2 -name '*COPYING*' | { while read a ; do mv "$a" $(echo $a | sed "s_^./__" | tr "/ " "__" )-COPYING ; done ; }

# case-sensitive list of partial matches to exclude from the nextcloud integrity checker
# include readme, license, other docs, and any files we move or patch during the build
excludedFilenames="
README
readme
LICENSE
LICENCE
license
copying
COPYING
AUTHORS
htaccess
gitignore
user.ini
update.admin.php
Updater.php
occ
Checker.php
"

# nextcloud source files use tabs rather than spaces, ew
tabs="				"
cr="
"

# Add quotes, commas, and escaped newlines
for f in $excludedFilenames; do
  formattedlist="$formattedlist$tabs'$f',\\$cr"
done

# look for our sed placeholder we patched in earlier, then insert our formatted list of keywords
sed -i "s|//sedplaceholder|${formattedlist}|" lib/private/IntegrityCheck/Checker.php

# Build nextcloud-defaults.inc from upstream .htaccess. We will install it later.
cat .htaccess >> %{SOURCE105}

%check

: Check for leftover license files
find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \)
nb=$( find . -mindepth 2 \( -name '*LICENSE*' -o -name '*LICENCE*' -o  -name '*COPYING*' \) | wc -l )
if [ $nb -gt 0 ]
  then
  false Found unexpected licenses to verify
fi
%build

%install
install -dm 755 %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/data
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/apps
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
for d in $(find . -mindepth 1 -maxdepth 1 -type d | grep -v config); do
    cp -a "$d" %{buildroot}%{_datadir}/%{name}
done
for f in {*.php,*.html,robots.txt}; do
    install -pm 644 "$f" %{buildroot}%{_datadir}/%{name}
done
install -pm 755 occ %{buildroot}%{_datadir}/%{name}
ln -s ../../../%{_sysconfdir}/%{name} %{buildroot}%{_datadir}/%{name}/config
ln -s ../pki/ca-trust/extracted/pem/tls-ca-bundle.pem %{buildroot}%{_sysconfdir}/%{name}/ca-bundle.crt
install -pm 644 %{SOURCE1}    %{buildroot}%{_sysconfdir}/%{name}/config.php
install -Dpm 644 %{SOURCE100} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE101} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}-access.conf.avail
install -Dpm 644 %{SOURCE102} %{SOURCE103} %{SOURCE104} %{SOURCE105} \
    %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -Dpm 644 %{SOURCE200} \
    %{buildroot}%{_sysconfdir}/nginx/default.d/%{name}.conf
install -Dpm 644 %{SOURCE201} \
    %{buildroot}%{_sysconfdir}/nginx/conf.d/%{name}.conf
install -Dpm 644 %{SOURCE202} \
    %{buildroot}%{_sysconfdir}/php-fpm.d/%{name}.conf
install -Dpm 644 %{SOURCE203} \
    %{buildroot}%{_sysconfdir}/php.d/60-%{name}.ini
install -Dpm 644 %{SOURCE2} %{buildroot}%{_unitdir}/nextcloud-cron.service
install -Dpm 644 %{SOURCE3} %{buildroot}%{_unitdir}/nextcloud-cron.timer
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

INSTALLED=$(grep -c secret /etc/nextcloud/config.php)
if [ "${INSTALLED}" -eq "0" ]; then
  echo "First time installation, enabling installation wizard"
  touch %{_sysconfdir}/%{name}/CAN_INSTALL
  chown apache:apache %{_sysconfdir}/%{name}/CAN_INSTALL
fi
/usr/bin/systemctl restart php-fpm.service > /dev/null 2>&1 || :
%post httpd

/usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
/usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
%postun httpd

if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload httpd.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi
%post nginx

/usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
/usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
%postun nginx

if [ $1 -eq 0 ]; then
  /usr/bin/systemctl reload nginx.service > /dev/null 2>&1 || :
  /usr/bin/systemctl reload php-fpm.service > /dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list
%files -n nextcloud-httpd -f %{oreon_filedir}/nextcloud-httpd.list
%files -n nextcloud-nginx -f %{oreon_filedir}/nextcloud-nginx.list
%files -n nextcloud-mysql -f %{oreon_filedir}/nextcloud-mysql.list
%files -n nextcloud-postgresql -f %{oreon_filedir}/nextcloud-postgresql.list
%files -n nextcloud-sqlite -f %{oreon_filedir}/nextcloud-sqlite.list

%changelog

%autochangelog
