%global source0_hash ca261e43b8e163f87c343d64087166a4c2c21ee410493f0e34db8ef5977619f0

# remirepo/fedora spec file for php-zetacomponents-console-tools
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%global gh_commit    de081f422b574d638e62e15661bf833d80fac61a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   ConsoleTools
%global cname        console-tools
%global ezcdir       %{_datadir}/php/ezc

%if 0%{?fedora}
%bcond_without  tests
%else
%bcond_with     tests
%endif
%bcond_without  phpab

Name:           php-%{gh_owner}-%{cname}
Version:        1.7.5
Release:        4%{?dist}
Summary:        Zeta %{gh_project} Component

License:        Apache-2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        autoloader.php

BuildArch:      noarch
%if %{with phpab}
BuildRequires:  %{_bindir}/phpab
%endif
%if %{with tests}
BuildRequires: (php-composer(%{gh_owner}/base) >= 1.8   with php-composer(%{gh_owner}/base) < 2)
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "~9.0",
#        "zetacomponents/unit-test": "*"
BuildRequires:  phpunit9
BuildRequires:  php-composer(%{gh_owner}/unit-test) >= 1.2.4
%endif

# From composer.json, "require": {
#            "zetacomponents/base": "~1.8"
Requires:      (php-composer(%{gh_owner}/base) >= 1.8   with php-composer(%{gh_owner}/base) < 2)
# From phpcompatinfo report for 1.7
Requires:       php(language) > 5.3
Requires:       php-iconv
Requires:       php-pcre
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}

%description
A set of classes to do different actions with the console, also called shell.
It can render a progress bar, tables and a status bar and contains a class for
parsing command line options.

Documentation is available in the %{name}-doc package.

%package doc
Summary:  Documentation for %{name}
Group:    Documentation
# For License
Requires: %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
%if %{with phpab}
: Generate a simple autoloader
%{_bindir}/phpab \
   --output src/autoloader.php \
   src
cat <<EOF | tee -a  src/autoloader.php
# Dependencies
require_once '%{ezcdir}/Base/autoloader.php';
EOF
%else
cp %{SOURCE1} src/autoloader.php
%endif

%install
mkdir -p %{buildroot}%{ezcdir}/autoload

: The library
cp -pr src \
       %{buildroot}%{ezcdir}/%{gh_project}
: For ezcBase autoloader
cp -pr src/*_autoload.php \
       %{buildroot}%{ezcdir}/autoload

%check
%if %{with tests}
: Create test autoloader
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require '%{ezcdir}/UnitTest/autoloader.php';
require '%{buildroot}%{ezcdir}/%{gh_project}/autoloader.php';
EOF

: Drop assertion which rely on path in sources dir
sed -e '/realpath/d' -i tests/statusbar_test.php

: Run test test suite
for cmd in php php81 php82 php83 php84
do
  if which $cmd;
  then
    $cmd %{_bindir}/phpunit9 --exclude-group interactive
  fi
done
%else
: Test suite disabled
%endif

%files
%license LICENSE* CREDITS
%doc ChangeLog
%doc composer.json
%{ezcdir}/autoload/*
%{ezcdir}/%{gh_project}

%files doc
%doc docs design

%changelog
%autochangelog
