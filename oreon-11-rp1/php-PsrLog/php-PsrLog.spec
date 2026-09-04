%global source0_hash 0ef9bb7e9b9f84dc92a27e150a63b0f9c828a117c2fc36490649f262b7dda977

#
# Fedora spec file for php-PsrLog
#
# Copyright (c) 2013-2021 Shawn Iwinski <shawn.iwinski@gmail.com>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve the changelog entries
#

%global github_owner     php-fig
%global github_name      log
%global github_version   1.1.4
%global github_commit    d49695b909c3b7628b6289db5479a1c204601f11

%global composer_vendor  psr
%global composer_project log

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:      php-PsrLog
Version:   %{github_version}
Release:   12%{?dist}
Summary:   Common interface for logging libraries

License:   MIT
URL:       https://www.php-fig.org/psr/psr-3/
Source0:   https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch: noarch
# For tests
BuildRequires:  php-cli
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

Requires:  php(language) >= 5.3.0
# phpcompatinfo requires (computed from version 1.1.0)
Requires:  php-date
Requires:  php-pcre
Requires:  php-spl
# Autoloader
Requires:  php-composer(fedora/autoloader)

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:  php-%{composer_vendor}-%{composer_project}           = %{version}-%{release}
# Composer
Provides:  php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
This package holds all interfaces/classes/traits related to PSR-3 [1].

Note that this is not a logger of its own. It is merely an interface that
describes a logger. See the specification for more details.

[1] https://www.php-fig.org/psr/psr-3/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee Psr/Log/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 *
 * @return \Symfony\Component\ClassLoader\ClassLoader
 */

if (!class_exists('Fedora\\Autoloader\\Autoload', false)) {
    require_once '%{phpdir}/Fedora/Autoloader/autoload.php';
}

\Fedora\Autoloader\Autoload::addPsr4('Psr\\Log\\', __DIR__);
AUTOLOAD

%build
# Empty build section, nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/php
cp -rp Psr %{buildroot}%{_datadir}/php/

%check
: Check if our autoloader works
php -r '
require "%{buildroot}%{_datadir}/php/Psr/Log/autoload.php";
$a = new Psr\Log\NullLogger();
echo "Ok\n";
exit(0);
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md
%doc composer.json
%dir %{_datadir}/php/Psr
     %{_datadir}/php/Psr/Log

%changelog
%autochangelog
