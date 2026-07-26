%global source0_hash 8d368fbec27deb9ae5bdad66fad97ad9a6e7b5e930f2b7214451d36d14a03057

# remirepo/fedora spec file for php-zetacomponents-base
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global gh_commit    f91dd2f04280741de7125350a8c47b6673fc8537
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   Base
%global cname        base
%global ezcdir       %{_datadir}/php/ezc

%if 0%{?fedora}
%bcond_without  tests
%bcond_without  phpab
%else
%bcond_with     tests
%bcond_with     phpab
%endif

Name:           php-%{gh_owner}-%{cname}
Version:        1.9.5
Release:        2%{?dist}
Summary:        Zeta Base Component

Group:          Development/Libraries
License:        Apache-2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        autoloader.php

# Use old PEAR layout
Patch0:         %{name}-layout.patch

BuildArch:      noarch
%if %{with phpab}
BuildRequires:  %{_bindir}/phpab
%endif
%if %{with tests}
BuildRequires:  phpunit9
BuildRequires:  %{_bindir}/convert
BuildRequires:  php-composer(%{gh_owner}/unit-test) >= 1.2.3
BuildRequires:  php-posix
%endif

# From phpcompatinfo report for 1.9
Requires:       php(language) > 5.3
Requires:       php-pcre
Requires:       php-posix
Requires:       php-simplexml
Requires:       php-spl

Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}

%description
This is the base package of the Zeta components, offering the basic
support that all Components need. In the first version this will be the
autoload support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p0

%build
%if %{with phpab}
: Generate a simple autoloader
%{_bindir}/phpab \
   --output src/autoloader.php \
   src
%else
cp %{SOURCE1} src/autoloader.php
%endif

%install
mkdir -p %{buildroot}%{ezcdir}/autoload

: The library
cp -pr src \
       %{buildroot}%{ezcdir}/%{gh_project}
: For ezcBase autoloader
cp -pr src/*_autoload.php \
       %{buildroot}%{ezcdir}/autoload

%check
%if %{with tests}
: Ignore test relying on composer layout
rm tests/file_find_recursive_test.php

: Create test autoloader
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require '%{ezcdir}/UnitTest/autoloader.php';
require '$PWD/src/autoloader.php';
EOF

: Run test test suite
ret=0
for cmd in php php81 php82 php83 php84 php85; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE* CREDITS
%doc ChangeLog
%doc composer.json
%doc docs design
%dir %{ezcdir}
%dir %{ezcdir}/autoload
     %{ezcdir}/autoload/*_autoload.php
     %{ezcdir}/%{gh_project}

%changelog
%autochangelog
