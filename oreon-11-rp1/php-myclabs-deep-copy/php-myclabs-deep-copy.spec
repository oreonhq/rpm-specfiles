%global source0_hash 58391e80187d430bb45795b12d6b723ee055d4406a476126e3f77cf333f7ec85

# remirepo/fedora spec file for php-myclabs-deep-copy
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%bcond_without       tests

%global gh_commit    07d290f0c47959fd5eed98c95ee5602db07e0b6a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     myclabs
%global gh_project   DeepCopy
%global c_project    deep-copy
%global major        %nil
%global php_home     %{_datadir}/php

Name:           php-myclabs-deep-copy%{major}
Version:        1.13.4
Release:        2%{?dist}

Summary:        Create deep copies (clones) of your objects

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snashop to get upstream test suite
Source0:        php-myclabs-deep-copy-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-reflection
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "doctrine/collections": "^1.6.8",
#        "doctrine/common": "^2.13.3 || ^3.2.2",
#        "phpspec/prophecy": "^1.10",
#        "phpunit/phpunit": "^7.5.20 || ^8.5.23 || ^9.5.13"
BuildRequires: (php-composer(phpspec/prophecy)     >= 1.10  with php-composer(phpspec/prophecy)     < 2)
BuildRequires:  phpunit9 >= 9.5.13
%endif
# For autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 1.8.0
Requires:       php-reflection
Requires:       php-date
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{c_project}) = %{version}

%description
DeepCopy helps you create deep copies (clones) of your objects.
It is designed to handle cycles in the association graph.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
phpab --template fedora --output src/%{gh_project}/autoload.php src/%{gh_project}
cat << 'EOF' | tee -a src/%{gh_project}/autoload.php
require_once __DIR__ . '/deep_copy.php';
EOF

%install
: Library
mkdir -p %{buildroot}%{php_home}
cp -pr src/%{gh_project} %{buildroot}%{php_home}/%{gh_project}%{major}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_home}/%{gh_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('DeepCopy\\', dirname(__DIR__).'/fixtures/');
\Fedora\Autoloader\Autoload::addPsr4('DeepCopyTest\\', dirname(__DIR__).'/tests/DeepCopyTest/');
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/Prophecy/autoload.php',
]);
EOF

# disable doctrine related tests
rm -r tests/DeepCopyTest/Matcher/Doctrine \
      tests/DeepCopyTest/Filter/Doctrine

ret=0
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=vendor/autoload.php \
       %{_bindir}/phpunit9 \
         --filter '^((?!(test_it_can_apply_two_filters_with_chainable_filter|test_it_can_copy_property_after_applying_doctrine_proxy_filter_with_chainable_filter)).)*$' \
         --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc README.md
%{php_home}/%{gh_project}%{major}

%changelog
%autochangelog
