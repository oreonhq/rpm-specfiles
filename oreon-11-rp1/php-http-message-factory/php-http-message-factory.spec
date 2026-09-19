%global source0_hash d50daab1f123259ce57bdfb40dea3f3092d32b7dab65a97c0cc7f2699c7f6f95

# remirepo/fedora spec file for php-http-message-factory
#
# Copyright (c) 2019-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# Github
%global gh_commit    4d8778e1c7d405cbb471574821c1ff5b68cc8f57
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-http
%global gh_project   message-factory
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Http
%global ns_project   Message

# skip duplicated php prefix
Name:      %{pk_vendor}-%{pk_project}
Version:   1.1.0
Release:   8%{?dist}
Summary:   Factory interfaces for PSR-7 HTTP Message

License:   MIT
URL:       https://github.com/%{gh_owner}/%{gh_project}
# git snapshot for skip .gitattributes
Source0:   %{name}-%{version}-%{gh_short}.tgz
Source1:   makesrc.sh

BuildArch: noarch
# For tests
BuildRequires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 3)
%else
BuildRequires:  php-psr-http-message
%endif
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel

# From composer.json,    "require": {
#        "php": ">=5.4",
#        "psr/http-message": "^1.0 || ^2.0"
Requires:  php(language) >= 5.4
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires: (php-composer(psr/http-message) >= 1.0   with php-composer(psr/http-message) < 3)
%else
Requires:  php-psr-http-message
%endif
# phpcompatinfo (computed from version 1.0.2)
#     only Core
# Autoloader
Requires:   php-composer(fedora/autoloader)

# Composer
Provides:   php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
Factory interfaces for PSR-7 HTTP Message.

Documentation: http://docs.php-http.org/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{gh_project}-%{gh_commit}

%build
: Generate autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Psr/Http/Message2/autoload.php',
        '%{_datadir}/php/Psr/Http/Message/autoload.php',
    ],
]);
EOF

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -rp src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%check
: Test autoloader
php -nr '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php";
exit (interface_exists("%{ns_vendor}\\%{ns_project}\\RequestFactory") ? 0 : 1);
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}

%changelog
%autochangelog
