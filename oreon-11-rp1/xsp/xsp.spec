%global source0_hash cba1c239fdc3bff759bb5cdcc38a6f5c89746b80fb575e440c572ac0d3e556f0

Name:			xsp
Version:	4.7.1
Release:	14%{?dist}
License:	MIT
URL:			http://www.mono-project.com/Main_Page
Summary:	A small web server that hosts ASP.NET

Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	mono-web-devel, mono-data, mono-devel, mono-data-sqlite, mono-nunit-devel
BuildRequires:	mono-data-oracle monodoc-devel
BuildRequires:	autoconf automake libtool
Requires:	mono-core
# Mono only available on these:
ExclusiveArch: %mono_arches

%define debug_package %{nil}

%description

XSP is a standalone web server written in C# that can be used to run ASP.NET 
applications as well as a set of pages, controls and web services that you can 
use to experience ASP.NET.

%package devel
Requires: %{name} = %{version}-%{release} pkgconfig
Summary: Development files for xsp

%description devel
Development files for xsp

%package tests
Requires: %{name} = %{version}-%{release}
Summary: xsp test files

%description tests
Files for testing the xsp server

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

sed -i "s#dmcs#mcs#g" configure

%build
%configure --libdir=%{_prefix}/lib --disable-docs
make

%install
make DESTDIR=%{buildroot} install

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete

# Remove scripts that are referencing .NET 2.0
for f in asp-state dbsessmgr mod-mono-server fastcgi-mono-server xsp
do
  rm %{buildroot}/%{_bindir}/${f}
  rm %{buildroot}/%{_bindir}/${f}2
done

# Remove monodoc sources
rm -Rf "%{buildroot}/usr/lib/monodoc/sources"

%files
%doc NEWS README COPYING
%{_bindir}/asp-state4
%{_bindir}/dbsessmgr4
%{_bindir}/mod-mono-server4
%{_bindir}/mono-fpm
%{_bindir}/shim
%{_bindir}/xsp4
%{_bindir}/fastcgi-mono-server4
%{_prefix}/lib/xsp
%{_monogacdir}/Mono.WebServer*/
%{_monogacdir}/fastcgi-mono-server4
%{_monogacdir}/mod-mono-server*/
%{_monogacdir}/mono-fpm
%{_monogacdir}/xsp*/
%{_monodir}/4.?/Mono.WebServer2.dll
%{_monodir}/4.?/fastcgi-mono-server4.exe
%{_monodir}/4.?/mod-mono-server4.exe
%{_monodir}/4.?/mono-fpm.exe
%{_monodir}/4.?/xsp4.exe
%{_prefix}/lib/libfpm_helper.so.0*
%{_mandir}/man1/asp*
%{_mandir}/man1/dbsessmgr*
%{_mandir}/man1/mod-mono-server*
%{_mandir}/man1/xsp*
%{_mandir}/man1/fastcgi-mono-server*

%files devel
%{_libdir}/pkgconfig/xsp*
%{_prefix}/lib/libfpm_helper.so

%files tests
%{_prefix}/lib/xsp/test

%changelog
%autochangelog
