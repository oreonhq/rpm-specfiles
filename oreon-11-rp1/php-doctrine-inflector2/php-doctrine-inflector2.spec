%global source0_hash b161b22de99dffa2f6c8fa1609957a73d2d51930b755223fd6a451c6e4290cd5
%global github_owner     doctrine
%global github_name      inflector
%global github_version   2.1.0
%global major            2
%global github_commit    f9301a5b2fb1216b2b08f02ba04dc45423db6bff
%global composer_vendor  doctrine
%global composer_project inflector
%global php_min_ver 7.2
%global with_tests 0%{!?_without_tests:1}
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}%{major}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Common string manipulations with regard to casing and singular/plural rules
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh
BuildArch:     noarch
%if %{with_tests}
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
Doctrine Inflector is a small library that can perform string manipulations
with regard to upper-/lowercase and singular/plural forms of words.

Autoloader: %{phpdir}/Doctrine/Inflector%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build

: Create autoloader
phpab --template fedora --output lib/Doctrine/Inflector/autoload.php lib
%install
mkdir -p %{buildroot}%{phpdir}/Doctrine
cp -rp lib/Doctrine/Inflector %{buildroot}%{phpdir}/Doctrine/Inflector%{major}
%oreon_autofiles main

%check

%if %{with_tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Inflector%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr0('Doctrine\\Tests', __DIR__.'/tests');
BOOTSTRAP
: Upstream tests
RETURN_CODE=0
for PHP_EXEC in "" php80 php81 php82 php83; do
    if [ -z "$PHP_EXEC" ] || which $PHP_EXEC; then
        phpunit9 --verbose --bootstrap bootstrap.php \
            || RETURN_CODE=1
    fi
done
exit $RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
