%global source0_hash 1fd5e074dacf5149603493c454b476d69850bec0a71d7ea69a36a00db728a0fb

%bcond_without     tests

%global pecl_name oauth
%global ini_name  40-%{pecl_name}.ini
%global sources   %{pecl_name}-%{version}

Name:		php-pecl-oauth	
Version:	2.0.10
Release:	2%{?dist}
Summary:	PHP OAuth consumer extension
License:	BSD-3-Clause
URL:		https://pecl.php.net/package/oauth
Source0:	https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	php-devel
BuildRequires:	php-pear
%if %{with tests}
BuildRequires:	php-posix
%endif
BuildRequires:	libcurl-devel

Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}

Provides:	php-pecl(%{pecl_name}) = %{version}
Provides:	php-pecl(%{pecl_name})%{_isa} = %{version}
Provides:	php-%{pecl_name} = %{version}
Provides:	php-%{pecl_name}%{_isa} = %{version}

%description
OAuth is an authorization protocol built on top of HTTP which allows 
applications to securely access data without having to store
user names and passwords.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_OAUTH_VERSION/{s/.* //;s/".*$//;p}' php_oauth.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

cat >%{ini_name} << 'EOF'
; Enable %{pecl_name} extension module
extension=%{pecl_name}.so
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --with-php-config=%{__phpconfig}

%make_build

%install
: Drop in the bit of configuration
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

cd %{sources}
: Install the extension
%make_install

: Install Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
: Minimal load test for the extension
%{__php} -n \
    -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^OAuth$'

%if %{with tests}
cd %{sources}
# Ignore know as failing
rm tests/rsa.phpt

: Upstream test suite for the extension
TEST_PHP_ARGS="-n -d extension=posix.so -d extension=%{buildroot}%{php_extdir}/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif

%files
%license %{sources}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%{pecl_xmldir}/%{name}.xml

%config(noreplace) %{_sysconfdir}/php.d/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
