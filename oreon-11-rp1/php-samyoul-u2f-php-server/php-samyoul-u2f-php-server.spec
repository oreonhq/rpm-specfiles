%global source0_hash 1e76537f051ec96fa850947a1cb4e1da0bad2e40da49ac0d21c7edfcfed42846
%global with_tests   0%{!?_without_tests:1}
%global gh_commit    0625202c79d570e58525ed6c4ae38500ea3f0883
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     Samyoul
%global gh_project   U2F-php-server
%global pk_vendor    samyoul
%global pk_project   u2f-php-server
%global ns_vendor    Samyoul
%global ns_project   U2F
%global ns_library   U2FServer
Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.1.4
Release:        1%{?dist}
Summary:        Server side handling class for FIDO U2F registration and authentication
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php-openssl
Requires:       php-hash
Requires:       php-json
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php-cli
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-hash
BuildRequires:  php-json
BuildRequires:  php-openssl
BuildRequires:  php-spl
# /oreon:deps
%description
Server-side handling of FIDO U2F registration and authentication for PHP.

Securing your online accounts and doing your bit to protect your data is
extremely important and increasingly more so as hackers get more sophisticated.
FIDO's U2F enables you to add a simple unobtrusive method of 2nd factor
authentication, allowing users of your service and/or application to link
a hardware key to their account.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

mv LICENCE.md LICENCE

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\%{ns_library}\\', __DIR__);
AUTOLOAD

%build

: Nothing to build
%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}
%oreon_autofiles main

%check

%if %{with_tests}
php -r '
  require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_library}/autoload.php";
  exit (%{ns_vendor}\%{ns_project}\%{ns_library}\U2FServer::checkOpenSSLVersion() ? 0 : 1);
'
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
