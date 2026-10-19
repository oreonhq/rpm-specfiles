%global source0_hash 9fab1f8653d40249bd433ad2c3ca02431f9a5ab06d50f988c8ec53fc6a846eef
%global php_base         php
%global pecl_name        zip
%global pie_vend         pecl
%global pie_proj         zip
%global ini_name         40-%{pecl_name}.ini
%global upstream_version 1.22.8
%global gh_vend     pierrejoye
%global gh_proj     php_zip
%global forgeurl    https://github.com/%{gh_vend}/%{gh_proj}
%global tag         %{upstream_version}%{?upstream_prever}
Summary:        A ZIP archive management extension
Name:         %{php_base}-pecl-zip
License:      PHP-3.01
Version:      %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
%global sources          %{pecl_name}-%{upstream_version}%{?upstream_prever}
Release:        1%{?dist}
%forgemeta
URL:          %{forgeurl}
Source0:        https://%{pie_vend}.%{php_base}.net/get/%{pecl_name}-%{upstream_version}.tgz
ExcludeArch:   %{ix86}
Requires:     php(zend-abi)
Requires:     php(api)
Provides:     php-%{pecl_name} = %{version}-%{release}
Provides:     php-%{pecl_name}%{?_isa} = %{version}-%{release}
Provides:     php-pecl(%{pecl_name}) = %{version}
Provides:     php-pecl(%{pecl_name})%{?_isa} = %{version}
Provides:     php-pie(%{pie_vend}/%{pie_proj}) = %{version}
%if "%{php_base}" != "php"
Requires:     %{php_base}-common%{?_isa}
Conflicts:    php-pecl-%{pecl_name}
Provides:     php-pecl-%{pecl_name} = %{version}-%{release}
Provides:     php-pecl-%{pecl_name}%{?_isa} = %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  pkgconfig(libzip)
BuildRequires:  zlib-devel
# /oreon:deps
%description
Zip is an extension to create and read zip files.

%prep 

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{sources}

# Sanity check, really often broken
extver=$(sed -n '/#define PHP_ZIP_VERSION/{s/.* "//;s/".*$//;p}' php8/php_zip.h)
if test "x${extver}" != "x%{upstream_version}%{?upstream_prever}"; then
   : Error: Upstream extension version is ${extver}, expecting %{upstream_version}%{?upstream_prever}.
   exit 1
fi

: Create the configuration file
cat >%{ini_name} << 'EOF'
; Enable ZIP extension module
extension=%{pecl_name}.so
EOF

%build

%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global
%configure \
  --with-libzip \
  --with-libdir=%{_lib} \
  --with-php-config=%{__phpconfig}
%make_build
%install
: Install the configuration file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}
: Install the extension
%make_install
%oreon_autofiles main

%check

: minimal load test of the extension
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'
: upstream test suite
TEST_PHP_ARGS="-n -d extension=$PWD/modules/%{pecl_name}.so" \
TEST_PHP_EXECUTABLE=%{__php} \
%{__php} -n run-tests.php -q --show-diff
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{upstream_version}%{?upstream_prever:~%{upstream_prever}}-3
- Prepare for Oreon 11 (RP1)
