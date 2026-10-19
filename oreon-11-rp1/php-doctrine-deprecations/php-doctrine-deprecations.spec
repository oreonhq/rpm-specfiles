%global source0_hash a8095fae80cd05b9751713b5084c4623ccce6d1be6c5ef86080c32ba668696ac
%bcond_without       tests
%global gh_commit    d4fe3e6fd9bb9e72557a19674f44d8ac7db4c6ca
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   deprecations
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    Doctrine
%global ns_project   Deprecations
Name:           php-%{pk_vendor}-%{pk_project}
Version:        1.1.6
Release:        1%{?dist}
Summary:        A small layer on top of triggeFr_error or PSR-3 logging
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit12
%endif
Requires:       php(language) >= 7.1
Requires:      (php-composer(psr/log) >= 1.0   with php-composer(psr/log) < 4)
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(psr/log) >= 1.0 with php-composer(psr/log) < 4)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  phpunit12
# /oreon:deps
%description
A small (side-effect free by default) layer on top of
trigger_error(E_USER_DEPRECATED) or PSR-3 logging.

* no side-effects by default, making it a perfect fit for libraries
  that don't know how the error handler works they operate under
* options to avoid having to rely on error handlers global state by
  using PSR-3 logging
* deduplicate deprecation messages to avoid excessive triggering and
  reduce overhead

We recommend to collect Deprecations using a PSR logger instead of
relying on the global error handler.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate a simple autoloader
%{_bindir}/phpab \
    --output src/autoload.php \
    --template fedora \
    src
cat << 'EOF' | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Psr/Log3/autoload.php',
        '%{_datadir}/php/Psr/Log2/autoload.php',
        '%{_datadir}/php/Psr/Log/autoload.php',
    ],
]);
EOF
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
%oreon_autofiles main

%check

%if %{with tests}
: Generate autoloader
mkdir vendor
%{_bindir}/phpab \
    --output vendor/autoload.php \
    --template fedora \
    test_fixtures/src \
    test_fixtures/vendor/doctrine/foo
cat << 'EOF' | tee -a vendor/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}/autoload.php',
]);
EOF
ret=0
for cmd in "php %{phpunit}" "php82 %{_bindir}/phpunit11" "php83 %{_bindir}/phpunit12" "php84 %{_bindir}/phpunit12" "php85 %{_bindir}/phpunit13"; do
  if which $cmd; then
    set $cmd
    $1 -d auto_prepend_file=vendor/autoload.php \
      $2 \
        --filter '^((?!(testDeprecationTrackByEnv)).)*$' \
        || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
