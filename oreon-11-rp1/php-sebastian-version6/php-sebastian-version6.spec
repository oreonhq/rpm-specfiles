%global source0_hash 8167e642bc8bab82b801d644f8fb5fe54c5992d3453fe2eecef90d3f3e17ee9d

# remirepo/fedora spec file for php-sebastian-version6
#
# SPDX-FileCopyrightText:  Copyright 2013-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    3e6ccf7657d4f0a59200564b08cead899313b53c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   version
%global gh_date      2025-02-07
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace (fake ns_project as not PSR-4 compliant)
%global ns_vendor    SebastianBergmann
%global ns_project   Version
%global ver_major    6
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        6.0.0
Release:        3%{?dist}
Summary:        Managing the version number of Git-hosted PHP projects, version %{ver_major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.3
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=8.3"
Requires:       php(language) >= 8.3
Requires:       git
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Library that helps with managing the version number
of Git-hosted PHP projects.

This package provides version %{ver_major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate the Autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
# Not PSR-4 compliant, but ok as we use a classmap
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%check
: check autoloader
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php";
exit (class_exists("%{ns_vendor}\\%{ns_project}") ? 0 : 1);
'

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}

%changelog
%autochangelog
