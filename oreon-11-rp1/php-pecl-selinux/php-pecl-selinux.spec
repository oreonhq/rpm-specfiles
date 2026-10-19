%global source0_hash b4b4885f036209cf9bc27ebd4e2cbd9ed1fab5bf258d7cbd35254c90a62e230b
%bcond_without      tests
%define pecl_name   selinux
%global pie_vend    pecl
%global pie_proj    selinux
%global ini_name    40-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}
%global _configure  ../%{sources}/configure
Summary:        SELinux binding for PHP scripting language
Name:    php-pecl-selinux
Version: 0.6.1
Release:        1%{?dist}
License: PHP-3.01
URL:     https://pecl.php.net/package/%{pecl_name}
Source0:        https://%{pie_vend}.php.net/get/%{sources}.tgz
ExcludeArch:   %{ix86}
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Provides: php-%{pecl_name}                 = %{version}
Provides: php-%{pecl_name}%{?_isa}         = %{version}
Provides: php-pecl(%{pecl_name})           = %{version}-%{release}
Provides: php-pie(%{pie_vend}/%{pie_proj}) = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
This package is an extension to the PHP Hypertext Preprocessor.
It wraps the libselinux library and provides a set of interfaces
to the PHP runtime engine.
The libselinux is a set of application program interfaces towards in-kernel
SELinux, contains get/set security context, communicate security server,
translate between raw and readable format and so on.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

pushd %{sources}
extver=$(sed -n '/#define PHP_SELINUX_VERSION/{s/.* "//;s/".*$//;p}' php_selinux.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
popd

# Drop in the bit of configuration
cat > %{ini_name} << 'EOF'
; Enable SELinux extension module
extension=%{pecl_name}.so
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --with-php-config=%{__phpconfig} \
    --enable-selinux
%make_build
%install
: Drop in the bit of configuration
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
: Install the extension
cd %{sources}
%make_install
: Install Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
cd %{sources}
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
REPORT_EXIT_STATUS=0 \
%{__php} -n run-tests.php -q --show-diff
: Ignore result as unreliable in mock
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
