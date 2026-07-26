%global source0_hash da7e65a1a4b695b778eaae6d75c27d8e14a86379028faedde2c2707d73297fee

#
# Fedora spec file for php-patchwork-jsqueeze
#
# Copyright (c) 2016-2021 Adam Williamson <awilliam@redhat.com>
#                         Shawn Iwinski <shawn@iwin.ski>
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#

%global github_owner     tchwork
%global github_name      jsqueeze
%global github_version   2.0.5
%global github_commit    693d64850eab2ce6a7c8f7cf547e1ab46e69d542

%global composer_vendor  patchwork
%global composer_project jsqueeze

# "php": ">=5.3.0"
%global php_min_ver 5.3.0

%if 0%{?fedora}
%bcond_without tests
%else
%bcond_with    tests
%endif

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:           php-%{composer_vendor}-%{composer_project}
Version:        %{github_version}
Release:        23%{?dist}
Summary:        Efficient JavaScript minification

# Automatically converted from old format: ASL 2.0 or GPLv2 - review is highly recommended.
License:        Apache-2.0 OR GPL-2.0-only
URL:            https://github.com/%{github_owner}/%{github_name}

# GitHub export does not include tests.
# Run php-patchwork-jsqueeze-get-source.sh to create full source.
Source0:       %{name}-%{github_version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh

BuildArch:      noarch
# Autoloader
BuildRequires: %{_bindir}/phpab
# Tests
%if %{with tests}
## composer.json
BuildRequires: php(language) >= %{php_min_ver}
BuildRequires: phpunit9
## phpcompatinfo (computed from version 2.0.5)
BuildRequires: php-pcre
%endif

Requires:       php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 2.0.5)
Requires:       php-pcre

Provides:       php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
JSqueeze shrinks / compresses / minifies / mangles Javascript code.

It's a single PHP class that is developed, maintained and thoroughly
tested since 2003 on major JavaScript frameworks (e.g. jQuery).

JSqueeze operates on any parse error free JavaScript code, even when
semi-colons are missing.

In term of compression ratio, it compares to YUI Compressor and
UglifyJS.

Autoloader: %{phpdir}/Patchwork/autoload-jsqueeze.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
: Generate autoloader
%{_bindir}/phpab --output src/autoload-jsqueeze.php src/
cat src/autoload-jsqueeze.php

%install
mkdir -p %{buildroot}%{phpdir}/Patchwork
cp -pr src/* %{buildroot}%{phpdir}/Patchwork/

%check
%if %{with tests}
: Create tests autoloader
cat << 'EOF' | tee tests/bootstrap.php
<?php
require "%{buildroot}%{phpdir}/Patchwork/autoload-jsqueeze.php";
class_alias("PHPUnit\\Framework\\TestCase", "PHPUnit_Framework_TestCase");
EOF

: Run upstream test suite
ret=0
for cmd in php php74 php80 php81
do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%else
: Tests skipped
%endif

%files
%license LICENSE.*
%doc *.md
%doc composer.json
%dir %{phpdir}/Patchwork
     %{phpdir}/Patchwork/autoload-jsqueeze.php
     %{phpdir}/Patchwork/JSqueeze.php

%changelog
%autochangelog
