%global source0_hash 5fbc15aba3dd10b2393827726063dc29f57abc5fc000b387e4549da5b37ccedd
%global gh_commit    2b4765fddfe3b508ac62f829e852b1501d3f6e8a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-factory
%global pk_vendor    psr
%global pk_project   %{gh_project}
Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.1.0
Release:        3%{?dist}
Summary:        Common interfaces for PSR-7 HTTP message factories
License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch: noarch
Requires:  php(language) >= 7.1
Requires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 3)
Requires:  php-composer(fedora/autoloader)
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/http-message) >= 1.0 with php-composer(psr/http-message) < 3)
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
This package holds all interfaces related to
PSR-17 (HTTP Message Factories). 

Please refer to the specification for a description:
https://www.php-fig.org/psr/psr-17/

Autoloader: %{_datadir}/php/Psr/Http/Message/%{pk_project}-autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

%build

: Generate autoloader
%{_bindir}/phpab --template fedora --output src/%{pk_project}-autoload.php src
cat << 'EOF' | tee -a src/%{pk_project}-autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Psr/Http/Message2/autoload.php',
        '%{_datadir}/php/Psr/Http/Message/autoload.php',
    ],
]);
EOF
%install
mkdir -p   %{buildroot}%{_datadir}/php/Psr/Http
cp -rp src %{buildroot}%{_datadir}/php/Psr/Http/Message
%oreon_autofiles main

%check

: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/Psr/Http/Message/%{pk_project}-autoload.php";
exit (interface_exists("Psr\\Http\\Message\\RequestFactoryInterface") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
