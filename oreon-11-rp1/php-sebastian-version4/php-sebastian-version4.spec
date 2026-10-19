%global source0_hash 32d6bb9d7c2f501312586778905889d88087b8a5040dedf33929a1c13f6f5ed5
%global gh_commit    c51fa83a5d8f43f1402e3f32a005e6262244ef17
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   version
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global ns_vendor    SebastianBergmann
%global ns_project   Version
%global ver_major    4
%global php_home     %{_datadir}/php
Name:           php-%{pk_vendor}-%{pk_project}%{ver_major}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Managing the version number of Git-hosted PHP projects, version 4
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
Requires:       php(language) >= 8.1
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
