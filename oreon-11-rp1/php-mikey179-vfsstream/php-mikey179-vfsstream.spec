%global source0_hash a31bdedf4d950deee6d94c81173361190f5628895769c6a0ddeae77606e1f3ab

# spec file for php-mikey179-vfsstream
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    fe695ec993e0a55c3abdda10a9364eb31c6f1bf0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     bovigo
%global gh_project   vfsStream
%global pk_owner     mikey179
%global pk_project   vfsstream
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}

Name:           php-%{pk_owner}-%{pk_project}
Version:        1.6.12
Release:        5%{?dist}
Summary:        PHP stream wrapper for a virtual file system

# Automatically converted from old format: BSD-3-Clause - review is highly recommended.
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  %{_bindir}/phpab
%if %{with_tests}
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^7.5||^8.5||^9.6",
#        "yoast/phpunit-polyfills": "^2.0"
BuildRequires:  phpunit9 >= 9.6
BuildRequires: (php-composer(yoast/phpunit-polyfills) >= 2.0 with php-composer(yoast/phpunit-polyfills) < 3)
%endif

# From composer.json, "require": {
#        "php": ">=7.1.0"
Requires:       php(language) >= 7.1
# From phpcompatifo report for 1.6.0
Requires:       php-date
Requires:       php-dom
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
Requires:       php-xml
Requires:       php-zip

# provides both cases for compatibility
Provides:       php-composer(%{pk_owner}/%{pk_project}) = %{version}
Provides:       php-composer(%{pk_owner}/%{gh_project}) = %{version}

%description
vfsStream is a PHP stream wrapper for a virtual file system that may be
helpful in unit tests to mock the real file system.

It can be used with any unit test framework, like PHPUnit or SimpleTest.

To use this library, you just have to add, in your project:
  require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate autoloader
%{_bindir}/phpab \
    --output src/main/php/org/bovigo/vfs/autoload.php \
             src/main/php/org/bovigo/vfs

%install
mkdir -p                %{buildroot}%{_datadir}/php
cp -pr src/main/php/org %{buildroot}%{_datadir}/php/org

%if %{with_tests}
%check
# erratic result in mock
rm src/test/php/org/bovigo/vfs/vfsStreamWrapperLargeFileTestCase.php

: Use installed tree and autoloader
mkdir vendor
cat << 'EOF' | tee -a vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/org/bovigo/vfs/autoload.php';
require_once '%{_datadir}/php/Yoast/PHPUnitPolyfills2/autoload.php';
EOF

ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    VER=$($cmd -r 'echo PHP_VERSION_ID;')
    $cmd %{_bindir}/phpunit9 \
      --filter '^((?!(unregisterThirdPartyVfsScheme|unregisterWhenNotInRegisteredState)).)*$' \
      --verbose --no-coverage || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json

%dir %{_datadir}/php/org
%dir %{_datadir}/php/org/bovigo
     %{_datadir}/php/org/bovigo/vfs

%changelog
%autochangelog
