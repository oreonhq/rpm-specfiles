%global source0_hash 681d8a3b7cbd5bf41c963405cdeae53a58854624e0ac7bbca44a0cef932c82b6
%{!?php_inidir:  %global php_inidir  %{_sysconfdir}/php.d}
%{!?__php:       %global __php       %{_bindir}/php}
%{!?_pkgdocdir:  %global _pkgdocdir  %{_docdir}/%{name}-%{version}}
%undefine _strict_symbol_defs_build
%define _legacy_common_support 1
%global  req_libvirt_version 1.2.13
%global  extname             libvirt-php
%global  ini_name            40-%{extname}.ini
Name:		php-libvirt
Version:	0.5.8
Release:        5%{?dist}
Summary:        PHP language bindings for Libvirt
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://libvirt.org/php
Source0:        http://libvirt.org/sources/php/libvirt-php-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:	libvirt >= %{req_libvirt_version}
Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}
%global __provides_exclude_from ^%{_libdir}/.*\\.so$
# oreon:deps
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  php-devel
BuildRequires:  xhtml1-dtds
# /oreon:deps
%description
PHP language bindings for Libvirt API.
For more details see: http://www.libvirt.org/php/

%package doc
Summary:	Documentation for %{name}
BuildArch:	noarch
Requires:	%{name} = %{version}-%{release}
%description doc
PHP language bindings for Libvirt API.
For more details see: http://www.libvirt.org/php/ http://www.php.net/

This package contains the documentation for php-libvirt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{extname}-%{version} -p1

%build

%configure \
  --with-html-dir=%{_docdir} \
  --with-html-subdir=$(echo %{_pkgdocdir} | sed -e 's|^%{_docdir}/||')/html \
  --libdir=%{php_extdir}
%make_build
%install
%make_install
chmod +x %{buildroot}%{php_extdir}/%{extname}.so
if [ -f %{buildroot}%{php_inidir}/%{extname}.ini ]; then
    mv %{buildroot}%{php_inidir}/%{extname}.ini \
       %{buildroot}%{php_inidir}/%{ini_name}
else
  install -Dpm 644 src/libvirt-php.ini %{buildroot}%{php_inidir}/%{ini_name}
fi
rm %{buildroot}%{php_extdir}/%{extname}.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

: simple module load test
%{__php} --no-php-ini \
    --define extension=%{buildroot}%{php_extdir}/%{extname}.so \
    --modules | grep libvirt
%files -f %{oreon_filedir}/main.list
%files -n php-libvirt-doc -f %{oreon_filedir}/php-libvirt-doc.list

%changelog

%autochangelog
