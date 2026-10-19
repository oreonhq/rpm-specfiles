%global source0_hash 657d469551e55ee05abc9adb5ad3c547c3b9a5673d93a481926e01230de7ac00
%bcond_without       tests
%global gh_commit    54391c61e4af8078e5b276ab082b6d3c54c9ad64
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   code-unit
%global gh_date      2025-03-19
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   CodeUnit
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.3
Release:        1%{?dist}
Summary:        Collection of value objects that represent the PHP code units, version 3
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.2
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit11
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
require_once dirname(__DIR__) . '/tests/_fixture/issue_9.php';
EOF
: Run tests
ret=0
for cmd in php php82 php83 php84; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit11 --bootstrap vendor/autoload.php || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
