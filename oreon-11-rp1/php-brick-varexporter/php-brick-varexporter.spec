%global source0_hash 35ed9f433575b47462a30110231e26f5eeb66c1431f2748a7e2640c1fe76b99a

# remirepo/fedora spec file for php-brick-varexporter
#
# SPDX-FileCopyrightText:  Copyright 2020-2026 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
# Github
%global gh_commit    b3a50b8f630a9ed5015ea3e1f00479af261ed80d
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     brick
%global gh_project   varexporter
# Packagist
%global pk_vendor    %{gh_owner}
%global pk_name      %{gh_project}
# Namespace
%global ns_vendor    Brick
%global ns_project   VarExporter

Name:           php-%{pk_vendor}-%{pk_name}
Version:        0.7.0
Release:        2%{?dist}
Summary:        A powerful alternative to var_export

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
# Create git snapshot as tests are excluded from official tarball
Source1:        makesrc.sh

BuildArch:      noarch

BuildRequires:  php(language) >= 8.2
BuildRequires: (php-composer(nikic/php-parser) >= 5.0   with php-composer(nikic/php-parser) < 6)
# From composer.json, "require-dev": {
#    "phpunit/phpunit": "^11.0",
#    "php-coveralls/php-coveralls": "^2.2",
#    "vimeo/psalm": "6.14.3"
BuildRequires:  phpunit11
%global phpunit %{_bindir}/phpunit11
# Autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#    "php": "^8.2",
#    "nikic/php-parser": "^5.0"
Requires:       php(language) >= 8.2
Requires:      (php-composer(nikic/php-parser) >= 5.0   with php-composer(nikic/php-parser) < 6)
# From phpcompatifo report for 0.3.2
# Only reflection pcre spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_name}) = %{version}

%description
This library aims to provide a prettier, safer, and powerful alternative
to var_export(). The output is valid and standalone PHP code, that does
not depend on the brick/varexporter library.

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
    '/usr/share/php/PhpParser5/autoload.php',
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
\Fedora\Autoloader\Autoload::addPsr4('Brick\\VarExporter\\Tests\\', dirname(__DIR__) . '/tests');
EOF

: Run upstream test suite
ret=0
for cmdarg in "php %{phpunit}" php82 php83 php84 php85; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit11} \
      --no-coverage || ret=1
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
