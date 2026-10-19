%global source0_hash ecdcf9fd784d930ad91093ab9ef7ffa6bb3ffaebce494fc225949aab6e17f4e0
%bcond_without           tests
%global github_owner     guzzle
%global github_name      promises
%global github_version   3.0.2
%global github_commit    b94b2807d85443f9719887892882d0329d1e2598
%global composer_vendor  guzzlehttp
%global composer_project promises
%global php_min_ver 5.5
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Guzzle promises library
Group:         Development/Libraries
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh
BuildArch:     noarch
%if %{with tests}
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-json
Requires:      php-spl
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(fedora/autoloader)
BuildRequires:  php-json
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
Promises/A+ [1] implementation that handles promise chaining and resolution
interactively, allowing for "infinite" promise chaining while keeping the
stack size constant.

Autoloader: %{phpdir}/GuzzleHttp/Promise/autoload.php

[1] https://promisesaplus.com/

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{phpdir}/Fedora/Autoloader/autoload.php';

\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Promise\\', __DIR__);

require_once __DIR__ . '/functions_include.php';
AUTOLOAD

%build

%install
mkdir -p %{buildroot}%{phpdir}/GuzzleHttp/Promise
cp -rp src/* %{buildroot}%{phpdir}/GuzzleHttp/Promise/
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require "%{buildroot}%{phpdir}/GuzzleHttp/Promise/autoload.php";
\Fedora\Autoloader\Autoload::addPsr4('GuzzleHttp\\Promise\\Tests\\', dirname(__DIR__).'/tests');
EOF
: Upstream tests with SCLs if available
SCL_RETURN_CODE=0
for SCL in php php74 php80 php81 php82; do
    if which $SCL; then
       $SCL %{_bindir}/phpunit9 || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
