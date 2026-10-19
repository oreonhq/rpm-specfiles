%global source0_hash 9a8c4fcd2350c4138f8fadc9a04882096dd145329692b2bdb98ffb8935006f6b
%global gh_commit    513e0666f7216c7459170d56df27dfcefe1689ea
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   container
%global pk_vendor    psr
%global pk_project   container
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:      php-%{pk_vendor}-%{pk_project}
Version:   2.0.2
Release:        1%{?dist}
Summary:        Common Container Interface
License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz
BuildArch: noarch
Requires:  php(language) >= 7.2.0
Requires:  php-composer(fedora/autoloader)
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-composer(fedora/autoloader)
# /oreon:deps
%description
This package holds all interfaces/classes/traits related to PSR-11.

Note that this is not a container implementation of its own. 

Autoloader: %{_datadir}/php/Psr/Container/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{pk_vendor}/%{pk_project} and its dependencies */

require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Psr\\Container\\', __DIR__);
AUTOLOAD

%build

%install
mkdir -p   %{buildroot}%{_datadir}/php/Psr
cp -rp src %{buildroot}%{_datadir}/php/Psr/Container
%oreon_autofiles main

%check

: Test autoloader
php -r '
require "%{buildroot}%{_datadir}/php/Psr/Container/autoload.php";
exit (interface_exists("Psr\\Container\\ContainerInterface") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
