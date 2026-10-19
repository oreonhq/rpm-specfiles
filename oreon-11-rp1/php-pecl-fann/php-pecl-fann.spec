%global source0_hash e9603a4bcd2e16339ab55747595995ae1156de43749583026b7e2c5bd1d59dee
%bcond_without           tests
%global pecl_name        fann
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.2.0
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global _configure       ../%{sources}/configure
Summary:        Wrapper for FANN Library
Name:           php-pecl-%{pecl_name}
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# oreon:deps
BuildRequires:  fann-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
This package provides a PHP binding for FANN
(Fast Artificial Neural Network) Library.

Documentation: http://php.net/fann

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_FANN_VERSION/{s/.* "//;s/".*$//;p}' php_fann.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build

cd %{sources}
%{__phpize}
%configure \
    --with-php-config=%{__phpconfig}
make %{?_smp_mflags}
%install
make -C %{sources} install INSTALL_ROOT=%{buildroot}
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 %{sources}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
: Upstream test suite  for NTS extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff %{?_smp_mflags}
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
