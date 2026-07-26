%global source0_hash 6f8032ac123fddef04595df9b8ec1dcf049e80d68253d37307cb92fb5f832fa9

# remirepo/fedora spec file for phpunit8
#
# SPDX-FileCopyrightText:  Copyright 2010-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    1015741814413c156abb0f53d7db7bbd03c6e858
%global gh_date      2026-01-27
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit
# Packagist
%global pk_vendor    phpunit
%global pk_project   phpunit
# Namespace
%global ns_vendor    PHPUnit8
%global php_home     %{_datadir}/php
%global ver_major    8
%global ver_minor    5

%global upstream_version 8.5.52
#global upstream_prever  dev

Name:           %{pk_project}%{ver_major}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        The PHP Unit Testing framework version %{ver_major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{upstream_version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix command for autoload
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  (php-composer(doctrine/instantiator) >= 1.5.0         with php-composer(doctrine/instantiator) <  2)
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.13.4            with php-composer(myclabs/deep-copy) <  2)
BuildRequires:  (php-composer(phar-io/manifest) >= 2.0.4              with php-composer(phar-io/manifest) <  3)
BuildRequires:  (php-composer(phar-io/version) >= 3.2.1               with php-composer(phar-io/version) <  4)
BuildRequires:  (php-composer(phpspec/prophecy) >= 1.10.3             with php-composer(phpspec/prophecy) <  2)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 7.0.17    with php-composer(phpunit/php-code-coverage) <  8)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 2.0.6     with php-composer(phpunit/php-file-iterator) <  3)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 1.2.1     with php-composer(phpunit/php-text-template) <  2)
BuildRequires:  (php-composer(phpunit/php-timer) >= 2.1.4             with php-composer(phpunit/php-timer) <  3)
BuildRequires:  (php-composer(sebastian/comparator) >= 3.0.7          with php-composer(sebastian/comparator) <  4)
BuildRequires:  (php-composer(sebastian/diff) >= 3.0.6                with php-composer(sebastian/diff) <  4)
BuildRequires:  (php-composer(sebastian/environment) >= 4.2.5         with php-composer(sebastian/environment) <  5)
BuildRequires:  (php-composer(sebastian/exporter) >= 3.1.8            with php-composer(sebastian/exporter) <  4)
BuildRequires:  (php-composer(sebastian/global-state) >= 3.0.6        with php-composer(sebastian/global-state) <  4)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 3.0.5   with php-composer(sebastian/object-enumerator) <  4)
BuildRequires:  (php-composer(sebastian/resource-operations) >= 2.0.3 with php-composer(sebastian/resource-operations) < 3)
BuildRequires:  (php-composer(sebastian/version) >= 2.0.1             with php-composer(sebastian/version) <  3)
BuildRequires:  (php-composer(sebastian/type) >= 1.1.5                with php-composer(sebastian/type) <  2)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 2.0.0           with php-composer(phpunit/php-invoker) <  3)
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-xml
BuildRequires:  php-libxml
BuildRequires:  php-xmlwriter
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0

# From composer.json, "require": {
#        "php": ">=7.2",
#        "ext-dom": "*",
#        "ext-json": "*",
#        "ext-libxml": "*",
#        "ext-mbstring": "*",
#        "ext-xml": "*",
#        "ext-xmlwriter": "*",
#        "doctrine/instantiator": "^1.5.0",
#        "myclabs/deep-copy": "^1.13.4",
#        "phar-io/manifest": "^2.0.4",
#        "phar-io/version": "^3.2.1",
#        "phpunit/php-code-coverage": "^7.0.17",
#        "phpunit/php-file-iterator": "^2.0.6",
#        "phpunit/php-text-template": "^1.2.1",
#        "phpunit/php-timer": "^2.1.4",
#        "sebastian/comparator": "^3.0.7",
#        "sebastian/diff": "^3.0.6",
#        "sebastian/environment": "^4.2.5",
#        "sebastian/exporter": "^3.1.8",
#        "sebastian/global-state": "^3.0.6",
#        "sebastian/object-enumerator": "^3.0.5",
#        "sebastian/resource-operations": "^2.0.3",
#        "sebastian/type": "^1.1.3",
#        "sebastian/version": "^2.0.1",
Requires:       php(language) >= 7.2
Requires:       php-cli
Requires:       php-dom
Requires:       php-json
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-xmlwriter
Requires:       (php-composer(doctrine/instantiator) >= 1.5.0         with php-composer(doctrine/instantiator) <  2)
Requires:       (php-composer(myclabs/deep-copy) >= 1.13.4            with php-composer(myclabs/deep-copy) <  2)
Requires:       (php-composer(phar-io/manifest) >= 2.0.4              with php-composer(phar-io/manifest) <  3)
Requires:       (php-composer(phar-io/version) >= 3.2.1               with php-composer(phar-io/version) <  4)
Recommends:     (php-composer(phpspec/prophecy) >= 1.10.3             with php-composer(phpspec/prophecy) <  2)
Requires:       (php-composer(phpunit/php-code-coverage) >= 7.0.17    with php-composer(phpunit/php-code-coverage) <  8)
Requires:       (php-composer(phpunit/php-file-iterator) >= 2.0.6     with php-composer(phpunit/php-file-iterator) <  3)
Requires:       (php-composer(phpunit/php-text-template) >= 1.2.1     with php-composer(phpunit/php-text-template) <  2)
Requires:       (php-composer(phpunit/php-timer) >= 2.1.4             with php-composer(phpunit/php-timer) <  3)
Requires:       (php-composer(sebastian/comparator) >= 3.0.7          with php-composer(sebastian/comparator) <  4)
Requires:       (php-composer(sebastian/diff) >= 3.0.6                with php-composer(sebastian/diff) <  4)
Requires:       (php-composer(sebastian/environment) >= 4.2.5         with php-composer(sebastian/environment) <  5)
Requires:       (php-composer(sebastian/exporter) >= 3.1.8            with php-composer(sebastian/exporter) <  4)
Requires:       (php-composer(sebastian/global-state) >= 3.0.6        with php-composer(sebastian/global-state) <  4)
Requires:       (php-composer(sebastian/object-enumerator) >= 3.0.5   with php-composer(sebastian/object-enumerator) <  4)
Requires:       (php-composer(sebastian/resource-operations) >= 2.0.3 with php-composer(sebastian/resource-operations) < 3)
Requires:       (php-composer(sebastian/type) >= 1.1.5                with php-composer(sebastian/type) <  2)
Requires:       (php-composer(sebastian/version) >= 2.0.1             with php-composer(sebastian/version) <  3)
# From composer.json, "suggest": {
#        "phpunit/php-invoker": "^2.0.0",
#        "ext-soap": "*",
#        "ext-xdebug": "*"
Requires:       (php-composer(phpunit/php-invoker) >= 2.0.0           with php-composer(phpunit/php-invoker) <  3)
Suggests:       php-soap
Suggests:       php-xdebug
# recommends latest versions
Recommends:     phpunit9
Recommends:     phpunit10
Recommends:     phpunit11
Recommends:     phpunit12
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 8.0.0
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-phar

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
Provides:       php-composer(phpunit/phpunit) = %{version}
Provides:       phpunit                       = %{version}-%{release}
%endif

%description
PHPUnit is a programmer-oriented testing framework for PHP.
It is an instance of the xUnit architecture for unit testing frameworks.

This package provides the version %{ver_major} of PHPUnit,
available using the %{name} command.

Documentation: https://phpunit.de/documentation.html

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p0 -b .rpm

find . -name \*.rpm -delete -print

%build
%{_bindir}/phpab \
  --template fedora2 \
  --output   src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/FileIterator2/autoload.php',
    '%{php_home}/Text/Template/Autoload.php',
    '%{php_home}/SebastianBergmann/CodeCoverage7/autoload.php',
    '%{php_home}/SebastianBergmann/Timer/autoload.php',
    '%{php_home}/SebastianBergmann/Diff3/autoload.php', // Before comparator which may load v2
    '%{php_home}/SebastianBergmann/Comparator3/autoload.php',
    '%{php_home}/SebastianBergmann/Environment4/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter3/autoload.php',
    '%{php_home}/SebastianBergmann/GlobalState3/autoload.php',
    '%{php_home}/SebastianBergmann/ObjectEnumerator3/autoload.php',
    '%{php_home}/SebastianBergmann/ResourceOperations2/autoload.php',
    '%{php_home}/SebastianBergmann/Type/autoload.php',
    '%{php_home}/SebastianBergmann/Version/autoload.php',
    '%{php_home}/Doctrine/Instantiator/autoload.php',
    '%{php_home}/DeepCopy/autoload.php',
    '%{php_home}/SebastianBergmann/Invoker/autoload.php',
    '%{php_home}/PharIo/Manifest2/autoload.php',
    '%{php_home}/PharIo/Version3/autoload.php',
]);
// Extensions
\Fedora\Autoloader\Dependencies::optional([
    '%{php_home}/Prophecy/autoload.php',
]);
\Fedora\Autoloader\Dependencies::optional(
    glob("%{php_home}/%{ns_vendor}/Extensions/*/autoload.php")
);
EOF
cat src/autoload.php

%{_bindir}/phpab \
  --output   tests/autoload.php \
  --exclude  '*/BankAccountTest2.php' \
  --exclude  '*/regression/Trac/783/OneTest.php' \
  --exclude  'tests/end-to-end/regression/3889/Issue3889Test.test.php' \
  --exclude  'tests/end-to-end/regression/3904/Issue3904Test.php' \
  tests

%install
mkdir -p       %{buildroot}%{php_home}
cp -pr src     %{buildroot}%{php_home}/%{ns_vendor}
mkdir          %{buildroot}%{php_home}/%{ns_vendor}/Extensions

install -D -p -m 755 phpunit %{buildroot}%{_bindir}/%{name}
install -p -m 644 phpunit.xsd %{buildroot}%{php_home}/%{ns_vendor}/phpunit.xsd

%check
OPT="--testsuite=unit --no-coverage"
sed -e 's:@PATH@:%{buildroot}%{php_home}/%{ns_vendor}:' -i tests/bootstrap.php
sed -e 's:%{php_home}/%{ns_vendor}:%{buildroot}%{php_home}/%{ns_vendor}:' -i phpunit

ret=0
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
     $cmd ./phpunit $OPT --verbose || ret=1
  fi
done
exit $ret

%files
%license LICENSE
%doc README.md ChangeLog-%{ver_major}.%{ver_minor}.md
%doc composer.json
%{_bindir}/%{name}
%{php_home}/%{ns_vendor}

%changelog
%autochangelog
