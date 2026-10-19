%global source0_hash d07e6a7370d6b4b689e644c265f93739e15482dee9685f9eb65daa7d3c684ccc
%bcond_without       tests
%global gh_commit    a5c75038693ad2e8d4b6c15ba2403532647830c4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   environment
%global gh_date      2025-05-21
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        7
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Environment
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.2.1
Release:        1%{?dist}
Summary:        Handle HHVM/PHP environments, version 7
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.2
Requires:       php-pcre
Requires:       php-posix
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-posix
BuildRequires:  phpunit11
# /oreon:deps
%description
This component provides functionality that helps writing PHP code that
has runtime-specific (PHP / HHVM) execution paths.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

mkdir vendor
touch vendor/autoload.php
: Run tests
ret=0
for cmd in php php82 php83 php84; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     -d pcov.enabled=1 \
     %{_bindir}/phpunit11 || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
