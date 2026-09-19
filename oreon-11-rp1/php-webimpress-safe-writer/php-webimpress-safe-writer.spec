%global source0_hash c50fad24180132e30c712b13b76af6fed3c1f09a21f16ce3199834cdd11e2d50

#
# Fedora spec file for php-webimpress-safe-writer
#
# Copyright (c) 2020-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%bcond_without           tests

%global github_owner     webimpress
%global github_name      safe-writer
%global github_version   2.2.0
%global github_commit    9d37cc8bee20f7cb2f58f6e23e05097eab5072e6

%global composer_vendor  webimpress
%global composer_project safe-writer

# "php": "^7.3 || ^8.0"
%global php_min_ver 7.3

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       13%{?github_release}%{?dist}
Summary:       Tool to write files safely, to avoid race conditions

# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests
# Run php-webimpress-safe-writer-get-source.sh to create full source
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9 >= 9.5.4
## phpcompatinfo for version 2.0.0
BuildRequires: php-json
BuildRequires: php-spl
## Autoloader
BuildRequires: php-composer(fedora/autoloader)
%endif

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo for version 2.0.0
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Write files safely to avoid race conditions when the same file is written
multiple times in a short time period.

Autoloader: %{phpdir}/Webimpress/SafeWriter/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

mv LICENSE.md LICENSE

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Webimpress\\SafeWriter\\', __DIR__);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/Webimpress
cp -rp src %{buildroot}%{phpdir}/Webimpress/SafeWriter

%check
%if %{with tests}
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit9)
for PHP_EXEC in php php73 php74 php80; do
    if [ "php" == "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose \
            --bootstrap %{buildroot}%{phpdir}/Webimpress/SafeWriter/autoload.php \
            --filter '^((?!(testMultipleWriters)).)*$' \
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
%dir %{phpdir}/Webimpress
     %{phpdir}/Webimpress/SafeWriter

%changelog
%autochangelog
