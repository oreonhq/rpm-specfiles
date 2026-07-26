%global source0_hash 860342e41ac92842f4a612ff9d49f7d65ff9e49a99bc4efac16b76b59b218b3f

# remirepo/fedora spec file for phpunit9
#
# SPDX-FileCopyrightText:  Copyright 2010-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    b36f02317466907a230d3aa1d34467041271ef4a
%global gh_date      2026-01-27
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit
# Packagist
%global pk_vendor    phpunit
%global pk_project   phpunit
# Namespace
%global ns_vendor    PHPUnit9
%global php_home     %{_datadir}/php
%global ver_major    9
%global ver_minor    6

%global upstream_version 9.6.34
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
BuildRequires:  php(language) >= 7.3
BuildRequires:  (php-composer(doctrine/instantiator) >= 1.5.0         with php-composer(doctrine/instantiator) <  3)
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.13.4            with php-composer(myclabs/deep-copy) <  2)
BuildRequires:  (php-composer(phar-io/manifest) >= 2.0.4              with php-composer(phar-io/manifest) < 3)
BuildRequires:  (php-composer(phar-io/version) >= 3.2.1               with php-composer(phar-io/version) <  4)
BuildRequires:  (php-composer(phpspec/prophecy) >= 1.12.1             with php-composer(phpspec/prophecy) <  2)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 9.2.31    with php-composer(phpunit/php-code-coverage) <  10)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 3.0.6     with php-composer(phpunit/php-file-iterator) <  4)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 3.1             with php-composer(phpunit/php-invoker) <  4)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 2.0.4     with php-composer(phpunit/php-text-template) <  3)
BuildRequires:  (php-composer(phpunit/php-timer) >= 5.0.3             with php-composer(phpunit/php-timer) < 6)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 1.0.2          with php-composer(sebastian/cli-parser) < 2)
BuildRequires:  (php-composer(sebastian/code-unit) >= 1.0.8           with php-composer(sebastian/code-unit) < 2)
BuildRequires:  (php-composer(sebastian/comparator) >= 4.0.10         with php-composer(sebastian/comparator) <  5)
BuildRequires:  (php-composer(sebastian/diff) >= 4.0.6                with php-composer(sebastian/diff) <  5)
BuildRequires:  (php-composer(sebastian/environment) >= 5.1.5         with php-composer(sebastian/environment) <  6)
BuildRequires:  (php-composer(sebastian/exporter) >= 4.0.8            with php-composer(sebastian/exporter) <  5)
BuildRequires:  (php-composer(sebastian/global-state) >= 5.0.8        with php-composer(sebastian/global-state) <  6)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 4.0.4   with php-composer(sebastian/object-enumerator) <  5)
BuildRequires:  (php-composer(sebastian/resource-operations) >= 3.0.4 with php-composer(sebastian/resource-operations) < 4)
BuildRequires:  (php-composer(sebastian/type) >= 3.2.1                with php-composer(sebastian/type) < 4)
BuildRequires:  (php-composer(sebastian/version) >= 3.0.1             with php-composer(sebastian/version) <  4)
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-xml
BuildRequires:  php-libxml
BuildRequires:  php-xmlwriter
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0

# From composer.json, "require": {
#        "php": ">=7.3",
#        "ext-dom": "*",
#        "ext-json": "*",
#        "ext-libxml": "*",
#        "ext-mbstring": "*",
#        "ext-xml": "*",
#        "ext-xmlwriter": "*",
#        "doctrine/instantiator": "^1.5.0 || ^2",
#        "myclabs/deep-copy": "^1.13.4",
#        "phar-io/manifest": "^2.0.4",
#        "phar-io/version": "^3.2.1",
#        "phpunit/php-code-coverage": "^9.2.31",
#        "phpunit/php-file-iterator": "^3.0.6",
#        "phpunit/php-invoker": "^3.1.1",
#        "phpunit/php-text-template": "^2.0.4",
#        "phpunit/php-timer": "^5.0.3",
#        "sebastian/cli-parser": "^1.0.2",
#        "sebastian/code-unit": "^1.0.8",
#        "sebastian/comparator": "^4.0.10",
#        "sebastian/diff": "^4.0.6",
#        "sebastian/environment": "^5.1.5",
#        "sebastian/exporter": "^4.0.8",
#        "sebastian/global-state": "^5.0.8",
#        "sebastian/object-enumerator": "^4.0.4",
#        "sebastian/resource-operations": "^3.0.4",
#        "sebastian/type": "^3.2.1",
#        "sebastian/version": "^3.0.2"
Requires:       php(language) >= 7.3
Requires:       php-cli
Requires:       php-dom
Requires:       php-json
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-xmlwriter
Requires:       (php-composer(doctrine/instantiator) >= 1.5.0         with php-composer(doctrine/instantiator) <  3)
Requires:       (php-composer(myclabs/deep-copy) >= 1.13.4            with php-composer(myclabs/deep-copy) <  2)
Requires:       (php-composer(phar-io/manifest) >= 2.0.4              with php-composer(phar-io/manifest) < 3)
Requires:       (php-composer(phar-io/version) >= 3.2.1               with php-composer(phar-io/version) < 4)
Recommends:     (php-composer(phpspec/prophecy) >= 1.12.1             with php-composer(phpspec/prophecy) <  2)
Requires:       (php-composer(phpunit/php-code-coverage) >= 9.2.31    with php-composer(phpunit/php-code-coverage) <  10)
Requires:       (php-composer(phpunit/php-file-iterator) >= 3.0.6     with php-composer(phpunit/php-file-iterator) <  4)
Requires:       (php-composer(phpunit/php-invoker) >= 3.1             with php-composer(phpunit/php-invoker) <  4)
Requires:       (php-composer(phpunit/php-text-template) >= 2.0.4     with php-composer(phpunit/php-text-template) <  3)
Requires:       (php-composer(phpunit/php-timer) >= 5.0.3             with php-composer(phpunit/php-timer) < 6)
Requires:       (php-composer(sebastian/cli-parser) >= 1.0.2          with php-composer(sebastian/cli-parser) < 2)
Requires:       (php-composer(sebastian/code-unit) >= 1.0.8           with php-composer(sebastian/code-unit) < 2)
Requires:       (php-composer(sebastian/comparator) >= 4.0.10         with php-composer(sebastian/comparator) <  5)
Requires:       (php-composer(sebastian/diff) >= 4.0.6                with php-composer(sebastian/diff) <  5)
Requires:       (php-composer(sebastian/environment) >= 5.1.5         with php-composer(sebastian/environment) <  6)
Requires:       (php-composer(sebastian/exporter) >= 4.0.8            with php-composer(sebastian/exporter) <  5)
Requires:       (php-composer(sebastian/global-state) >= 5.0.8        with php-composer(sebastian/global-state) <  6)
Requires:       (php-composer(sebastian/object-enumerator) >= 4.0.4   with php-composer(sebastian/object-enumerator) <  5)
Requires:       (php-composer(sebastian/resource-operations) >= 3.0.4 with php-composer(sebastian/resource-operations) <  4)
Requires:       (php-composer(sebastian/type) >= 3.2.1                with php-composer(sebastian/type) < 4)
Requires:       (php-composer(sebastian/version) >= 3.0.1             with php-composer(sebastian/version) <  4)
# From composer.json, "suggest": {
#        "ext-soap": "*",
#        "ext-xdebug": "*"
Suggests:       php-soap
Suggests:       php-xdebug
# recommends latest versions
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
if (PHP_VERSION_ID > 80400) {
	$inst = [
        '%{php_home}/Doctrine/Instantiator2/autoload.php',
        '%{php_home}/Doctrine/Instantiator/autoload.php',
    ];
} else {
	$inst = '%{php_home}/Doctrine/Instantiator/autoload.php';
}
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/SebastianBergmann/CodeCoverage9/autoload.php',
    '%{php_home}/SebastianBergmann/FileIterator3/autoload.php',
    '%{php_home}/SebastianBergmann/Template2/autoload.php',
    '%{php_home}/SebastianBergmann/Timer5/autoload.php',
    $inst,
    '%{php_home}/SebastianBergmann/CliParser/autoload.php',
    '%{php_home}/SebastianBergmann/CodeUnit/autoload.php',
    '%{php_home}/SebastianBergmann/Invoker3/autoload.php',
    '%{php_home}/SebastianBergmann/Diff4/autoload.php',
    '%{php_home}/SebastianBergmann/Comparator4/autoload.php',
    '%{php_home}/SebastianBergmann/Environment5/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter4/autoload.php',
    '%{php_home}/SebastianBergmann/GlobalState5/autoload.php',
    '%{php_home}/SebastianBergmann/ObjectEnumerator4/autoload.php',
    '%{php_home}/SebastianBergmann/ResourceOperations3/autoload.php',
    '%{php_home}/SebastianBergmann/Type3/autoload.php',
    '%{php_home}/SebastianBergmann/Version3/autoload.php',
    '%{php_home}/DeepCopy/autoload.php',
    '%{php_home}/PharIo/Manifest2/autoload.php',
    '%{php_home}/PharIo/Version3/autoload.php',
    __DIR__ . '/Framework/Assert/Functions.php',
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
  --exclude  'tests/end-to-end/regression/4376/tests/Test.php' \
  --exclude  'tests/end-to-end/regression/2448/Test.php' \
  --exclude  'tests/end-to-end/migration/_files/possibility-to-migrate-from-85-is-detected/src/Greeter.php' \
  --exclude  'tests/end-to-end/migration/_files/possibility-to-migrate-from-85-is-detected/tests/GreeterTest.php' \
  tests

%install
mkdir -p       %{buildroot}%{php_home}
cp -pr src     %{buildroot}%{php_home}/%{ns_vendor}
cp -pr schema  %{buildroot}%{php_home}/%{ns_vendor}/schema
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
