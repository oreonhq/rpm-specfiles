%global source0_hash 1e5a697b4da09933d5d63c379161910f562d8fb35d1239c4cacfac1281c84b4b

# remirepo/fedora spec file for php-williamdes-mariadb-mysql-kbs
#
# Copyright (c) 2019-2024 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Github
%global gh_commit    07106dab252127c329cc206cd79cf2f51f989e5e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     williamdes
%global gh_project   mariadb-mysql-kbs
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Williamdes
%global ns_project   MariaDBMySQLKBS
%global major        %nil

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.3.0
Release:        5%{?gh_date?%{gh_date}git%{gh_short}}%{?dist}
Summary:        An index of the MariaDB and MySQL Knowledge bases

License:        MPL-2.0
URL:            https://github.com/%{gh_owner}/%{gh_project}
# pull from github to retrieve full data
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.2
BuildRequires:  php-json
BuildRequires:  php-pcre
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": "^8 || ^9 || ^10 || ^11"",
#        "phpstan/phpstan": "^1.2",
#        "wdes/coding-standard": "^3.2.1",
#        "swaggest/json-schema": "^0.12.29"
BuildRequires:  phpunit10
%global phpunit %{_bindir}/phpunit10
BuildRequires: (php-composer(swaggest/json-schema)    >= 0.12.29 with php-composer(swaggest/json-schema)    < 1)
# For autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.2 || ^8.0"
Requires:       php(language) >= 7.2
# From phpcompatinfo report for 1.2.7
Requires:       php-json
Requires:       php-pcre
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
An index of the MariaDB and MySQL Knowledge bases.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm
find src -name \*.rpm -delete

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
AUTOLOAD

%build
: Generate merged data
%{_bindir}/php -d auto_prepend_file=src/autoload.php src/merge.php

%install
: Library
mkdir -p       %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src     %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}

: Data
mkdir -p       %{buildroot}%{_datadir}/%{name}
# only dist is used at runtime
cp -pr dist    %{buildroot}%{_datadir}/%{name}/dist
cp -pr data    %{buildroot}%{_datadir}/%{name}/data
cp -pr schemas %{buildroot}%{_datadir}/%{name}/schemas

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Test\\', dirname(__DIR__).'/test');
require '%{_datadir}/php/Swaggest/JsonSchema/autoload.php';
EOF

export RPM_BUILDROOT=%{buildroot}

ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit10} --no-coverage || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc *.md
%dir     %{_datadir}/php/%{ns_vendor}/
         %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/merge.php
%exclude %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/rust
%dir     %{_datadir}/%{name}/
         %{_datadir}/%{name}/dist
%doc     %{_datadir}/%{name}/data
%doc     %{_datadir}/%{name}/schemas

%changelog
%autochangelog
