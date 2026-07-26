%global source0_hash 5b4ab2c7753f64fd8d2ca82b553e367c3b5accbed5103ce6a455ab156f7fa08e

%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif

Name:	 	log4net
URL:		http://logging.apache.org/log4net/
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:	Apache-2.0
Version:	2.0.8
Release:	24%{?dist}
Summary:	A .NET framework for logging
Source:		http://mirror.reverse.net/pub/apache/logging/log4net/source/%{name}-%{version}-src.zip
Patch0:		log4net-2.0.8-xmlconfigurator.patch

BuildRequires:	dos2unix
BuildRequires:	mono-data-sqlite
BuildRequires:	mono-devel

# Mono only available on these:
ExclusiveArch: %mono_arches

# %define debug_package %{nil}
# This is a mono package

%description
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime

%package devel
Summary:	A .NET framework for logging
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
log4net is a tool to help the programmer output log statements to a
variety of output targets. log4net is a port of the excellent log4j
framework to the .NET runtime

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
dos2unix src/Config/XmlConfigurator.cs
%patch -P0 -p1
sed -i 's/\r//' NOTICE
sed -i 's/\r//' README.txt
sed -i 's/\r//' LICENSE
# Remove prebuilt dll files
rm -rf bin/

# mv src/Layout/XMLLayout.cs src/Layout/XmlLayout.cs
# mv src/Layout/XMLLayoutBase.cs src/Layout/XmlLayoutBase.cs

# Fix for mono 4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

# Use system mono.snk key
sed -i -e 's!"..\\..\\..\\log4net.snk")]!"/etc/pki/mono/mono.snk")]!' src/AssemblyInfo.cs
sed -i -e 's!|| SSCLI)!|| SSCLI || MONO)!' src/AssemblyInfo.cs

%build
# ASF recommend using nant to build log4net
xbuild /property:Configuration=Debug /property:DefineConstants=DEBUG,MONO,STRONG src/log4net.vs2010.csproj

%install
# install pkgconfig file
cat > %{name}.pc <<EOF
Name: log4net
Description: log4net - .Net logging framework
Version: %{version}
Libs: -r:%{_monodir}/log4net/log4net.dll
EOF

mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
cp %{name}.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
mkdir -p $RPM_BUILD_ROOT/%{_monogacdir}

#gacutil -i bin/mono/*/release/log4net.dll -f -package log4net -root ${RPM_BUILD_ROOT}/%{_prefix}/lib
gacutil -i build/bin/net/*/debug/log4net.dll -f -package log4net -root ${RPM_BUILD_ROOT}/%{_prefix}/lib

%files
%{_monogacdir}/log4net
%{_monodir}/log4net
%doc NOTICE README.txt
%license LICENSE

%files devel
%{_libdir}/pkgconfig/log4net.pc

%changelog
%autochangelog
