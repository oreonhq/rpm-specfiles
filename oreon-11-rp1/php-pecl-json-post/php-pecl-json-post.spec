%global source0_hash 31af67f0f08e6a928750a3bff863d5caa5fbc29d3568d117d5a0e74857cde376

# Fedora spec file for php-pecl-json-post
#
# SPDX-FileCopyrightText:  Copyright 2015-2025 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

%bcond_without     tests

%global pecl_name  json_post
%global pie_vend   m6w6
%global pie_proj   ext-json_post
# after 40-json.ini
%global ini_name   50-%{pecl_name}.ini
%global sources    %{pecl_name}-%{version}

Summary:        JSON POST handler
Name:           php-pecl-json-post
Version:        1.1.0
Release:        19%{?dist}
License:        BSD-2-Clause
URL:            https://pecl.php.net/package/%{pecl_name}
Source0:        https://pecl.php.net/get/%{sources}.tgz

ExcludeArch:    %{ix86}

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  php-json
BuildRequires:  php-pear

Requires:       php(zend-abi) = %{php_zend_api}
Requires:       php(api) = %{php_core_api}
Requires:       php-json%{?_isa}

Provides:       php-%{pecl_name}                 = %{version}
Provides:       php-%{pecl_name}%{?_isa}         = %{version}
Provides:       php-pecl(%{pecl_name})           = %{version}
Provides:       php-pecl(%{pecl_name})%{?_isa}   = %{version}
Provides:       php-pie(%{pie_vend}/%{pie_proj}) = %{version}
Provides:       php-%{pie_vend}-%{pie_proj}      = %{version}

%description
This extension provides a PHP content type handler for "text/json" to PHP's
form data parser. If the `Content-Type` of an incoming request is `text/json`,
the JSON contents of the request body will by parsed into `$_POST`.

This extension does not provide any constants, functions or classes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c

# Don't install/register tests
sed -e 's/role="test"/role="src"/' \
    -e '/LICENSE/s/role="doc"/role="src"/' \
    -i package.xml

cd %{sources}
# Sanity check, really often broken
extver=$(sed -n '/#define PHP_JSON_POST_VERSION/{s/.* "//;s/".*$//;p}' php_json_post.h)
if test "x${extver}" != "x%{version}"; then
   : Error: Upstream extension version is ${extver}, expecting %{version}.
   exit 1
fi
cd ..

# Create configuration file
cat << 'EOF' | tee %{ini_name}
; Enable '%{summary}' extension module
extension=%{pecl_name}.so

; Configuration
;json_post.flags=1
;json_post.onerror.response = 0
;json_post.onerror.exit = 0
;json_post.onerror.warning = 0
EOF

%build
cd %{sources}
%{__phpize}
sed -e 's/INSTALL_ROOT/DESTDIR/' -i build/Makefile.global

%configure \
    --enable-json-post \
    --with-php-config=%{__phpconfig}

%make_build

%install
: Install config file
install -D -m 644 %{ini_name} %{buildroot}%{php_inidir}/%{ini_name}

: Install XML package description
install -D -m 644 package.xml %{buildroot}%{pecl_xmldir}/%{name}.xml

: Install the extension
cd %{sources}
%make_install

: Install the Documentation
for i in $(grep 'role="doc"' ../package.xml | sed -e 's/^.*name="//;s/".*$//')
do install -Dpm 644 $i %{buildroot}%{pecl_docdir}/%{pecl_name}/$i
done

%check
OPT="-n"
[ -f %{php_extdir}/json.so ] && OPT="$OPT -d extension=json.so"

cd %{sources}
: Minimal load test for NTS extension
%{__php} $OPT \
    --define extension=%{buildroot}%{php_extdir}/%{pecl_name}.so \
    --modules | grep '^%{pecl_name}$'

%if %{with tests}
: Upstream test suite  for NTS extension
TEST_PHP_CGI_EXECUTABLE=%{_bindir}/php-cgi \
TEST_PHP_ARGS="$OPT -d extension=$PWD/modules/%{pecl_name}.so" \
%{__php} -n run-tests.php -q --show-diff
%endif

%files
%doc %{pecl_docdir}/%{pecl_name}
%license %{sources}/LICENSE

%{pecl_xmldir}/%{name}.xml
%config(noreplace) %{php_inidir}/%{ini_name}
%{php_extdir}/%{pecl_name}.so

%changelog
%autochangelog
