%global source0_hash ecb3d3c9dc9f7ce034182d478b724ac3cb02098efc69a39c03534f0b1920922b
%global pie_vend   pecl
%global pie_proj   mailparse
%global pecl_name  mailparse
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}
Summary:        PHP PECL package for parsing and working with email messages
Name:      php-pecl-mailparse
Version:   3.1.9
Release:        1%{?dist}
License:   PHP-3.01
URL:       https://pecl.php.net/package/mailparse
Source0:        https://%{pie_vend}.php.net/get/%{sources}.tgz
ExcludeArch:   %{ix86}
Requires: php-mbstring%{?_isa}
Requires: php(zend-abi) = %{php_zend_api}
Requires: php(api) = %{php_core_api}
Provides: php-%{pecl_name} = %{version}
Provides: php-%{pecl_name}%{?_isa} = %{version}
Provides: php-pecl(%{pecl_name}) = %{version}
Provides: php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides: php-pie(%{pie_vend}/%{pie_proj}) = %{version}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-mbstring
BuildRequires:  php-pear
# /oreon:deps
%description
Mailparse is an extension for parsing and working with email messages.
It can deal with rfc822 and rfc2045 (MIME) compliant messages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# We need to create our working directory since the package*.xml files from
# the sources extract straight to it
%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
extver=$(sed -n '/#define PHP_MAILPARSE_VERSION/{s/.* "//;s/".*$//;p}' php_mailparse.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

cat > %{ini_name} << 'EOF'
; Enable mailparse extension module
extension = mailparse.so

; Set the default charset
;mailparse.def_charset = us-ascii
EOF

%build

cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure --with-php-config=%{__phpconfig}
%make_build
%install
install -Dpm 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
cd %{sources}
%make_install
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

cd %{sources}
: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=mbstring.so \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
: Upstream test suite for NTS extension
TEST_PHP_EXECUTABLE=%{__php} \
NO_INTERACTION=1 \
%{__php} run-tests.php \
    -n -q \
    -d extension=mbstring.so \
    -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --show-diff
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
