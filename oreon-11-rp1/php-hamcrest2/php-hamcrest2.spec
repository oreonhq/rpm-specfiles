%global source0_hash 6af4eef690e95665ed72e26d45d192434232b142c4a811302bced64501e6ad5a

# remirepo/fedora spec file for php-hamcrest2
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#
%global gh_date      2025-04-30
%global gh_commit    f8b1c0173b22fa6ec77a81fe63e5b01eba7e6487
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     hamcrest
%global gh_project   hamcrest-php
%global ns_project   Hamcrest
%global major        2
%bcond_without       tests

Name:           php-hamcrest2
Version:        2.1.1
Release:        3%{?dist}
Summary:        PHP port of Hamcrest Matchers

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# git snapshot with tests
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

# Use generated autoloader instead of composer one
Patch0:         bootstrap-autoload.patch

BuildArch:      noarch
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json, require-dev:
#               "phpunit/php-file-iterator": "^1.4 || ^2.0 || ^3.0",
#               "phpunit/phpunit": "^4.8.36 || ^5.7 || ^6.5 || ^7.0 || ^8.0 || ^9.0"
BuildRequires:  phpunit9
BuildRequires:  php(language) >= 7.4
# From phpcompatinfo report for 2.1.1
BuildRequires:  php-ctype
BuildRequires:  php-dom
%endif

# composer.json, require:
#      "php": "^7.4|^8.0"
Requires:       php(language) >= 7.4
# From phpcompatinfo report for 2.1.1
Requires:       php-ctype
Requires:       php-dom
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(hamcrest/hamcrest-php) = %{version}

%description
Hamcrest is a matching library originally written for Java,
but subsequently ported to many other languages.

%{name} is the official PHP port of Hamcrest and essentially follows
a literal translation of the original Java API for Hamcrest,
with a few Exceptions, mostly down to PHP language barriers.

Autoloader: %{_datadir}/php/%{ns_project}%{major}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0 -b .rpm
find . -name \*.rpm -exec rm {} \; -print

# Move to Library tree
mv hamcrest/%{ns_project}.php hamcrest/%{ns_project}/%{ns_project}.php

%build
# Library autoloader
%{_bindir}/phpab \
    --template fedora \
    --output hamcrest/%{ns_project}/autoload.php \
    hamcrest/%{ns_project}

# Test suite autoloader
%{_bindir}/phpab \
    --output tests/autoload.php \
    --exclude '*Test.php' \
    tests generator

%install
mkdir -p %{buildroot}%{_datadir}/php
cp -pr hamcrest/%{ns_project} %{buildroot}%{_datadir}/php/%{ns_project}%{major}

%check
%if %{with tests}
cd tests
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%license LICENSE.txt
%doc CHANGES.txt README.md
%doc composer.json
%{_datadir}/php/%{ns_project}%{major}

%changelog
%autochangelog
