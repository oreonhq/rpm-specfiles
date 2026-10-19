%global source0_hash 88538198029a9daca5fc83dd0ca8adfd1429377bcee8bf78e6e41ec53677a116
%global bootstrap    0
%global gh_commit    92a1a52e86d34cde6caa54f1b5ffa9fda18e5d54
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   code-unit-reverse-lookup
%global php_home     %{_datadir}/php/SebastianBergmann
%global ns_name      CodeUnitReverseLookup
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
Name:           php-sebastian-%{gh_project}
Version:        4.0.1
Release:        1%{?dist}
Summary:        Looks up which function or method a line of code belongs to, version 1
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 5.6
Requires:       php-reflection
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(sebastian/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit8
# /oreon:deps
%description
Looks up which function or method a line of code belongs to.

This package provides the version 1 of the library.

Autoloader: %{php_home}/%{ns_name}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
%install
mkdir -p   %{buildroot}%{php_home}
cp -pr src %{buildroot}%{php_home}/%{ns_name}
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
touch vendor/autoload.php
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_name}/autoload.php \
     %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
