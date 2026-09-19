%global source0_hash 626f5f1cab293e01bbee17ac56f6d0ad53a6fd8be4499db806eb277069033eea

# remirepo/fedora spec file for php-phpunit-php-file-iterator2
#
# Copyright (c) 2009-2024 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    69deeb8664f611f156a924154985fbd4911eb36b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-file-iterator
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        2
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   FileIterator
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.6
Release:        5%{?dist}
Summary:        FilterIterator implementation that filters files based on a list of suffixes

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with_tests}
# From composer.json, "require-dev"
#        "phpunit/phpunit": "^8.5"
BuildRequires:  phpunit8 >= 8.5
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-pcre
BuildRequires:  php-spl
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require"
#        "php": "^7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for 2.0.2
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/php-file-iterator) = %{version}

%description
FilterIterator implementation that filters files based on a list of suffixes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%{_bindir}/phpab \
   --template fedora \
   --output   src/autoload.php \
   src

%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src  %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with_tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit8  --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc ChangeLog.md README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
