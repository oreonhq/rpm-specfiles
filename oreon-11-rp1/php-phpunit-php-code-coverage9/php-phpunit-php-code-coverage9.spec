%global source0_hash 02e12918f11598a4a6e377a3ae378ecaa0ae25544aee44846013c17601b49e5b
%bcond_without       tests
%global gh_commit    85402a822d1ecf1db1096959413d35e1c37cf1a5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-code-coverage
%global gh_date      2024-08-22
%global pk_vendor    phpunit
%global pk_project   php-code-coverage
%global ns_vendor    SebastianBergmann
%global ns_project   CodeCoverage
%global php_home     %{_datadir}/php
%global ver_major    9
Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        9.2.32
Release:        4%{?dist}
Summary:        PHP code coverage information, version 9
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.3
Requires:       php-dom
Requires:       php-libxml
Requires:       php-xmlwriter
Requires:       (php-composer(nikic/php-parser)                   >= 4.19.1 with php-composer(nikic/php-parser)                   < 6)
Requires:       (php-composer(phpunit/php-file-iterator)          >= 3.0.6  with php-composer(phpunit/php-file-iterator)          < 4)
Requires:       (php-composer(phpunit/php-text-template)          >= 2.0.4  with php-composer(phpunit/php-text-template)          < 3)
Requires:       (php-composer(sebastian/code-unit-reverse-lookup) >= 2.0.3  with php-composer(sebastian/code-unit-reverse-lookup) < 3)
Requires:       (php-composer(sebastian/complexity)               >= 2.0.3  with php-composer(sebastian/complexity)               < 3)
Requires:       (php-composer(sebastian/environment)              >= 5.1.5  with php-composer(sebastian/environment)              < 6)
Requires:       (php-composer(sebastian/lines-of-code)            >= 1.0.4  with php-composer(sebastian/lines-of-code)            < 2)
Requires:       (php-composer(sebastian/version)                  >= 3.0.2  with php-composer(sebastian/version)                  < 4)
Requires:       (php-composer(theseer/tokenizer)                  >= 1.2.3  with php-composer(theseer/tokenizer)                  < 2)
Suggests:       php-xdebug
Recommends:     php-pcov
Requires:       php-reflection
Requires:       php-date
Requires:       php-hash
Requires:       php-json
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
Provides:       bundled(js-bootstrap) = 4.3.1
Provides:       bundled(js-d3)        = 3.5.17
Provides:       bundled(js-jquery)    = 3.4.1
Provides:       bundled(js-nvd3)      = 1.8.1
Provides:       bundled(js-popper)
# oreon:deps
BuildRequires:  (php-composer(nikic/php-parser) >= 4.19.1 with php-composer(nikic/php-parser) < 6)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 3.0.6 with php-composer(phpunit/php-file-iterator) < 4)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 2.0.4 with php-composer(phpunit/php-text-template) < 3)
BuildRequires:  (php-composer(sebastian/code-unit-reverse-lookup) >= 2.0.3 with php-composer(sebastian/code-unit-reverse-lookup) < 3)
BuildRequires:  (php-composer(sebastian/complexity) >= 2.0.3 with php-composer(sebastian/complexity) < 3)
BuildRequires:  (php-composer(sebastian/environment) >= 5.1.5 with php-composer(sebastian/environment) < 6)
BuildRequires:  (php-composer(sebastian/lines-of-code) >= 1.0.4 with php-composer(sebastian/lines-of-code) < 2)
BuildRequires:  (php-composer(sebastian/version) >= 3.0.2 with php-composer(sebastian/version) < 4)
BuildRequires:  (php-composer(theseer/tokenizer) >= 1.2.3 with php-composer(theseer/tokenizer) < 2)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-xdebug
BuildRequires:  phpunit9
# /oreon:deps
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
    '%{php_home}/%{ns_vendor}/FileIterator3/autoload.php',
    '%{php_home}/%{ns_vendor}/Template2/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeUnitReverseLookup2/autoload.php',
    '%{php_home}/%{ns_vendor}/Complexity/autoload.php',
    '%{php_home}/%{ns_vendor}/Environment5/autoload.php',
    '%{php_home}/%{ns_vendor}/LinesOfCode/autoload.php',
    '%{php_home}/%{ns_vendor}/Version3/autoload.php',
    '%{php_home}/TheSeer/Tokenizer/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}
%oreon_autofiles main
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
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd $EXT \
      -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
        %{_bindir}/phpunit9 \
          --verbose || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
