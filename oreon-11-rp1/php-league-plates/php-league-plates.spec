%global source0_hash 2999e06cff21f20e3472c60ad6662152a2ce03ff4c7147e2676a720e2bb2ca1a

# remirepo/fedora spec file for php-league-plates
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    12ee65166adbc6fb5916fb80b0c0758e49a2d996
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   plates
# Packagist
%global pk_vendor    league
%global pk_name      plates
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Plates

Name:           php-%{pk_vendor}-%{pk_name}
Version:        3.6.0
Release:        4%{?dist}
Summary:        Native PHP template system

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.0
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "mikey179/vfsstream": "^1.6",
#        "phpunit/phpunit": "^11.4",
#        "squizlabs/php_codesniffer": "^3.5"
BuildRequires:  php-composer(mikey179/vfsStream) >= 1.6
# phpunit11 not yet available
BuildRequires:  phpunit10
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^8.0"
Requires:       php(language) >= 8.0
# From phpcompatinfo report for 3.1.1
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
Plates is a native PHP template system that's fast, easy to use and easy
to extend. It's inspired by the excellent Twig template engine and strives
to bring modern template language functionality to native PHP templates.
Plates is designed for developers who prefer to use native PHP templates
over compiled template languages, such as Twig or Smarty.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate classmap autoloader
phpab --template fedora --output src/autoload.php src

%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';

// Dependency
require_once '%{_datadir}/php/org/bovigo/vfs/autoload.php';
EOF

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit10 || ret=1
  fi
done
exit $ret

%files
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}

%changelog
%autochangelog
