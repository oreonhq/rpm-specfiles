%global source0_hash f92302a60d3cc9a3686ab61eaca4eb510dc3d6ec1566d311ac74efd55ef61373
%global bootstrap    0
%global gh_commit    9ee24c724374ba355385e98808da8b4343b28f67
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-invoker
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Invoker
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
Name:           php-phpunit-php-invoker2
Version:        5.0.0
Release:        1%{?dist}
Summary:        Invoke callables with a timeout
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-pcntl
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(phpunit/php-invoker) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit8
# /oreon:deps
%description
phpunit/php-invoker provides the means to invoke a callable with a timeout.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

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
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}
%oreon_autofiles main
%if %{with_tests}
%check

: Generate tests autoloader
mkdir vendor
%{_bindir}/phpab --output vendor/autoload.php tests
: Run upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php \
      %{_bindir}/phpunit8 --verbose || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
