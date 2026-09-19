%global source0_hash f3ee072af3b00c36ef8a3ce8eb7261273931e5f995fa12707c1210d46dff602f

# remirepo/fedora spec file for php-phpunit-php-code-coverage10
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    7e308268858ed6baedc8704a304727d20bc07c77
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-code-coverage
%global gh_date      2024-08-22
# Packagist
%global pk_vendor    phpunit
%global pk_project   php-code-coverage
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   CodeCoverage
%global php_home     %{_datadir}/php
%global ver_major    10

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        10.1.16
Release:        4%{?dist}
Summary:        PHP code coverage information, version %{ver_major}

# SPDX: Main license is BSD-3-Clause
# BSD-3-Clause: D3
# MIT: boostrap, d3, holder, html5shiv, jquery, respond
# Apache-2.0: nvd3
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
BuildRequires:  (php-composer(nikic/php-parser)                   >= 4.19.1 with php-composer(nikic/php-parser)                   < 6)
BuildRequires:  (php-composer(phpunit/php-file-iterator)          >= 4.1.0  with php-composer(phpunit/php-file-iterator)          < 5)
BuildRequires:  (php-composer(phpunit/php-text-template)          >= 3.0.1  with php-composer(phpunit/php-text-template)          < 4)
BuildRequires:  (php-composer(sebastian/code-unit-reverse-lookup) >= 3.0.0  with php-composer(sebastian/code-unit-reverse-lookup) < 4)
BuildRequires:  (php-composer(sebastian/complexity)               >= 3.2.0  with php-composer(sebastian/complexity)               < 4)
BuildRequires:  (php-composer(sebastian/environment)              >= 6.1.0  with php-composer(sebastian/environment)              < 7)
BuildRequires:  (php-composer(sebastian/lines-of-code)            >= 2.0.2  with php-composer(sebastian/lines-of-code)            < 3)
BuildRequires:  (php-composer(sebastian/version)                  >= 4.0.1  with php-composer(sebastian/version)                  < 5)
BuildRequires:  (php-composer(theseer/tokenizer)                  >= 1.2.3  with php-composer(theseer/tokenizer)                  < 2)
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlwriter
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^10.1"
BuildRequires:  phpunit10 >= 10.1
BuildRequires:  php-xdebug
%endif

# From composer.json, require
#        "php": ">=8.1",
#        "ext-dom": "*",
#        "ext-libxml": "*",
#        "ext-xmlwriter": "*",
#        "nikic/php-parser": "^4.19.1 || ^5.1.0",
#        "phpunit/php-file-iterator": "^4.1.0",
#        "phpunit/php-text-template": "^3.0.1",
#        "sebastian/code-unit-reverse-lookup": "^3.0.0",
#        "sebastian/complexity": "^3.2.0",
#        "sebastian/environment": "^6.1.0",
#        "sebastian/lines-of-code": "^2.0.2",
#        "sebastian/version": "^4.0.1",
#        "theseer/tokenizer": "^1.2.3"
Requires:       php(language) >= 8.1
Requires:       php-dom
Requires:       php-libxml
Requires:       php-xmlwriter
Requires:       (php-composer(nikic/php-parser)                   >= 4.19.1 with php-composer(nikic/php-parser)                   < 6)
Requires:       (php-composer(phpunit/php-file-iterator)          >= 4.1.0  with php-composer(phpunit/php-file-iterator)          < 5)
Requires:       (php-composer(phpunit/php-text-template)          >= 3.0.1  with php-composer(phpunit/php-text-template)          < 4)
Requires:       (php-composer(sebastian/code-unit-reverse-lookup) >= 3.0.0  with php-composer(sebastian/code-unit-reverse-lookup) < 4)
Requires:       (php-composer(sebastian/complexity)               >= 3.2.0  with php-composer(sebastian/complexity)               < 4)
Requires:       (php-composer(sebastian/environment)              >= 6.1.0  with php-composer(sebastian/environment)              < 7)
Requires:       (php-composer(sebastian/lines-of-code)            >= 2.0.2  with php-composer(sebastian/lines-of-code)            < 3)
Requires:       (php-composer(sebastian/version)                  >= 4.0.1  with php-composer(sebastian/version)                  < 5)
Requires:       (php-composer(theseer/tokenizer)                  >= 1.2.3  with php-composer(theseer/tokenizer)                  < 2)
# From composer.json, suggest
#        "ext-pcov": "*",
#        "ext-xdebug": "*"
Suggests:       php-xdebug
Recommends:     php-pcov
# From phpcompatinfo report for version 10.0.0
Requires:       php-date
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Bundled assets in HTML template
Provides:       bundled(js-bootstrap) = 4.3.1
Provides:       bundled(js-d3)        = 3.5.17
Provides:       bundled(js-jquery)    = 3.4.1
Provides:       bundled(js-nvd3)      = 1.8.1
Provides:       bundled(js-popper)

%description
Library that provides collection, processing, and rendering functionality
for PHP code coverage information.

This package provides version %{ver_major} of %{pk_vendor}/%{pk_project} library.

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
    [
        '%{php_home}/PhpParser5/autoload.php',
        '%{php_home}/PhpParser4/autoload.php',
    ],
    '%{php_home}/%{ns_vendor}/FileIterator4/autoload.php',
    '%{php_home}/%{ns_vendor}/Template3/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeUnitReverseLookup3/autoload.php',
    '%{php_home}/%{ns_vendor}/Complexity3/autoload.php',
    '%{php_home}/%{ns_vendor}/Environment6/autoload.php',
    '%{php_home}/%{ns_vendor}/LinesOfCode2/autoload.php',
    '%{php_home}/%{ns_vendor}/Version4/autoload.php',
    '%{php_home}/TheSeer/Tokenizer/autoload.php',
]);
EOF

%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%if %{with tests}
%check
if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so -d xdebug.mode=coverage"
fi
export XDEBUG_MODE=coverage

cat << 'EOF' | tee tests/bootstrap.php
<?php
require __DIR__ . '/TestCase.php';
require __DIR__ . '/_files/BankAccountTest.php';
define('TEST_FILES_PATH', __DIR__ . '/_files/');
EOF

ret=0
# testCanBeCreatedFromDefaults rely on git layout

for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd $EXT \
      -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
        %{_bindir}/phpunit10 \
          --filter "^((?!(testCanBeCreatedFromDefaults)).)*$" \
          || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md
%doc ChangeLog-10.1.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%changelog
%autochangelog
