%global source0_hash c6888ba2767f675dfe9cd6e1a77466a7e3af54430abf9116174eb0c2ccb110f7

#
# Fedora spec file for php-cache-tag-interop
#
# Copyright (c) 2017 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-cache
%global github_name      tag-interop
%global github_version   2.0.0
%global github_commit    c7496dd81530f538af27b4f2713cde97bc292832

%global composer_vendor  cache
%global composer_project tag-interop

# "php": "^5.5 || ^7.0"
%global php_min_ver 5.5
# "psr/cache": "^1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       1%{?github_release}%{?dist}
Summary:       Framework interoperable interfaces for tags

License:       MIT
URL:           http://www.php-cache.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Minimal autoloader test
BuildRequires: php-cli
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: php-composer(psr/cache) >= %{psr_cache_min_ver}
BuildRequires: php-composer(psr/cache) <  %{psr_cache_max_ver}
## Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:      php-composer(psr/cache) >= %{psr_cache_min_ver}
Requires:      php-composer(psr/cache) <  %{psr_cache_max_ver}
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This repository holds two interfaces for tagging. These interfaces will make
their way into PHP Fig. Representatives from Symfony, PHP-cache and Drupal has
worked together to agree on these interfaces.

Autoloader: %{phpdir}/Cache/TagInterop/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Cache\\TagInterop\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Psr/Cache/autoload.php',
]);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/Cache/TagInterop
cp -rp *.php %{buildroot}%{phpdir}/Cache/TagInterop/

%check
: Minimal autoloader test
php -r '
    require_once "%{buildroot}%{phpdir}/Cache/TagInterop/autoload.php";
    exit(interface_exists("Cache\\TagInterop\\TaggableCacheItemInterface") ? 0 : 1);
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%dir %{phpdir}/Cache
     %{phpdir}/Cache/TagInterop

%changelog
%autochangelog
