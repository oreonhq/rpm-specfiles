%global source0_hash 73761bdcbb0810bdd45b01a6bb262794db6bd244cc14d3667ab373a858b2b54a
%global composer_vendor  smarty
%global composer_project smarty
%global php_min_ver 7.1
%{!?phpdir:  %global phpdir  %{_datadir}/php}
Name:          php-smarty4
Summary:        Smarty - the compiling PHP template engine
Version:       4.5.6
Release:        1%{?dist}
License:       LGPL-3.0-only
URL:           http://www.smarty.net
Source0:        smarty-%{version}.tar.gz
Source1:       make_smarty_tarball.sh
BuildArch:     noarch
Requires:      php(language) >= %{php_min_ver}
Recommends:    php-pecl-apcu
Requires:      php-ctype
Requires:      php-mbstring
%if ! 0%{?el8}
Recommends:    php-memcache
Recommends:    php-memcached
%endif
Requires:      php-opcache
Requires:      php-pdo
Requires:      php-zlib
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-fedora-autoloader-devel
# /oreon:deps
%description
Smarty is a template engine for PHP, facilitating the separation of
presentation (HTML/CSS) from application logic. This implies that PHP
code is application logic, and is separated from the presentation.

Autoloader: %{phpdir}/smarty4/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n smarty-%{version}

%build

%install
: Generate autoloader
phpab --template fedora --output libs/autoload.php libs
mkdir -p %{buildroot}%{phpdir}
cp -rp libs %{buildroot}%{phpdir}/smarty4/
%oreon_autofiles main

%check

: Library version value check
php -r '
    require_once "%{buildroot}%{phpdir}/smarty4/autoload.php";
    $version = Smarty::SMARTY_VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
