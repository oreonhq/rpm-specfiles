%global source0_hash 71ca88bb5ff94d0dc94a3a20572d35ad8e972ff78391ab726ab4c8dd1b4d25dc
%global bootstrap    0
%global gh_commit    64cfeaa341951ceb2019d7b98232399d57bb2296
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   exporter
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Exporter
%global major        3
%global php_home     %{_datadir}/php
%global pear_name    Exporter
%global pear_channel pear.phpunit.de
%global with_tests   %{?_without_tests:0}%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.1.8
Release:        1%{?dist}
Summary:        Export PHP variables for visualization, version 3
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.2
Requires:       (php-composer(%{pk_vendor}/recursion-context) >= 3.0 with php-composer(%{pk_vendor}/recursion-context) < 4)
Requires:       php-mbstring
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/recursion-context) >= 3.0 with php-composer(sebastian/recursion-context) < 4)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-mbstring
BuildRequires:  phpunit8
# /oreon:deps
%description
Provides the functionality to export PHP variables for visualization.

This package provides the version %{major} of the library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
cat <<EOF | tee -a src/autoload.php
// Dependency' autoloader
require_once '%{php_home}/%{ns_vendor}/RecursionContext3/autoload.php';
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with_tests}
%check

mkdir vendor
touch vendor/autoload.php
: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    %{_bindir}/php -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{_bindir}/phpunit8	  --verbose || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
