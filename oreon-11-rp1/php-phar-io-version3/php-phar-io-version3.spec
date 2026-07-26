%global source0_hash 9ab930c1d3a453a8fd63f3fe954514867cd07eb663f2bce4df8b67569ad20621

# remirepo/fedora spec file for php-phar-io-version3
#
# Copyright (c) 2017-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    4f7fd7836c6f332bb2933569e566a0d6c4cbed74
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   version
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Version
%global major        3
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.2.1
Release:        10%{?dist}
Summary:        Library for handling version information and constraints

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif

# from composer.json
#    "php": "^7.2 || ^8.0",
Requires:       php(language) >= 7.2
# from phpcompatinfo report for version 3.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Library for handling version information and constraints.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
: Run upstream test suite
ret=0
BS=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php
for cmd in "php %{phpunit}" php80 php81 php82; do
  if which $cmd; then
    set $cmd
    $1 -d auto_prepend_file=$BS \
      ${2:-%{_bindir}/phpunit9} \
        --bootstrap $BS --verbose || ret=1
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
