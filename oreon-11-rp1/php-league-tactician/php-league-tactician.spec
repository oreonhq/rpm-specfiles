%global source0_hash 5c8aa4126c420afc96a974f492e14e396fc84a33c05955571b0f3e14781079fe

# remirepo/fedora spec file for php-league-tactician
#
# Copyright (c) 2019-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    e79f763170f3d5922ec29e85cffca0bac5cd8975
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   tactician
# Packagist
%global pk_vendor    league
%global pk_name      tactician
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Tactician

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.1.0
Release:        12%{?dist}
Summary:        A small, flexible command bus

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-date
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "mockery/mockery": "^1.3",
#        "phpunit/phpunit": "^7.5.20 || ^9.3.8",
#        "squizlabs/php_codesniffer": "^3.5.8"
BuildRequires: (php-composer(mockery/mockery) >= 1.3   with php-composer(mockery/mockery) < 2)
BuildRequires:  phpunit9 >= 9.3.8
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php":  ">=7.1"
Requires:       php(language) >= 7.1
# From phpcompatifo report for 1.0.3
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
A small, flexible command bus. Handy for building service layers.

Documentation: http://tactician.thephpleague.com/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate a simple autoloader
%{_bindir}/phpab -t fedora -o src/autoload.php src

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%check
: Generate a simple autoloader
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
// Installed library
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('League\\Tactician\\Tests\\', dirname(__DIR__).'/tests');
\Fedora\Autoloader\Dependencies::required([
    dirname(__DIR__).'/tests/Fixtures/Command/CommandWithoutNamespace.php',
    '%{_datadir}/php/Mockery1/autoload.php',
]);
EOF

: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
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
