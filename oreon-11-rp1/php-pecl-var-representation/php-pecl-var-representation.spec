%global source0_hash a43352b65a20a01c455fb3327fa99c4a03a9ca90fa92e937d8ad1b9e364dae41
%bcond_without      tests
%global pecl_name   var_representation
%global ini_name    40-%{pecl_name}.ini
%global upstream_version 0.1.5
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
%global _configure       ../%{sources}/configure
Summary:        A compact, more readable alternative to var_export
Name:           php-pecl-var-representation
Version:        %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release:        1%{?dist}
License:        BSD-3-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name}               = %{version}
Provides:       php-%{pecl_name}%{?_isa}       = %{version}
Provides:       php-pecl(%{pecl_name})         = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:       php-pecl-%{pecl_name}          = %{version}-%{release}
Provides:       php-pecl-%{pecl_name}%{?_isa}  = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  tzdata
# /oreon:deps
%description
var_representation is a compact alternative to var_export that
properly escapes control characters.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/COPYING/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Check version as upstream often forget to update this
extver=$(sed -n '/define PHP_VAR_REPRESENTATION_VERSION/{s/.* "//;s/".*$//;p}' php_var_representation.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}%{?gh_date:-dev}"; then
   : Error: Upstream version is ${extver}, expecting %{upstream_version}%{?upstream_prever}%{?gh_date:-dev}.
   exit 1
fi
cd ..

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build

peclconf() {
%configure \
    --with-var_representation \
    --with-php-config=$1
}
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
peclconf %{__phpconfig}
%make_build
%install
cd %{sources}
: Install the extension
%make_install
: Install the configuration
install -D -m 644 ../%{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml
: Install Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main

%check

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%if %{with tests}
cd %{sources}
: Run upstream test suite
TEST_PHP_EXECUTABLE=%{__php} \
TEST_PHP_ARGS="-n -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
