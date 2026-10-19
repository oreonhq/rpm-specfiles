%global source0_hash 1f6485b92a2ac82986e158b5a503cc0abf034692e5d487d1e1afcbebe2be9d3d
%global github_owner     mnapoli
%global github_name      phpunit-easymock
%global github_version   1.5.0
%global github_commit    3620599d773e9c4924acc7e40061047c75bac574
%global composer_vendor  mnapoli
%global composer_project phpunit-easymock
%global php_min_ver 7.3
%global phpunit8_min_ver 8.5
%global phpunit9_min_ver 9.0
%global with_tests 0%{!?_without_tests:1}
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%global with_rich_dependencies 1
%else
%global with_rich_dependencies 0
%endif
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Helpers to build PHPUnit mocks
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh
BuildArch:     noarch
%if %{with_tests}
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-reflection
BuildRequires:  phpunit8
BuildRequires:  phpunit9
# /oreon:deps
%description
%{summary}.

Autoloader: %{phpdir}/EasyMock/autoload.php

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
\Fedora\Autoloader\Autoload::addPsr4('EasyMock\\', __DIR__);
AUTOLOAD
%install
mkdir -p %{buildroot}%{phpdir}/EasyMock
cp -rp src/* %{buildroot}%{phpdir}/EasyMock/
%oreon_autofiles main

%check

%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/EasyMock/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('EasyMock\\Test\\', __DIR__.'/tests');
BOOTSTRAP
: Upstream tests
RETURN_CODE=0
PHPUNIT=$(which phpunit8)
for PHP_EXEC in "" php73 php74; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
PHPUNIT=$(which phpunit9)
for PHP_EXEC in "" php73 php74 php80; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        $PHP_EXEC $PHPUNIT --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
