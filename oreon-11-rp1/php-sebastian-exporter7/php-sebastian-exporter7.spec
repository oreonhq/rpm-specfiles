%global source0_hash c8dba05e13dcbf1a9ff9a8b24892b78a498286623bacbb7314b7812b477cadc8
%bcond_without       tests
%global gh_commit    016951ae10980765e4e7aee491eb288c64e505b7
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   exporter
%global gh_date      2025-09-24
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Exporter
%global major        7
%global php_home     %{_datadir}/php
%global pear_name    Exporter
%global pear_channel pear.phpunit.de
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.0.2
Release:        2%{?dist}
Summary:        Export PHP variables for visualization, version 7
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.3
Requires:       php-mbstring
Requires:       (php-composer(%{pk_vendor}/recursion-context) >= 7.0 with php-composer(%{pk_vendor}/recursion-context) < 8)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/recursion-context) >= 7.0 with php-composer(sebastian/recursion-context) < 8)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-mbstring
BuildRequires:  phpunit12
# /oreon:deps
%description
Provides the functionality to export PHP variables for visualization.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
cat <<EOF | tee -a src/autoload.php
// Dependency' autoloader
require_once '%{php_home}/%{ns_vendor}/RecursionContext7/autoload.php';
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

mkdir vendor
phpab --template fedora --output vendor/autoload.php tests/_fixture/
: Run upstream test suite
ret=0
for cmd in php php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit12 --bootstrap vendor/autoload.php || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
