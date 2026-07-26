%global source0_hash 6863d6bb819c32ae01bf080cdf35291070430c88c0ed4be515efc07d7fc2e2bc

# remirepo/fedora spec file for php-phpunit-php-code-coverage13
#
# SPDX-FileCopyrightText:  Copyright 2013-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_with          tests

# Github
%global gh_commit    a8b58fde2f4fbc69a064e1f80ff917607cf7737c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    sebastianbergmann
%global gh_project   php-code-coverage
%global gh_date      2026-02-06
# Packagist
%global pk_vendor    phpunit
%global pk_project   php-code-coverage
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   CodeCoverage
%global php_home     %{_datadir}/php
%global ver_major    13

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        13.0.1
Release:        1%{?dist}
Summary:        PHP code coverage information, version %{ver_major}

# SPDX: Main license is BSD-3-Clause
# BSD-3-Clause: D3
# MIT: boostrap, d3, holder, html5shiv, jquery, respond
# Apache-2.0: nvd3
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.4.1
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
BuildRequires:  (php-composer(nikic/php-parser)                   >= 5.7.0  with php-composer(nikic/php-parser)                   < 6)
BuildRequires:  (php-composer(phpunit/php-file-iterator)          >= 7.0    with php-composer(phpunit/php-file-iterator)          < 8)
BuildRequires:  (php-composer(phpunit/php-text-template)          >= 6.0    with php-composer(phpunit/php-text-template)          < 7)
BuildRequires:  (php-composer(sebastian/complexity)               >= 6.0    with php-composer(sebastian/complexity)               < 7)
BuildRequires:  (php-composer(sebastian/environment)              >= 9.0    with php-composer(sebastian/environment)              < 10)
BuildRequires:  (php-composer(sebastian/lines-of-code)            >= 5.0    with php-composer(sebastian/lines-of-code)            < 6)
BuildRequires:  (php-composer(sebastian/version)                  >= 7.0    with php-composer(sebastian/version)                  < 8)
BuildRequires:  (php-composer(theseer/tokenizer)                  >= 2.0.1  with php-composer(theseer/tokenizer)                  < 3)
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlwriter
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^13.0"
BuildRequires:  phpunit13
BuildRequires:  php-xdebug
%endif

# From composer.json, require
#        "php": ">=8.3",
#        "ext-dom": "*",
#        "ext-libxml": "*",
#        "ext-xmlwriter": "*",
#        "nikic/php-parser": "^5.7.0",
#        "phpunit/php-file-iterator": "^7.0",
#        "phpunit/php-text-template": "^6.0",
#        "sebastian/complexity": "^6.0",
#        "sebastian/environment": "^9.0",
#        "sebastian/lines-of-code": "^5.0",
#        "sebastian/version": "^7.0",
#        "theseer/tokenizer": "^2.0.1"
Requires:       php(language) >= 8.3
Requires:       php-dom
Requires:       php-libxml
Requires:       php-xmlwriter
Requires:       (php-composer(nikic/php-parser)                   >= 5.7.0  with php-composer(nikic/php-parser)                   < 6)
Requires:       (php-composer(phpunit/php-file-iterator)          >= 7.0    with php-composer(phpunit/php-file-iterator)          < 8)
Requires:       (php-composer(phpunit/php-text-template)          >= 6.0    with php-composer(phpunit/php-text-template)          < 7)
Requires:       (php-composer(sebastian/complexity)               >= 6.0    with php-composer(sebastian/complexity)               < 7)
Requires:       (php-composer(sebastian/environment)              >= 9.0    with php-composer(sebastian/environment)              < 10)
Requires:       (php-composer(sebastian/lines-of-code)            >= 5.0    with php-composer(sebastian/lines-of-code)            < 6)
Requires:       (php-composer(sebastian/version)                  >= 7.0    with php-composer(sebastian/version)                  < 8)
Requires:       (php-composer(theseer/tokenizer)                  >= 2.0.1  with php-composer(theseer/tokenizer)                  < 3)
# From composer.json, suggest
#        "ext-pcov": "*",
#        "ext-xdebug": "*"
Suggests:       php-xdebug
Recommends:     php-pcov
# From phpcompatinfo report for version 10.0.0
Requires:       php-json
Requires:       php-tokenizer
# Autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# Bundled assets in HTML template
Provides:       bundled(js-bootstrap) = 5.3.6
Provides:       bundled(js-jquery)    = 3.7.1
Provides:       bundled(js-billboard) = 3.15.1

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
    '%{php_home}/PhpParser5/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator7/autoload.php',
    '%{php_home}/%{ns_vendor}/Template6/autoload.php',
    '%{php_home}/%{ns_vendor}/Complexity6/autoload.php',
    '%{php_home}/%{ns_vendor}/Environment9/autoload.php',
    '%{php_home}/%{ns_vendor}/LinesOfCode5/autoload.php',
    '%{php_home}/%{ns_vendor}/Version7/autoload.php',
    '%{php_home}/TheSeer/Tokenizer2/autoload.php',
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

%{_bindir}/phpab \
  --template fedora \
  --output tests/bootstrap.php \
  --exclude 'tests/_files/*.php' \
  tests

cat << 'EOF' | tee -a tests/bootstrap.php
define('TEST_FILES_PATH', __DIR__ . '/_files/');
EOF

ret=0
# testCanBeCreatedFromDefaults rely on git layout

for cmd in php php84 php85; do
  if which $cmd; then
    $cmd $EXT \
      -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
        %{_bindir}/phpunit13 \
          --filter "^((?!(testCanBeCreatedFromDefaults)).)*$" \
          || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md
%doc ChangeLog-%{ver_major}.0.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%changelog
%autochangelog
