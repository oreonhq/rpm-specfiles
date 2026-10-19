%global source0_hash 6518416b757ecaee884ca05bf8e44d2a419e9bf2874a3743cfb22231b87dad38
%bcond_without       tests
%global gh_commit    7b8842c2d8e85d0c3a5831236bf5869af6ab2a11
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   environment
%global gh_date      2026-03-15
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        8
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Environment
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        8.0.4
Release:        1%{?dist}
Summary:        Handle HHVM/PHP environments, version 8
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.3
Requires:       php-posix
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-posix
BuildRequires:  phpunit12
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
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php vendor/autoload.php
: Run tests
ret=0
for cmd in php php83 php84 php85; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     -d pcov.enabled=1 \
     %{_bindir}/phpunit12 || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
