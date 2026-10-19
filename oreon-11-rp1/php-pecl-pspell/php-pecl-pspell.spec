%global source0_hash 585441202e3a53e7b5190b38c2f8438d37b53845448d28af5f904cf65c56c02f
%bcond_without         tests
%global pecl_name      pspell
%global ini_name       30-%{pecl_name}.ini
%global sources        %{pecl_name}-%{version}
Summary:        Spell checker extension
Name:         php-pecl-%{pecl_name}
Version:      1.0.1
Release:        1%{?dist}
License:      PHP-3.01
URL:          https://pecl.php.net/package/pspell
Source0:        https://pecl.php.net/get/%{sources}.tgz
ExcludeArch:   %{ix86}
%if %{with tests}
%endif
Requires:     php(zend-abi) = %{php_zend_api}
Requires:     php(api) = %{php_core_api}
Provides:     php-pecl(%{pecl_name})         = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Obsoletes:    php-%{pecl_name}         < 8.4
Provides:     php-%{pecl_name}         = 1:%{version}-%{release}
Provides:     php-%{pecl_name}%{?_isa} = 1:%{version}-%{release}
# oreon:deps
BuildRequires:  aspell-devel
BuildRequires:  aspell-en
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
# /oreon:deps
%description
This extension allows you to check the spelling of a word and offer suggestions,
using GNU Aspell library and dictionaries.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_PSPELL_VERSION/{s/.* "//;s/".*$//;p}' php_pspell.h)
if test "x${extver}" != "x%{version}%{?prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}%{?prever}.
   exit 1
fi
cd ..

: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
  --with-pspell \
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
: minimal load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
OPT="%{?_smp_mflags} -q --show-diff"
%if %{with tests}
: upstream test suite
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php $OPT
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
