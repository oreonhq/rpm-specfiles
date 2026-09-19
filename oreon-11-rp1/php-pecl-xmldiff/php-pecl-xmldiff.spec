%global source0_hash ec0882fda28f1c865b52466eec1a8e45b91cf0f1685b22f1f982ad6595edcbab

%global pecl_name  xmldiff
%global ini_name   40-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Name:             php-pecl-%{pecl_name}
Version:          1.1.6
Release:          2%{?dist}
Summary:          Pecl package for XML diff and merge

License:          BSD-2-Clause
URL:              http://pecl.php.net/package/%{pecl_name}
Source0:          http://pecl.php.net/get/%{sources}.tgz

ExcludeArch:      %{ix86}

BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    php-pear
BuildRequires:    php-devel
BuildRequires:    libxml2-devel
BuildRequires:    diffmark-devel
BuildRequires:    dos2unix
# dom.so needed by %%check
BuildRequires:    php-dom
BuildRequires:    php-libxml

Requires:         php-dom%{?_isa}
Requires:         php-libxml%{?_isa}
Requires:         php(zend-abi) = %{php_zend_api}
Requires:         php(api) = %{php_core_api}

Provides:         php-%{pecl_name}               = %{version}
Provides:         php-%{pecl_name}%{?_isa}       = %{version}
Provides:         php-pecl(%{pecl_name})         = %{version}
Provides:         php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
The extension is able to produce diffs of two XML documents and then
to apply the difference to the source document. The diff
is a XML document containing copy/insert/delete instruction nodes in
human readable format. DOMDocument objects, local files and strings in
memory can be processed.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc

sed -e '/name="diffmark/d' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# drop bundled library to ensure it is not used
rm -rf diffmark

# to make rpmlint happy
dos2unix --keepdate LICENSE

# Create configuration file
cat > %{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --with-libdiffmark \
    --with-libdir=%{_lib} \
    --with-php-config=%{__phpconfig}

%make_build

%install
cd %{sources}

: Install the extension
%make_install

: Install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 ../package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the documentation
install -D -m 644 CREDITS %{buildroot}/%{pecl_docdir}/%{pecl_name}/CREDITS

: Clean devel 
rm -rf %{buildroot}/%{_includedir}/php/ext/%{pecl_name}

%check
# only check if build extension can be loaded
php \
    --no-php-ini \
    --define extension=dom.so \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

cd %{sources}
TEST_PHP_ARGS="-n -d extension=dom.so -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
php -n run-tests.php -q --show-diff

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so
%{pecl_xmldir}/%{name}.xml

%changelog
%autochangelog
