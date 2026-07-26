%global source0_hash 79bfc933f45345d79adc791e5ffda8f961ee7106b88e553d57b7b49f596b0323

#
# Fedora spec file for php-psr-link
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-fig
%global github_name      link
%global github_version   1.1.1
%global github_commit    846c25f58a1f02b93a00f2404e3626b6bf9b7807

%global composer_vendor  psr
%global composer_project link

# "php": ">=8.0.0"
%global php_min_ver 8.0.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       12%{?github_release}%{?dist}
Summary:       Common interfaces for HTTP links (PSR-13)

License:       MIT
URL:           http://www.php-fig.org/psr/psr-13/
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Minimal autoloader test
BuildRequires: php-cli >= %{php_min_ver}
## Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package holds all interfaces/classes/traits related to PSR-13 [1].

Note that this is not an HTTP link implementation of its own. It is merely an
interface that describes an HTTP link. See the specification for more details.

Autoloader: %{phpdir}/Psr/Link/autoload.php

[1] https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-13-links.md

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Psr\\Link\\', __DIR__);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/Psr
cp -rp src %{buildroot}%{phpdir}/Psr/Link

%check
: Minimal autoloader test
%{_bindir}/php -r '
    require "%{buildroot}%{phpdir}/Psr/Link/autoload.php";
    exit(interface_exists("Psr\\Link\\LinkInterface") ? 0 : 1);
'

%files
%license LICENSE.md
%doc README.md
%doc composer.json
%dir %{phpdir}/Psr
     %{phpdir}/Psr/Link

%changelog
%autochangelog
