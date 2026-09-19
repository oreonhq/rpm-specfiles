%global source0_hash b2b4f8712cbbf66e72234c3ac64faad8ce56833060f2ae7a4da867adc44e2ad7

# remirepo/fedora spec file for php-phpunit-php-code-coverage7
#
# SPDX-FileCopyrightText:  Copyright 2013-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global bootstrap    0
# Github
%global gh_commit    40a4ed114a4aea5afd6df8d0f0c9cd3033097f66
#global gh_date      20150924
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-code-coverage
# Packagist
%global pk_vendor    phpunit
%global pk_project   php-code-coverage
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   CodeCoverage
%global php_home     %{_datadir}/php
%global ver_major    7
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        7.0.17
Release:        6%{?dist}
Summary:        PHP code coverage information

# SPDX: Main license is BSD-3-Clause
# BSD-3-Clause: D3
# MIT: boostrap, d3, holder, html5shiv, jquery, respond
# Apache-2.0: nvd3
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 2.0.2          with php-composer(phpunit/php-file-iterator) <  3)
BuildRequires:  (php-composer(phpunit/php-token-stream) >= 4.0             with php-composer(phpunit/php-token-stream) <  5)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 1.2.1          with php-composer(phpunit/php-text-template) <  2)
BuildRequires:  (php-composer(sebastian/code-unit-reverse-lookup) >= 1.0.1 with php-composer(sebastian/code-unit-reverse-lookup) <  2)
BuildRequires:  (php-composer(sebastian/environment) >= 4.2.2              with php-composer(sebastian/environment) <  5)
BuildRequires:  (php-composer(sebastian/version) >= 2.0.1                  with php-composer(sebastian/version) <  3)
BuildRequires:  (php-composer(theseer/tokenizer) >= 1.1.3                  with php-composer(theseer/tokenizer) <  2)
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^8.2.2"
# 7.2 because of tests
BuildRequires:  phpunit8 >= 8.2.2
BuildRequires:  php-xdebug  >= 2.6.1
%endif

# From composer.json, require
#        "php": ">=7.2",
#        "ext-dom": "*",
#        "ext-xmlwriter": "*",
#        "phpunit/php-file-iterator": "^2.0.2",
#        "phpunit/php-token-stream": "^3.1.3 || ^4.0",
#        "phpunit/php-text-template": "^1.2.1",
#        "sebastian/code-unit-reverse-lookup": "^1.0.1",
#        "sebastian/environment": "^4.2.2",
#        "sebastian/version": "^2.0.1",
#        "theseer/tokenizer": "^1.1.3"
Requires:       php(language) >= 7.1
Requires:       php-dom
Requires:       php-xmlwriter
Requires:       (php-composer(phpunit/php-file-iterator) >= 2.0.2          with php-composer(phpunit/php-file-iterator) <  3)
Requires:       (php-composer(phpunit/php-token-stream) >= 4.0             with php-composer(phpunit/php-token-stream) <  5)
Requires:       (php-composer(phpunit/php-text-template) >= 1.2.1          with php-composer(phpunit/php-text-template) <  2)
Requires:       (php-composer(sebastian/code-unit-reverse-lookup) >= 1.0.1 with php-composer(sebastian/code-unit-reverse-lookup) <  2)
Requires:       (php-composer(sebastian/environment) >= 4.2.2              with php-composer(sebastian/environment) <  5)
Requires:       (php-composer(sebastian/version) >= 2.0.1                  with php-composer(sebastian/version) <  3)
Requires:       (php-composer(theseer/tokenizer) >= 1.1.3                  with php-composer(theseer/tokenizer) <  2)
# From composer.json, suggest
#        "ext-xdebug": ">=2.6.1",
Suggests:       php-xdebug
Recommends:     php-pcov
# From phpcompatinfo report for version 5.0.0
Requires:       php-json
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Bundled assets in HTML template
Provides:       bundled(js-bootstrap) = 4.3.1
Provides:       bundled(js-d3)        = 3.5.17
Provides:       bundled(js-holder)    = 2.7.1
Provides:       bundled(js-html5shiv) = 3.7.3
Provides:       bundled(js-jquery)    = 3.4.1
Provides:       bundled(js-nvd3)      = 1.8.1
Provides:       bundled(js-respond)   = 1.1.2

%description
Library that provides collection, processing, and rendering functionality
for PHP code coverage information.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%{_bindir}/phpab \
  --template fedora \
  --output src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/FileIterator2/autoload.php',
    '%{php_home}/%{ns_vendor}/PhpTokenStream4/autoload.php',
    '%{php_home}/Text/Template/Autoload.php',
    '%{php_home}/%{ns_vendor}/CodeUnitReverseLookup/autoload.php',
    '%{php_home}/%{ns_vendor}/Environment4/autoload.php',
    '%{php_home}/%{ns_vendor}/Version/autoload.php',
    '%{php_home}/TheSeer/Tokenizer/autoload.php',
]);
EOF

%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%if %{with_tests}
%check
if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so"
fi
export XDEBUG_MODE=coverage

cat << 'EOF' | tee tests/bootstrap.php
<?php
require __DIR__ . '/TestCase.php';
require __DIR__ . '/_files/BankAccountTest.php';
define('TEST_FILES_PATH', __DIR__ . '/_files/');
EOF

ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    FILTER="--filter '^((?!(testCloverForFileWithIgnoredLines|testCloverForClassWithAnonymousFunction|testForFileWithIgnoredLines|testForClassWithAnonymousFunction|testForBankAccountTest|testGetLinesToBeIgnored3|testGetLinesToBeIgnoredOneLineAnnotations)).)*$'"
    $cmd $EXT \
      -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
        %{_bindir}/phpunit8 \
          --verbose $FILTER || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md
%doc ChangeLog.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%changelog
%autochangelog
