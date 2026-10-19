%global source0_hash a3645b25d573428891d7413ca091cfee9fc03733af805a935214113dd4da6bf6
%global gh_commit    d1ac35d784bf9f5e61b424901d5a014967f15b12
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     PHPMailer
%global gh_project   PHPMailer
%global pk_vendor    phpmailer
%global pk_project   phpmailer
%global ns_vendor    PHPMailer
%global ns_project   PHPMailer
%global major        6
%bcond_without       tests
%global php_home     %{_datadir}/php
Name:           php-%{pk_project}%{major}
Version:        6.12.0
Release:        1%{?dist}
Summary:        Full-featured email creation and transfer class for PHP
License:        LGPL-2.1-only
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Source2:        PHPMailerRpmTest.php
Patch0:         %{name}-layout.patch
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 5.5
Requires:       php-ctype
Recommends:     php-imap
Requires:       php-intl
Requires:       php-mbstring
Requires:       php-openssl
Suggests:       php-composer(psr/log)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(yoast/phpunit-polyfills) >= 1.0.4 with php-composer(yoast/phpunit-polyfills) < 2)
BuildRequires:  /usr/bin/phpunit9
BuildRequires:  /usr/bin/smtp-sink
BuildRequires:  php(language)
BuildRequires:  php-ctype
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-intl
BuildRequires:  php-mbstring
BuildRequires:  php-openssl
# /oreon:deps
%description
PHPMailer - A full-featured email creation and transfer class for PHP

Class Features
* Probably the world's most popular code for sending email from PHP!
* Used by many open-source projects:
  WordPress, Drupal, 1CRM, SugarCRM, Yii, Joomla! and many more
* Integrated SMTP support - send without a local mail server
* Send emails with multiple To, CC, BCC and Reply-to addresses
* Multipart/alternative emails for mail clients that do not read HTML email
* Add attachments, including inline
* Support for UTF-8 content and 8bit, base64, binary, and quoted-printable
  encodings
* SMTP authentication with LOGIN, PLAIN, CRAM-MD5 and XOAUTH2 mechanisms
  over SSL and SMTP+STARTTLS transports
* Validates email addresses automatically
* Protect against header injection attacks
* Error messages in 47 languages!
* DKIM and S/MIME signing support
* Compatible with PHP 5.5 and later
* Namespaced to prevent name clashes
* Much more!

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm
find src -name \*.rpm -delete

cp %{SOURCE2} test/PHPMailerRpmTest.php

cat << 'EOF' | tee src/autoload.php
<?php
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('PHPMailer\\PHPMailer\\', __DIR__);
\Fedora\Autoloader\Dependencies::optional(array(
    '%{php_home}/Psr/Log/autoload.php',
));
EOF

%build

%install
mkdir -p        %{buildroot}/%{php_home}/%{ns_vendor}
cp -pr src      %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}
cp -pr language %{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/language
%oreon_autofiles main

%check

%if %{with tests}
: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{buildroot}/%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
require_once '%{php_home}/Yoast/PHPUnitPolyfills/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('PHPMailer\\Test\\', dirname(__DIR__) . '/test');
EOF
sed -e '/colors/d;s/logging/nologging/' phpunit.xml.dist > phpunit.xml
: Start fake MTA and test environment
PORT=$(expr 2500 + %{?fedora}%{?rhel})
sed -e "s/2500/$PORT/" test/testbootstrap-dist.php > test/testbootstrap.php
mkdir -p build/logs
chmod +x test/fakesendmail.sh
pushd build
  smtp-sink -d "%%d.%%H.%%M.%%S" localhost:$PORT 1000 &>/dev/null &
  SMTPPID=$!
popd
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    $cmd  -d "sendmail_path=$PWD/test/fakesendmail.sh -t -i " \
      %{phpunit} \
         --exclude slow,pop3,languages \
         || ret=1
  fi
done
: Cleanup
kill $SMTPPID
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
