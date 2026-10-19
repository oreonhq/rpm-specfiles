%global source0_hash 0b3962719de45f7f6b8d6c5481d7e50c2e79cbcf7f1ce02810b65fcfa261cc28
%define debug_package %{nil}
Name:		mono-basic
Version:	4.7
Release:        19%{?dist}
Summary:        VisualBasic.NET support for mono
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.mono-project.com/Main_Page
Source0:        http://origin-download.mono-project.com/sources/mono-basic/%{name}-%{version}.tar.bz2
ExclusiveArch: %{mono_arches}
# oreon:deps
BuildRequires:  make
BuildRequires:  mono-data
BuildRequires:  mono-devel
BuildRequires:  mono-web
BuildRequires:  mono-winforms
BuildRequires:  pkgconfig
# /oreon:deps
%description
This package contains the Visual Basic .NET compiler and language
runtime. This allows you to compile and run VB.NET application and
assemblies.

%package devel
Summary: Development files for mono-basic
Requires: %{name} = %{version}-%{release} pkgconfig
%description devel
Development files for mono-basic

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --prefix=%{_prefix} --libdir=%{_prefix}/lib
make V=1
%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat <<EOF >%{buildroot}/%{_libdir}/pkgconfig/mono-basic.pc
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_prefix}/lib
Name: mono-basic
Description: mono-basic - VB for mono
Version: %{version}
Libs: -r:%{_prefix}/lib/mono/4.5/Microsoft.VisualBasic.dll
EOF
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mono-basic-devel -f %{oreon_filedir}/mono-basic-devel.list

%changelog

%autochangelog
