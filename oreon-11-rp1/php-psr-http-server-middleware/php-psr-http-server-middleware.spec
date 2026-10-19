%global source0_hash e4187db1020e5baeb9bcffd790e485f65a3fbe9707b69ad4a979f497655e942a
%global gh_commit    c1481f747daaa6a0782775cd6a8c26a1bf4a3829
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-server-middleware
%global pk_vendor    psr
%global pk_project   %{gh_project}
%global ns_vendor    Psr
%global ns_project   Http
%global ns_sub       Server
Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.0.2
Release:        8%{?dist}
Summary:        Common interface for HTTP server-side middleware
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_commit}.tar.gz
BuildArch:      noarch
Requires:       php(language) >= 7.0
Requires:      (php-composer(%{pk_vendor}/http-message)        >= 1.0  with php-composer(%{pk_vendor}/http-message)        < 3)
Requires:      (php-composer(%{pk_vendor}/http-server-handler) >= 1.0  with php-composer(%{pk_vendor}/http-server-handler) < 2)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 3)
BuildRequires:  (php-composer(psr/http-server-handler) >= 1.0 with php-composer(psr/http-server-handler) < 2)
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
This repository holds the MiddlewareInterface related to PSR-15
(HTTP Server Request Handlers).

Note that this is not a Middleware implementation of its own.
It is merely the interface that describe a Middleware.

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-15/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/middleware-autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

%build

: Generate autoloader
%{_bindir}/phpab --template fedora --output src/middleware-autoload.php src
cat << 'EOF' | tee -a src/middleware-autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Psr/Http/Message2/autoload.php',
        '%{_datadir}/php/Psr/Http/Message/autoload.php',
    ],
    '%{_datadir}/php/Psr/Http/Server/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}
%oreon_autofiles main

%check

: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_sub}/middleware-autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\%{ns_sub}\\MiddlewareInterface") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
