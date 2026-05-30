%global source0_hash none

# Fedora spec file for php-pecl-xdebug3
#
# Copyright (c) 2010-2026 Remi Collet
# Copyright (c) 2006-2009 Christopher Stone
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%global php_base   php

%bcond_without     tests

%global pie_vend   xdebug
%global pie_proj   xdebug
%global pecl_name  xdebug
%global gh_commit  af9280fff4eeb014309f8f66633c5e8f40e88b04
%global gh_short   %(c=%{gh_commit}; echo ${c:0:7})

# version/release
%global upstream_version 3.5.1
#global upstream_prever  alpha3
#global upstream_lower   %%(echo %%{upstream_prever} | tr '[:upper:]' '[:lower:]')
%global sources          src

# XDebug should be loaded after opcache
%global ini_name  15-%{pecl_name}.ini

Name:           %{php_base}-pecl-xdebug3
Summary:        Provides functions for function traces and profiling
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_lower}}
Release:        1%{?dist}
Source0:        https://github.com/xdebug/xdebug/archive/af9280fff4eeb014309f8f66633c5e8f40e88b04/xdebug-3.5.1%{?upstream_prever}-%(c=af9280fff4eeb014309f8f66633c5e8f40e88b04;.tar.gz

License:        Xdebug-1.03
URL:            https://xdebug.org/

ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires: (%{php_base}-devel >= 8.0 with %{php_base}-devel < 8.6)
BuildRequires:  php-pear
BuildRequires:  libtool
BuildRequires:  %{php_base}-xml
BuildRequires:  %{php_base}-soap
BuildRequires:  pkgconfig(zlib) >= 1.2.9

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# Extension
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
# PECL
Provides:       php-pecl(Xdebug)                 = %{version}
Provides:       php-pecl(Xdebug)%{?_isa}         = %{version}
# PIE
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%if "%{php_base}" != "php"
Requires:       %{php_base}-common%{?_isa}
Conflicts:      php-pecl-%{pecl_name}3
Provides:       php-pecl-%{pecl_name}3 = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}3%{?_isa}   = %{version}-%{release}
%else
# package was renamed on new major version
Obsoletes:      php-pecl-%{pecl_name}            < 3
%endif
Provides:       php-pecl-%{pecl_name}            = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}    = %{version}-%{release}


%description
The Xdebug extension helps you debugging your script by providing a lot of
valuable debug information. The debug information that Xdebug can provide
includes the following:

* stack and function traces in error messages with:
  o full parameter display for user defined functions
  o function name, file name and line indications
  o support for member functions
* memory allocation
* protection for infinite recursions

Xdebug also provides:

* profiling information for PHP scripts
* code coverage analysis
* capabilities to debug your scripts interactively with a debug client

Documentation: https://xdebug.org/docs/


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -qc
mv %{pecl_name}-%{gh_commit} %{sources}
mv %{sources}/package.xml .

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

pushd %{sources}
# Check extension version
ver=$(sed -n '/XDEBUG_VERSION/{s/.* "//;s/".*$//;p}' php_xdebug.h)
if test "$ver" != "%{upstream_version}%{?upstream_prever}%{?gh_date:-dev}"; then
   : Error: Upstream XDEBUG_VERSION version is ${ver}, expecting %{upstream_version}%{?upstream_perver}%{?gh_date:-dev}.
   exit 1
fi
popd

cat << 'EOF' >%{ini_name}
; Enable xdebug extension module
zend_extension=%{pecl_name}.so

; Configuration
; See https://xdebug.org/docs/all_settings
EOF
sed -e '1,2d' %{sources}/%{pecl_name}.ini >>%{ini_name}

head -n15 <%{ini_name}


%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-xdebug  \
    --with-xdebug-compression \
    --with-php-config=%{__phpconfig}

%make_build


%install

: Install package registration file
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install config file
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}


: Install the extension
cd %{sources}
%make_install

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do
  [ -f contrib/$i ] && j=contrib/$i || j=$i
  install -Dpm 644 $j %{buildroot}%{pecl_docdir}/%{pecl_name}/$j
done


%check
# Shared needed extensions
modules=""
for mod in simplexml; do
  if [ -f %{php_extdir}/${mod}.so ]; then
    modules="$modules -d extension=${mod}.so"
  fi
done

: check if the extension can be loaded
%{__php} \
    --no-php-ini \
    --define zend_extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^Xdebug$'

: check if provided config file is usable
%{__php} \
    --no-php-ini \
    -d extension_dir=%{buildroot}%{php_extdir} \
    -c %{buildroot}%{php_inidir}/%{ini_name} -v
%{__php} \
    --no-php-ini \
    -d extension_dir=%{buildroot}%{php_extdir} \
    -c %{buildroot}%{php_inidir}/%{ini_name} -v 2>err.log \
        | grep 'with Xdebug v%{upstream_version}%{?upstream_prever}'
if [ -s err.log ]; then
    cat err.log
    exit 1
fi

%if %{with tests}
cd %{sources}
: Upstream test suite

# see https://bugs.xdebug.org/view.php?id=2048
rm tests/base/bug02036*.phpt
# Erratic result
rm tests/debugger/bug00998-ipv6.phpt

# bug00886 is marked as slow as it uses a lot of disk space
TEST_OPTS="-q -x --show-diff"

TEST_PHP_ARGS="-n $modules -d zend_extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-xdebug-tests.php $TEST_OPTS
%else
: Test suite disabled
%endif


%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.5.1-1
- Import
