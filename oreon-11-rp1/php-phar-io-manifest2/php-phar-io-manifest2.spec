%global source0_hash af59ce4e178945e4e360ce52a7dae053dca63e5c1986229490e7ae09bbac0197

# remirepo/fedora spec file for php-phar-io-manifest2
#
# Copyright (c) 2017-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%bcond_with          bootstrap
%if %{with bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif

%global gh_commit    54750ef60c58e43759730615a392c31c80e23176
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   manifest
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Manifest
%global major        2
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.4
Release:        5%{?dist}
Summary:        Component for reading phar.io manifest information

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-dom
BuildRequires:  php-phar
BuildRequires: (php-composer(%{pk_vendor}/version) >= 3.0.1 with php-composer(%{pk_vendor}/version) <  4)
BuildRequires:  php-filter
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
BuildRequires:  %{phpunit}
%endif

# from composer.json
#    "php": "^7.2 || ^8.0",
#    "ext-dom": "*",
#    "ext-phar": "*",
#    "ext-libxml": "*",
#    "ext-xmlwriter": "*",
#    "phar-io/version": "^3.0.1"
Requires:       php(language) >= 7.2
Requires:       php-dom
Requires:       php-phar
Requires:       php-libxml
Requires:       php-xmlwriter
Requires:      (php-composer(%{pk_vendor}/version) >= 3.0.1 with php-composer(%{pk_vendor}/version) <  4)
# from phpcompatinfo report for version 2.0.0
Requires:       php-filter
Requires:       php-pcre
Requires:       php-spl
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
%{_bindir}/phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{ns_vendor}/Version3/autoload.php',
]);
EOF

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in "php %{phpunit}" php81 php82 php83; do
  if which $cmd; then
    set $cmd
    $1 -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      ${2:-%{_bindir}/phpunit9} \
        --verbose || ret=1
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
