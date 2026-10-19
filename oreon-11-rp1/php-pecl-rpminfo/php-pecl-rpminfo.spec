%global source0_hash af13be080c74ad449e31fd184fab718ce261c6c40a6ece65748ab0299a658c11
%global php_base   php
%global pecl_name  rpminfo
%global pie_vend   remi
%global pie_proj   rpminfo
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}
Summary:        RPM information
Name:           %{php_base}-pecl-%{pecl_name}
Version:        1.2.1
Release:        1%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.%{php_base}.net/get/%{sources}.tgz
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
Requires:     %{php_base}-common%{?_isa}
Conflicts:    php-pecl-%{pecl_name}
Provides:     php-pecl-%{pecl_name} = %{version}-%{release}
Provides:     php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  pkgconfig(rpm)
# /oreon:deps
%description
Retrieve RPM information using librpm, from local
RPM file or from installed packages database.

Documentation: https://www.php.net/rpminfo

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_RPMINFO_VERSION/{s/.* "//;s/".*$//;p}' php_rpminfo.h)
if test "x${extver}" != "x%{version}"; then
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
    --enable-rpminfo \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}
%make_build
%install
cd %{sources}
%make_install
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
%{__php} --no-php-ini \
    --define extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
TEST_PHP_ARGS="-n -d extension=%{buildroot}/%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
