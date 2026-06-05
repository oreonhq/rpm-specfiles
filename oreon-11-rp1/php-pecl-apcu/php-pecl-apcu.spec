%global source0_hash none

# Fedora spec file for php-pecl-apcu
#
# SPDX-FileCopyrightText:  Copyright 2013-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global php_base   php

%global pie_vend   apcu
%global pie_proj   apcu
%global pecl_name  apcu
%global ini_name   40-%{pecl_name}.ini

# Github forge
%global gh_vend    krakjoe
%global gh_proj    %{pie_proj}
%global forgeurl   https://github.com/%{gh_vend}/%{gh_proj}
%global tag        v%{version}

Name:           %{php_base}-pecl-apcu
Summary:        APC User Cache
License:        PHP-3.01
Version:        5.1.28
Release:        3%{?dist}
%forgemeta
URL:            %{forgeurl}

Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz
Source1:        %{pecl_name}.ini
Source2:        %{pecl_name}-panel.conf
Source3:        %{pecl_name}.conf.php

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  %{php_base}-devel

Requires:       php(zend-abi)
Requires:       php(api)

Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%if "%{php_base}" != "php"
Requires:     %{php_base}-common%{?_isa}
Conflicts:    php-pecl-%{pecl_name}
Provides:     php-pecl-%{pecl_name} = %{version}-%{release}
Provides:     php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif


%description
APCu is userland caching: APC stripped of opcode caching.

APCu only supports userland caching of variables.


%package devel
Summary:       APCu developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}

%if "%{php_base}" == "php"
Requires:     php-devel%{?_isa}
%else
Requires:     %{php_base}-devel%{?_isa}
Requires:     %{php_base}-common%{?_isa}
Conflicts:    php-pecl-%{pecl_name}-devel
Provides:     php-pecl-%{pecl_name}-devel = %{version}-%{release}
Provides:     php-pecl-%{pecl_name}-devel%{?_isa} = %{version}-%{release}
%endif

%description devel
These are the files needed to compile programs using APCu.


%if "%{php_base}" == "php"
%package -n apcu-panel
%else
%package panel
Requires:      %{php_base}-common
Conflicts:     apcu-panel
Provides:      apcu-panel = %{version}-%{release}
%endif
Summary:       APCu control panel
BuildArch:     noarch
Requires:      %{name} = %{version}-%{release}
Requires:      php(httpd)
Requires:      php-gd
Requires:      httpd

%if "%{php_base}" == "php"
%description -n apcu-panel
%else
%description panel
%endif
This package provides the APCu control panel, with Apache
configuration, available on http://localhost/apcu-panel/


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{pecl_name}-%{version}

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_APCU_VERSION/{s/.* "//;s/".*$//;p}' php_apc.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi

# Fix path to configuration file
sed -e s:apc.conf.php:%{_sysconfdir}/apcu-panel/conf.php:g \
    -i  apc.php


%build
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
   --enable-apcu \
   --with-php-config=%{__phpconfig}

%make_build


%install

# Install extension and configuration
%make_install
install -D -m 644 %{SOURCE1} %{buildroot}%{php_inidir}/%{ini_name}

# Install the Control Panel
# Pages
install -D -m 644 -p apc.php  \
        %{buildroot}%{_datadir}/apcu-panel/index.php
# Apache config
install -D -m 644 -p %{SOURCE2} \
        %{buildroot}%{_sysconfdir}/httpd/conf.d/apcu-panel.conf
# Panel config
install -D -m 644 -p %{SOURCE3} \
        %{buildroot}%{_sysconfdir}/apcu-panel/conf.php

# Test & Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done


%check
%{__php} -n \
   -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
   -m | grep '^apcu$'

# Upstream test suite
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff


%files
%license LICENSE
%doc NOTICE
%doc README.md
%doc TECHNOTES.txt

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%files devel
%doc tests
%{php_incldir}/ext/%{pecl_name}


%if "%{php_base}" == "php"
%files -n apcu-panel
%else
%files panel
%endif
# Need to restrict access, as it contains a clear password
%attr(550,apache,root) %dir %{_sysconfdir}/apcu-panel
%config(noreplace) %{_sysconfdir}/apcu-panel/conf.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/apcu-panel.conf
%{_datadir}/apcu-panel


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.28-3
- Prepare for Oreon 11 (RP1)
