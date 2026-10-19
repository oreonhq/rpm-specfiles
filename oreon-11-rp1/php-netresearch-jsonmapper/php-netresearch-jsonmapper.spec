%global source0_hash cac5426cbff60dc1a4cde6d525039be5091c09be81489db4b383a7696484c8b6
%bcond_without       tests
%global gh_commit    980674efdda65913492d29a8fd51c82270dd37bb
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     cweiske
%global gh_project   jsonmapper
%global pk_vendor    netresearch
%global pk_project   jsonmapper
%global php_home     %{_datadir}/php
%global major        5
Name:           php-%{pk_vendor}-%{pk_project}
Version:        6.0.0
Release:        1%{?dist}
Summary:        Map nested JSON structures onto PHP classes, version 5
License:        OSL-3.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit10
%endif
Requires:       php(language) >= 7.1
Requires:       php-spl
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  phpunit10
# /oreon:deps
%description
Takes data retrieved from a JSON web service and converts them into nested
object and arrays - using your own model classes.

Starting from a base object, it maps JSON data on class properties, converting
them into the correct simple types or objects.

It's a bit like the native SOAP parameter mapping PHP's SoapClient gives you,
but for JSON. It does not rely on any schema, only your PHP class definitions.

Type detection works by parsing @var docblock annotations of class properties,
as well as type hints in setter methods.

You do not have to modify your model classes by adding JSON specific code;
it works automatically by parsing already-existing docblocks.

Autoloader: %{php_home}/%{pk_vendor}/%{pk_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{pk_vendor}
cp -pr src %{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
phpab --template fedora --output vendor/autoload.php tests
cat << 'EOF' | tee -a vendor/autoload.php
require_once "%{buildroot}%{php_home}/%{pk_vendor}/%{pk_project}%{major}/autoload.php";
EOF
: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" php82 php83 php84 php85; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit10} \
      --no-coverage \
      . || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
