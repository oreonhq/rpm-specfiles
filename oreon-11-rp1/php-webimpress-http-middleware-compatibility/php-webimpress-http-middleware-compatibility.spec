%global source0_hash 61359ebbda6f9b1aabe2d1848273dd5ac78744cd5f59e8548faff8145d0e0edb
%bcond_without       tests
%global gh_commit    8ed1c2c7523dce0035b98bc4f3a73ca9cd1d3717
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     webimpress
%global gh_project   http-middleware-compatibility
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global major        %nil
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        0.1.4
Release:        18%{?dist}
Summary:        Compatibility library for Draft PSR-15 HTTP Middleware
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 5.6
Requires:      (php-composer(http-interop/http-middleware) > 0.1.1 with php-composer(http-interop/http-middleware) < 0.6)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(http-interop/http-middleware) > 0.1.1 with php-composer(http-interop/http-middleware) < 0.6)
BuildRequires:  php(language)
BuildRequires:  phpunit9
# /oreon:deps
%description
The purpose of the library is to deliver consistent interface for
different versions of http-interop/http-middleware which implements
Draft of PSR-15 HTTP Middleware.

Many projects currently use different version of library
http-interop/http-middleware and updating to newest version requires
usually major release. The library lets consumers of your component
decide what version of http-interop/http-middleware they want to use
and allow them to migrate to the latest version at any time.

Autoloader: %{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

mv LICENSE.md LICENSE

%build

cat << 'EOF' | tee autoload/autoload.php
<?php
require_once '%{_datadir}/php/Interop/Http/Middleware/autoload.php';
require_once __DIR__ . '/http-middleware.php';
EOF
%install
: Library
mkdir -p        %{buildroot}%{_datadir}/php/%{pk_vendor}/
cp -pr autoload %{buildroot}%{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}
%oreon_autofiles main

%check

%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{pk_vendor}/%{pk_project}%{major}/autoload.php';
EOF
ret=0
for cmd in php php73 php74 php80; do
   if which $cmd; then
      $cmd %{phpunit} --no-coverage --verbose || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
