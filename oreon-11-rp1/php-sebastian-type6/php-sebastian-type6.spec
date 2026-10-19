%global source0_hash 49591814abb27ee077d2a8ee968ed5157f2dd38665fdb36bf4defb95cd36af55
%bcond_without       tests
%global gh_commit    e549163b9760b8f71f191651d22acf32d56d6d4d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   type
%global gh_date      2025-08-09
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        6
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Type
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        6.0.3
Release:        1%{?dist}
Summary:        Collection of value objects that represent the types of the PHP type system, v6
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.3
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit12
# /oreon:deps
%description
Collection of value objects that represent the types of the PHP type system.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
phpab --template fedora --output tests/autoload.php tests/_fixture/
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require_once 'tests/autoload.php';
require_once 'tests/_fixture/callback_function.php';
require_once 'tests/_fixture/functions_that_declare_return_types.php';
EOF
: Run upstream test suite
ret=0
for cmd in php php83 php84 php85; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit12 --bootstrap vendor/autoload.php --no-coverage || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
