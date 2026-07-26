%global source0_hash 229dfd81c8bf5557cd077fb96d2dda53e64371cc1028280bf7c735e2d1d2d427

%global github_owner   smarty-php
%global github_name    smarty
%global github_version 3.1.48
%global github_commit  2fc443806cdcaee4441be4d0bb09f8fa56a17f2c

%global composer_vendor  smarty
%global composer_project smarty

# "php": "^5.2 || ^7.0"
%global php_min_ver 5.2

%{!?phpdir:  %global phpdir  %{_datadir}/php}

Name:          php-Smarty
Summary:       Smarty - the compiling PHP template engine
Version:       %{github_version}
Release:       9%{?dist}

# Automatically converted from old format: LGPLv3 - review is highly recommended.
License:       LGPL-3.0-only
URL:           http://www.smarty.net
Source0:       https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{name}-%{github_version}-%{github_commit}.tar.gz

BuildArch:     noarch
## Autoloader
BuildRequires: php-fedora-autoloader-devel
# composer.json
BuildRequires: php(language) >= %{php_min_ver}
# Library version value check
BuildRequires: php-cli

Requires:      php(language) >= %{php_min_ver}
# phpcompatinfo (computed from version 3.1.47)
Requires:      php-ctype
Requires:      php-date
Requires:      php-mbstring
Requires:      php-pcre
Requires:      php-spl

# php-{COMPOSER_VENDOR}-{COMPOSER_PROJECT}
Provides:      php-%{composer_vendor}-%{composer_project} = %{version}-%{release}
# Composer
Provides:      php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%description
Smarty is a template engine for PHP, facilitating the separation of
presentation (HTML/CSS) from application logic. This implies that PHP
code is application logic, and is separated from the presentation.

Autoloader: %{phpdir}/Smarty/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{github_name}-%{github_commit}

%build
# Empty build section, nothing required

%install
: Generate autoloader
phpab --template fedora --output libs/autoload.php libs

mkdir -p %{buildroot}%{phpdir}
cp -rp libs %{buildroot}%{phpdir}/Smarty

%check
: Library version value check
php -r '
    require_once "%{buildroot}%{phpdir}/Smarty/autoload.php";
    $version = Smarty::SMARTY_VERSION;
    echo "Version $version (expected %{version})\n";
    exit(version_compare("%{version}", "$version", "=") ? 0 : 1);
'

%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc *.md
%doc *.txt
%doc composer.json
%{phpdir}/Smarty

%changelog
%autochangelog
