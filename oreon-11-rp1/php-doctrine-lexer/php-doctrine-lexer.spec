%global source0_hash ddf6d88ce9164b8bf619b7fd07e3c8406db9c6884a9aed7894816b6ef7e1cb38
%global github_owner     doctrine
%global github_name      lexer
%global github_version   3.0.1
%global github_commit    c268e882d4dbdd85e36e4ad69e02dc284f89d229
%global github_short     %(c=%{github_commit}; echo ${c:0:7})
%global ns_vendor        Doctrine
%global ns_project       Common
%global ns_subproj       Lexer
%global composer_vendor  doctrine
%global composer_project lexer
%global php_min_ver      7.1
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global with_tests       0%{!?_without_tests:1}
Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Base library for a lexer that can be used in top-down, recursive descent parsers
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_short}.tgz
Source1:       makesrc.sh
BuildArch:     noarch
%if %{with_tests}
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-pcre
Requires:      php-reflection
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  phpunit9
# /oreon:deps
%description
Base library for a lexer that can be used in top-down, recursive descent
parsers.

This lexer is used in Doctrine Annotations and in Doctrine ORM (DQL).

Autoloader: %{phpdir}/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build

: Generate a simple autoloader
%{_bindir}/phpab \
    --output lib/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php \
    --template fedora \
    lib/%{ns_vendor}/%{ns_project}
%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/
%oreon_autofiles main

%check

%if %{with_tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    tests
cat << 'EOF' | tee -a vendor/autoload.php
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php";
EOF
: Run test suite
ret=0
for cmd in php php74 php80 php81; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit9 \
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
