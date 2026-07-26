%global source0_hash bc8404807a3a4dc896b310af21a7f8063aa238424ff77f27eb6ffa88b5874b8a

# Fedora spec file for php-pecl-yaml
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%bcond_without           tests

%global pecl_name        yaml
%global pie_vend         pecl
%global pie_proj         yaml
%global ini_name         40-%{pecl_name}.ini

%global upstream_version 2.3.0
#global upstream_prever  b2
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}

Summary:       PHP Bindings for libyaml
Name:          php-pecl-%{pecl_name}
Version:       %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:       2%{?dist}
License:       MIT
URL:           https://pecl.php.net/package/%{pecl_name}

Source0:       https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:   %{ix86}

BuildRequires: make
BuildRequires: gcc
BuildRequires: php-devel
BuildRequires: php-pear
BuildRequires: libyaml-devel

Requires:      php(zend-abi) = %{php_zend_api}
Requires:      php(api) = %{php_core_api}

# Extension
Provides:      php-%{pecl_name}                 = %{version}
Provides:      php-%{pecl_name}%{?_isa}         = %{version}
# PECL
Provides:      php-pecl(%{pecl_name})           = %{version}
Provides:      php-pecl(%{pecl_name})%{?_isa}   = %{version}
# PIE
Provides:      php-pie(%{pie_vend}/%{pie_proj}) = %{version}

%description
Support for YAML 1.1 (YAML Ain't Markup Language) serialization using the
LibYAML library.

Documentation: https://php.net/yaml

Package built for PHP %(%{__php} -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;')%{?scl: as Software Collection (%{scl} by %{?scl_vendor}%{!?scl_vendor:rh})}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q

# Remove test file to avoid regsitration
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Check upstream version (often broken)
extver=$(sed -n '/#define PHP_YAML_VERSION/{s/.* "//;s/".*$//;p}' php_yaml.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi
cd ..

cat << 'EOF' | tee %{ini_name}
; Enable %{summary} extension module
extension=%{pecl_name}.so

; %{pecl_name} extension configuration
; see http://www.php.net/manual/en/yaml.configuration.php

; Decode entities which have the explicit tag "tag:yaml.org,2002:binary"
;yaml.decode_binary = 0

; Controls the decoding of "tag:yaml.org,2002:timestamp"
; 0 will not apply any decoding, 1 will use strtotime() 2 will use date_create().
;yaml.decode_timestamp = 0

; Cause canonical form output.
;yaml.output_canonical = 0

; Number of spaces to indent sections. Value should be between 1 and 10.
;yaml.output_indent = 2

; Set the preferred line width. -1 means unlimited.
;yaml.output_width = 80

; Enable/disable serialized php object processing.
;yaml.decode_php = 0
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build

%install
: Install the XML package description
install -Dpm 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: install the config file
install -Dpm644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install the extension
cd %{sources}
%make_install

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{sources}

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite for NTS extension
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q -P --show-diff %{?_smp_mflags}
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
