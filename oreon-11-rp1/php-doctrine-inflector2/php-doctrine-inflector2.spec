%global source0_hash b161b22de99dffa2f6c8fa1609957a73d2d51930b755223fd6a451c6e4290cd5

# remirepo/fedora spec file for php-doctrine-inflector2
#
# Copyright (c) 2013-2023 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      inflector
%global github_version   2.0.8
%global major            2
%global github_commit    f9301a5b2fb1216b2b08f02ba04dc45423db6bff

%global composer_vendor  doctrine
%global composer_project inflector

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       8%{?github_release}%{?dist}
Summary:       Common string manipulations with regard to casing and singular/plural rules

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-inflector-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: phpunit9 >= 9.5
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 2.0.1)
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.1)
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Doctrine Inflector is a small library that can perform string manipulations
with regard to upper-/lowercase and singular/plural forms of words.

Autoloader: %{phpdir}/Doctrine/Inflector%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
phpab --template fedora --output lib/Doctrine/Inflector/autoload.php lib

%install
mkdir -p %{buildroot}%{phpdir}/Doctrine
cp -rp lib/Doctrine/Inflector %{buildroot}%{phpdir}/Doctrine/Inflector%{major}

%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Inflector%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr0('Doctrine\\Tests', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php80 php81 php82 php83; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        phpunit9 --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Doctrine
     %{phpdir}/Doctrine/Inflector%{major}

%changelog
%autochangelog
