%global source0_hash 942fb3660cc7b3be5fe5123708aa4c43df338a43304d3717384be4eb52f507eb

# fedora/remirepo spec file for phpcov
#
# SPDX-FileCopyrightText:  Copyright 2013-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without tests

%global gh_commit    74b950835e1b012ec422f112492929b2c832ffe5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcov
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   phpcov
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCOV

Name:           %{pk_project}
Version:        12.0.0
Release:        1%{?dist}
Summary:        CLI frontend for PHP_CodeCoverage

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix autoload for RPM
Patch0:         %{gh_project}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.4.1
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
BuildRequires:  phpunit13
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 13.0.1 with php-composer(phpunit/php-code-coverage) < 14)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 7.0.0  with php-composer(phpunit/php-file-iterator) < 8)
BuildRequires:  (php-composer(sebastian/cli-parser)      >= 5.0.0  with php-composer(sebastian/cli-parser)      < 6)
BuildRequires:  (php-composer(sebastian/diff)            >= 8.0.0  with php-composer(sebastian/diff)            < 9)
BuildRequires:  (php-composer(sebastian/version)         >= 7.0.0  with php-composer(sebastian/version)         < 8)
BuildRequires:  php-pecl(Xdebug) >= 3
%endif

# from composer.json
#        "php": ">=8.4",
#        "phpunit/phpunit": "^13.0.0",
#        "phpunit/php-code-coverage": "^13.0.1",
#        "phpunit/php-file-iterator": "^7.0.0",
#        "sebastian/cli-parser": "^5.0.0",
#        "sebastian/diff": "^8.0.0",
#        "sebastian/version": "^7.0.0"
Requires:       php(language) >= 8.4
Requires:       phpunit13
Requires:       (php-composer(phpunit/php-code-coverage) >= 13.0.1 with php-composer(phpunit/php-code-coverage) < 14)
Requires:       (php-composer(phpunit/php-file-iterator) >= 7.0.0  with php-composer(phpunit/php-file-iterator) < 8)
Requires:       (php-composer(sebastian/cli-parser)      >= 5.0.0  with php-composer(sebastian/cli-parser)      < 6)
Requires:       (php-composer(sebastian/diff)            >= 8.0.0  with php-composer(sebastian/diff)            < 9)
Requires:       (php-composer(sebastian/version)         >= 7.0.0  with php-composer(sebastian/version)         < 8)
# from phpcompatinfo report for version 4.0.0
# none

Obsoletes:      php-phpunit-phpcov < 4
Provides:       php-phpunit-phpcov = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
%{pk_project} is a command-line frontend for the PHP_CodeCoverage library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm

%build
phpab \
  --template fedora \
  --output   src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PHPUnit13/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeCoverage13/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator7/autoload.php',
    '%{php_home}/%{ns_vendor}/CliParser5/autoload.php',
    '%{php_home}/%{ns_vendor}/Diff8/autoload.php',
    '%{php_home}/%{ns_vendor}/Version7/autoload.php',
]);
EOF

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -D -p -m 755 %{pk_project} %{buildroot}%{_bindir}/%{pk_project}

%check
%if %{with tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php

if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so"
fi

# test with hardcoded path in data
rm tests/end-to-end/execute/valid-script-argument-with-cli-include-with-text-report.phpt
rm tests/end-to-end/merge/valid-directory-with-text-report.phpt
rm tests/end-to-end/merge/valid-directory-with-text-report-stdout.phpt
rm tests/end-to-end/patch-coverage/valid-arguments-with-valid-path-prefix.phpt

ret=0
for cmd in php php84 php85; do
  if which $cmd; then
    $cmd $EXT -d xdebug.mode=coverage %{_bindir}/phpunit13 --testsuite end-to-end || ret=1
  fi
done
exit $ret;
%else
: Test suite skipped
%endif

%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}
%{_bindir}/%{pk_project}

%changelog
%autochangelog
