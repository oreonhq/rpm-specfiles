%global source0_hash c3fd612190617cfcc6a59aae77c0b3a602ba9e67fa451d42b35c315163b97faf

# remirepo/fedora spec file for php-sebastian-comparator4
#
# SPDX-FileCopyrightText:  Copyright 2014-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global bootstrap    0
%global gh_commit    e4df00b9b3571187db2831ae9aada2c6efbd715d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   comparator
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global major        4
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Comparator
%if %{bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.0.10
Release:        1%{?dist}
Summary:        Compare PHP values for equality, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  (php-composer(%{pk_vendor}/diff)     >= 4.0   with php-composer(%{pk_vendor}/diff)     < 5)
BuildRequires:  (php-composer(%{pk_vendor}/exporter) >= 4.0   with php-composer(%{pk_vendor}/exporter) < 5)
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json
#        "php": ">=7.3",
#        "sebastian/diff": "^4.0",
#        "sebastian/exporter": "^4.0"
Requires:       php(language) >= 7.3
Requires:       (php-composer(%{pk_vendor}/diff)     >= 4.0   with php-composer(%{pk_vendor}/diff)     <  5)
Requires:       (php-composer(%{pk_vendor}/exporter) >= 4.0   with php-composer(%{pk_vendor}/exporter) <  5)
# from phpcompatinfo report for version 4.0.0
Requires:       php-dom
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
    '%{php_home}/%{ns_vendor}/Diff4/autoload.php',
    '%{php_home}/%{ns_vendor}/Exporter4/autoload.php',
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
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9 --no-coverage --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif

%files
%doc README.md composer.json
%license LICENSE
%{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
