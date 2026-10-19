%global source0_hash 7e782fbe7b7de2b5f1c43f49d9eb8c427649b547573564c78baaf2b8f8160ef4
%bcond_with       tests
%global pecl_name  raphf
%global pie_vend   m6w6
%global pie_proj   ext-raphf
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}
%global _configure ../%{sources}/configure
Summary:        Resource and persistent handles factory
Name:           php-pecl-%{pecl_name}
Version:        2.0.2
Release:        3%{?dist}
License:        BSD-2-Clause
URL:            http://pecl.php.net/package/%{pecl_name}
Source0:        http://pecl.php.net/get/%{sources}.tgz
ExcludeArch:    %{ix86}
%if %{with tests}
%endif
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}
# oreon:deps
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  php-pecl-http
# /oreon:deps
%description
A reusable split-off of pecl_http's persistent handle and resource
factory API.

%package devel
Summary:       %{name} developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}
%description devel
These are the files needed to compile programs using %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_RAPHF_VERSION/{s/.* "//;s/".*$//;p}' php_raphf.h)
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
;raphf.persistent_handle.limit = -1
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --with-php-config=%{__phpconfig}
%make_build
%install
cd %{sources}
: Install config file
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
: Install the extension
%make_install
: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

cd %{sources}
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=modules/%{pecl_name}.so \
    --modules | grep %{pecl_name}
%if %{with tests}
for mod in json hash iconv propro; do
  if [ -f %{php_extdir}/${mod}.so ]; then
    modules="$modules -d extension=${mod}.so"
  fi
done
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n $modules -d extension=$PWD/modules/%{pecl_name}.so -d extension=http.so" \
NO_INTERACTION=1 \
REPORT_EXIT_STATUS=1 \
%{__php} -n run-tests.php
%endif
%files -f %{oreon_filedir}/main.list
%files -n php-pecl-raphf-devel -f %{oreon_filedir}/php-pecl-raphf-devel.list

%changelog

%autochangelog
