%global source0_hash 260a9f32a6de7987b7ffc7d909fb2094d04c378b1344464f1edab0a8d1b04008

# remirepo/fedora spec file for php-composer-ca-bundle
#
# SPDX-FileCopyrightText:  Copyright 2016-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    961a5e4056dd2e4a2eedcac7576075947c28bf63
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     composer
%global gh_project   ca-bundle
%global php_home     %{_datadir}/php

Name:           php-composer-ca-bundle
Version:        1.5.10
Release:        2%{?dist}
Summary:        Lets you find a path to the system CA

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get everything, despite .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Never bundle a CA file
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-openssl
BuildRequires:  php-pcre
BuildRequires:  php-cli
# From composer.json, "require": {
#        "symfony/phpunit-bridge": "^8 || ^9",
#        "phpstan/phpstan": "^1.10",
#        "psr/log": "^1.0",
#        "symfony/process": "^4.0 || ^5.0 || ^6.0 || ^7.0"
BuildRequires:  phpunit10
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
# ca-certificates
BuildRequires:  %{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
%endif

# From composer.json, "require": {
#        "ext-openssl": "*",
#        "ext-pcre": "*",
#        "php": "^7.2 || ^8.0"
Requires:       php(language) >= 7.2
Requires:       php-openssl
Requires:       php-pcre
# From phpcompatinfo report for version 1.0.3
#nothing
# Autoloader
Requires:       php-composer(fedora/autoloader)
# ca-certificates
Requires:       %{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
Small utility library that lets you find a path to the system CA bundle.

Autoloader: %{php_home}/Composer/CaBundle/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm
find src -name \*.rpm -exec rm {} \;

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{gh_owner}/%{gh_project} and its dependencies */

require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Composer\\CaBundle\\', __DIR__);
EOF

%build
# Empty build section, most likely nothing required.

%install
: Library
mkdir -p   %{buildroot}%{php_home}/Composer/
cp -pr src %{buildroot}%{php_home}/Composer/CaBundle

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/Composer/CaBundle/autoload.php';
EOF

ret=0
%{_bindir}/phpunit10 --migrate-configuration

for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit10 --no-coverage || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md
%dir %{php_home}/Composer
     %{php_home}/Composer/CaBundle

%changelog
%autochangelog
