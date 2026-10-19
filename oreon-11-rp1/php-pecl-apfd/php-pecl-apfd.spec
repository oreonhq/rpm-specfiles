%global source0_hash de222ad4231f410d71b8232b01e3e22c9cc27a68e6d272f153b230f2b048995f
%bcond_without     tests
%global pecl_name  apfd
%global pie_vend   m6w6
%global pie_proj   ext-apfd
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}
Summary:        Always Populate Form Data
Name:           php-pecl-%{pecl_name}
Version:        1.0.3
Release:        20%{?dist}
License:        BSD-2-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj} = %{version}
Conflicts:      php-pecl(http) < 2.4
# oreon:deps
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
This tiny extension lets PHP's post handler parse `multipart/form-data` and
`application/x-www-form-urlencoded` (or any other customly registered form data
handler, like "json_post") without regard to the request's request method.

This extension does not provide any INI entries, constants, functions or classes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_APFD_VERSION/{s/.* "//;s/".*$//;p}' php_apfd.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
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
    --enable-apfd \
    --with-php-config=%{__phpconfig}
%make_build
%install
: Install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
: Install the extension
cd %{sources}
%make_install
: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
: Upstream test suite  for the extension
TEST_PHP_ARGS="-n -d extension=modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
