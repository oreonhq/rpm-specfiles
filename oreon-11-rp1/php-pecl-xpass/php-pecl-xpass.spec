%global source0_hash 9a1d713b69cb44e8f46c764daf2d87763944396d255a942d8b857e01f90dc3df
%global php_base         php
%bcond_without           tests
%global pie_vend         remi
%global pie_proj         xpass
%global pecl_name        xpass
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.2.0
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
Summary:        Extended password extension
Name:           %{php_base}-pecl-%{pecl_name}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        2%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.%{php_base}.net/get/%{pie_proj}-%{version}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}
%if "%{php_base}" != "php"
Requires:       %{php_base}-common%{?_isa}
Conflicts:      php-pecl-%{pecl_name}
Provides:       php-pecl-%{pecl_name} = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  pkgconfig(libxcrypt)
# /oreon:deps
%description
This extension provides password hashing algorithms used by Linux
distributions, using extended crypt library (libxcrypt):

* sha512 provided for legacy as used on some old distributions
* yescrypt used on modern distributions
* sm3crypt
* sm3yescrypt

It also provides additional functions from libxcrypt missing in core PHP:

* crypt_preferred_method
* crypt_gensalt
* crypt_checksalt

See PHP documentation on https://www.php.net/xpass

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_XPASS_VERSION/{s/.* "//;s/".*$//;p}' php_xpass.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --enable-xpass \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}
%make_build
%install
%make_install -C %{sources}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
%{__php} --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
TEST_PHP_ARGS="-n -d extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
