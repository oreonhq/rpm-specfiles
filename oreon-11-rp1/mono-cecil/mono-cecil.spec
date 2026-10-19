%global source0_hash fc9297f09e3b7b808b203318b167de1695f947099aad14f97b149e3051b0df8e
%global debug_package %{nil}
Name:           mono-cecil
Version:        0.11.6
Release:        1%{?dist}
Summary:        Library to generate and inspect programs and libraries in the ECMA CIL form
License:        MIT
URL:            http://www.mono-project.com/Cecil
Source0:        https://github.com/jbevain/cecil/archive/%{version}/cecil-%{version}.tar.gz
Source1:        %{name}.pc
ExclusiveArch:  %mono_arches
Requires:       mono-core
%global configuration net_462_Release
# oreon:deps
BuildRequires:  mono(xbuild)
# /oreon:deps
%description
Cecil is a library written by Jb Evain to generate and inspect programs and
libraries in the ECMA CIL format. It has full support for generics, and support
some debugging symbol format.

In simple English, with Cecil, you can load existing managed assemblies, browse
all the contained types, modify them on the fly and save back to the disk the
modified assembly.

Today it is used by the Mono Debugger, the bug-finding and compliance checking
tool Gendarme, MoMA, DB4O, as well as many other tools.

%package devel
Summary:        pkgconfig file for Mono.Cecil
Requires:       mono-cecil = %{version}-%{release}
Requires:       pkgconfig
%description devel
This package contains the cecil.pc file
which is required by other packages that reference Mono.Cecil.dll

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn cecil-%{version}

%build

export NoCompilerStandardLib=false
xbuild Mono.Cecil.sln /p:Configuration=%{configuration}
%install
mkdir -p %{buildroot}%{monogacdir}/
cd bin/%{configuration}/
gacutil -i Mono.Cecil.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Mdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Pdb.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
gacutil -i Mono.Cecil.Rocks.dll -f -package Mono.Cecil -root %{buildroot}/usr/lib
cd -
mkdir -p %{buildroot}/%{_libdir}/pkgconfig/
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/cecil.pc
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mono-cecil-devel -f %{oreon_filedir}/mono-cecil-devel.list

%changelog

%autochangelog
