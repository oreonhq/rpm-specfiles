%global source0_hash 51df91e1733a6659bcd02e33005e462d0dd8eea3397369be7469b76b78748c64
%global bootstrap    0
%global gh_commit    7761fcacf03b4d4f16e7ccb606d4879ca431fcf4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   manifest
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Manifest
%global major        %nil
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        2.0.4
Release:        1%{?dist}
Summary:        Component for reading phar.io manifest information
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with_tests}
%if 0%{?fedora} >= 32 || 0%{?rhel} >= 9 || 0%{?oreon} >= 11
%global phpunit %{_bindir}/phpunit9
%else
%global phpunit %{_bindir}/phpunit8
%endif
%endif
Requires:       php(language) >= 5.6
Requires:       php-dom
Requires:       php-phar
Requires:      (php-composer(%{pk_vendor}/version) >= 1.0.1 with php-composer(%{pk_vendor}/version) <  3)
Requires:       php-filter
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlwriter
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(phar-io/version) >= 1.0.1 with php-composer(phar-io/version) < 3)
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-filter
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-phar
BuildRequires:  php-spl
BuildRequires:  php-xmlwriter
BuildRequires:  phpunit9
# /oreon:deps
%description
Component for reading phar.io manifest information from a PHP Archive (PHAR).

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab --template fedora2 --output src/autoload.php src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{ns_vendor}/Version/autoload.php',
]);
EOF
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with_tests}
mkdir vendor
ln -s %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php vendor/autoload.php
: Fix for modern phpunit
find tests/ -name \*php -exec sed -e 's/setUp()/setUp():void/'  -i {} \;
: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{phpunit} --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
