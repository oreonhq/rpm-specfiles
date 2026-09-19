%global source0_hash 0b3962719de45f7f6b8d6c5481d7e50c2e79cbcf7f1ce02810b65fcfa261cc28

%define debug_package %{nil}

Name:		mono-basic
Version:	4.7
Release:	19%{?dist}
Summary:	VisualBasic.NET support for mono
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
URL:		http://www.mono-project.com/Main_Page
Source0:	http://origin-download.mono-project.com/sources/mono-basic/%{name}-%{version}.tar.bz2	

BuildRequires: make
BuildRequires:	pkgconfig
BuildRequires:	mono-devel >= 4.0.1
BuildRequires:	mono-winforms mono-data mono-web

ExclusiveArch: %{mono_arches}

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

%files 
%{_bindir}/vbnc*
%{_prefix}/lib/mono/?.?/vbnc*
%{_prefix}/lib/mono/?.?/Microsoft.VisualBasic.dll
%{_prefix}/lib/mono/gac/Microsoft.VisualBasic
%{_prefix}/lib/mono/?.?/Mono.Cecil.VB*dll
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Mdb
%{_prefix}/lib/mono/gac/Mono.Cecil.VB.Pdb
%{_prefix}/lib/mono/gac/Mono.Cecil.VB
%{_mandir}/man1/vbnc.*

%files devel
%{_libdir}/pkgconfig/mono-basic.pc

%changelog
%autochangelog
