%global source0_hash 4c1f6d25ff42ae70e8915662e32210a73c9516c879308fb1870af4e0b5b24d15
%bcond_without       tests
%global gh_commit    e1e4a170560925c26d424b6a03aed157e7dcc5c5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   lines-of-code
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        %nil
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   LinesOfCode
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.0
Release:        1%{?dist}
Summary:        Counting the lines of code in PHP source code, version 1
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.3
Requires:      (php-composer(nikic/php-parser)     >= 4.18  with php-composer(nikic/php-parser)     < 6)
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(nikic/php-parser) >= 4.18 with php-composer(nikic/php-parser) < 6)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
Library for counting the lines of code in PHP source code.

This package provides the version 1 of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
cat <<EOF | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{php_home}/PhpParser5/autoload.php',
        '%{php_home}/PhpParser4/autoload.php',
    ],
]);
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
touch vendor/autoload.php
: Run upstream test suite
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
