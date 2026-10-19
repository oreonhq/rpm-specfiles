%global source0_hash b2b4f8712cbbf66e72234c3ac64faad8ce56833060f2ae7a4da867adc44e2ad7
%global bootstrap    0
%global gh_commit    40a4ed114a4aea5afd6df8d0f0c9cd3033097f66
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-code-coverage
%global pk_vendor    phpunit
%global pk_project   php-code-coverage
%global ns_vendor    SebastianBergmann
%global ns_project   CodeCoverage
%global php_home     %{_datadir}/php
%global ver_major    7
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        7.0.17
Release:        1%{?dist}
Summary:        PHP code coverage information
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
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
Suggests:       php-xdebug
Recommends:     php-pcov
Requires:       php-json
Requires:       php-tokenizer
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
Provides:       bundled(js-bootstrap) = 4.3.1
Provides:       bundled(js-d3)        = 3.5.17
Provides:       bundled(js-holder)    = 2.7.1
Provides:       bundled(js-html5shiv) = 3.7.3
Provides:       bundled(js-jquery)    = 3.4.1
Provides:       bundled(js-nvd3)      = 1.8.1
Provides:       bundled(js-respond)   = 1.1.2
# oreon:deps
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 2.0.2 with php-composer(phpunit/php-file-iterator) < 3)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 1.2.1 with php-composer(phpunit/php-text-template) < 2)
BuildRequires:  (php-composer(phpunit/php-token-stream) >= 4.0 with php-composer(phpunit/php-token-stream) < 5)
BuildRequires:  (php-composer(sebastian/code-unit-reverse-lookup) >= 1.0.1 with php-composer(sebastian/code-unit-reverse-lookup) < 2)
BuildRequires:  (php-composer(sebastian/environment) >= 4.2.2 with php-composer(sebastian/environment) < 5)
BuildRequires:  (php-composer(sebastian/version) >= 2.0.1 with php-composer(sebastian/version) < 3)
BuildRequires:  (php-composer(theseer/tokenizer) >= 1.1.3 with php-composer(theseer/tokenizer) < 2)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-xdebug
BuildRequires:  phpunit8
# /oreon:deps
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
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}
%oreon_autofiles main
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
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
