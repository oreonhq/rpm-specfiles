%global source0_hash bba7a0e2dcd4a1d1935c7efcc0bd84c67e6615410c4eee411de4d61a9de4cf34

# remirepo/fedora spec file for php-sebastian-resource-operations3
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    05d5692a7993ecccd56a03e40cd7e5b09b1d404e
#global gh_date      20150728
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   resource-operations
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   ResourceOperations
%global major        3

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.4
Release:        5%{?dist}
Summary:        Provides a list of PHP built-in functions that operate on resources, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json
#        "phpunit/phpunit": "^9.0"
BuildRequires:  phpunit9
%endif

# from composer.json
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# Autoloader
Requires:       php-composer(fedora/autoloader)
# from phpcompatinfo report for version 3.0.0: nothing

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
%{summary}.

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
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9  --verbose tests || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
