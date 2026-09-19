%global source0_hash 112162012f5dd9c62620d11ee16ba5ea79e256c1bf41608a5abd9e3bbbe5bb46

# remirepo/fedora spec file for php-sabre-uri2
#
# Copyright (c) 2016-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    b76524c22de90d80ca73143680a8e77b1266c291
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   uri
# Packagist
%global pk_vendor    sabre
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Sabre
%global ns_project   Uri
%global major        2

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Functions for making sense out of URIs
Version:        2.3.4
Release:        4%{?dist}

URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD-3-Clause
# Git snapshot with tests, because of .gitattributes
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.4
# From composer.json, "require-dev": {
#        "friendsofphp/php-cs-fixer": "^3.63",
#        "phpstan/phpstan": "^1.12",
#        "phpstan/phpstan-phpunit": "^1.4",
#        "phpstan/phpstan-strict-rules": "^1.6",
#        "phpstan/extension-installer": "^1.4",
#        "phpunit/phpunit" : "^9.6"
BuildRequires:  php-pcre
BuildRequires:  phpunit9 >= 9.6
%global phpunit %{_bindir}/phpunit9
%endif
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require" : {
#        "php": "^7.4 || ^8.0"
Requires:       php(language) > 7.4
# From phpcompatinfo report for version 2.1.2
Requires:       php-pcre
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
sabre/uri is a lightweight library that provides several functions for
working with URIs, staying true to the rules of RFC3986.

Partially inspired by Node.js URL library, and created to solve real
problems in PHP applications. 100% unitested and many tests are based
on examples from RFC3986.

The library provides the following functions:
* resolve to resolve relative urls.
* normalize to aid in comparing urls.
* parse, which works like PHP's parse_url.
* build to do the exact opposite of parse.
* split to easily get the 'dirname' and 'basename' of a URL without
  all the problems those two functions have.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Functions
if (!function_exists('Sabre\\Uri\\resolve')) {
    require_once __DIR__ . '/functions.php';
}
EOF

%build
# nothing to build

%install
# Install as a PSR-0 library
mkdir -p %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

%check
: Check version
php -r '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
echo  Sabre\Uri\Version::VERSION . "\n";
exit (Sabre\Uri\Version::VERSION === "%{version}" ? 0 : 1);
'

%if %{with tests}
: Run upstream test suite against installed library
mkdir vendor
ln -s %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php vendor/autoload.php

cd tests
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
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
