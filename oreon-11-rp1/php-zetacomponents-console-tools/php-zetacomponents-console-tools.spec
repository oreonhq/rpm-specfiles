%global source0_hash ca261e43b8e163f87c343d64087166a4c2c21ee410493f0e34db8ef5977619f0
%global gh_commit    de081f422b574d638e62e15661bf833d80fac61a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zetacomponents
%global gh_project   ConsoleTools
%global cname        console-tools
%global ezcdir       %{_datadir}/php/ezc
%bcond_with     tests
%bcond_without  phpab
Name:           php-%{gh_owner}-%{cname}
Version:        1.7.5
Release:        1%{?dist}
Summary:        Zeta ConsoleTools Component
License:        Apache-2.0
URL:            http://zetacomponents.org/
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Source1:        autoloader.php
BuildArch:      noarch
%if %{with phpab}
%endif
%if %{with tests}
%endif
Requires:      (php-composer(%{gh_owner}/base) >= 1.8   with php-composer(%{gh_owner}/base) < 2)
Requires:       php(language) > 5.3
Requires:       php-iconv
Requires:       php-pcre
Requires:       php-spl
Provides:       php-composer(%{gh_owner}/%{cname}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(zetacomponents/base) >= 1.8 with php-composer(zetacomponents/base) < 2)
BuildRequires:  //bin/phpab
BuildRequires:  php-composer(zetacomponents/unit-test)
BuildRequires:  phpunit9
# /oreon:deps
%description
A set of classes to do different actions with the console, also called shell.
It can render a progress bar, tables and a status bar and contains a class for
parsing command line options.

Documentation is available in the %{name}-doc package.

%package doc
Summary:  Documentation for %{name}
Group:    Documentation
Requires: %{name} = %{version}-%{release}
%description doc
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%if %{with phpab}
: Generate a simple autoloader
%{_bindir}/phpab \
   --output src/autoloader.php \
   src
cat <<EOF | tee -a  src/autoloader.php
require_once '%{ezcdir}/Base/autoloader.php';
EOF
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
: Create test autoloader
mkdir vendor
cat <<EOF | tee vendor/autoload.php
<?php
require '%{ezcdir}/UnitTest/autoloader.php';
require '%{buildroot}%{ezcdir}/%{gh_project}/autoloader.php';
EOF
: Drop assertion which rely on path in sources dir
sed -e '/realpath/d' -i tests/statusbar_test.php
: Run test test suite
for cmd in php php81 php82 php83 php84
do
  if which $cmd;
  then
    $cmd %{_bindir}/phpunit9 --exclude-group interactive
  fi
done
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list
%files -n php-zetacomponents-console-tools-doc -f %{oreon_filedir}/php-zetacomponents-console-tools-doc.list

%changelog

%autochangelog
