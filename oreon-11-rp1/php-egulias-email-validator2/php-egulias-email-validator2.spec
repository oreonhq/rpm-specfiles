%global source0_hash 95206c9a12369e77d50e07c15e8afc95008f950d56f587442e571acc9583b28d

# remirepo/fedora spec file for php-egulias-email-validator2
#
# Copyright (c) 2014-2021 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     egulias
%global github_name      EmailValidator
%global github_version   2.1.25
%global github_commit    0dbf5d78455d4d6a41d186da50adc1122ec066f4
%global github_short     %(c=%{github_commit}; echo ${c:0:7})
%global major            2

%global composer_vendor  egulias
%global composer_project email-validator

# "php": ">= 5.5"
%global php_min_ver 5.5
# "doctrine/lexer": "^1.0.1"
%global doctrine_lexer_min_ver 1.0.1
%global doctrine_lexer_max_ver 2.0

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       13%{?github_release}%{?dist}
Summary:       A library for validating emails

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:       %{name}-%{github_version}-%{github_short}.tgz
Source1:       makesrc.sh

# adapt for recent PHPUnit
Patch0:        %{name}-phpunit.patch

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json (require-dev)
#    "dominicsayers/isemail": "^3.0.7",
#    "phpunit/phpunit": "^4.8.36|^7.5.15",
#    "satooshi/php-coveralls": "^1.0.1"
%if 0%{?fedora} >= 31 || 0%{?rhel} >= 9
BuildRequires: (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver})
%global phpunit %{_bindir}/phpunit9
%else
BuildRequires:  php-doctrine-lexer  >= %{doctrine_lexer_min_ver}
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires:  %{phpunit}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 2.1.2)
BuildRequires: php-dom
BuildRequires: php-filter
BuildRequires: php-intl
BuildRequires: php-pcre
BuildRequires: php-spl
## Autoloader
BuildRequires: php-fedora-autoloader-devel
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/lexer) >= %{doctrine_lexer_min_ver} with php-composer(doctrine/lexer) <  %{doctrine_lexer_max_ver})
# phpcompatinfo (computed from version 2.1.2)
Requires:      php-intl
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
%{summary}.

Autoloader: %{phpdir}/Egulias/EmailValidator%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}
%patch -P0 -p1 -b .phpunit

%build
: Create autoloader
phpab --template fedora \
      --output src/autoload.php \
      src

cat <<'AUTOLOAD' | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required(array(
    '%{phpdir}/Doctrine/Common/Lexer/autoload.php',
));
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/Egulias
cp -rp src %{buildroot}%{phpdir}/Egulias/EmailValidator%{major}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once "%{buildroot}%{phpdir}/Egulias/EmailValidator%{major}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('Egulias\\Tests\\', dirname(__DIR__) . "/tests");
EOF

: Skip online tests
rm tests/EmailValidator/Validation/DNSCheckValidationTest.php
rm tests/EmailValidator/Validation/SpoofCheckValidationTest.php

: Upstream tests
ret=0
for cmdarg in "php %{phpunit}" "php72 %{_bindir}/phpunit8" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif

%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{phpdir}/Egulias
     %{phpdir}/Egulias/EmailValidator%{major}

%changelog
%autochangelog
