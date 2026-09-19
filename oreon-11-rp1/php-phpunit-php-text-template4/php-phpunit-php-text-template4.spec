%global source0_hash 86aaa7ef183f3ed3cb6480aefc083ed7794c5ea1a03ea8f5fccb8660b915b6f1

# remirepo/fedora spec file for php-phpunit-php-text-template4
#
# SPDX-FileCopyrightText:  Copyright 2010-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# disabled until phpunit11 available
%bcond_without       tests

%global gh_commit    3e0404dc6b300e6bf56415467ebcb3fe4f33e964
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-text-template
%global gh_date      2024-07-03
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   Template
%global php_home     %{_datadir}/php
%global ver_major    4

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        4.0.1
Release:        5%{?dist}
Summary:        Simple template engine, version %{ver_major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.2
BuildRequires:  php-spl
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json, require-dev
#        "phpunit/phpunit": "^11.0"
BuildRequires:  phpunit11
%endif

# From composer.json
#        "php": ">=8.2"
Requires:       php(language) >= 8.2
# From phpcompatinfo report for version 3.0.0
Requires:       php-spl

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Simple template engine.

This package provides version %{ver_major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%if %{with tests}
%check
: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests

: Run upstream test suite
ret=0
for cmd in php php82 php83 php84; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php \
      %{_bindir}/phpunit11 || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%changelog
%autochangelog
