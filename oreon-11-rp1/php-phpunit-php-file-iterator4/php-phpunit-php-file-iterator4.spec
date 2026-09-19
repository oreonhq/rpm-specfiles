%global source0_hash 7ea19c760985f259943e4ae4432a3b12c7758fed9e4f285a6a5b21909e9277ae

# remirepo/fedora spec file for php-phpunit-php-file-iterator4
#
# Copyright (c) 2009-2023 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    a95037b6d9e608ba092da1b23931e537cadc3c3c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-file-iterator
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        4
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   FileIterator

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.1.0
Release:        7%{?dist}
Summary:        FilterIterator implementation based on a list of suffixes, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-pcre
BuildRequires:  php-spl
%if %{with tests}
# From composer.json, "require-dev"
#        "phpunit/phpunit": "^10.0"
BuildRequires:  phpunit10
%endif
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require"
#        "php": ">=8.1"
Requires:       php(language) >= 8.1
# From phpcompatinfo report for 4.0.0
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
FilterIterator implementation that filters files based on a list of suffixes.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

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
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit10 || ret=1
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
