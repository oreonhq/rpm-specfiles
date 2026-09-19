%global source0_hash f9a51510ab52da51c2b39ba9329036247a3784b3a32788cbf199326b90f8bc78

%global pecl_name LZF
%global ini_name  40-lzf.ini

Name:           php-pecl-lzf
Version:        1.7.0
Release:        18%{?dist}
Summary:        Extension to handle LZF de/compression
License:        PHP-3.01
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{pecl_name}-%{version}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  php-pear
BuildRequires:  liblzf-devel
Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}

Provides:       php-pecl(%{pecl_name}) = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa} = %{version}

%description
This extension provides LZF compression and decompression using the liblzf
library.  LZF is a very fast compression algorithm, ideal for saving space with
a slight speed cost.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q
sed -e '/name="lib/d' -i package.xml
rm -r %{pecl_name}-%{version}/lib/

sed -e '/LICENSE/s/role="doc"/role="src"/' -i package.xml

cat > %{ini_name} << EOF
; Enable %{pecl_name} extension module
extension=lzf.so
EOF

%build
cd %{pecl_name}-%{version}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure --enable-lzf --with-liblzf --with-php-config=%{__phpconfig}
%make_build

%install
%make_install -C %{pecl_name}-%{version}

install -D -p -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

install -D -p -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

for i in $(grep 'role="doc"' package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -D -p -m 644 %{pecl_name}-%{version}/$i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
cd %{pecl_name}-%{version}
%{__php} run-tests.php \
    -n -P -q \
    -d extension=%{buildroot}%{php_extdir}/lzf.so

%files
%license %{pecl_name}-%{version}/LICENSE
%doc %{pecl_docdir}/%{pecl_name}
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/lzf.so
%{pecl_xmldir}/%{name}.xml

%changelog
%autochangelog
