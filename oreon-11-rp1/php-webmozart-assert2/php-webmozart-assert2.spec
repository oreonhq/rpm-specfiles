%global source0_hash 1fc89668025322b1b2fe87b52432afca197ca2d3611d35e28eb3df0d45e012c5

# remirepo/Fedora spec file for php-webmozart-assert
#
# Copyright (c) 2020-2025 Remi Collet
# Copyright (c) 2016-2020 Shawn Iwinski
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

# enable bootstrap when need to provide a new autoloader
%global bootstrap 0
%global github_owner     webmozart
%global github_name      assert
%global github_version   2.1.6
%global github_commit    ff31ad6efc62e66e518fbab1cde3453d389bcdc8
%global github_short     %(c=%{github_commit}; echo ${c:0:7})
%global major            2

%global composer_vendor  webmozart
%global composer_project assert

# "php": "^8.2"
%global php_min_ver 8.2

# PHPUnit
%global phpunit_require phpunit11
%global phpunit_exec    phpunit11

%if %{bootstrap}
# Build using "--with tests" to enable tests
%global with_tests 0%{?_with_tests:1}
%else
# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Assertions to validate method input/output with nice error messages

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-webmozart-assert-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_short}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-ctype
BuildRequires: %{phpunit_require}
## phpcompatinfo (computed from version 1.7.0)
BuildRequires: php-mbstring
BuildRequires: php-simplexml
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-ctype
# phpcompatinfo (computed from version 1.7.0)
Requires:      php-mbstring
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This library contains efficient assertions to test the input and output of your
methods. With these assertions, you can greatly reduce the amount of coding
needed to write a safe implementation.

All assertions in the Assert class throw an \InvalidArgumentException if they
fail.

Autoloader: %{phpdir}/Webmozart/Assert%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Webmozart\\Assert\\', __DIR__);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/Webmozart
cp -rp src %{buildroot}%{phpdir}/Webmozart/Assert%{major}

%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
\Fedora\Autoloader\Autoload::addPsr4('Webmozart\\Assert\\Tests\\', __DIR__.'/tests');
\Fedora\Autoloader\Autoload::addPsr4('Webmozart\\Assert\\Bin\\', __DIR__.'/bin/src');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which %{phpunit_exec})
for PHP_EXEC in php82 php83 php84 php85; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC \
            -d auto_prepend_file=%{buildroot}%{phpdir}/Webmozart/Assert%{major}/autoload.php \
            $PHPUNIT \
                --bootstrap bootstrap.php \
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
%dir %{phpdir}/Webmozart
     %{phpdir}/Webmozart/Assert%{major}

%changelog
%autochangelog
