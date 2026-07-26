%global source0_hash f180c51d8056aabbe48022c1ec5b38978a26313a3093e1b3f296ee381d1892ba

# remirepo/fedora spec file for php-symfony-requirements-checker
#
# Copyright (c) 2020-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    cf8893f384348a338157d637e170fe8fb2356016
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     symfony
%global gh_project   requirements-checker
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Symfony
%global ns_project   Requirements
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}
Version:        2.0.1
Release:        11%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Check Symfony requirements and give recommendations

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

# Use our autoloader
Patch0:         %{name}-bin.patch

BuildArch:      noarch

BuildRequires:  php(language) >= 5.3.9
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-iconv
BuildRequires:  php-intl
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": ">=5.3.9"
Requires:       php(language) >= 5.3.9
# From phpcompatinfo report for version 2.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-date
Requires:       php-dom
Requires:       php-iconv
Requires:       php-intl
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project})   = %{version}

%description
Checks requirements for running Symfony and gives useful recommendations
to optimize PHP for Symfony.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm

%build
: Create autoloader
phpab --template fedora --output src/autoload.php src

%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}/
cp -pr src  %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

install -Dpm 755 bin/requirements-checker.php %{buildroot}%{_bindir}/%{name}

%check
: Check autoloader
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php";
exit(class_exists("Symfony\\Requirements\\Requirement") ? 0 : 1);
'

%files
%license LICENSE
%doc *composer.json
%doc *.rst
%{_bindir}/%{name}
%dir %{php_home}/%{ns_vendor}/
     %{php_home}/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
