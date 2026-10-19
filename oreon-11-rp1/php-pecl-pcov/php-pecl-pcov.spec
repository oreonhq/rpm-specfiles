%global source0_hash 23255c8c9335a9636ccb743f5302436a97a582a0bbde9869485be911bbc15da8
%global pie_vend  pecl
%global pie_proj  pcov
%global pecl_name pcov
%global ini_name  40-%{pecl_name}.ini
%global sources   %{pecl_name}-%{version}
Summary:        Code coverage driver
Name:           php-pecl-%{pecl_name}
Version:        1.0.12
Release:        5%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://%{pie_vend}.php.net/get/%{sources}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
A self contained php-code-coverage compatible driver for PHP7.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PCOV_VERSION/{s/.* "//;s/".*$//;p}' php_pcov.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so

; Configuration

; The recommended defaults for production should be:
pcov.enabled = 0

; The recommended defaults for development should be:
;pcov.enabled = 1
;pcov.directory = /path/to/your/source/directory
;pcov.exclude = ''
;pcov.initial.memory = 65536
;pcov.initial.files = 64
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --enable-pcov \
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
: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=modules/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
: Upstream test suite for NTS extension
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q -P --show-diff
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
