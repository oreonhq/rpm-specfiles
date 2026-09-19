%global source0_hash dface0c0a6a8d3ce87881edd185c688d9bfdb33c0b6fc077f46cb4d638b91f69

# remirepo/fedora spec file for php-sebastian-exporter4
#
# SPDX-FileCopyrightText:  Copyright 2013-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    14c6ba52f95a36c3d27c835d65efc7123c446e8c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   exporter
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   Exporter
%global major        4
%global php_home     %{_datadir}/php
%global pear_name    Exporter
%global pear_channel pear.phpunit.de

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.0.8
Release:        2%{?dist}
Summary:        Export PHP variables for visualization, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3",
#        "ext-mbstring": "*"
BuildRequires:  phpunit9 >= 9.3
BuildRequires:  php-mbstring
BuildRequires:  (php-composer(%{pk_vendor}/recursion-context) >= 4.0 with php-composer(%{pk_vendor}/recursion-context) < 5)
%endif

# from composer.json
#        "php": ">=7.3",
#        "sebastian/recursion-context": "^4.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(%{pk_vendor}/recursion-context) >= 4.0 with php-composer(%{pk_vendor}/recursion-context) < 5)
# from phpcompatinfo report for version 4.0.0
Requires:       php-mbstring
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Provides the functionality to export PHP variables for visualization.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# generate the Autoloader
phpab --template fedora --output src/autoload.php src

cat <<EOF | tee -a src/autoload.php
// Dependency' autoloader
require_once '%{php_home}/%{ns_vendor}/RecursionContext4/autoload.php';
EOF

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%if %{with tests}
%check
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9  --verbose || ret=1
  fi
done
exit $ret
%endif

%files
%license LICENSE
%doc README.md
%doc composer.json
%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
