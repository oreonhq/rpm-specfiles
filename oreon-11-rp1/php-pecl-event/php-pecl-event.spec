%global source0_hash b7943948d0afededf7ceb2d19c35adf963afe75c2814f84895e4382d39232c98
%bcond_without      tests
%global pecl_name   event
%global pie_vend    osmanov
%global pie_proj    pecl-event
%global ini_name    40-%{pecl_name}.ini
%global upstream_version 3.1.5
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
Summary:        Provides interface to libevent library
Name:          php-pecl-%{pecl_name}
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_prever}}%{?upstream_postver:+%{upstream_postver}}
Release:        1%{?dist}
License:       PHP-3.01
URL:           https://pecl.php.net/package/event
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz
ExcludeArch:   %{ix86}
Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}
Requires:      php-sockets%{?_isa}
Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:      php-%{pie_vend}-%{pie_proj}      = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  pkgconfig
# /oreon:deps
%description
This is an extension to efficiently schedule I/O, time and signal based
events using the best I/O notification mechanism available for specific
platform. This is a port of libevent to the PHP infrastructure.

Version 1.0.0 introduces:
* new OO API breaking backwards compatibility
* support of libevent 2+ including HTTP, DNS, OpenSSL and the event listener.

Documentation: http://php.net/event

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c 

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
DIR=$(%{__php} -r 'echo "php" . PHP_MAJOR_VERSION;')
extver=$(sed -n '/#define PHP_EVENT_VERSION/{s/.* "//;s/".*$//;p}' $DIR/php_event.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?upstream_postver}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?upstream_postver}.
   exit 1
fi
cd ..

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension = %{pecl_name}.so
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --with-event-libevent-dir=%{_prefix} \
    --with-openssl-dir=%{_prefix} \
    --with-libdir=%{_lib} \
    --with-event-core \
    --with-event-extra \
    --with-event-openssl \
    --with-php-config=%{__phpconfig}
%make_build
%install
cd %{sources}
: Install the extension
%make_install
: Install the configuration file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install the package XML file
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
if [ -f %{php_extdir}/sockets.so ]; then
  OPTS="-d extension=sockets.so"
fi
: Minimal load test for the extension
%{__php} --no-php-ini $OPTS  \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
: Upstream test suite for the extension
SKIP_ONLINE_TESTS=1 \
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $OPTS -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
