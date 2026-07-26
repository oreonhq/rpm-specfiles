%global source0_hash 6e41f884af75022b7cd95c4cf128c58a3461e69ca8d8e05a1a35912eb2162452

# remirepo/fedora spec file for php-doctrine-instantiator
#
# Copyright (c) 2014-2023 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# bootstrap needed when rebuilding PHPUnit for new major version
%global bootstrap    0
%global gh_commit    0a0fa9780f5d4e507415a065172d26a98d02047b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   instantiator
%global major        %nil
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-doctrine-instantiator
Version:        1.5.0
Release:        9%{?dist}
Summary:        Instantiate objects in PHP without invoking their constructors

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        php-%{gh_owner}-%{gh_project}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with_tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-phar
BuildRequires:  php-pdo
BuildRequires:  php-reflection
BuildRequires:  php-spl
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif

# From composer.json
#        "php": "^7.1 || ^8.0"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 1.1.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Obsoletes:      php-doctrine-instantiator11 < %{version}-%{release}
Provides:       php-doctrine-instantiator11 = %{version}-%{release}
Provides:       php-composer(doctrine/instantiator) = %{version}

%description
This library provides a way of avoiding usage of constructors when
instantiating PHP classes.

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
require "%{buildroot}%{_datadir}/php/Doctrine/Instantiator/autoload.php";
Fedora\Autoloader\Autoload::addPsr0('DoctrineTest\\InstantiatorPerformance\\', dirname(__DIR__).'/tests');
Fedora\Autoloader\Autoload::addPsr0('DoctrineTest\\InstantiatorTest\\', dirname(__DIR__).'/tests');
Fedora\Autoloader\Autoload::addPsr0('DoctrineTest\\InstantiatorTestAsset\\', dirname(__DIR__).'/tests');
EOF

: Run test suite
ret=0
for cmdarg in "php %{phpunit}" php80 php81 php82; do
  if which $cmdarg; then
    set $cmdarg
    $1 -d auto_prepend_file=vendor/autoload.php \
      ${2:-%{_bindir}/phpunit9} \
        --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc *.md composer.json
%dir %{_datadir}/php/Doctrine
     %{_datadir}/php/Doctrine/Instantiator%{major}

%changelog
%autochangelog
