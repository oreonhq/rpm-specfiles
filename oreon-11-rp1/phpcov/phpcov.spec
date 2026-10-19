%global source0_hash 942fb3660cc7b3be5fe5123708aa4c43df338a43304d3717384be4eb52f507eb
%bcond_without tests
%global gh_commit    74b950835e1b012ec422f112492929b2c832ffe5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   phpcov
%global php_home     %{_datadir}/php
%global pk_vendor    phpunit
%global pk_project   phpcov
%global ns_vendor    SebastianBergmann
%global ns_project   PHPCOV
Name:           %{pk_project}
Version:        13.1.0
Release:        1%{?dist}
Summary:        CLI frontend for PHP_CodeCoverage
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
Patch0:         %{gh_project}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.4
Requires:       phpunit13
Requires:       (php-composer(phpunit/php-code-coverage) >= 13.0.1 with php-composer(phpunit/php-code-coverage) < 14)
Requires:       (php-composer(phpunit/php-file-iterator) >= 7.0.0  with php-composer(phpunit/php-file-iterator) < 8)
Requires:       (php-composer(sebastian/cli-parser)      >= 5.0.0  with php-composer(sebastian/cli-parser)      < 6)
Requires:       (php-composer(sebastian/diff)            >= 8.0.0  with php-composer(sebastian/diff)            < 9)
Requires:       (php-composer(sebastian/version)         >= 7.0.0  with php-composer(sebastian/version)         < 8)
Obsoletes:      php-phpunit-phpcov < 4
Provides:       php-phpunit-phpcov = %{version}
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(phpunit/php-code-coverage) >= 13.0.1 with php-composer(phpunit/php-code-coverage) < 14)
BuildRequires:  (php-composer(phpunit/php-file-iterator) >= 7.0.0 with php-composer(phpunit/php-file-iterator) < 8)
BuildRequires:  (php-composer(sebastian/cli-parser) >= 5.0.0 with php-composer(sebastian/cli-parser) < 6)
BuildRequires:  (php-composer(sebastian/diff) >= 8.0.0 with php-composer(sebastian/diff) < 9)
BuildRequires:  (php-composer(sebastian/version) >= 7.0.0 with php-composer(sebastian/version) < 8)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pecl(Xdebug)
BuildRequires:  phpunit13
# /oreon:deps
%description
%{pk_project} is a command-line frontend for the PHP_CodeCoverage library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm

%build

phpab \
  --template fedora \
  --output   src/autoload.php \
  src
cat << 'EOF' | tee -a src/autoload.php
// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PHPUnit13/autoload.php',
    '%{php_home}/%{ns_vendor}/CodeCoverage13/autoload.php',
    '%{php_home}/%{ns_vendor}/FileIterator7/autoload.php',
    '%{php_home}/%{ns_vendor}/CliParser5/autoload.php',
    '%{php_home}/%{ns_vendor}/Diff8/autoload.php',
    '%{php_home}/%{ns_vendor}/Version7/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
install -D -p -m 755 %{pk_project} %{buildroot}%{_bindir}/%{pk_project}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php vendor/autoload.php
if ! php -v | grep Xdebug
then EXT="-d zend_extension=xdebug.so"
fi
rm tests/end-to-end/execute/valid-script-argument-with-cli-include-with-text-report.phpt
rm tests/end-to-end/merge/valid-directory-with-text-report.phpt
rm tests/end-to-end/merge/valid-directory-with-text-report-stdout.phpt
rm tests/end-to-end/patch-coverage/valid-arguments-with-valid-path-prefix.phpt
ret=0
for cmd in php php84 php85; do
  if which $cmd; then
    $cmd $EXT -d xdebug.mode=coverage %{_bindir}/phpunit13 --testsuite end-to-end || ret=1
  fi
done
exit $ret;
%else
: Test suite skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
