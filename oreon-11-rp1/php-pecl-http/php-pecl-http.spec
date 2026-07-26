%global source0_hash 1512dc02fea2356c4df50113e00943b0b7fc99bb22d34d9f624b4662f1dad263

# Fedora spec file for php-pecl-http
#
# SPDX-FileCopyrightText:  Copyright 2012-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# The project is pecl_http but the extension is only http
%global proj_name pecl_http
%global pecl_name http
%global pie_vend  m6w6
%global pie_proj  ext-http
# after 20-iconv 40-raphf
%global ini_name  50-%{pecl_name}.ini

%ifarch %{arm} aarch64
# Test suite disabled because of erratic results on slow ARM (timeout)
%bcond_with    tests
%else
%bcond_without tests
%endif

%global upstream_version 4.3.1
#global upstream_prever  RC1
%global sources          %{proj_name}-%{upstream_version}%{?upstream_prever}

Name:           php-pecl-http
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        2%{?dist}
Summary:        Extended HTTP support

License:        BSD-2-Clause
URL:            https://pecl.php.net/package/pecl_http
Source0:        https://pecl.php.net/get/%{sources}.tgz

# From http://www.php.net/manual/en/http.configuration.php
Source1:        %{proj_name}.ini

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 8.0
BuildRequires:  php-iconv
BuildRequires:  php-spl
BuildRequires:  php-pear
BuildRequires:  zlib-devel >= 1.2.0.4
BuildRequires:  curl-devel >= 7.18.2
BuildRequires:  libicu-devel
BuildRequires:  php-pecl-raphf-devel >= 2
BuildRequires:  libevent-devel >= 1.4
BuildRequires:  brotli-devel >= 1.0
BuildRequires:  pkgconfig
# only needed in F27+
BuildRequires:  openssl-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-iconv%{?_isa}
Requires:       php-spl%{?_isa}
Requires:       php-raphf%{?_isa} >= 2
# V1 don't support PHP 5.6 https://bugs.php.net/66879
Obsoletes:      php-pecl-http1 < 2
# to allow migration from PHP 7 (last is 2.1.0)
Obsoletes:      php-pecl-propro < 2.2

Provides:       php-pecl(%{proj_name})           = %{version}
Provides:       php-pecl(%{proj_name})%{?_isa}   = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%description
The HTTP extension aims to provide a convenient and powerful set of
functionality for major applications.

The HTTP extension eases handling of HTTP URLs, dates, redirects, headers
and messages in a HTTP context (both incoming and outgoing). It also provides
means for client negotiation of preferred language and charset, as well as
a convenient way to exchange arbitrary data with caching and resuming
capabilities.

Also provided is a powerful request and parallel interface.

Version 2 is completely incompatible to previous version.

Documentation : https://mdref.m6w6.name/http

%package devel
Summary:       Extended HTTP support developer files (header)
Requires:      php-pecl-http%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa} >= 5.3.0
Obsoletes:     php-pecl-http1-devel < 2

%description devel
These are the files needed to compile programs using HTTP extension.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q 

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cd %{sources}
extver=$(sed -n '/#define PHP_PECL_HTTP_VERSION/{s/.* "//;s/".*$//;p}' php_http.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?gh_date:dev}"; then
   : Error: Upstream HTTP version is now ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?gh_date:dev}.
   : Update the pdover macro and rebuild.
   exit 1
fi
cd ..

cp %{SOURCE1} %{ini_name}

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
  --with-http \
  --with-http-zlib-dir=%{_prefix} \
  --with-http-libcurl-dir=%{_prefix} \
  --without-http-libidn-dir \
  --without-http-libidn2-dir \
  --without-http-libidnkit-dir \
  --without-http-libidnkit2-dir \
  --with-http-libicu-dir=%{_prefix} \
  --with-http-libevent-dir=%{_prefix} \
  --with-http-libbrotli-dir=%{_prefix} \
  --with-libdir=%{_lib} \
  --with-php-config=%{__phpconfig}

%make_build

%install
: Install XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install config file
install -Dpm644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

cd %{sources}
: Install the extension
%make_install

: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{proj_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{proj_name}/$i
done

%check
cd %{sources}
export SKIP_ONLINE_TESTS=1

: ignore tests with erratic results
rm tests/client021.phpt
rm tests/client022.phpt
rm tests/client025.phpt
rm tests/client027.phpt
# sometime on s390x
rm tests/client016.phpt
rm tests/client028.phpt
rm tests/etag001.phpt

# Shared needed extensions
modules=""
for mod in iconv raphf; do
  if [ -f %{php_extdir}/${mod}.so ]; then
    modules="$modules -d extension=${mod}.so"
  fi
done

: Minimal load test for the extension
%{__php} --no-php-ini \
    $modules \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite for the extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $modules -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{proj_name}
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml

%files devel
%doc %{pecl_testdir}/%{proj_name}
%{php_incldir}/ext/%{pecl_name}

%changelog
%autochangelog
