%global source0_hash 15a9547998fb7c5fe6ab3313239b02c0fa47e5d1c3c6f699b3b4e0a6b06b96b3
%bcond_without     tests
%undefine _strict_symbol_defs_build
%global gh_commit  4b6e81fc73b9473123a353c7c71112bf66a420ae
%global gh_short   %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner   nrk
%global gh_project phpiredis
%global pecl_name  phpiredis
%global with_zts   0%{!?_without_zts:%{?__ztsphp:1}}
%if "%{php_version}" < "5.6"
%global ini_name   %{pecl_name}.ini
%else
%global ini_name   40-%{pecl_name}.ini
%endif
Name:           php-%{pecl_name}
Version:        1.0.1
Release:        24%{?dist}
Summary:        Client extension for Redis
License:        BSD-2-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{version}-%{gh_short}.tar.gz
Patch0:         %{pecl_name}-pr67.patch
ExcludeArch:    %{ix86}
%if %{with tests}
%endif
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
%if 0%{?fedora} < 20 && 0%{?rhel} < 7 && 0%{?oreon} < 11
%{?filter_provides_in: %filter_provides_in %{_libdir}/.*\.so$}
%{?filter_setup}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  hiredis-devel
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  redis
# /oreon:deps
%description
Phpiredis is an extension for PHP based on hiredis
that provides a simple and efficient client for Redis and a fast
incremental parser / serializer for the RESP protocol.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
mv %{gh_project}-%{gh_commit} NTS

cd NTS
%patch -P0 -p1 -b .pr67

# Check extension version
ver=$(sed -n '/define PHP_PHPIREDIS_VERSION/{s/.* "//;s/".*$//;p}' php_phpiredis.h)
if test "$ver" != "%{version}%{?prever}%{?gh_date:-dev}"; then
   : Error: Upstream VERSION version is ${ver}, expecting %{version}%{?prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

cat  << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%if %{with_zts}
# Duplicate source tree for NTS / ZTS build
cp -pr NTS ZTS
%endif

%build

cd NTS
%{_bindir}/phpize
%configure --with-php-config=%{_bindir}/php-config
make %{?_smp_mflags}
%if %{with_zts}
cd ../ZTS
%{_bindir}/zts-phpize
%configure --with-php-config=%{_bindir}/zts-php-config
make %{?_smp_mflags}
%endif
%install
make -C NTS install INSTALL_ROOT=%{buildroot}
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
%if %{with_zts}
make -C ZTS install INSTALL_ROOT=%{buildroot}
install -Dpm 644 %{ini_name} %{buildroot}%{php_ztsinidir}/%{ini_name}
%oreon_autofiles main
%endif
%check

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with_zts}
: Minimal load test for NTS extension
%{__ztsphp} --no-php-ini \
    --define extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%endif
%if %{with tests}
: Upstream test suite for NTS extension
pidfile=$PWD/redis.pid
port=$(%{__php} -r 'echo 9000 + PHP_MAJOR_VERSION*100 + PHP_MINOR_VERSION*10 + PHP_INT_SIZE;')
sed -e "/REDIS_PORT/s/6379/$port/" -i ?TS/tests/testsuite_configuration.inc
mkdir -p data
redis-server                   \
    --bind      127.0.0.1      \
    --port      $port          \
    --daemonize yes            \
    --logfile   $PWD/redis.log \
    --dir       $PWD/data      \
    --pidfile   $pidfile
cd NTS
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php --show-diff || ret=1
%if %{with_zts}
cd ../ZTS
: Upstream test suite for ZTS extension
TEST_PHP_EXECUTABLE=%{__ztsphp} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_ztsextdir}/%{pecl_name}.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__ztsphp} -n run-tests.php --show-diff || ret=1
%endif
: Cleanup
if [ -s $pidfile ]; then
   kill $(cat $pidfile)
   sleep 1
fi
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
