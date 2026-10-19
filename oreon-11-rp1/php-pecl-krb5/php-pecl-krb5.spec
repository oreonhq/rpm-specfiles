%global source0_hash 8dab1d0c61873f85b11be53d908e572eac124399c3837aa311374cecb5e13c9e
%global pecl_name   krb5
%global ini_name    40-%{pecl_name}.ini
%global sources     %{pecl_name}-%{version}
Summary:        Kerberos authentification extension
Name:           php-pecl-%{pecl_name}
Version:        1.2.4
Release:        1%{?dist}
License:        MIT
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz
ExcludeArch:    %{ix86}
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Provides:       php-%{pecl_name} = %{version}
Provides:       php-%{pecl_name}%{?_isa} = %{version}
Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  krb5-devel
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  pkgconfig(com_err)
# /oreon:deps
%description
Features:
+ An interface for maintaining credential caches (KRB5CCache),
  that can be used for authenticating against a kerberos5 realm
+ Bindings for nearly the complete GSSAPI (RFC2744)
+ The administrative interface (KADM5)
+ Support for HTTP Negotiate authentication via GSSAPI

%package devel
Summary:       Kerberos extension developer files (header)
Requires:      %{name}%{?_isa} = %{version}-%{release}
Requires:      php-devel%{?_isa}
%description devel
These are the files needed to compile programs using the Kerberos extension.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_KRB5_VERSION/{s/.* "//;s/".*$//;p}' php_krb5.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable the '%{pecl_name}' extension module
extension=%{pecl_name}.so
EOF

%build

export CFLAGS="%{optflags} $(pkg-config --cflags com_err)"
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
    --with-krb5 \
    --with-krb5config=%{_bindir}/krb5-config \
    --with-krb5kadm \
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
: Install Test and Documentation
for i in $(grep 'role="test"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_testdir}/%{pecl_name}/$i
done
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

: Minimal load test for NTS extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
%files -f %{oreon_filedir}/main.list
%files -n php-pecl-krb5-devel -f %{oreon_filedir}/php-pecl-krb5-devel.list

%changelog

%autochangelog
