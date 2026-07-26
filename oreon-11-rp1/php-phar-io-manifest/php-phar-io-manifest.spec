%global source0_hash 51df91e1733a6659bcd02e33005e462d0dd8eea3397369be7469b76b78748c64

# remirepo/fedora spec file for php-phar-io-manifest
#
# Copyright (c) 2017-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    7761fcacf03b4d4f16e7ccb606d4879ca431fcf4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   manifest
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Manifest
%global major        %nil
%global php_home     %{_datadir}/php
%if %{bootstrap}
%global with_tests   0%{?_with_tests:1}
%else
%global with_tests   0%{!?_without_tests:1}
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.3
Release:        18%{?dist}
Summary:        Component for reading phar.io manifest information

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# PHP 7.2 for phpunit8, 7.3 for phpunit9
BuildRequires:  php(language) >= 5.6
BuildRequires:  php-dom
BuildRequires:  php-phar
BuildRequires: (php-composer(%{pk_vendor}/version) >= 1.0.1 with php-composer(%{pk_vendor}/version) <  3)
BuildRequires:  php-filter
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with_tests}
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9
%else
%global phpunit %{_bindir}/phpunit8
BuildRequires:  phpunit8
%endif
%endif

# from composer.json
#    "php": "^5.6 || ^7.0",
#    "ext-dom": "*",
#    "ext-phar": "*",
# ignore exact version, test suite passes with 1.0.1
#    "phar-io/version": "2.0.0"
Requires:       php(language) >= 5.6
Requires:       php-dom
Requires:       php-phar
Requires:      (php-composer(%{pk_vendor}/version) >= 1.0.1 with php-composer(%{pk_vendor}/version) <  3)
# from phpcompatinfo report for version 1.0.1
Requires:       php-filter
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlwriter
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Component for reading phar.io manifest information from a PHP Archive (PHAR).

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
%{_bindir}/phpab --template fedora2 --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{ns_vendor}/Version/autoload.php',
]);
EOF

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with_tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php vendor/autoload.php

: Fix for modern phpunit
find tests/ -name \*php -exec sed -e 's/setUp()/setUp():void/'  -i {} \;

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{phpunit} --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%license LICENSE
%doc README.md composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
