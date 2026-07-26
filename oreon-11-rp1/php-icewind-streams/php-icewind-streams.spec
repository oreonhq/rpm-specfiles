%global source0_hash 2866d333dd4eabb5055409cfaa9806c9bc27651ef82921ff971040692697b559

# remirepo/fedora spec file for php-icewind-streams
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
# Github information
%global gh_commit    cb2bd3ed41b516efb97e06e8da35a12ef58ba48b
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     icewind1991
%global gh_project   Streams
# Packagist information
%global pk_vendor    icewind
%global pk_name      streams
# Namespace information
%global ns_vendor    Icewind
%global ns_name      Streams

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.7.8
Release:        4%{?dist}
Summary:        A set of generic stream wrappers

# See SPDX-License-Identifier in src tree
License:        MIT AND AGPL-3.0-or-later
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{url}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz

BuildArch:      noarch
# For tests
# because of PHPUnit 9
BuildRequires:  php(language) >= 7.3
# From composer.json, "require-dev": {
#               "phpunit/phpunit": "^9",
#               "friendsofphp/php-cs-fixer": "^2",
#               "phpstan/phpstan": "^0.12"
BuildRequires:  phpunit9
BuildRequires:  php-composer(theseer/autoload)
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#      "php": ">=7.1"
Requires:       php(language) >= 7.1
# From phpcompatinfo report for version 0.7.2
Requires:       php-hash
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
Generic stream wrappers for php.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
: Generate classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src

%install
# Restore PSR-0 tree
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}

%check
cd tests
: Generate a simple autoloader for test suite
%{_bindir}/phpab --output bootstrap.php .
echo "require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_name}/autoload.php';" >> bootstrap.php

: Run the test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret

%files
%license LICENSE.txt
%license LICENSES/*txt
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_name}

%changelog
%autochangelog
