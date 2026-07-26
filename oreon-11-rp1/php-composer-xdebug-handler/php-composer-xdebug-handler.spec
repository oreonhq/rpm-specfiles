%global source0_hash bf9b6ea47b4c2b2cc3507c696055215abbca48c06863b3d0f398745f07c25a90

# remirepo/fedora spec file for php-composer-xdebug-handler
#
# Copyright (c) 2018-2021 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global gh_commit    f27e06cd9675801df441b3656569b328e04aa37c
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
#global gh_date      20150717
%global gh_owner     composer
%global gh_project   xdebug-handler

%global ns_vendor    Composer
%global ns_project   XdebugHandler

%global php_home     %{_datadir}/php
%bcond_without       tests

Name:           php-%{gh_owner}-%{gh_project}
Version:        1.4.6
Release:        12%{?gh_date:.%{gh_date}git%{gh_short}}%{?dist}
Summary:        Restarts a process without Xdebug

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 5.3.2
BuildRequires:  php-reflection
BuildRequires:  php-ctype
BuildRequires:  php-pcre
BuildRequires:  php-posix
BuildRequires:  php-spl
# From composer.json,     "require-dev": {
#        "symfony/phpunit-bridge": "^4.2 || ^5",
#        "phpstan/phpstan": "^0.12.55"
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 2)
BuildRequires:  phpunit8
%global phpunit %{_bindir}/phpunit8
%else
BuildRequires:  php-PsrLog
BuildRequires:  php-phpunit-PHPUnit >= 4.8.35
%global phpunit %{_bindir}/phpunit
%endif
%endif
# Autoloader
BuildRequires:  php-composer(fedora/autoloader)

# From composer.json, "require": {
#        "php": "^5.3.2 || ^7.0 || ^8.0",
#        "psr/log": "^1.0"
Requires:       php(language) >= 5.3.2
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:      (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 2)
%else
Requires:       php-PsrLog
%endif
# From phpcompatinfo report for version 1.0.0
Requires:       php-reflection
Requires:       php-ctype
Requires:       php-pcre
Requires:       php-posix
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}

%description
Restart a CLI process without loading the xdebug extension.

Originally written as part of composer/composer, now extracted
and made available as a stand-alone library.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build
cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Psr/Log/autoload.php',
));
EOF

%install
: Library
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}

%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', dirname(__DIR__).'/tests');
EOF

%if %{with tests}
ret=0
for cmdarg in "php %{phpunit}" php73 php74 php80; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit8} --verbose|| ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc composer.json
%doc *.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
