%global source0_hash 58f7408661eb7932df2d5dc167dc7d4554c25987e320a319c63228e653f060dc
%global gh_commit    ad37a5552c8e2b88572249fdc19b6da7792e021b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   version
%global gh_date      2026-02-06
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Version
%global ver_major    7
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        7.0.0
Release:        1%{?dist}
Summary:        Managing the version number of Git-hosted PHP projects, version 7
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
Requires:       php(language) >= 8.4.1
Requires:       git
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
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
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}
%oreon_autofiles main

%check

: check autoloader
php -r '
require "%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{ver_major}/autoload.php";
exit (class_exists("%{ns_vendor}\\%{ns_project}") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
