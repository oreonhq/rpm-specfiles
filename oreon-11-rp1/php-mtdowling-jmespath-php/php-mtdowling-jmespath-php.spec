%global source0_hash d8e603f9b143d33e509cf30b46133794dfe0c1c38754b9ba65782f236cd1028d

#
# Fedora spec file for php-mtdowling-jmespath-php
#
# Copyright (c) 2015-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%bcond_without           tests

%global github_owner     jmespath
%global github_name      jmespath.php
%global github_version   2.6.0
%global github_commit    42dae2cbd13154083ca6d70099692fef8ca84bfb

%global composer_vendor  mtdowling
%global composer_project jmespath.php

# "php": "^5.4 || ^7.0 || ^8.0"
%global php_min_ver 5.4

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-jmespath-php
Version:       %{github_version}
Release:       10%{?github_release}%{?dist}
Summary:       Declaratively specify how to extract elements from a JSON document

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
# GitHub export does not include tests.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit7 >= 7.5.15
## phpcompatinfo (computed from version 2.5.0)
BuildRequires: php-json
BuildRequires: php-mbstring
BuildRequires: php-spl
%endif
## Autoloader
BuildRequires: php-composer(fedora/autoloader)

Requires:      php-cli
# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.5.0)
Requires:      php-json
Requires:      php-mbstring
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
JMESPath (pronounced "jaymz path") allows you to declaratively specify how to
extract elements from a JSON document. jmespath.php allows you to use JMESPath
in PHP applications with PHP data structures.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('JmesPath\\', __DIR__);

require_once __DIR__ . '/JmesPath.php';
AUTOLOAD

: Modify bin script
sed "s#.*require.*autoload.*#require_once '%{phpdir}/JmesPath/autoload.php';#" \
    -i bin/jp.php

%build
# Empty build section, nothing to build

%install
: Lib
mkdir -p %{buildroot}%{phpdir}/JmesPath
cp -rp src/* %{buildroot}%{phpdir}/JmesPath/

: Bin
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 bin/jp.php %{buildroot}%{_bindir}/

%check
%if %{with tests}
: Run tests
RETURN_CODE=0
for PHP_EXEC in php php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC %{_bindir}/phpunit7 \
                --bootstrap %{buildroot}%{phpdir}/JmesPath/autoload.php \
                --verbose || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.rst
%doc composer.json
%{phpdir}/JmesPath
%{_bindir}/jp.php

%changelog
%autochangelog
