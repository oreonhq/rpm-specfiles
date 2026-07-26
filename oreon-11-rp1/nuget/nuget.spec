%global source0_hash b57781eaa57985248458f6b0984f774b086e15ff6a5ef1e38937d679758898e4

%global debug_package %{nil}

Name:           nuget
Version:        2.8.7
Release:        24%{?dist}
Summary:        Package manager for .Net/Mono development platform
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
Url:            http://nuget.org/

%global tarballversion %{version}+md510+dhx1.orig
Source0:        http://download.mono-project.com/sources/%{name}/%{name}_%{tarballversion}.tar.bz2
Source1:        nuget-core.pc
Source2:        nuget.sh
Patch0:         nuget-fix_xdt_hintpath
BuildRequires:  mono-devel mono-winfx

ExclusiveArch:  %{mono_arches}

%description
NuGet is the package manager for the Microsoft
development platform including .NET. The NuGet client
tools provide the ability to produce and consume
packages. The NuGet Gallery is the central package
repository used by all package authors and consumers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development package for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn nuget-git
sed -i "s/\r//g" src/Core/Core.csproj
%patch -P0 -p1

# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%build
%{?exp_env}
%{?env_options}

xbuild xdt/XmlTransform/Microsoft.Web.XmlTransform.csproj
xbuild src/Core/Core.csproj /p:Configuration="Mono Release"
xbuild src/CommandLine/CommandLine.csproj /p:Configuration="Mono Release"

%install
%{?env_options}
%{__mkdir_p} %{buildroot}%{_monodir}/nuget
%{__mkdir_p} %{buildroot}%{_libdir}/pkgconfig
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 %{SOURCE2} %{buildroot}%{_bindir}/`basename -s .sh %{SOURCE2}`
sed -i -e 's/cli/mono/' %{buildroot}%{_bindir}/*
%{__install} -m0755 src/CommandLine/bin/Release/NuGet.Core.dll %{buildroot}%{_monodir}/nuget/
%{__install} -m0755 xdt/XmlTransform/bin/Debug/Microsoft.Web.XmlTransform.dll %{buildroot}%{_monodir}/nuget/
%{__install} -m0755 src/CommandLine/bin/Release/NuGet.exe %{buildroot}%{_monodir}/nuget/

%files
%{license} LICENSE.txt
%{_monodir}/nuget
%{_bindir}/*

%files devel
%{_libdir}/pkgconfig/nuget-core.pc

%changelog
%autochangelog
