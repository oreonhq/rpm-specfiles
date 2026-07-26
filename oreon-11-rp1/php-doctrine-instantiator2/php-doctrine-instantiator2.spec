%global source0_hash b5325e8aa10d00b0ac9cd3577183d10c41d81a0dcd7fcf2bd14bb8e7c4c51eb9

# remirepo/fedora spec file for php-doctrine-instantiator2
#
# SPDX-FileCopyrightText:  Copyright 2014-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# bootstrap needed when rebuilding PHPUnit for new major version
%global bootstrap    0
%global gh_commit    23da848e1a2308728fe5fdddabf4be17ff9720c7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   instantiator
%global major        2
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-doctrine-instantiator%{major}
Version:        2.1.0
Release:        2%{?dist}
Summary:        Instantiate objects in PHP without invoking their constructors, version %{major}

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 8.4
BuildRequires:  php-phar
BuildRequires:  php-pdo
BuildRequires:  php-reflection
BuildRequires:  php-spl
%global phpunit %{_bindir}/phpunit10
BuildRequires:  %{phpunit}
%endif

# From composer.json
#        "php": "^8.4"
Requires:       php(language) >= 8.4
# From phpcompatinfo report for version 1.1.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(doctrine/instantiator) = %{version}

%description
This library provides a way of avoiding usage of constructors when
instantiating PHP classes.

This package provides version %{major}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate a simple autoloader
%{_bindir}/phpab \
    --output src/Doctrine/Instantiator/autoload.php \
    --template fedora \
    src/Doctrine/Instantiator

%install
mkdir -p                         %{buildroot}%{_datadir}/php/Doctrine
cp -pr src/Doctrine/Instantiator %{buildroot}%{_datadir}/php/Doctrine/Instantiator%{major}

%check
%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests
cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/Doctrine/Instantiator%{major}/autoload.php";
Fedora\Autoloader\Autoload::addPsr0('DoctrineTest\\InstantiatorPerformance\\', dirname(__DIR__).'/tests');
Fedora\Autoloader\Autoload::addPsr0('DoctrineTest\\InstantiatorTest\\', dirname(__DIR__).'/tests');
Fedora\Autoloader\Autoload::addPsr0('DoctrineTest\\InstantiatorTestAsset\\', dirname(__DIR__).'/tests');
EOF

: Run test suite
ret=0
for cmdarg in "php %{phpunit}" php84 php85; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d auto_prepend_file=vendor/autoload.php \
      ${2:-%{_bindir}/phpunit10} || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
# remirepo:1
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md composer.json
%dir %{_datadir}/php/Doctrine
     %{_datadir}/php/Doctrine/Instantiator%{major}

%changelog
%autochangelog
