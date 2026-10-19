%global source0_hash c657652b7716072ed676cb698909cc89789b0af54d053496abc5601ed2c10325
%global bootstrap    0
%global gh_commit    72a7f7674d053d548003b16ff5a106e7e0e06eee
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   resource-operations
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   ResourceOperations
%global major        2
%global with_tests   0%{!?_without_tests:1}
Name:           php-sebastian-resource-operations%{major}
Version:        3.0.4
Release:        1%{?dist}
Summary:        Provides a list of PHP built-in functions that operate on resources, version 2
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(sebastian/resource-operations) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit8
# /oreon:deps
%description
%{summary}.

This package provides version %{major}.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with_tests}
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{_bindir}/phpunit8  --verbose tests || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
