%global source0_hash 1d3cc34a0eef32612b8c6580730b72b5ea927f070ad0aec5bed50fd0c63e75c2

# remirepo/fedora spec file for php-symfony-contracts2
#
# Copyright (c) 2019-2022 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    d3da2932c17d3cc0d6cd167518cc63ab7b909f38
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     symfony
%global gh_project   contracts
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    Symfony
%global ns_project   Contracts
%global php_home     %{_datadir}/php

%global major        2

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.5.2
Release:        10%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        A set of abstractions extracted out of the Symfony, version %{major}

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{?gh_short}.tar.gz

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.2.5
BuildRequires:  php-reflection
BuildRequires:  php-intl
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-zlib
# From composer.json, "require-dev": {
#        "symfony/polyfill-intl-idn": "^1.10"
BuildRequires: (php-composer(psr/cache)            >= 1.0  with php-composer(psr/cache)            < 4)
BuildRequires: (php-composer(psr/container)        >= 1.1  with php-composer(psr/container)        < 2)
BuildRequires: (php-composer(psr/event-dispatcher) >= 1.0  with php-composer(psr/event-dispatcher) < 2)
%if 0%{?fedora} >= 31 || 0%{?rhel} >=9
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
BuildRequires: %{phpunit}
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": ">=7.2.5"
#        "psr/cache": "^1.0|^2.0|^3.0",
#        "psr/container": "^1.1",
#        "psr/event-dispatcher": "^1.0"
Requires:       php(language) >= 7.2.5
# From composer.json, "suggest": {
#        "symfony/cache-implementation": "",
#        "symfony/event-dispatcher-implementation": "",
#        "symfony/http-client-implementation": "",
#        "symfony/service-implementation": "",
#        "symfony/translation-implementation": ""
Requires:      (php-composer(psr/cache)            >= 1.0  with php-composer(psr/cache)            < 4)
Requires:      (php-composer(psr/container)        >= 1.1  with php-composer(psr/container)        < 2)
Requires:      (php-composer(psr/event-dispatcher) >= 1.0  with php-composer(psr/event-dispatcher) < 2)
# From phpcompatinfo report for version 2.3.1
Requires:       php-reflection
Requires:       php-intl
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-zlib
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project})              = %{version}
Provides:       php-composer(%{pk_vendor}/cache-contracts)            = %{version}
Provides:       php-composer(%{pk_vendor}/event-dispatcher-contracts) = %{version}
Provides:       php-composer(%{pk_vendor}/http-client-contracts)      = %{version}
Provides:       php-composer(%{pk_vendor}/service-contracts)          = %{version}
Provides:       php-composer(%{pk_vendor}/translation-contracts)      = %{version}
Provides:       php-composer(%{pk_vendor}/deprecation-contracts)      = %{version}

%description
A set of abstractions extracted out of the Symfony components.

Can be used to build on semantics that the Symfony components
proved useful - and that already have battle tested implementations.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

# sub CHANGELOG and README only refer to main file
rm */*.md

for i in */composer.json */LICENSE
do
  mv $i $(dirname $i)_$(basename $i)
done

%build
: Create autoloader
cat <<'AUTOLOAD' | tee autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{php_home}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required([
    [
        '%{php_home}/Psr/Cache3/autoload.php',
        '%{php_home}/Psr/Cache2/autoload.php',
        '%{php_home}/Psr/Cache/autoload.php',
    ],
    '%{php_home}/Psr/Container/autoload.php',
    '%{php_home}/Psr/EventDispatcher/autoload.php',
    __DIR__ . '/Deprecation/function.php',
]);
AUTOLOAD

%install
mkdir -p    %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
for i in autoload.php Cache EventDispatcher HttpClient Service Translation Deprecation
do
  rm -f $i/.gitignore
  cp -pr $i %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/$i
done

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Tests\\Fixtures\\', dirname(__DIR__)."/Tests/Fixtures/");
EOF

ret=0
for cmdarg in "php %{phpunit}" php74 php80 php81; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} \
      --no-coverage \
      --verbose
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license *LICENSE
%doc *composer.json
%doc *.md
%dir %{php_home}/%{ns_vendor}/
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}

%changelog
%autochangelog
