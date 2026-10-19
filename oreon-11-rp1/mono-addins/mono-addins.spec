%global source0_hash 254539d14e71789814a4fd37ed444dd33fc8ddb5fc082b1bf8e93f3d5d840b14
%define debug_package %{nil}
Name:		mono-addins
Version:	1.3.3
Release:        1%{?dist}
Summary:        Addins for mono
License:	MIT
URL:		http://www.mono-project.com/Main_Page
Source0:        https://github.com/mono/mono-addins/archive/refs/tags/mono-addins-%{version}.tar.gz
Patch0:		mono-addins-1.0-libdir.patch
ExclusiveArch: %mono_arches
Provides: mono(Mono.Addins) = 0.2.0.0
Provides: mono(Mono.Addins) = 0.3.0.0
Provides: mono(Mono.Addins) = 0.4.0.0
Provides: mono(Mono.Addins) = 0.5.0.0
Provides: mono(Mono.Addins) = 0.6.0.0
Provides: mono(Mono.Addins.Gui) = 0.2.0.0
Provides: mono(Mono.Addins.Gui) = 0.3.0.0
Provides: mono(Mono.Addins.Gui) = 0.4.0.0
Provides: mono(Mono.Addins.Gui) = 0.5.0.0
Provides: mono(Mono.Addins.Gui) = 0.6.0.0
Provides: mono(Mono.Addins.Setup) = 0.2.0.0
Provides: mono(Mono.Addins.Setup) = 0.3.0.0
Provides: mono(Mono.Addins.Setup) = 0.4.0.0
Provides: mono(Mono.Addins.Setup) = 0.5.0.0
Provides: mono(Mono.Addins.Setup) = 0.6.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.2.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.3.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.4.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.5.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.6.0.0
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-sharp2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  pkgconfig
# /oreon:deps
%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

%package devel
Summary: Development files for mono-addins
Requires: %{name} = %{version}-%{release} pkgconfig
Provides: mono(Mono.Addins.MSBuild) = 0.2.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.3.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.4.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.5.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.6.0.0
%description devel
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.
This package contains MSBuild tasks file and target, which allows
using add-in references directly in a build file (still experimental).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}
%patch -P0 -p1 -b .libdir

%build

sed -i "s#AC_PATH_PROG(MCS, gmcs, no)#AC_PATH_PROG(MCS, mcs, no)#g" configure.ac
autoreconf -vif
%configure --enable-gui
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n mono-addins-devel -f %{oreon_filedir}/mono-addins-devel.list

%changelog

%autochangelog
