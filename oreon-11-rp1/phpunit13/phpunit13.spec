%global source0_hash bee9c0c73bb6e9e2b6b675396158f164c4c08a747cace4be2aca69bbfc037070
%bcond_without       tests
%if 0%{?fedora} >= 44 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
%bcond_without       defcmd
%else
%bcond_with          defcmd
%endif
%global gh_commit    d57826e8921a534680c613924bfd921ded8047f4
%global gh_date      2026-02-18
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit
%global pk_vendor    phpunit
%global pk_project   phpunit
%global ns_vendor    PHPUnit13
%global php_home     %{_datadir}/php
%global ver_major    13
%global ver_minor    0
%global upstream_version 13.0.5
Name:           %{pk_project}%{ver_major}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        The PHP Unit Testing framework version 13
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
Requires:       php(language) >= 8.4.1
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
Requires:       (php-composer(phpunit/php-code-coverage) >= 13.0.1    with php-composer(phpunit/php-code-coverage) < 14)
Requires:       (php-composer(phpunit/php-file-iterator) >= 7.0.0     with php-composer(phpunit/php-file-iterator) < 8)
Requires:       (php-composer(phpunit/php-invoker) >= 7.0.0           with php-composer(phpunit/php-invoker) < 8)
Requires:       (php-composer(phpunit/php-text-template) >= 6.0.0     with php-composer(phpunit/php-text-template) < 7)
Requires:       (php-composer(phpunit/php-timer) >= 9.0.0             with php-composer(phpunit/php-timer) < 10)
Requires:       (php-composer(sebastian/cli-parser) >= 5.0.0          with php-composer(sebastian/cli-parser) < 6)
Requires:       (php-composer(sebastian/comparator) >= 8.0.0          with php-composer(sebastian/comparator) < 9)
Requires:       (php-composer(sebastian/diff) >= 8.0.0                with php-composer(sebastian/diff) < 9)
Requires:       (php-composer(sebastian/environment) >= 9.0.0         with php-composer(sebastian/environment) < 10)
Requires:       (php-composer(sebastian/exporter) >= 8.0.0            with php-composer(sebastian/exporter) < 9)
Requires:       (php-composer(sebastian/global-state) >= 9.0.0        with php-composer(sebastian/global-state) < 10)
Requires:       (php-composer(sebastian/object-enumerator) >= 8.0.0   with php-composer(sebastian/object-enumerator) < 9)
Requires:       (php-composer(sebastian/recursion-context) >= 8.0.0   with php-composer(sebastian/recursion-context) < 9)
Requires:       (php-composer(sebastian/type) >= 7.0.0                with php-composer(sebastian/type) < 8)
Requires:       (php-composer(sebastian/version) >= 7.0.0             with php-composer(sebastian/version) < 8)
Requires:       (php-composer(staabm/side-effects-detector) >= 1.0.5  with php-composer(staabm/side-effects-detector) < 2)
Recommends:     phpunit13
Requires:       php-composer(fedora/autoloader)
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-phar
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
Provides:       php-composer(phpunit/phpunit) = %{version}
%endif
%if %{with defcmd}
Provides:       phpunit                       = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.13.4 with php-composer(myclabs/deep-copy) < 2)
BuildRequires:  (php-composer(phar-io/manifest) >= 2.0.4 with php-composer(phar-io/manifest) < 3)
BuildRequires:  (php-composer(phar-io/version) >= 3.2.1 with php-composer(phar-io/version) < 4)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 13.0.1 with php-composer(phpunit/php-code-coverage) < 14)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 7.0.0 with php-composer(phpunit/php-file-iterator) < 8)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 7.0.0 with php-composer(phpunit/php-invoker) < 8)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 6.0.0 with php-composer(phpunit/php-text-template) < 7)
BuildRequires:  (php-composer(phpunit/php-timer) >= 9.0.0 with php-composer(phpunit/php-timer) < 10)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 5.0.0 with php-composer(sebastian/cli-parser) < 6)
BuildRequires:  (php-composer(sebastian/comparator) >= 8.0.0 with php-composer(sebastian/comparator) < 9)
BuildRequires:  (php-composer(sebastian/diff) >= 8.0.0 with php-composer(sebastian/diff) < 9)
BuildRequires:  (php-composer(sebastian/environment) >= 9.0.0 with php-composer(sebastian/environment) < 10)
BuildRequires:  (php-composer(sebastian/exporter) >= 8.0.0 with php-composer(sebastian/exporter) < 9)
BuildRequires:  (php-composer(sebastian/global-state) >= 9.0.0 with php-composer(sebastian/global-state) < 10)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 8.0.0 with php-composer(sebastian/object-enumerator) < 9)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 8.0.0 with php-composer(sebastian/recursion-context) < 9)
BuildRequires:  (php-composer(sebastian/type) >= 7.0.0 with php-composer(sebastian/type) < 8)
BuildRequires:  (php-composer(sebastian/version) >= 7.0.0 with php-composer(sebastian/version) < 8)
BuildRequires:  (php-composer(staabm/side-effects-detector) >= 1.0.5 with php-composer(staabm/side-effects-detector) < 2)
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-json
BuildRequires:  php-libxml
BuildRequires:  php-mbstring
BuildRequires:  php-xml
BuildRequires:  php-xmlwriter
# /oreon:deps
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
    '%{php_home}/SebastianBergmann/CodeCoverage13/autoload.php',
    '%{php_home}/SebastianBergmann/FileIterator7/autoload.php',
    '%{php_home}/SebastianBergmann/Template6/autoload.php',
    '%{php_home}/SebastianBergmann/Timer9/autoload.php',
    '%{php_home}/SebastianBergmann/CliParser5/autoload.php',
    '%{php_home}/SebastianBergmann/Invoker7/autoload.php',
    '%{php_home}/SebastianBergmann/Diff8/autoload.php',
    '%{php_home}/SebastianBergmann/Comparator8/autoload.php',
    '%{php_home}/SebastianBergmann/Environment9/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter8/autoload.php',
    '%{php_home}/SebastianBergmann/GlobalState9/autoload.php',
    '%{php_home}/SebastianBergmann/ObjectEnumerator8/autoload.php',
    '%{php_home}/SebastianBergmann/RecursionContext8/autoload.php',
    '%{php_home}/SebastianBergmann/Type7/autoload.php',
    '%{php_home}/SebastianBergmann/Version7/autoload.php',
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
  __DIR__ . '/unit/TextUI/AbstractSouceFilterTestCase.php',
  __DIR__ . '/unit/Framework/MockObject/TestDoubleTestCase.php',
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
%oreon_autofiles main
%endif
%if %{with tests}
%check

OPT='--filter "^((?!(testIsInitialized|testExclusionOfFileCanBeQueried)).)*$" --testsuite=unit --no-coverage'
sed -e 's:@PATH@:%{buildroot}%{php_home}/%{ns_vendor}:' -i tests/bootstrap.php
sed -e 's:%{php_home}/%{ns_vendor}:%{buildroot}%{php_home}/%{ns_vendor}:' -i phpunit
ret=0
for cmd in php php84 php85; do
  if which $cmd; then
     $cmd ./phpunit $OPT || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
