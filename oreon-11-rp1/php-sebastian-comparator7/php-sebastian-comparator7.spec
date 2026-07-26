%global source0_hash dcfd255fa9caf385940c87ad1a1e9949c1a68b90fa738dceb3cec90cadf21387

# remirepo/fedora spec file for php-sebastian-comparator7
#
# SPDX-FileCopyrightText:  Copyright 2014-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    6a7de5df2e094f9a80b40a522391a7e6022df5f6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   comparator
%global gh_date      2026-01-24
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global major        7
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Comparator

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        7.1.4
Release:        1%{?dist}
Summary:        Compare PHP values for equality, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.3
BuildRequires:  php-bcmath
BuildRequires:  php-dom
BuildRequires:  php-mbstring
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^12.2"
BuildRequires:  phpunit12 >= 12.2
BuildRequires:  (php-composer(%{pk_vendor}/diff)     >= 7.0   with php-composer(%{pk_vendor}/diff)     < 8)
BuildRequires:  (php-composer(%{pk_vendor}/exporter) >= 7.0   with php-composer(%{pk_vendor}/exporter) < 8)
%endif

# from composer.json
#        "php": ">=8.3",
#        "sebastian/diff": "^7.0",
#        "sebastian/exporter": "^7.0"
#        "ext-dom": "*",
#        "ext-mbstring": "*"
Requires:       php(language) >= 8.3
Requires:       php-dom
Requires:       php-mbstring
Requires:       (php-composer(%{pk_vendor}/diff)     >= 7.0   with php-composer(%{pk_vendor}/diff)     < 8)
Requires:       (php-composer(%{pk_vendor}/exporter) >= 7.0   with php-composer(%{pk_vendor}/exporter) < 8)
# from phpcompatinfo report for version 6.3.0
#   Only core, date, spl (bcmath is optional)
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
This component provides the functionality to compare PHP values for equality.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# Rely on include_path as in PHPUnit dependencies
cat <<EOF | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/Diff7/autoload.php',
    '%{php_home}/%{ns_vendor}/Exporter7/autoload.php',
]);
EOF

%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%check
%if %{with tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture

: Run upstream test suite
ret=0
for cmd in php php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit12 --bootstrap vendor/autoload.php --no-coverage || ret=1
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
