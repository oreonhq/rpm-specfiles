%global source0_hash ffef75b6bf16afbff399ccdc9ea5684226614aa6fecbd9696216bb0669453d0f

# remirepo/fedora spec file for composer
#
# SPDX-FileCopyrightText:  Copyright 2015-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    72a8f8e653710e18d83e5dd531eb5a71fc3223e6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_branch    2.0-dev
%global gh_owner     composer
%global gh_project   composer
%global api_version  2.9.0
%global run_version  2.2.2

%global upstream_version 2.9.5
#global upstream_prever  RC1
#global upstream_lower   rc1

%global _phpunit       %{_bindir}/phpunit9
%global bashcompdir    %(pkg-config --variable=completionsdir bash-completion 2>/dev/null)
%global bashcomproot   %(dirname %{bashcompdir} 2>/dev/null)

Name:           composer
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:        1%{?dist}
Summary:        Dependency Manager for PHP

# SPDX: composer and all dependencies are MIT
License:        MIT
URL:            https://getcomposer.org/
Source0:        %{gh_project}-%{upstream_version}%{?upstream_prever}-%{gh_short}.tgz
# Profile scripts
Source1:        %{name}-bash-completion
Source3:        %{name}.sh
Source4:        %{name}.csh
# Create a git snapshot with dependencies
Source5:        makesrc.sh

# Use our autoloader, resources path, fix for tests
Patch0:         %{name}-rpm.patch
# Disable XDG support as only partially implemented
Patch1:         %{name}-noxdg.patch

BuildArch:      noarch
# platform set in makesrc.sh
BuildRequires:  php(language) >= 7.2.5
BuildRequires:  php-cli
BuildRequires:  php-json
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  composer-generators

# From composer.json, "require": {
#        "php": "^7.2.5 || ^8.0",
#        "ext-json": "*",
#        "composer/ca-bundle": "^1.5",
#        "composer/class-map-generator": "^1.4.0",
#        "composer/metadata-minifier": "^1.0",
#        "composer/semver": "^3.3",
#        "composer/spdx-licenses": "^1.5.7",
#        "composer/xdebug-handler": "^2.0.2 || ^3.0.3",
#        "justinrainbow/json-schema": "^6.5.1",
#        "psr/log": "^1.0 || ^2.0 || ^3.0",
#        "seld/jsonlint": "^1.4",
#        "seld/phar-utils": "^1.2",
#        "symfony/console": "^5.4.47 || ^6.4.25 || ^7.1.10 || ^8.0",
#        "symfony/filesystem": "^5.4.45 || ^6.4.24 || ^7.1.10 || ^8.0",
#        "symfony/finder": "^5.4.45 || ^6.4.24 || ^7.1.10 || ^8.0",
#        "symfony/process": "^5.4.47 || ^6.4.25 || ^7.1.10 || ^8.0",
#        "react/promise": "^3.3",
#        "composer/pcre": "^2.3 || ^3.3",
#        "symfony/polyfill-php73": "^1.24",
#        "symfony/polyfill-php80": "^1.24",
#        "symfony/polyfill-php81": "^1.24",
#        "seld/signal-handler": "^2.0"
Requires:       php(language)                           >= 7.2.5
Requires:       php-json
Requires:       php-cli
# System certificates
Requires:       /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem

# From composer.json, suggest
#        "ext-curl": "Provides HTTP support (will fallback to PHP streams if missing)",
#        "ext-openssl": "Enables access to repositories and packages over HTTPS",
#        "ext-zip": "Allows direct extraction of ZIP archives (unzip/7z binaries will be used instead if available)",
#        "ext-zlib": "Enables gzip for HTTP requests"
Requires:       php-curl
Requires:       php-openssl
Requires:       php-zip
Requires:       php-zlib
# From phpcompatinfo for version 2.2.5
Requires:       php-ctype
Requires:       php-date
Requires:       php-dom
Requires:       php-filter
Requires:       php-hash
Requires:       php-iconv
Requires:       php-intl
Requires:       php-libxml
Requires:       php-mbstring
Requires:       php-pcntl
Requires:       php-pcre
Requires:       php-phar
Requires:       php-posix
Requires:       php-reflection
Requires:       php-spl
Requires:       php-tokenizer
Requires:       php-xsl
Requires:       php-zlib

# Special internal for Plugin API
Provides:       php-composer(composer-plugin-api) = %{api_version}
Provides:       php-composer(composer-runtime-api) = %{run_version}

# PEAR is now deprecated
# composer is designed to replace it
Supplements:    php-pear

%description
Composer helps you declare, manage and install dependencies of PHP projects,
ensuring you have the right stack everywhere.

Documentation: https://getcomposer.org/doc/

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm
%patch -P1 -p1 -b .noxdg
find . \( -name \*.rpm -o -name \*noxdg \) -delete -print

rm vendor/composer/ca-bundle/res/cacert.pem

: fix reported version
sed -e '/BRANCH_ALIAS_VERSION/s/@package_branch_alias_version@//' \
    -i src/Composer/Composer.php

: check Plugin API version
php -r '
namespace Composer;
include "src/bootstrap.php";
if (version_compare(Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}")) {
  printf("Plugin API version is %s, expected %s\n", Plugin\PluginInterface::PLUGIN_API_VERSION, "%{api_version}");
  exit(1);
}
if (version_compare(Composer::RUNTIME_API_VERSION, "%{run_version}")) {
  printf("Runtime API version is %s, expected %s\n", Composer::RUNTIME_API_VERSION, "%{run_version}");
  exit(1);
}'

%build
: Nothing to build

%install
: Profile scripts
install -Dpm 644 %{SOURCE1} %{buildroot}%{bashcompdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 644 %{SOURCE3} %{SOURCE4} %{buildroot}%{_sysconfdir}/profile.d/

: Library autoloader for compatibility
mkdir -p     %{buildroot}%{_datadir}/php/Composer
ln -s ../../composer/vendor/autoload.php %{buildroot}%{_datadir}/php/Composer/autoload.php

: Sources
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr src res vendor LICENSE\
         %{buildroot}%{_datadir}/%{name}/

: Command
install -Dpm 755 bin/%{name} %{buildroot}%{_bindir}/%{name}

: Licenses
ln -sf ../../%{name}/LICENSE LICENSE
cd vendor
for lic in */*/LICENSE
do dir=$(dirname $lic)
   own=$(dirname $dir)
   prj=$(basename $dir)
   ln -sf ../../composer/vendor/$own/$prj/LICENSE ../$own-$prj-LICENSE
done

%check
: Check autoloader
php -r '
  include "%{buildroot}%{_datadir}/%{name}/src/bootstrap.php";
  exit (class_exists("Composer\\Composer") ? 0 : 1);
'
: Check compatibility autoloader
php -r '
  include "%{buildroot}%{_datadir}/php/Composer/autoload.php";
  exit (class_exists("Composer\\Composer") ? 0 : 2);
'

%files
%license *LICENSE
%doc *.md
%doc doc
%doc composer.json
%config(noreplace) %{_sysconfdir}/profile.d/%{name}.*
%{_bindir}/%{name}
%{_datadir}/php/Composer
%{_datadir}/%{name}
%{bashcomproot}

%changelog
%autochangelog
