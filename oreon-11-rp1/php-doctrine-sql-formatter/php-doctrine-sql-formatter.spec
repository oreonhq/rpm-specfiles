%global source0_hash fa0e0d2b8359d5d2b25ba5d680fe8c0e2365f1030b6b5cbb07622fd1b29ab8a2
%bcond_with          bootstrap
%if %{with bootstrap}
%bcond_with          tests
%else
%bcond_without       tests
%endif
%global gh_commit    25a06c7bf4c6b8218f47928654252863ffc890a5
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   sql-formatter
%global major        %nil
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    Doctrine
%global ns_project   SqlFormatter
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.1.3
Release:        10%{?dist}
Summary:        SQL highlighting library
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 7.1
Requires:       php-pcre
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  phpunit8
# /oreon:deps
%description
A lightweight php package for formatting sql statements.

It can automatically indent and add line breaks in addition to syntax
highlighting.

This package is a fork from jdorn/sql-formatter.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate a simple autoloader
%{_bindir}/phpab \
    --output src/autoload.php \
    --template fedora \
    src
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests
cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
EOF
: Run test suite
ret=0
for cmd in php php74 php80 php81 php82; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 \
        --bootstrap vendor/autoload.php \
        --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
