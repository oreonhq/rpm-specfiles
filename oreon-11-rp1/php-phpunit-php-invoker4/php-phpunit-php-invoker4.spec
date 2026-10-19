%global source0_hash 95db05a88a93243f174df5d202a0d6544b44d250988647c94ce252de1ed7600a
%bcond_without       tests
%global gh_commit    f5e568ba02fa5ba0ddd0f618391d5a9ea50b06d7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global php_home     %{_datadir}/php
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
%global major        4
%global ns_vendor    SebastianBergmann
%global ns_project   Invoker
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Invoke callables with a timeout, version 4
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.1
Requires:       php-pcntl
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcntl
BuildRequires:  php-spl
BuildRequires:  phpunit10
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
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit10 || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
