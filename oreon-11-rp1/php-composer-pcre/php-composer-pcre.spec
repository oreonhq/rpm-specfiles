%global source0_hash 12eeb43902b618f5be97073e7e617b837cc0d881b9411d175a06b66d2e8f57be
%bcond_without       tests
%global gh_commit    67a32d7d6f9f560b726ab25a061b38ff3a80c560
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     composer
%global gh_project   pcre
%global ns_vendor    Composer
%global ns_project   Pcre
%global php_home     %{_datadir}/php
%global major        %nil
Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        3.4.0
Release:        1%{?dist}
Summary:        PCRE wrapping library version 1
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global         phpunit /usr/bin/phpunit9
%endif
Requires:       php(language) >= 5.3.2
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  /usr/bin/phpunit9
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-spl
# /oreon:deps
%description
PCRE wrapping library that offers type-safe preg_* replacements.

This library gives you a way to ensure preg_* functions do not fail silently,
returning unexpected nulls that may not be handled.

It also makes it easier ot work with static analysis tools like PHPStan or
Psalm as it simplifies and reduces the possible return values from all the
preg_* functions which are quite packed with edge cases.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate classmap autoloader
phpab --template fedora --output src/autoload.php src
%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}/
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}', dirname(__DIR__).'/tests');
EOF
ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
    $cmd %{phpunit} \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
