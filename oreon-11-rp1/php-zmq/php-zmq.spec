%global source0_hash f46243657e76717c349cf4b90f8c96ac2c5632f34c370f92ae3bc68636bd6538

# Fedora spec file for php-zmq
#
# SPDX-FileCopyrightText:  Copyright 2013-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name  zmq
%global with_tests %{?_without_tests:0}%{!?_without_tests:1}
%global ini_name   40-%{pecl_name}.ini

Summary:        ZeroMQ messaging
Name:           php-%{pecl_name}
Version:        1.1.3
Release:        37%{?dist}
License:        BSD-3-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz

Patch0:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/216.patch
Patch1:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/222.patch
Patch2:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/228.patch
Patch3:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/238.patch
Patch4:         https://patch-diff.githubusercontent.com/raw/zeromq/php-zmq/pull/240.patch

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel > 5.2
BuildRequires:  php-pear
BuildRequires:  zeromq-devel

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

# 1.0.7 is the first pecl release.
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
ZeroMQ is a software library that lets you quickly design and implement
a fast message-based applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# fix new default of MAX_SOCKETS
# Using current version, so this can be checked in next version and removed
# if appropriate. (still not fixed in 1.1.2, maybe later)
sed -i "s/int(1024)/int(1023)/g" %{pecl_name}-%{version}/tests/032-contextopt.phpt

mv %{pecl_name}-%{version} NTS

cd NTS
%patch -P0 -p1 -b .pr216
%patch -P1 -p1 -b .pr222
%patch -P2 -p1 -b .pr228
%patch -P3 -p1 -b .pr238
%patch -P4 -p1 -b .pr240
cd ..

# Create configuration file
cat << 'EOF' | tee  %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so
EOF

%build
cd NTS
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-zmq \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build

%install
%make_install -C NTS

# install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

# Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

# Test & Documentation
for i in $(grep 'role="test"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 NTS/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd NTS
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with_tests}
: upstream test suite for NTS extension
export TEST_PHP_ARGS="-n -d extension_dir=$PWD/modules -d extension=%{pecl_name}.so"
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%endif

%files
%doc %{pecl_docdir}/%{pecl_name}
%doc %{pecl_testdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
