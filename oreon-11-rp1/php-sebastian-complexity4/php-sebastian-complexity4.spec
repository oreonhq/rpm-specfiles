%global source0_hash d6a71af50ea0d4436e7b94c9981d42e9d5e33a3777847deed0899d64becb64f3
%bcond_without       tests
%global gh_commit    ee41d384ab1906c68852636b6de493846e13e5a0
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   complexity
%global gh_date      2024-07-03
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        4
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Complexity
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        4.0.1
Release:        1%{?dist}
Summary:        Calculating the complexity of PHP code units, version 4
License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.2
Requires:      (php-composer(nikic/php-parser)     >= 5.0   with php-composer(nikic/php-parser)     < 6)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(nikic/php-parser) >= 5.0 with php-composer(nikic/php-parser) < 6)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit11
# /oreon:deps
%description
Library for calculating the complexity of PHP code units.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

phpab --template fedora --output src/autoload.php src
cat <<EOF | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PhpParser5/autoload.php',
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
for cmd in php php82 php83 php84; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit11 || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
