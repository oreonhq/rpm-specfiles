%global source0_hash 5f7313a0f2af0908305f9db3047661299604919122dc9838fa01247da0b97a4b
%global bootstrap    0
%global gh_commit    45a2ec53a73c70ce41d55cedef9063630abaf1b6
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     phar-io
%global gh_project   version
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    PharIo
%global ns_project   Version
%global major        %nil
%global php_home     %{_datadir}/php
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.2.1
Release:        1%{?dist}
Summary:        Library for handling version information and constraints
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
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
Library for handling version information and constraints.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

%{_bindir}/phpab --template fedora2 --output src/autoload.php src
%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with_tests}
: Run upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
    %{phpunit} --bootstrap %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}/autoload.php --verbose || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
