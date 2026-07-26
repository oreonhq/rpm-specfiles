%global source0_hash 21c638106a85daaee4b9562d8547ef8a6b98e0319fcc1ca8c17997ab5e7cb822

# remirepo/fedora spec file for php-league-flysystem
#
# Copyright (c) 2016-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    3239285c825c152bcc315fe0e87d6b55f5972ed1
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     thephpleague
%global gh_project   flysystem
# Packagist
%global pk_vendor    league
%global pk_name      flysystem
# PSR-0 namespace
%global ns_vendor    League
%global ns_project   Flysystem

Name:           php-%{pk_vendor}-%{pk_name}
Version:        1.1.10
Release:        9%{?dist}
Summary:        Filesystem abstraction: Many filesystems, one API

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-fileinfo
BuildRequires: (php-composer(league/mime-type-detection) >= 1.3   with php-composer(league/mime-type-detection) < 2)
BuildRequires:  php-date
BuildRequires:  php-ftp
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpspec/prophecy": "^1.11.1",
#        "phpunit/phpunit": "^8.5.8"
BuildRequires:  phpunit8 >= 8.5.8
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.2.5 || ^8.0",
#        "ext-fileinfo": "*",
#        "league/mime-type-detection": "^1.3"
Requires:       php(language) >= 7.2.5
Requires:       php-fileinfo
Requires:      (php-composer(league/mime-type-detection) >= 1.3   with php-composer(league/mime-type-detection) < 2)
# From phpcompatifo report for 1.1.3
Requires:       php-date
Requires:       php-ftp
Requires:       php-hash
Requires:       php-mbstring
Requires:       php-pcre
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
Flysystem is a filesystem abstraction which allows you to easily swap out
a local filesystem for a remote one.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Create classmap autoloader
phpab \
  --template fedora \
  --output src/autoload.php \
  src

cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/%{ns_vendor}/MimeTypeDetection/autoload.php',
]);

EOF

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

// Test suite
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Stub\\', dirname(__DIR__).'/stub');
EOF

ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
   : Run upstream test suite
   $cmd %{_bindir}/phpunit8 \
     --exclude-group integration \
     --filter '^((?!(testPathinfoHandlesUtf8|testStreamSizeForUrl)).)*$' \
     --no-coverage --verbose || ret=1
  fi
done
exit $ret

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc composer.json
%{_datadir}/php/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
