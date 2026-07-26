%global source0_hash b47ac22c1c6f09d6d281700b53ed69e2c913d4678399dba381f0fa876bab6f1d

#
# Fedora spec file for php-psr-cache
#
# Copyright (c) 2016 Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     php-fig
%global github_name      cache
%global github_version   1.0.1
%global github_commit    d11b50ad223250cf17b86e38383413f5a6764bf8

%global composer_vendor  psr
%global composer_project cache

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-%{composer_vendor}-%{composer_project}
Version:   %{github_version}
Release:   22%{?github_release}%{?dist}
Summary:   PSR Cache: Common interface for caching libraries

License:   MIT
URL:       https://github.com/%{github_owner}/%{github_name}
Source0:   %{url}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires: php-cli
BuildRequires: php-composer(fedora/autoloader)

# composer.json
Requires:  php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 1.0.0)
#     <none>
# Autoloader
Requires:  php-composer(fedora/autoloader)

# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package holds all interfaces defined by PSR-6 [1].

Note that this is not a Cache implementation of its own. It is merely an
interface that describes a Cache implementation. See the specification for
more details.

Autoloader: %{phpdir}/Psr/Cache/autoload.php

[1] http://www.php-fig.org/psr/psr-6/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Psr\\Cache\\', __DIR__);

AUTOLOAD

%build
# Empty build section, nothing to build

%install
mkdir -p %{buildroot}%{phpdir}/Psr/Cache
cp -rp src/* %{buildroot}%{phpdir}/Psr/Cache/

%check
: Test autoloader
php -r '
require "%{buildroot}%{phpdir}/Psr/Cache/autoload.php";
exit (interface_exists("Psr\\Cache\\CacheItemInterface") ? 0 : 1);
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE.txt
%doc *.md
%doc composer.json
%dir %{phpdir}/Psr
     %{phpdir}/Psr/Cache

%changelog
%autochangelog
