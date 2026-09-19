%global source0_hash 5fbc15aba3dd10b2393827726063dc29f57abc5fc000b387e4549da5b37ccedd

# remirepo/fedora spec file for php-psr-http-factory
#
# SPDX-FileCopyrightText:  Copyright 2018-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    2b4765fddfe3b508ac62f829e852b1501d3f6e8a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-fig
%global gh_project   http-factory

%global pk_vendor    psr
%global pk_project   %{gh_project}

Name:      php-%{pk_vendor}-%{pk_project}
Version:   1.1.0
Release:   3%{?dist}
Summary:   Common interfaces for PSR-7 HTTP message factories

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
Source0:   %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php(language) >= 7.1
BuildRequires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 3)
BuildRequires: php-cli
BuildRequires: php-fedora-autoloader-devel

# From composer.json,    "require": {
#       "php": ">=7.1",
#       "psr/http-message": "^1.0 || ^2.0"
Requires:  php(language) >= 7.1
Requires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 3)
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{pk_vendor}/%{pk_project}) = %{version}

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

%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/Psr/Http/Message/%{pk_project}-autoload.php";
exit (interface_exists("Psr\\Http\\Message\\RequestFactoryInterface") ? 0 : 1);
'

%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/Psr/Http/Message/*php

%changelog
%autochangelog
