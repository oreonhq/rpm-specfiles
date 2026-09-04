%global source0_hash e9a690ba0e971f230bef09f1e05e2b489bf119419f6531744ea0b08906cdefff

Name:           mrbs
Version:        1.12.2
Release:        1%{?dist}
Summary:        Meeting Room Booking System

License:        GPL-2.0-only
URL:            https://mrbs.sourceforge.net
Source0:        https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        mrbs-httpd.conf
Patch0:         mrbs-1.11.5-fix_autoloader_for_phpmailer.patch

BuildArch:      noarch

Requires:       php >= 7.2.0
# php-imap has been dropped from F34+
%if ! 0%{?fedora} > 33
Requires:       php-imap
%endif
Requires:       php-ldap
Requires:       php-mysqli
Requires:       php-pear-CAS
Requires:       php-pear-File-Passwd
Requires:       php-pear-Mail-Mime
Requires:       php-pgsql
Requires:       php-phpmailer6

Provides:       bundled(js-flatpickr) = 4.6.13
Provides:       bundled(js-html5shiv) = 3.7.3
Provides:       bundled(js-jquery) = 3.7.0
Provides:       bundled(js-jquery-datatables) = 1.13.6
Provides:       bundled(js-jquery-migrate) = 3.4.0
Provides:       bundled(js-jquery-select2) = 4.0.13
Provides:       bundled(js-jquery-ui) = 1.13.2
Provides:       bundled(php-chillerlan-qrcode) = 4.3.4
Provides:       bundled(php-openpsa-ranger) = 0.5.8

%description
The Meeting Room Booking System (MRBS) is a PHP-based application for
booking meeting rooms.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Clean up bundled libs
pushd web
rm -rf File* Mail* PEAR.php
rm -rf lib/PHPMailer/
rm -rf lib/CAS/ lib/CAS.php lib/phpCAS.php
popd

# remove exec perms on the perl scripts
chmod a-x *.pl

%build
## Nothing to build ##

%install
# Install the code
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mrbs
cp -a web/* $RPM_BUILD_ROOT/%{_datadir}/mrbs/

# Move the conf to the proper place
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/mrbs
mv $RPM_BUILD_ROOT/%{_datadir}/mrbs/config.inc.php-sample \
    $RPM_BUILD_ROOT/%{_sysconfdir}/mrbs/config.inc.php
ln -s %{_sysconfdir}/mrbs/config.inc.php \
    $RPM_BUILD_ROOT/%{_datadir}/mrbs/config.inc.php

sed -i \
    -e "s!require_once 'lib/autoload.inc';!require_once '%{_datadir}/mrbs/lib/autoload.inc';!" \
    $RPM_BUILD_ROOT/%{_sysconfdir}/mrbs/config.inc.php

# Apache conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE1} \
    $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/mrbs.conf

%files
%doc AUTHENTICATION ChangeLog INSTALL LANGUAGE NEWS README
%doc README.sqlapi UPGRADE
%doc *.sql *.pl *.php crypt_passwd.example
%license COPYING
%config(noreplace) %{_sysconfdir}/httpd/conf.d/mrbs.conf
%config(noreplace) %{_sysconfdir}/mrbs/config.inc.php
%{_datadir}/mrbs

%changelog
%autochangelog
