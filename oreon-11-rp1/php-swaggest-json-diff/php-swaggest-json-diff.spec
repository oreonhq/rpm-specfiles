%global source0_hash 8f50fd7148f0ef1055d97f5b5524d95d427ca1349a9f1aafb13af524e59465e3

# remirepo/fedora spec file for php-swaggest-json-diff
#
# SPDX-FileCopyrightText:  Copyright 2019-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    7ebc4eab95bcc73916433964c266588d09b35052
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     swaggest
%global gh_project   json-diff
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Swaggest
%global ns_project   JsonDiff
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.12.1
Release:        3%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        JSON diff/rearrange/patch/pointer library for PHP

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-json
# For tests, from composer.json "require-dev": {
#    "phpunit/phpunit": "4.8.37"
BuildRequires:  phpunit9
%global phpunit %{_bindir}/phpunit9
# For autoloader
BuildRequires:  php-fedora-autoloader-devel
%endif

# From composer.json, "require": {
#    "ext-json": "*",
#    "php": ">=7.1"
Requires:       php(language) >= 7.1
Requires:       php-json
# From phpcompatinfo report for 3.12.1
# only filter, json and pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

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

%files
%license LICENSE
%doc composer.json
%doc README.md
%doc CHANGELOG.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
