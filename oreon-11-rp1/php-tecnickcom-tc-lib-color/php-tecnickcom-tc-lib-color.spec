%global source0_hash 69532e02cf817179871993ac35bb0c6a4fd3760f674ce61478ff0dff9040bbd2
%global gh_commit    6331d57bd847d883652012a5c3594aa03aea4c50
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global c_vendor     tecnickcom
%global gh_owner     tecnickcom
%global gh_project   tc-lib-color
%global php_project  %{_datadir}/php/Com/Tecnick/Color
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{gh_owner}-%{gh_project}
Version:        3.0.5
Release:        1%{?dist}
Summary:        PHP library to manipulate various color representations
License:        LGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{c_vendor}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%global phpunit %{_bindir}/phpunit10
%endif
Requires:       php(language) >= 8.1
Requires:       php-pcre
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{c_vendor}/%{gh_project}) = %{version}
Provides:       php-%{gh_project} = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  phpunit10
# /oreon:deps
%description
Provides tc-lib-color: PHP library to manipulate various color
representations (GRAY, RGB, HSL, CMYK) and parse Web colors.

The initial source code has been extracted from TCPDF (http://www.tcpdf.org).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

: Sanity check
grep -q '^%{version}$' VERSION

: Fix the examples
sed -e 's:^require:////require:' \
    -e 's:^//require:require:'   \
    -i example/*php

%build

phpab --template fedora --output src/autoload.php src
%install
mkdir -p   $(dirname %{buildroot}%{php_project})
cp -pr src %{buildroot}%{php_project}
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{php_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Test\\', dirname(__DIR__) . '/test');
EOF
ret=0
for cmdarg in php php82 php83 php84 php85; do
   if which $cmdarg; then
      set $cmdarg
      cp phpunit.xml.dist phpunit.xml
      $1 ${2:-%{phpunit}} --migrate-configuration || :
      $1 ${2:-%{phpunit}} --no-coverage \
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
