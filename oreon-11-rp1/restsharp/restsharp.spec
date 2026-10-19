%global source0_hash 1ace876278078ea2b40220c049179a551c5dc8fafcc0f2fb9218d1529e74d879
%global libname RestSharp
%global debug_package %{nil}
Name:           restsharp
Version:        105.2.3
Release:        31%{?dist}
Summary:        Simple REST and HTTP API Client
License:        Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            http://restsharp.org 
Source0:        https://github.com/%{name}/%{libname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         %{name}-case.patch
Patch1:         %{name}-unbundle-nunit.patch
Patch2:         %{name}-disable-nuget.patch
ExclusiveArch: %{mono_arches}
ExcludeArch:    armv7hl
# oreon:deps
BuildRequires:  mono-devel
BuildRequires:  nunit2
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{libname}-%{version}
%patch -P0
%patch -P1
# FIXME check why last hunk gets rejected
#%patch2
find . -name \*.csproj |xargs sed -i \
 -e /nuget/d -e /NuSpecUpdateTask.cs/d \
 -e 's#,1658##g'
# disable sloppy tests, https://github.com/restsharp/RestSharp/issues/767
sed -i -r 's,.*Can_Deserialize_DateTime_With_DateTimeStyles,[Ignore("broken")]\n\0,' %{libname}.Tests/JsonTests.cs
sed -i -r -e 's,.*Can_Deserialize_DateTimeOffset,[Ignore("broken")]\n\0,' \
 -e 's,.*Can_Deserialize_TimeSpan,[Ignore("broken")]\n\0,' \
 %{libname}.Tests/XmlAttributeDeserializerTests.cs %{libname}.Tests/XmlDeserializerTests.cs

%build

pushd %{libname}.Net45
xbuild %{libname}.Net45.Signed.csproj
%install
mkdir -p %{buildroot}/%{_monogacdir}
gacutil -i %{libname}.Net45/bin/DebugSigned/%{libname}.dll -f -package %{name} -root %{buildroot}/usr/lib
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat <<EOT >>%{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
Name: %{libname}
Description: %{summary}
Version: %{version}
Requires: mono
Libs: -r:%{_monodir}/%{name}/%{libname}.dll
Libraries=%{_monodir}/%{name}/%{libname}.dll
EOT
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

pushd %{libname}.Tests
%ifnarch s390x
xbuild /p:TargetFrameworkVersion=v4.5 %{libname}.Tests.csproj
nunit-console26 -labels -stoponerror bin/Debug/%{libname}.Tests.dll
%endif
%files -f %{oreon_filedir}/main.list
%files -n restsharp-devel -f %{oreon_filedir}/restsharp-devel.list

%changelog

%autochangelog
