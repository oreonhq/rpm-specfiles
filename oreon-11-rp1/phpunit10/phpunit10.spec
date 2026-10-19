%global source0_hash cab4b3739f9f99fcf6c4b523fe32a6145883d44dede2346b944db27f154829a2
%bcond_without       tests
%bcond_with          defcmd
%global gh_commit    33198268dad71e926626b618f3ec3966661e4d90
%global gh_date      2026-01-27
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpunit
%global pk_vendor    phpunit
%global pk_project   phpunit
%global ns_vendor    PHPUnit10
%global php_home     %{_datadir}/php
%global ver_major    10
%global ver_minor    5
%global upstream_version 10.5.63
Name:           %{pk_project}%{ver_major}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
Summary:        The PHP Unit Testing framework version 10
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
Requires:       php(language) >= 8.1
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
Requires:       (php-composer(phpunit/php-code-coverage) >= 10.1.15   with php-composer(phpunit/php-code-coverage) < 11)
Requires:       (php-composer(phpunit/php-file-iterator) >= 4.1.0     with php-composer(phpunit/php-file-iterator) < 5)
Requires:       (php-composer(phpunit/php-invoker) >= 4.0             with php-composer(phpunit/php-invoker) < 5)
Requires:       (php-composer(phpunit/php-text-template) >= 3.0.1     with php-composer(phpunit/php-text-template) < 4)
Requires:       (php-composer(phpunit/php-timer) >= 6.0               with php-composer(phpunit/php-timer) < 7)
Requires:       (php-composer(sebastian/cli-parser) >= 2.0.1          with php-composer(sebastian/cli-parser) < 3)
Requires:       (php-composer(sebastian/code-unit) >= 2.0             with php-composer(sebastian/code-unit) < 3)
Requires:       (php-composer(sebastian/comparator) >= 5.0.5          with php-composer(sebastian/comparator) < 6)
Requires:       (php-composer(sebastian/diff) >= 5.1.1                with php-composer(sebastian/diff) < 6)
Requires:       (php-composer(sebastian/environment) >= 6.1.0         with php-composer(sebastian/environment) < 7)
Requires:       (php-composer(sebastian/exporter) >= 5.1.4            with php-composer(sebastian/exporter) < 6)
Requires:       (php-composer(sebastian/global-state) >= 6.0.2        with php-composer(sebastian/global-state) < 7)
Requires:       (php-composer(sebastian/object-enumerator) >= 5.0     with php-composer(sebastian/object-enumerator) < 6)
Requires:       (php-composer(sebastian/recursion-context) >= 5.0.1   with php-composer(sebastian/recursion-context) < 6)
Requires:       (php-composer(sebastian/type) >= 4.0                  with php-composer(sebastian/type) < 5)
Requires:       (php-composer(sebastian/version) >= 4.0.1             with php-composer(sebastian/version) < 5)
Suggests:       php-soap
Recommends:     phpunit11
Recommends:     phpunit12
Requires:       php-composer(fedora/autoloader)
Requires:       php-openssl
Requires:       php-pcntl
Requires:       php-phar
%if 0%{?fedora} >= 39 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
Provides:       php-composer(phpunit/phpunit) = %{version}
Provides:       phpunit                       = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  (php-composer(myclabs/deep-copy) >= 1.13.4 with php-composer(myclabs/deep-copy) < 2)
BuildRequires:  (php-composer(phar-io/manifest) >= 2.0.4 with php-composer(phar-io/manifest) < 3)
BuildRequires:  (php-composer(phar-io/version) >= 3.2.1 with php-composer(phar-io/version) < 4)
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 10.1.15 with php-composer(phpunit/php-code-coverage) < 11)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 4.1.0 with php-composer(phpunit/php-file-iterator) < 5)
BuildRequires:  (php-composer(phpunit/php-invoker) >= 4.0 with php-composer(phpunit/php-invoker) < 5)
BuildRequires:  (php-composer(phpunit/php-text-template) >= 3.0.1 with php-composer(phpunit/php-text-template) < 4)
BuildRequires:  (php-composer(phpunit/php-timer) >= 6.0 with php-composer(phpunit/php-timer) < 7)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 2.0.1 with php-composer(sebastian/cli-parser) < 3)
BuildRequires:  (php-composer(sebastian/code-unit) >= 2.0 with php-composer(sebastian/code-unit) < 3)
BuildRequires:  (php-composer(sebastian/comparator) >= 5.0.5 with php-composer(sebastian/comparator) < 6)
BuildRequires:  (php-composer(sebastian/diff) >= 5.1.1 with php-composer(sebastian/diff) < 6)
BuildRequires:  (php-composer(sebastian/environment) >= 6.1.0 with php-composer(sebastian/environment) < 7)
BuildRequires:  (php-composer(sebastian/exporter) >= 5.1.4 with php-composer(sebastian/exporter) < 6)
BuildRequires:  (php-composer(sebastian/global-state) >= 6.0.2 with php-composer(sebastian/global-state) < 7)
BuildRequires:  (php-composer(sebastian/object-enumerator) >= 5.0 with php-composer(sebastian/object-enumerator) < 6)
BuildRequires:  (php-composer(sebastian/recursion-context) >= 5.0.1 with php-composer(sebastian/recursion-context) < 6)
BuildRequires:  (php-composer(sebastian/type) >= 4.0 with php-composer(sebastian/type) < 5)
BuildRequires:  (php-composer(sebastian/version) >= 4.0.1 with php-composer(sebastian/version) < 5)
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
    '%{php_home}/SebastianBergmann/CodeCoverage10/autoload.php',
    '%{php_home}/SebastianBergmann/FileIterator4/autoload.php',
    '%{php_home}/SebastianBergmann/Template3/autoload.php',
    '%{php_home}/SebastianBergmann/Timer6/autoload.php',
    '%{php_home}/SebastianBergmann/CliParser2/autoload.php',
    '%{php_home}/SebastianBergmann/CodeUnit2/autoload.php',
    '%{php_home}/SebastianBergmann/Invoker4/autoload.php',
    '%{php_home}/SebastianBergmann/Diff5/autoload.php',
    '%{php_home}/SebastianBergmann/Comparator5/autoload.php',
    '%{php_home}/SebastianBergmann/Environment6/autoload.php',
    '%{php_home}/SebastianBergmann/Exporter5/autoload.php',
    '%{php_home}/SebastianBergmann/GlobalState6/autoload.php',
    '%{php_home}/SebastianBergmann/ObjectEnumerator5/autoload.php',
    '%{php_home}/SebastianBergmann/RecursionContext5/autoload.php',
    '%{php_home}/SebastianBergmann/Type4/autoload.php',
    '%{php_home}/SebastianBergmann/Version4/autoload.php',
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
  __DIR__ . '/unit/Event/AbstractEventTestCase.php',
  __DIR__ . '/unit/Framework/MockObject/TestDoubleTestCase.php',
  __DIR__ . '/unit/Metadata/Parser/AnnotationParserTestCase.php',
  __DIR__ . '/unit/Metadata/Parser/AttributeParserTestCase.php',
  __DIR__ . '/_files/CoverageNamespacedFunctionTest.php',
  __DIR__ . '/_files/CoveredFunction.php',
  __DIR__ . '/_files/Generator.php',
  __DIR__ . '/_files/NamespaceCoveredFunction.php',
  __DIR__ . '/end-to-end/code-coverage/ignore-function-using-attribute/src/CoveredFunction.php',
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
for cmd in php php82 php83 php84 php85; do
  if which $cmd; then
     $cmd ./phpunit $OPT || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
