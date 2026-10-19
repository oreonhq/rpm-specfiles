%global source0_hash f328d1659da33c78a9de775f28e3be02058c3cefb18b6cb0a0f733a24d06d086
%bcond_without       tests
%global gh_commit    1f3a77a382c5d273a0f1fe34be3b8af4060a88cd
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swaggest
%global gh_project   php-json-schema
%global pk_vendor    %{gh_owner}
%global pk_project   json-schema
%global ns_vendor    Swaggest
%global ns_project   JsonSchema
%global major        %nil
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        0.12.43
Release:        4%{?dist}
Summary:        High definition PHP structures with JSON-schema based validation
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.1
Requires:       php-json
Requires:       php-mbstring
Requires:      (php-composer(phplang/scope-exit)    >= 1.0   with php-composer(phplang/scope-exit)    < 2)
Requires:      (php-composer(swaggest/json-diff)    >= 3.8.2 with php-composer(swaggest/json-diff)    < 4)
Requires:       php-date
Requires:       php-filter
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(phplang/scope-exit) >= 1.0 with php-composer(phplang/scope-exit) < 2)
BuildRequires:  (php-composer(swaggest/json-diff) >= 3.8.2 with php-composer(swaggest/json-diff) < 4)
BuildRequires:  php(language)
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-filter
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
High definition PHP structures with JSON-schema based validation.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Fix layout
mkdir src/spec
cp -p spec/*.json src/spec/
sed -e 's:/../spec/:/spec/:' -i src/RemoteRef/Preloaded.php

%build

: Create autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/PhpLang/scope-exit-autoload.php',
    '%{_datadir}/php/Swaggest/JsonDiff/autoload.php',
]);
EOF
%install
: Library
mkdir -p         %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src       %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests/src');
class PHPUnit_Framework_TestCase extends \PHPUnit\Framework\Testcase {
	function setExpectedException($e, $m = '') {
		$this->expectException($e);
		if ($m) $this->expectExceptionMessage($m);
	}
}
EOF
sed -e '/setUp()/s/$/:void/' \
  -i tests/src/PHPUnit/Example/ExampleTest.php
ret=0
for cmd in php php81 php82 php83 php84; do
   if which $cmd; then
      $cmd %{phpunit} \
        --no-coverage \
        --filter '^((?!(SwaggerTest::testInvalid|SwaggerTest::testValidate|testPatternPropertiesMismatch)).)*$' \
        || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
