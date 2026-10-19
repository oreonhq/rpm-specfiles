%global source0_hash 00f32153e3d7895a22bd3857b602005c6b97e29332451ec880a910086c152aa5
%bcond_with          tests
%global gh_commit    42e5c5cae0c65df12d1b1a3ab52bf3f50f244d88
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global gh_date      2026-02-06
%global php_home     %{_datadir}/php
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        7
%global ns_vendor    SebastianBergmann
%global ns_project   Invoker
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.0.0
Release:        1%{?dist}
Summary:        Invoke callables with a timeout, version 7
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.4
Requires:       php-pcntl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcntl
BuildRequires:  phpunit13
# /oreon:deps
%description
phpunit/php-invoker provides the means to invoke a callable with a timeout.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate autoloader
%{_bindir}/phpab \
   --template fedora \
   --output  src/autoload.php \
   src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests
: Run upstream test suite
ret=0
for cmd in php php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit13 --bootstrap vendor/autoload.php || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
