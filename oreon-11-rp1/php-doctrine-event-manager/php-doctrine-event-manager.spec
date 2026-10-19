%global source0_hash b511b1c55989af7f0f0f2b73b209c1de046b8d6997be9972e0f3f4f03bdadadc
%global bootstrap    0
%global gh_commit    95aa4cb529f1e96576f3fda9f5705ada4056a520
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     doctrine
%global gh_project   event-manager
%global pk_vendor    %{gh_owner}
%global pk_project   %{gh_project}
%global ns_vendor    Doctrine
%global ns_project   Common
%global ns_subproj   EventManager
%global with_tests   0%{!?_without_tests:1}
Name:           php-%{pk_vendor}-%{pk_project}
Version:        2.1.1
Release:        1%{?dist}
Summary:        Simple PHP event system
License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with_tests}
%endif
Requires:       php(language) >= 7.1
Requires:      (php-composer(doctrine/deprecations)  >= 0.5.3 with php-composer(doctrine/deprecations)  < 2)
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
Conflicts:      php-doctrine-common < 1:2.9
# oreon:deps
BuildRequires:  (php-composer(doctrine/deprecations) >= 0.5.3 with php-composer(doctrine/deprecations) < 2)
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-reflection
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
The Doctrine Event Manager is a simple PHP event system that was built
to be used with the various Doctrine projects.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}/%{ns_subproj}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate a simple autoloader
mkdir src/%{ns_subproj}
%{_bindir}/phpab \
    --output src/%{ns_subproj}/autoload.php \
    --template fedora \
    src
cat << 'AUTOLOAD' | tee -a src/%{ns_subproj}/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}
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
for cmd in php php74 php80 php81 php82; do
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
