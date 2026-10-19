%global source1_hash f18caed5fb89ca9f0080e99c81c94be87bcfe0aca5e7d89113256b295e2f62ff
%global source0_hash f18caed5fb89ca9f0080e99c81c94be87bcfe0aca5e7d89113256b295e2f62ff
%bcond_with          tests
%global pie_vend     php-ds
%global pie_proj     ext-ds
%global pecl_name    ds
%global ini_name     40-%{pecl_name}.ini
%global sources      %{pecl_name}-%{version}
%global gh_commit    3d14aa6f8c25d38d79c90924150c51636544e4a8
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     php-ds
%global gh_project   tests
Summary:        Data Structures for PHP
Name:           php-pecl-%{pecl_name}
Version:        2.0.1
Release:        1%{?dist}
License:        MIT
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz
Source1:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{gh_project}-%{gh_short}.tar.gz
ExcludeArch:    %{ix86}
%if %{with tests}
%endif
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}
Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}
# oreon:deps
BuildRequires:  /usr/bin/phpab
BuildRequires:  /usr/bin/phpunit9
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-gmp
BuildRequires:  php-json
BuildRequires:  php-pear
# /oreon:deps
%description
An extension providing specialized data structures as efficient alternatives
to the PHP array.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -a 1
mv %{gh_project}-%{gh_commit} tests

# Don't install/register tests, install examples as doc
sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_DS_VERSION/{s/.* "//;s/".*$//;p}' php_ds.h)
if test "x${extver}" != "x%{version}%{?prever:-%{prever}}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever:-%{prever}}.
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
    --enable-ds \
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

: Minimal load test for the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
: Generate autoloader for tests
%{_bindir}/phpab \
   --output tests/autoload.php \
   tests
: Run upstream test suite
%{__php} \
   -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
   %{_bindir}/phpunit9 \
      --do-not-cache-result \
      --bootstrap tests/autoload.php \
      tests
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
