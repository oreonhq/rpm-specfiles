%global source0_hash 479143c5df17c5afef1d83c84e67dd456bf660418ec4be7e7ba9d7ff10f630c3
%bcond_without       tests
%global gh_commit    2c1ed04922802c15e1de5d7447b4856de949cf56
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner    sebastianbergmann
%global gh_project   php-code-coverage
%global gh_date      2025-12-24
%global pk_vendor    phpunit
%global pk_project   php-code-coverage
%global ns_vendor    SebastianBergmann
%global ns_project   CodeCoverage
%global php_home     %{_datadir}/php
%global ver_major    11
Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        11.0.12
Release:        1%{?dist}
Summary:        PHP code coverage information, version 11
License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.2
Requires:       php-dom
Requires:       php-libxml
Requires:       php-xmlwriter
Requires:       (php-composer(nikic/php-parser)                   >= 5.7.0  with php-composer(nikic/php-parser)                   < 6)
Requires:       (php-composer(phpunit/php-file-iterator)          >= 5.1.0  with php-composer(phpunit/php-file-iterator)          < 6)
Requires:       (php-composer(phpunit/php-text-template)          >= 4.0.1  with php-composer(phpunit/php-text-template)          < 5)
Requires:       (php-composer(sebastian/code-unit-reverse-lookup) >= 4.0.1  with php-composer(sebastian/code-unit-reverse-lookup) < 5)
Requires:       (php-composer(sebastian/complexity)               >= 4.0.1  with php-composer(sebastian/complexity)               < 5)
Requires:       (php-composer(sebastian/environment)              >= 7.2.1  with php-composer(sebastian/environment)              < 8)
Requires:       (php-composer(sebastian/lines-of-code)            >= 3.0.1  with php-composer(sebastian/lines-of-code)            < 4)
Requires:       (php-composer(sebastian/version)                  >= 5.0.2  with php-composer(sebastian/version)                  < 6)
Requires:       (php-composer(theseer/tokenizer)                  >= 1.3.1  with php-composer(theseer/tokenizer)                  < 2)
Suggests:       php-xdebug
Recommends:     php-pcov
Requires:       php-json
Requires:       php-tokenizer
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
Provides:       bundled(js-bootstrap) = 5.3.6
Provides:       bundled(js-d3)        = 3.5.17
Provides:       bundled(js-jquery)    = 3.7.1
Provides:       bundled(js-nvd3)      = 1.8.1
# oreon:deps
BuildRequires:  (php-composer(nikic/php-parser) >= 5.7.0 with php-composer(nikic/php-parser) < 6)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 5.1.0 with php-composer(phpunit/php-file-iterator) < 6)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 4.0.1 with php-composer(phpunit/php-text-template) < 5)
BuildRequires:  (php-composer(sebastian/code-unit-reverse-lookup) >= 4.0.1 with php-composer(sebastian/code-unit-reverse-lookup) < 5)
BuildRequires:  (php-composer(sebastian/complexity) >= 4.0.1 with php-composer(sebastian/complexity) < 5)
BuildRequires:  (php-composer(sebastian/environment) >= 7.2.1 with php-composer(sebastian/environment) < 8)
BuildRequires:  (php-composer(sebastian/lines-of-code) >= 3.0.1 with php-composer(sebastian/lines-of-code) < 4)
BuildRequires:  (php-composer(sebastian/version) >= 5.0.2 with php-composer(sebastian/version) < 6)
BuildRequires:  (php-composer(theseer/tokenizer) >= 1.3.1 with php-composer(theseer/tokenizer) < 2)
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-tokenizer
BuildRequires:  php-xdebug
BuildRequires:  php-xmlwriter
BuildRequires:  phpunit11
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
    '%{php_home}/PhpParser5/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator5/autoload.php',
    '%{php_home}/%{ns_vendor}/Template4/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeUnitReverseLookup4/autoload.php',
    '%{php_home}/%{ns_vendor}/Complexity4/autoload.php',
    '%{php_home}/%{ns_vendor}/Environment7/autoload.php',
    '%{php_home}/%{ns_vendor}/LinesOfCode3/autoload.php',
    '%{php_home}/%{ns_vendor}/Version5/autoload.php',
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
%{_bindir}/phpab \
  --template fedora \
  --output tests/bootstrap.php \
  --exclude 'tests/_files/*.php' \
  tests
cat << 'EOF' | tee -a tests/bootstrap.php
define('TEST_FILES_PATH', __DIR__ . '/_files/');
EOF
ret=0
for cmd in php php82 php83 php84; do
  if which $cmd; then
    $cmd $EXT \
      -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
        %{_bindir}/phpunit11 \
          --filter "^((?!(testCanBeCreatedFromDefaults)).)*$" \
          || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
