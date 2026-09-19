%global source0_hash 2bbcf5940759d0090bab38d3caf321e24eaac8bdcff872695115e18f6e853956

# remirepo/fedora spec file for php-league-container4
#
# Copyright (c) 2016-2025 Shawn Iwinski <shawn@iwin.ski>
#                         Remi Collet <remi@remirepo.net>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     thephpleague
%global github_name      container
%global github_version   4.2.5
%global github_commit    d3cebb0ff4685ff61c749e54b27db49319e2ec00

%global major            4

%global composer_vendor  league
%global composer_project container

# "php": "^7.2 || ^8.0"
%global php_min_ver 7.2
# "psr/container": "^1.1 || ^2.0"
%global psr_container_min_ver 1.1
%global psr_container_max_ver 3

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:       3%{?github_release}%{?dist}
Summary:       A fast and intuitive dependency injection container version %{major}

License:       MIT
URL:           http://container.thephpleague.com/

# GitHub export does not include tests.
# Run php-league-container-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with_tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit8 >= 8.5.17
BuildRequires: (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
## phpcompatinfo (computed from version 3.2.2)
BuildRequires: php-reflection
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(psr/container) >= %{psr_container_min_ver} with php-composer(psr/container) < %{psr_container_max_ver})
# phpcompatinfo (computed from version 3.3.5)
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Provides:      php-composer(psr/container-implementation) =  1.0

%description
A small but powerful dependency injection container that allows you to decouple
components in your application in order to write clean and testable code.

Autoloader: %{phpdir}/League/Container%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    [
        '%{phpdir}/Psr/Container2/autoload.php',
        '%{phpdir}/Psr/Container/autoload.php',
    ]
]);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/League
cp -rp src %{buildroot}%{phpdir}/League/Container%{major}

%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/League/Container%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('League\\Container\\Test\\', __DIR__.'/tests');
require __DIR__ . '/tests/Asset/function.php';
BOOTSTRAP

: cleanup for phpunit8/9
sed -e '/log/d' -i phpunit.xml

: Upstream tests
RETURN_CODE=0
# TODO PHP 8.1, Call to undefined method ReflectionUnionType::getName()
PHPUNIT=$(which phpunit8)
for PHP_EXEC in php php81 php82 php83 php84; do
    if which $PHP_EXEC; then
        FILTER="--filter '^((?!(testResolverResolvesArgumentsViaReflection|testResolverThrowsExceptionWhenReflectionDoesNotResolve)).)*\$'"
        $PHP_EXEC $PHPUNIT $FILTER \
            --bootstrap bootstrap.php \
            --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif

%files
%license LICENSE.md
%doc CHANGELOG.md
%doc composer.json
%doc CONTRIBUTING.md
%doc README.md
%dir %{phpdir}/League
     %{phpdir}/League/Container%{major}

%changelog
%autochangelog
