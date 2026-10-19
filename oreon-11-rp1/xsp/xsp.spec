%global source0_hash cba1c239fdc3bff759bb5cdcc38a6f5c89746b80fb575e440c572ac0d3e556f0
Name:			xsp
Version:	4.7.1
Release:        14%{?dist}
License:	MIT
URL:			http://www.mono-project.com/Main_Page
Summary:        A small web server that hosts ASP.NET
Source0:        http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Requires:	mono-core
ExclusiveArch: %mono_arches
%define debug_package %{nil}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-data
BuildRequires:  mono-data-oracle
BuildRequires:  mono-data-sqlite
BuildRequires:  mono-devel
BuildRequires:  mono-nunit-devel
BuildRequires:  mono-web-devel
BuildRequires:  monodoc-devel
# /oreon:deps
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
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
for f in asp-state dbsessmgr mod-mono-server fastcgi-mono-server xsp
do
  rm %{buildroot}/%{_bindir}/${f}
  rm %{buildroot}/%{_bindir}/${f}2
done
rm -Rf "%{buildroot}/usr/lib/monodoc/sources"
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n xsp-devel -f %{oreon_filedir}/xsp-devel.list
%files -n xsp-tests -f %{oreon_filedir}/xsp-tests.list

%changelog

%autochangelog
