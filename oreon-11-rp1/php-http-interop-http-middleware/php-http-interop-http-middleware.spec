%global source0_hash 5685a55e3789e67f993df5571c92d6a1b145b3a84fa3c1f21bdae58da3356559
%global gh_commit    b49e1f9f6c584e704317b563302e566b8ce11858
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     http-interop
%global gh_project   http-middleware
Name:           php-%{gh_owner}-%{gh_project}
Version:        0.5.0
Release:        15%{?dist}
Summary:        Common interface for HTTP middleware
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
%endif
Requires:       php(language) > 5.3
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Requires:      (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 2)
%else
Requires:       php-psr-http-message
%endif
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 2)
BuildRequires:  php-cli
BuildRequires:  php-composer(fedora/autoloader)
# /oreon:deps
%description
PSR-15 interfaces for HTTP middleware.

Autoloader: %{_datadir}/php/Interop/Http/Middleware/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

cat << 'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Interop\\Http\\Server\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Psr/Http/Message/autoload.php',
));
AUTOLOAD
%install
mkdir -p %{buildroot}%{_datadir}/php/Interop/Http
cp -pr src %{buildroot}%{_datadir}/php/Interop/Http/Middleware
%oreon_autofiles main

%check

php -r '
require "%{buildroot}%{_datadir}/php/Interop/Http/Middleware/autoload.php";
if (interface_exists("Interop\\Http\\Server\\MiddlewareInterface")) {
   echo "Autoload OK\n";
   exit (0);
} else {
   echo "Autoload fails\n";
   exit (1);
}'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
