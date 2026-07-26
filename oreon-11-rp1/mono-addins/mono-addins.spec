%global source0_hash 254539d14e71789814a4fd37ed444dd33fc8ddb5fc082b1bf8e93f3d5d840b14

%if 0%{?rhel}%{?el6}%{?el7}
# see https://lists.fedoraproject.org/pipermail/packaging/2011-May/007762.html
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_prefix}/lib/mono/gac
%endif

%define debug_package %{nil}

Name:		mono-addins
Version:	1.3.3
Release:	10%{?dist}
Summary:	Addins for mono
License:	MIT
URL:		http://www.mono-project.com/Main_Page
Source0:	https://github.com/mono/mono-addins/archive/refs/tags/mono-addins-%{version}.tar.gz
Patch0:		mono-addins-1.0-libdir.patch

BuildRequires: make
BuildRequires:	mono-devel >= 2.4
BuildRequires:	gtk-sharp2-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:	pkgconfig

# Mono only available on these:
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
#find . -name "Makefile*" -print -exec sed -i 's#ASSEMBLY_COMPILER_COMMAND = gmcs#ASSEMBLY_COMPILER_COMMAND = mcs#g; s#-r:Microsoft.Build.Utilities #-r:Microsoft.Build.Utilities.v4.0 #g' {} \;
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files 
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/mautil
%dir %{_monodir}/mono-addins
%{_monodir}/mono-addins/Mono.Addins.CecilReflector.dll
%{_monodir}/mono-addins/Mono.Addins.Gui*.dll
%{_monodir}/mono-addins/Mono.Addins.Setup.dll
%{_monodir}/mono-addins/Mono.Addins.dll
%{_monodir}/mono-addins/mautil.exe
%{_monogacdir}/Mono.Addins.Gui*
%{_monogacdir}/Mono.Addins.Setup
%{_monogacdir}/Mono.Addins
%{_monogacdir}/Mono.Addins.CecilReflector
%{_monogacdir}/policy.*.Mono.Addins
%{_monogacdir}/policy.*.Mono.Addins.Gui*
%{_monogacdir}/policy.*.Mono.Addins.Setup
%{_monogacdir}/policy.*.Mono.Addins.CecilReflector

%{_mandir}/man1/mautil.1.gz

%files devel
%{_monodir}/gac/policy.*.Mono.Addins.MSBuild
%{_monodir}/mono-addins/Mono.Addins.MSBuild.dll
%{_monodir}/gac/Mono.Addins.MSBuild
%{_libdir}/pkgconfig/mono-addins*

%changelog
%autochangelog
