%global source0_hash c9d9e924f9906ee1e48fc8352cb580b1d82ef3c73a3b64b058f1cba1a81516b5
%bcond_without       tests
%global gh_commit    25f207c40d62b8b7aa32f5ab026c53561964053a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   complexity
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        %nil
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Complexity
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.0.0
Release:        1%{?dist}
Summary:        Calculating the complexity of PHP code units, version 2
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
Library for calculating the complexity of PHP code units.

This package provides version 2 of %{pk_vendor}/%{pk_project} library.

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
