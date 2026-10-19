%global source0_hash 52bf21a8697352d996a7b4d0465eadc70171bbc11bc68504b31be5b1c82f4106
%global github_owner     doctrine
%global github_name      collections
%global github_version   3.1.0
%global github_commit    2b44dd4cbca8b5744327de78bafef5945c7e7b5e
%global composer_vendor  doctrine
%global composer_project collections
%global php_min_ver 7.1.3
%global doctrine_depr_min_ver 1
%global doctrine_depr_max_ver 2
%bcond_without tests
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-%{composer_vendor}-%{composer_project}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        Collections abstraction library
License:       MIT
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_commit}.tar.gz
Source1:       %{name}-get-source.sh
BuildArch:     noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:     (php-composer(doctrine/deprecations) >= %{doctrine_depr_min_ver} with php-composer(doctrine/deprecations) < %{doctrine_depr_max_ver})
Requires:      php-pcre
Requires:      php-spl
Requires:      php-composer(fedora/autoloader)
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
Conflicts:     php-pear(pear.doctrine-project.org/DoctrineCommon) < 2.4
# oreon:deps
BuildRequires:  (php-composer(doctrine/deprecations) >= 1 with php-composer(doctrine/deprecations) < 2)
BuildRequires:  /usr/bin/phpunit9
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  php-spl
# /oreon:deps
%description
%{summary}.

Autoloader: %{phpdir}/Doctrine/Common/Collections/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build

: Create autoloader
phpab --template fedora \
      --output lib/Doctrine/Common/Collections/autoload.php \
      lib/Doctrine/Common/Collections
cat <<'AUTOLOAD' | tee -a lib/Doctrine/Common/Collections/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{phpdir}/Doctrine/Deprecations/autoload.php',
]);
AUTOLOAD
%install
mkdir -p %{buildroot}%{phpdir}
cp -rp lib/* %{buildroot}%{phpdir}/
%oreon_autofiles main

%check

%if %{with tests}
: Create tests bootstrap
cat <<'BOOTSTRAP' | tee bootstrap.php
<?php
require_once '%{buildroot}%{phpdir}/Doctrine/Common/Collections/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Doctrine\\Tests\\', __DIR__.'/tests/Doctrine/Tests');
BOOTSTRAP
: Upstream tests
SCL_RETURN_CODE=0
for CMD in "php %{phpunit}" php74 php80 php81 php82; do
    if which $CMD; then
        set $CMD
        $1 ${2:-%{_bindir}/phpunit9} --verbose --bootstrap bootstrap.php \
            || SCL_RETURN_CODE=1
    fi
done
exit $SCL_RETURN_CODE
%else
: Tests skipped
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
