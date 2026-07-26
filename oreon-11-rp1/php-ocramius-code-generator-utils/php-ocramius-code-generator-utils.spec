%global source0_hash 51394889feae635de56a4edcdc0f08ab15e83d0992eb898a1a7a3668c3481fd5

#
# Fedora spec file for php-ocramius-code-generator-utils
#
# Copyright (c) 2014-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     Ocramius
%global github_name      CodeGenerationUtils
%global github_version   1.2.0
%global github_commit    02aab6ab303c93f60915d0f6d4ffaf0381a6671b

%global composer_vendor  ocramius
%global composer_project code-generator-utils

# "php": "^8.0"
%global php_min_ver 8.0
# "nikic/php-parser": "^4.10.4"
%global php_parser_min_ver 4.10.4
%global php_parser_max_ver 5

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       11%{?github_release}%{?dist}
Summary:       A set of code generator utilities built on top of PHP-Parsers

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-ocramius-code-generator-utils-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
%if %{with tests}
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
BuildRequires: (php-composer(nikic/php-parser) >= %{php_parser_min_ver} with php-composer(nikic/php-parser) < %{php_parser_max_ver})
# phpcompatinfo (computed from version 1.2.0)
BuildRequires: php-pcre
BuildRequires: php-reflection
BuildRequires: php-spl
# Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      (php-composer(nikic/php-parser) >= %{php_parser_min_ver} with php-composer(nikic/php-parser) < %{php_parser_max_ver})
# phpcompatinfo (computed from version 1.2.0)
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
A set of code generator utilities built on top of PHP-Parsers that ease its use
when combined with Reflection.

Autoloader: %{phpdir}/CodeGenerationUtils/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/CodeGenerationUtils/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

require_once '/usr/share/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('CodeGenerationUtils\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/PhpParser4/autoload.php',
]);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}
cp -rp src/CodeGenerationUtils %{buildroot}%{phpdir}/

%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require '%{buildroot}%{phpdir}/CodeGenerationUtils/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('CodeGenerationUtilsTest\\', __DIR__.'/tests/CodeGenerationUtilsTests');
\Fedora\Autoloader\Autoload::addPsr4('CodeGenerationUtilsTestAsset\\', __DIR__.'/tests/CodeGenerationUtilsTestAsset');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in php php81; do
    if [ "php" = "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/CodeGenerationUtils

%changelog
%autochangelog
