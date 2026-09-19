%global source0_hash 0ca5b0b3bf4f28cbcacc0b2a7824ea5472b20d07fd95642b281932be9d6009b1

# Fedora spec file for php-pecl-ssdeep
#
# SPDX-FileCopyrightText:  Copyright 2014-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%global pecl_name ssdeep
%global ini_name  40-%{pecl_name}.ini
%global sources   %{pecl_name}-%{version}

Summary:        Wrapper for libfuzzy library
Name:           php-pecl-%{pecl_name}
Version:        1.1.0
Release:        28%{?dist}
License:        BSD-2-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

Patch0:         https://patch-diff.githubusercontent.com/raw/php/pecl-text-ssdeep/pull/2.patch

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  ssdeep-devel > 2.5

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
The ssdeep project page describes it as a library for
"...computing context triggered piecewise hashes (CTPH).
Also called fuzzy hashes, CTPH can match inputs that have homologies.
Such inputs have sequences of identical bytes in the same order,
although bytes in between these sequences may be different in both
content and length".

For an in depth paper explaining context triggered piecewise hashes please
see http://dfrws.org/2006/proceedings/12-Kornblum.pdf

This extensions wraps the ssdeep fuzzy hashing API created by Jesse Kornblum.

Documentation: http://php.net/ssdeep

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

pushd %{sources}
%patch -P0 -p1 -b .pr2

# Sanity check, really often broken
extver=$(sed -n '/# *define PHP_SSDEEP_VERSION/{s/.* "//;s/".*$//;p}' php_ssdeep.h)
if test "x${extver}" != "x%{version}%{?versuf}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?versuf}.
   exit 1
fi
popd

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}

%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-ssdeep=%{_prefix} \
    --with-php-config=%{__phpconfig} \
    --with-libdir=%{_lib}

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install the config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install Test and Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
   sed -e 's/\r//'  -i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep %{pecl_name}

: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
