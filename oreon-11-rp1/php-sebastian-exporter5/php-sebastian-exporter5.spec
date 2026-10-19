%global source0_hash cb8b02e7232707ab8b567254924cda5c0c6cd37d4ce7f6bdbc51cf3006da1f7b
%bcond_without       tests
%global gh_commit    0735b90f4da94969541dac1da743446e276defa6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   exporter
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Exporter
%global major        5
%global php_home     %{_datadir}/php
%global pear_name    Exporter
%global pear_channel pear.phpunit.de
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.1.4
Release:        1%{?dist}
Summary:        Export PHP variables for visualization, version 5
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.1
Requires:       php-mbstring
Requires:       (php-composer(%{pk_vendor}/recursion-context) >= 5.0 with php-composer(%{pk_vendor}/recursion-context) < 6)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sebastian/recursion-context) >= 5.0 with php-composer(sebastian/recursion-context) < 6)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-mbstring
BuildRequires:  phpunit10
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
require_once '%{php_home}/%{ns_vendor}/RecursionContext5/autoload.php';
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
for cmd in php php81 php82 php83 php84 php85; do
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
