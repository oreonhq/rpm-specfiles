%global source0_hash 52bf21a8697352d996a7b4d0465eadc70171bbc11bc68504b31be5b1c82f4106

#
# Fedora spec file for php-doctrine-collections
#
# Copyright (c) 2013-2022 Shawn Iwinski, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     doctrine
%global github_name      collections
%global github_version   1.8.0
%global github_commit    2b44dd4cbca8b5744327de78bafef5945c7e7b5e

%global composer_vendor  doctrine
%global composer_project collections

# "php": "^7.1.3 || ^8.0"
%global php_min_ver 7.1.3
# "doctrine/deprecations": "^0.5.3 || ^1"
%global doctrine_depr_min_ver 1
%global doctrine_depr_max_ver 2

# Build using "--without tests" to disable tests
%bcond_without tests

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       9%{?github_release}%{?dist}
Summary:       Collections abstraction library

License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-doctrine-collections-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:     noarch
# Tests
%if %{with tests}
## composer.json
%global phpunit %{_bindir}/phpunit9
BuildRequires: %{phpunit}
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: (php-composer(doctrine/deprecations) >= %{doctrine_depr_min_ver} with php-composer(doctrine/deprecations) < %{doctrine_depr_max_ver})
## phpcompatinfo (computed from version 1.6.0)
BuildRequires: php-pcre
BuildRequires: php-spl
%endif
# Autoloader
BuildRequires: php-fedora-autoloader-devel

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/deprecations) >= %{doctrine_depr_min_ver} with php-composer(doctrine/deprecations) < %{doctrine_depr_max_ver})
# phpcompatinfo (computed from version 1.6.0)
Requires:      php-pcre
Requires:      php-spl
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

# Extracted from Doctrine Common as of version 2.4
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4

%description
%{summary}.

Autoloader: %{phpdir}/Doctrine/Common/Collections/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
phpab --template fedora \
      --output lib/Doctrine/Common/Collections/autoload.php \
      lib/Doctrine/Common/Collections

cat <<'AUTOLOAD' | tee -a lib/Doctrine/Common/Collections/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/

%check
%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Collections/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests/Doctrine/Tests');
BOOTSTRAP

: Upstream tests
SCL_RETURN_CODE=0
for CMD in "php %{phpunit}" php74 php80 php81 php82; do
    if which $CMD; then
        set $CMD
        $1 ${2:-%{_bindir}/phpunit9} --verbose --bootstrap bootstrap.php \
            || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Doctrine
%dir %{phpdir}/Doctrine/Common
     %{phpdir}/Doctrine/Common/Collections

%changelog
%autochangelog
