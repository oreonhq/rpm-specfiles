%global source0_hash 0b90807294c977b68798e4ecd2bed881b98544d238ec44af6c5c924b3a8e0745
%global gh_commit    dbefd12671e8a14ec7f180cab83036ed26714bb0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   event-dispatcher
%global pk_vendor    psr
%global pk_project   %{gh_project}
%global ns_vendor    Psr
%global ns_project   EventDispatcher
Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.0.0
Release:        1%{?dist}
Summary:        Standard interfaces for event handling
License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz
BuildArch: noarch
Requires:  php(language) >= 7.2
Requires:  php-composer(fedora/autoloader)
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
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
%oreon_autofiles main

%check

: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\EventDispatcherInterface") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
