%global source0_hash 382c88dba4825161f6e342be681c168c3b84e67285fc6f2af00756ee022fcc87

# remirepo/fedora spec file for phpunit11
#
# SPDX-FileCopyrightText:  Copyright 2010-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%if 0%{?fedora} == 41
%bcond_without       defcmd
%else
%bcond_with          defcmd
%endif

%global gh_commit    adc7262fccc12de2b30f12a8aa0b33775d814f00
%global gh_date      2026-02-18
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit
# Packagist
%global pk_vendor    phpunit
%global pk_project   phpunit
# Namespace
%global ns_vendor    PHPUnit11
%global php_home     %{_datadir}/php
%global ver_major    11
%global ver_minor    5

%global upstream_version 11.5.55
#global upstream_prever  dev

Name:           %{pk_project}%{ver_major}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        The PHP Unit Testing framework version %{ver_major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{upstream_version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Fix command for autoload
Patch0:         %{name}-rpm.patch

BuildArch:      noarch
BuildRequires:  php(language) >= 8.2
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.13.4            with php-composer(myclabs/deep-copy) <  2)
BuildRequires:  (php-composer(phar-io/manifest) >= 2.0.4              with php-composer(phar-io/manifest) < 3)
BuildRequires:  (php-composer(phar-io/version) >= 3.2.1               with php-composer(phar-io/version) <  4)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 11.0.12   with php-composer(phpunit/php-code-coverage) < 12)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 5.1.1     with php-composer(phpunit/php-file-iterator) < 6)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 5.0.1           with php-composer(phpunit/php-invoker) < 6)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 4.0.1     with php-composer(phpunit/php-text-template) < 5)
BuildRequires:  (php-composer(phpunit/php-timer) >= 7.0.1             with php-composer(phpunit/php-timer) < 8)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 3.0.2          with php-composer(sebastian/cli-parser) < 4)
BuildRequires:  (php-composer(sebastian/code-unit) >= 3.0.3           with php-composer(sebastian/code-unit) < 4)
BuildRequires:  (php-composer(sebastian/comparator) >= 6.3.3          with php-composer(sebastian/comparator) < 7)
BuildRequires:  (php-composer(sebastian/diff) >= 6.0.2                with php-composer(sebastian/diff) < 7)
BuildRequires:  (php-composer(sebastian/environment) >= 7.2.1         with php-composer(sebastian/environment) < 8)
BuildRequires:  (php-composer(sebastian/exporter) >= 6.3.2            with php-composer(sebastian/exporter) < 7)
BuildRequires:  (php-composer(sebastian/global-state) >= 7.0.2        with php-composer(sebastian/global-state) < 8)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 6.0.1   with php-composer(sebastian/object-enumerator) < 7)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 6.0.3   with php-composer(sebastian/recursion-context) < 7)
BuildRequires:  (php-composer(sebastian/type) >= 5.1.3                with php-composer(sebastian/type) < 6)
BuildRequires:  (php-composer(sebastian/version) >= 5.0.2             with php-composer(sebastian/version) < 6)
BuildRequires:  (php-composer(staabm/side-effects-detector) >= 1.0.5  with php-composer(staabm/side-effects-detector) < 2)
BuildRequires:  php-dom
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-xml
BuildRequires:  php-libxml
BuildRequires:  php-xmlwriter
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0

# From composer.json, "require": {
#        "php": ">=8.2",
#        "ext-dom": "*",
#        "ext-json": "*",
#        "ext-libxml": "*",
#        "ext-mbstring": "*",
#        "ext-xml": "*",
#        "ext-xmlwriter": "*",
#        "myclabs/deep-copy": "^1.13.4",
#        "phar-io/manifest": "^2.0.4",
#        "phar-io/version": "^3.2.1",
#        "phpunit/php-code-coverage": "^11.0.12",
#        "phpunit/php-file-iterator": "^5.1.1",
#        "phpunit/php-invoker": "^5.0.1",
#        "phpunit/php-text-template": "^4.0.1",
#        "phpunit/php-timer": "^7.0.1",
#        "sebastian/cli-parser": "^3.0.2",
#        "sebastian/code-unit": "^3.0.3",
#        "sebastian/comparator": "^6.3.3",
#        "sebastian/diff": "^6.0.2",
#        "sebastian/environment": "^7.2.1",
#        "sebastian/exporter": "^6.3.2",
#        "sebastian/global-state": "^7.0.2",
#        "sebastian/object-enumerator": "^6.0.1",
#        "sebastian/recursion-context": "^6.0.3",
#        "sebastian/type": "^5.1.3",
#        "sebastian/version": "^5.0.2",
#        "staabm/side-effects-detector": "^1.0.5"
Requires:       php(language) >= 8.2
Requires:       php-cli
Requires:       php-dom
Requires:       php-json
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-xmlwriter
Requires:       (php-composer(myclabs/deep-copy) >= 1.13.4            with php-composer(myclabs/deep-copy) <  2)
Requires:       (php-composer(phar-io/manifest) >= 2.0.4              with php-composer(phar-io/manifest) < 3)
Requires:       (php-composer(phar-io/version) >= 3.2.1               with php-composer(phar-io/version) < 4)
Requires:       (php-composer(phpunit/php-code-coverage) >= 11.0.12   with php-composer(phpunit/php-code-coverage) < 12)
Requires:       (php-composer(phpunit/php-file-iterator) >= 5.1.1     with php-composer(phpunit/php-file-iterator) < 6)
Requires:       (php-composer(phpunit/php-invoker) >= 5.0.1           with php-composer(phpunit/php-invoker) < 6)
Requires:       (php-composer(phpunit/php-text-template) >= 4.0.1     with php-composer(phpunit/php-text-template) < 5)
Requires:       (php-composer(phpunit/php-timer) >= 7.0.1             with php-composer(phpunit/php-timer) < 8)
Requires:       (php-composer(sebastian/cli-parser) >= 3.0.2          with php-composer(sebastian/cli-parser) < 4)
Requires:       (php-composer(sebastian/code-unit) >= 3.0.3           with php-composer(sebastian/code-unit) < 4)
Requires:       (php-composer(sebastian/comparator) >= 6.3.3          with php-composer(sebastian/comparator) < 7)
Requires:       (php-composer(sebastian/diff) >= 6.0.2                with php-composer(sebastian/diff) < 7)
Requires:       (php-composer(sebastian/environment) >= 7.2.1         with php-composer(sebastian/environment) < 8)
Requires:       (php-composer(sebastian/exporter) >= 6.3.2            with php-composer(sebastian/exporter) < 7)
Requires:       (php-composer(sebastian/global-state) >= 7.0.2        with php-composer(sebastian/global-state) < 8)
Requires:       (php-composer(sebastian/object-enumerator) >= 6.0.1   with php-composer(sebastian/object-enumerator) < 7)
Requires:       (php-composer(sebastian/recursion-context) >= 6.0.3   with php-composer(sebastian/recursion-context) < 7)
Requires:       (php-composer(sebastian/type) >= 5.1.3                with php-composer(sebastian/type) < 6)
Requires:       (php-composer(sebastian/version) >= 5.0.2             with php-composer(sebastian/version) < 6)
Requires:       (php-composer(staabm/side-effects-detector) >= 1.0.5  with php-composer(staabm/side-effects-detector) < 2)
# From composer.json, "suggest": {
#        "ext-soap": "*",
Suggests:       php-soap
# recommends latest versions
Recommends:     phpunit12
Recommends:     phpunit13
# Autoloader
Requires:       php-composer(fedora/autoloader)
# From phpcompatinfo report for version 10.0.0
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-phar

%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10
Provides:       php-composer(phpunit/phpunit) = %{version}
%endif
%if %{with defcmd}
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
    '%{php_home}/SebastianBergmann/CodeCoverage11/autoload.php',
    '%{php_home}/SebastianBergmann/FileIterator5/autoload.php',
    '%{php_home}/SebastianBergmann/Template4/autoload.php',
    '%{php_home}/SebastianBergmann/Timer7/autoload.php',
    '%{php_home}/SebastianBergmann/CliParser3/autoload.php',
    '%{php_home}/SebastianBergmann/CodeUnit3/autoload.php',
    '%{php_home}/SebastianBergmann/Invoker5/autoload.php',
    '%{php_home}/SebastianBergmann/Diff6/autoload.php',
    '%{php_home}/SebastianBergmann/Comparator6/autoload.php',
    '%{php_home}/SebastianBergmann/Environment7/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter6/autoload.php',
    '%{php_home}/SebastianBergmann/GlobalState7/autoload.php',
    '%{php_home}/SebastianBergmann/ObjectEnumerator6/autoload.php',
    '%{php_home}/SebastianBergmann/RecursionContext6/autoload.php',
    '%{php_home}/SebastianBergmann/Type5/autoload.php',
    '%{php_home}/SebastianBergmann/Version5/autoload.php',
    '%{php_home}/staabm/SideEffectsDetector/autoload.php',
    '%{php_home}/DeepCopy/autoload.php',
    '%{php_home}/PharIo/Manifest2/autoload.php',
    '%{php_home}/PharIo/Version3/autoload.php',
    __DIR__ . '/Framework/Assert/Functions.php',
]);
// Extensions
\Fedora\Autoloader\Dependencies::optional(
    glob("%{php_home}/%{ns_vendor}/Extensions/*/autoload.php")
);
EOF
cat src/autoload.php

%{_bindir}/phpab \
  --output   tests/autoload.php \
  tests/_files
cat << 'EOF' | tee -a tests/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
  __DIR__ . '/_files/deprecation-trigger/trigger_deprecation.php',
  __DIR__ . '/unit/Event/AbstractEventTestCase.php',
  __DIR__ . '/unit/Framework/MockObject/TestDoubleTestCase.php',
  __DIR__ . '/unit/Metadata/Parser/AnnotationParserTestCase.php',
  __DIR__ . '/unit/Metadata/Parser/AttributeParserTestCase.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyArrayTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyBoolTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyCallableTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyFloatTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyInstancesOfTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyIntTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyIterableTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyNullTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyNumericTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyObjectTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyResourceTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyClosedResourceTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyScalarTest.php',
  __DIR__ . '/unit/Framework/Assert/assertContainsOnlyStringTest.php',
  __DIR__ . '/unit/Framework/Assert/assertDirectoryExistsTest.php',
  __DIR__ . '/unit/Framework/Assert/assertFileExistsTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsNumericTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsObjectTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsReadableTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsResourceTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsScalarTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsStringTest.php',
  __DIR__ . '/unit/Framework/Assert/assertIsWritableTest.php',
  __DIR__ . '/unit/Framework/Assert/assertMatchesRegularExpressionTest.php',
  __DIR__ . '/unit/Framework/Assert/assertNullTest.php',
  __DIR__ . '/unit/Framework/Assert/assertSameSizeTest.php',
  __DIR__ . '/unit/Framework/Assert/assertSameTest.php',
  __DIR__ . '/_files/CoverageNamespacedFunctionTest.php',
  __DIR__ . '/_files/CoveredFunction.php',
  __DIR__ . '/_files/Generator.php',
  __DIR__ . '/_files/NamespaceCoveredFunction.php',
  __DIR__ . '/end-to-end/_files/listing-tests-and-groups/ExampleAbstractTestCase.php',
]);
EOF

%install
mkdir -p       %{buildroot}%{php_home}
cp -pr src     %{buildroot}%{php_home}/%{ns_vendor}
cp -pr schema  %{buildroot}%{php_home}/%{ns_vendor}/schema
mkdir          %{buildroot}%{php_home}/%{ns_vendor}/Extensions

install -D -p -m 755 phpunit %{buildroot}%{_bindir}/%{name}
install -p -m 644 phpunit.xsd %{buildroot}%{php_home}/%{ns_vendor}/phpunit.xsd

%if %{with defcmd}
ln -s %{name} %{buildroot}%{_bindir}/phpunit
%endif

%if %{with tests}
%check
# ignore tests relying on git layout
OPT='--filter "^((?!(testIsInitialized|testExclusionOfFileCanBeQueried)).)*$" --testsuite=unit --no-coverage'
sed -e 's:@PATH@:%{buildroot}%{php_home}/%{ns_vendor}:' -i tests/bootstrap.php
sed -e 's:%{php_home}/%{ns_vendor}:%{buildroot}%{php_home}/%{ns_vendor}:' -i phpunit

ret=0
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
     $cmd ./phpunit $OPT || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md ChangeLog-%{ver_major}.%{ver_minor}.md
%doc composer.json
%{_bindir}/%{name}
%if %{with defcmd}
%{_bindir}/phpunit
%endif
%{php_home}/%{ns_vendor}

%changelog
%autochangelog
