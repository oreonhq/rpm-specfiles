%global source0_hash 0530a6f6808f49d132aa409f24ef72d66abef9e87ff5a8a9753b1661865faa5f
%bcond_without       tests
%global gh_commit    d8334211a140ce329c13726d4a715adbddd0a163
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     staabm
%global gh_project   side-effects-detector
%global php_home     %{_datadir}/php
%global ns_owner     staabm
%global ns_project   SideEffectsDetector
Name:           php-%{gh_owner}-%{gh_project}
Version:        1.0.5
Release:        1%{?dist}
Summary:        A static analysis tool to detect side effects in PHP code
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.4
Requires:       php-tokenizer
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-tokenizer
BuildRequires:  phpunit9
# /oreon:deps
%description
Analyzes php-code for side-effects.

When code has no side-effects it can e.g. be used with eval($code)
in the same process without interfering.

Side-effects are classified into categories to filter them more easily
depending on your use-case.

This library is used e.g. in PHPUnit to improve performance of PHPT test-cases.

Autoloader: %{php_home}/%{ns_owner}/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate autoloader
phpab --template fedora --output lib/autoload.php lib
%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_owner}
cp -pr lib %{buildroot}%{php_home}/%{ns_owner}/%{ns_project}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{ns_owner}/%{ns_project}/autoload.php';
EOF
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --no-coverage || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
