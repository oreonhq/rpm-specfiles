%global source0_hash 8f50fd7148f0ef1055d97f5b5524d95d427ca1349a9f1aafb13af524e59465e3
%bcond_without       tests
%global gh_commit    7ebc4eab95bcc73916433964c266588d09b35052
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swaggest
%global gh_project   json-diff
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    Swaggest
%global ns_project   JsonDiff
%global major        %nil
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.12.1
Release:        1%{?dist}
Summary:        JSON diff/rearrange/patch/pointer library for PHP
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
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-json
BuildRequires:  phpunit9
# /oreon:deps
%description
A PHP implementation for finding unordered diff between two JSON documents.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Create autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src
%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\', dirname(__DIR__).'/tests');
class PHPUnit_Framework_TestCase extends \PHPUnit\Framework\Testcase {
	function setExpectedException($e, $m) {
		$this->expectException($e);
		$this->expectExceptionMessage($m);
	}
}
EOF
ret=0
for cmd in php php81 php82 php83 php84; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
