%global source0_hash 9ae96c5f0be6c84fbbd07e04d5f6cb0e825e39a245b6a65434c8c6040fda6305

# Fedora spec file for php-pecl-pq
# without SCL compatibility, from
#
# remirepo spec file for php-pecl-pq
#
# SPDX-FileCopyrightText:  Copyright 2014-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# Build using "--without tests" to disable tests
%bcond_without     tests

%global pecl_name  pq
%global pie_vend   m6w6
%global pie_proj   ext-pq
%global ini_name   50-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:        PostgreSQL client library (libpq) binding
Name:           php-pecl-%{pecl_name}
Version:        2.2.3
Release:        9%{?dist}
License:        BSD-2-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}%{?rcver}.tgz

Patch0:         53.patch

ExcludeArch:    %{ix86}

BuildRequires:  libpq-devel > 9
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel >= 7.0
BuildRequires:  php-pear
BuildRequires:  php-json
BuildRequires:  php-pecl-raphf-devel >= 1.1.0
%if %{with tests}
BuildRequires:  postgresql-server
BuildRequires:  postgresql-contrib
%endif

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}
Requires:       php-raphf%{?_isa}  >= 1.1.0

Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%description
PostgreSQL client library (libpq) binding.

Documents: http://devel-m6w6.rhcloud.com/mdref/pq

Highlights:
* Nearly complete support for asynchronous usage
* Extended type support by pg_type
* Fetching simple multi-dimensional array maps
* Working Gateway implementation

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install tests nor LICENSE
sed -e '/role="test"/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
%patch -P0 -p1 -b .pr53

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PQ_VERSION/{s/.* "//;s/".*$//;p}' php_pq.h)
if test "x${extver}" != "x%{version}%{?rcver}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?rcver}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable "%{summary}" extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install  Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
: ignore tests with erratic results
rm %{sources}/tests/cancel001.phpt
rm %{sources}/tests/flush001.phpt

OPT="-n"
[ -f %{php_extdir}/json.so ]  && OPT="$OPT -d extension=json.so"
[ -f %{php_extdir}/raphf.so ] && OPT="$OPT -d extension=raphf.so"

: Minimal load test for NTS extension
%{__php} $OPT \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
RET=0

: Running a server
DATABASE=$PWD/data
%ifarch x86_64
PORT=5440
%else
PORT=5436
%endif
pg_ctl initdb -D $DATABASE
cat <<EOF >>$DATABASE/postgresql.conf
unix_socket_directories = '$DATABASE'
port = $PORT
EOF
pg_ctl -D $DATABASE -l $PWD/server.log -w -t 200  start
createdb -h localhost -p $PORT rpmtest

cd %{sources}
sed -e "/PQ_DSN/s/\"host.*\"/'host=localhost port=$PORT dbname=rpmtest'/" \
    -i tests/_setup.inc

: Upstream test suite  for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="$OPT -d extension=$PWD/../NTS/modules/%{pecl_name}.so" \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php -q --show-diff || RET=1

cd ..
: Cleanup
psql -h localhost -p $PORT -c "SELECT version()" rpmtest
pg_ctl -D $DATABASE -w stop
rm -rf $DATABASE

exit $RET
%endif

%files
%doc %{pecl_docdir}/%{pecl_name}
%license %{sources}/LICENSE
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
