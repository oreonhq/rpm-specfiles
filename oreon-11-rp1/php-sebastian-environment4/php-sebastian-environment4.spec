%global source0_hash ad34d526dafd7552fb5e3f4d9d27da6714447558a9287fde6b7a0ce812707dc1
%global bootstrap    0
%global gh_commit    56932f6049a0482853056ffd617c91ffcc754205
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   environment
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        4
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Environment
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.2.5
Release:        5%{?dist}
Summary:        Handle HHVM/PHP environments, version 4
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-pcre
Requires:       php-posix
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-posix
BuildRequires:  phpunit8
# /oreon:deps
%description
This component provides functionality that helps writing PHP code that
has runtime-specific (PHP / HHVM) execution paths.

This package provides the version %{major} of the library.

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
%if %{with_tests}
%check

mkdir vendor
touch vendor/autoload.php
: Run tests
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit8 \
       --filter '^((?!(testCanCollectCodeCoverageWhenPcovExtensionIsEnabled|testPCOVCanBeDetected)).)*$' \
       --verbose || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
