%global source0_hash 2e362ea488adf3a2c499ff41620172482c5453338bbcbd77b4c00867f93f33fa

#
# Fedora spec file for php-cache-integration-tests
#
# Copyright (c) 2017-2021 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-cache
%global github_name      integration-tests
%global github_version   0.17.0
%global github_commit    eda2e6b8bc5abcd623c8047e2345cda38dd6479e

%global composer_vendor  cache
%global composer_project integration-tests

# "php": "^5.4|^7",
%global php_min_ver 5.4
# "psr/cache": "~1.0"
%global psr_cache_min_ver 1.0
%global psr_cache_max_ver 2.0
# "cache/tag-interop": "^1.0"
%global cache_tag_interop_min_ver 1.0
%global cache_tag_interop_max_ver 2.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:       13%{?github_release}%{?dist}
Summary:       Integration tests for PSR-6 and PSR-16 cache implementations

License:       MIT
URL:           http://www.php-cache.com
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
# Minimal autoloader test
BuildRequires: php-cli
BuildRequires: phpunit9
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires:(php-composer(cache/tag-interop) >= %{cache_tag_interop_min_ver} with php-composer(cache/tag-interop) <  %{cache_tag_interop_max_ver})
BuildRequires:(php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) <  %{psr_cache_max_ver})
## Autoloader
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(cache/tag-interop) >= %{cache_tag_interop_min_ver} with php-composer(cache/tag-interop) <  %{cache_tag_interop_max_ver})
Requires:     (php-composer(psr/cache) >= %{psr_cache_min_ver} with php-composer(psr/cache) <  %{psr_cache_max_ver})
# phpcompatinfo (computed from version 0.17.0)
Requires:      php-date
# Autoloader
Requires:      php-composer(fedora/autoloader)

# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package contains integration tests to make sure your implementation of a
PSR-6 and/or PSR-16 cache follows the rules by PHP-FIG. It is a part of the PHP
Cache organization.

Autoloader: %{phpdir}/Cache/IntegrationTests/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Remove unnecessary exec bits
chmod a-x composer.json LICENSE

%build
: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('Cache\\IntegrationTests\\', __DIR__);

\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Cache/TagInterop/autoload.php',
    '%{phpdir}/Psr/Cache/autoload.php',
]);
AUTOLOAD

%install
mkdir -p %{buildroot}%{phpdir}/Cache
cp -rp src %{buildroot}%{phpdir}/Cache/IntegrationTests

%check
: Minimal autoloader test
php -r '
    require_once "%{phpdir}/PHPUnit9/autoload.php";
    require_once "%{buildroot}%{phpdir}/Cache/IntegrationTests/autoload.php";
    exit(class_exists("Cache\\IntegrationTests\\CachePoolTest") ? 0 : 1);
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{phpdir}/Cache/IntegrationTests

%changelog
%autochangelog
