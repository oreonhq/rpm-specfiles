%global source0_hash d9acf402b718a7337a3fb534f7525cd59680e1a9361f7447226480e775363e42
%bcond_without       tests
%global gh_commit    a81fee9eef0b7a76af11d121767abc44c104e503
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   code-unit
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        2
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   CodeUnit
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Collection of value objects that represent the PHP code units, version 2
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.1
Requires:       php-reflection
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  phpunit10
# /oreon:deps
%description
Collection of value objects that represent the PHP code units.

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
%{_bindir}/phpab \
   --template fedora \
   --output tests/_fixture/autoload.php \
   tests/_fixture
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once dirname(__DIR__) . '/tests/_fixture/autoload.php';
require_once dirname(__DIR__) . '/tests/_fixture/file_with_multiple_code_units.php';
require_once dirname(__DIR__) . '/tests/_fixture/function.php';
EOF
: Run tests
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit10 --bootstrap vendor/autoload.php || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
