%global source0_hash ace5d9d0cd76e629019257dd544cc5b17d1ffa487b2d9c1501ee44794eac8536

#
# Fedora spec file for php-doctrine-inflector
#
# Copyright (c) 2013-2020 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      inflector
%global github_version   1.4.4
%global github_commit    4bd5c1cdfcd00e9e2d8c484f79150f67e5d355d9

%global composer_vendor  doctrine
%global composer_project inflector

# "php": "^7.1 || ^8.0"
%global php_min_ver 7.1

# Build using "--without tests" to disable tests
%global with_tests 0%{!?_without_tests:1}

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       12%{?github_release}%{?dist}
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
BuildRequires: phpunit8
BuildRequires: php(language) >= %{php_min_ver}
## phpcompatinfo (computed from version 1.4.1)
BuildRequires: php-mbstring
BuildRequires: php-pcre
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.4.1)
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

Autoloader: %{phpdir}/Doctrine/Common/Inflector/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
phpab --template fedora --output lib/Doctrine/Common/Inflector/autoload.php lib

%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/

%check
%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Inflector/autoload.php';
\Fedora\Autoloader\Autoload::addPsr0('Doctrine\\Tests', __DIR__.'/tests');
BOOTSTRAP

: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php72 php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        phpunit8 --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
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
%dir %{phpdir}/Doctrine
%dir %{phpdir}/Doctrine/Common
     %{phpdir}/Doctrine/Common/Inflector
     %{phpdir}/Doctrine/Inflector

%changelog
%autochangelog
