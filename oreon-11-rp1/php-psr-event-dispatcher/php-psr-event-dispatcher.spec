%global source0_hash 0b90807294c977b68798e4ecd2bed881b98544d238ec44af6c5c924b3a8e0745

# remirepo/fedora spec file for php-psr-event-dispatcher
#
# Copyright (c) 2019 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Github
%global gh_commit    dbefd12671e8a14ec7f180cab83036ed26714bb0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   event-dispatcher
# Packagist
%global pk_vendor    psr
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Psr
%global ns_project   EventDispatcher

Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.0.0
Release:   16%{?dist}
Summary:   Standard interfaces for event handling

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:   %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php(language) >= 7.2
BuildRequires: php-cli
BuildRequires: php-fedora-autoloader-devel

# From composer.json,    "require": {
#       "php": ">=7.2.0",
Requires:  php(language) >= 7.2
# phpcompatinfo (computed from version 1.0.0)
#     only core
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
This repository holds all interfaces related to PSR-14 (Event Dispatcher).

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-14/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\EventDispatcherInterface") ? 0 : 1);
'

%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
