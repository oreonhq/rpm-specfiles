%global source0_hash fee1db3c09b6b2dec908d98445a229f0e9c782da70716a04fb7f3f334616e4b1

# remirepo/fedora spec file for php-sabre-event5
#
# Copyright (c) 2013-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without      tests

# Github
%global gh_commit    86d57e305c272898ba3c28e9bd3d65d5464587c2
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   event
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   Event
# For RPM
%global major        5

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Lightweight library for event-based programming
Version:        5.1.7
Release:        4%{?dist}

URL:            http://sabre.io/event
License:        BSD-3-Clause
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.1
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "friendsofphp/php-cs-fixer": "~2.17.1",
#        "phpstan/phpstan": "^0.12||^3.63",
#        "phpunit/phpunit" : "^7.5 || ^8.5 || ^9.6"
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.1 || ^8.0"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 5.0.2
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
This library provides the following event-based concepts:

* EventEmitter.
* Promises.
* An event loop.
* Co-routines.

Full documentation can be found on http://sabre.io/event/

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

cat << 'EOF' | tee lib/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Sabre\\Event\\', __DIR__);

if (!function_exists('Sabre\\Event\\coroutine')) {
    require_once __DIR__ . '/coroutine.php';
    require_once __DIR__ . '/Loop/functions.php';
    require_once __DIR__ . '/Promise/functions.php';
}
EOF

%build
# nothing to build

%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

%check
: Check version
php -r '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
echo  Sabre\Event\Version::VERSION . "\n";
exit (Sabre\Event\Version::VERSION === "%{version}" ? 0 : 1);
'

%if %{with tests}
: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --bootstrap=%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      --configuration tests/phpunit.xml \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif

%files
%license LICENSE
%doc *md
%doc composer.json
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
