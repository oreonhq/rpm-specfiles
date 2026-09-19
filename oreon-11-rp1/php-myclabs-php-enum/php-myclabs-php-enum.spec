%global source0_hash 7cda9cfc2e2849a22486d14dcbf5aa5354c480735112fb5a5b7b26fb760dac4c

# remirepo/fedora spec file for php-myclabs-php-enum
#
# SPDX-FileCopyrightText:  Copyright 2017-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_commit    e7be26966b7398204a234f8673fdad5ac6277802
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     myclabs
%global gh_project   php-enum

%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}

%global ns_vendor    MyCLabs
%global ns_project   Enum
%global php_home     %{_datadir}/php

%bcond_without       tests

Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.8.5
Release:        4%{?dist}
Summary:        PHP Enum implementation

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snashop to get upstream test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
# For tests
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
BuildRequires:  php-json
BuildRequires:  php-spl
# From composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.5",
#        "squizlabs/php_codesniffer": "1.*"
#        "vimeo/psalm": "^4.6.2 || ^5.2"
%global phpunit %{_bindir}/phpunit9
BuildRequires:  phpunit9 >= 9.5
# Required by autoloader
BuildRequires:  php-composer(fedora/autoloader)
%endif

# From composer.json, "require": {
#        "php": "^7.3 || ^8.0",
#        "ext-json": "*"
Requires:       php(language) >= 7.3
Requires:       php-json
# From phpcompatinfo report for version 1.6.1
Requires:       php-reflection
Requires:       php-spl
# Required by autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}

%description
PHP Enum implementation inspired from SplEnum.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

mv stubs/Stringable.php src/

cat << 'EOF' | tee src/autoload.php
<?php
/* Autoloader for %{name} and its dependencies */
require_once '/usr/share/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\', __DIR__);
require_once __DIR__ . '/Stringable.php';
EOF

%build
# Empty build section, most likely nothing required.

%install
: Library
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}

%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee tests/autoload.php
<?php
require '%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\Tests\\%{ns_project}\\', __DIR__ . '/../tests');
require __DIR__ . '/bootstrap.php';
EOF

ret=0
for cmd in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmd; then
    set $cmd
    $1 ${2:-%{_bindir}/phpunit9} --verbose --bootstrap tests/autoload.php || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE
%doc composer.json
%doc README.md
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}

%changelog
%autochangelog
