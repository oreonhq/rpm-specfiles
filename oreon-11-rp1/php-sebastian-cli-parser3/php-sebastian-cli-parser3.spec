%global source0_hash 9edfdc899f0ff5de7341f8999b57222ba207dd6386132fcb53f6cef9c043a99f

# remirepo/fedora spec file for php-sebastian-cli-parser3
#
# SPDX-FileCopyrightText:  Copyright 2020-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# disabled until phpunit11 available
%bcond_without       tests

# github
%global gh_commit    15c5dd40dc4f38794d383bb95465193f5e0ae180
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   cli-parser
%global gh_date      2024-07-03
# packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
# namespace
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   CliParser

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.2
Release:        4%{?dist}
Summary:        Library for parsing CLI options, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^11.0"
BuildRequires:  phpunit11
%endif

# from composer.json, "require": {
#        "php": ">=8.2",
Requires:       php(language) >= 8.2
# from phpcompatinfo report for version 2.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Library for parsing $_SERVER['argv'], extracted from phpunit/phpunit.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php82 php83 php84; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit11 || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
