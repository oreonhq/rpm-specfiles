%global source0_hash 2709160a3eeabd8e9e5884fa90072af2235899eb25c4d725a727243333b3489f
%bcond_with          tests
%global gh_commit    a0e12065831f6ab0d83120dc61513eb8d9a966f6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-timer
%global gh_date      2026-02-06
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Timer
%global major        9
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        9.0.0
Release:        1%{?dist}
Summary:        PHP Utility class for timing, version 9
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.4
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit13
# /oreon:deps
%description
Utility class for timing things, factored out of PHPUnit into a stand-alone
component.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab \
   --template fedora \
   --output  src/autoload.php \
   src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

mkdir vendor
touch vendor/autoload.php
: Run upstream test suite
ret=0
for cmd in php php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit13 || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
