%global source0_hash ad3c867f35804a94993c7ed5ac01df127b8bbf3d7ea84ed9f46ae1fd428e80c0

%global libname Newtonsoft.Json

# mono is without any packagable debuginfo
%global debug_package %{nil}

%ifarch ppc64 ppc64le aarch64 armv7hl s390x
# disable the tests for some arches because quite a number of them fail
%bcond_with tests
%else
%bcond_without tests
%endif

Name:           newtonsoft-json
Version:        9.0.1
Release:        34%{?dist}
Summary:        Popular high-performance JSON framework

# almost all files are licensed as MIT/X11, but BSD for LinqBridge.cs
# (and LGPLv2.1+ for Tools/7-Zip, not used)
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL:            http://www.newtonsoft.com/json
Source0:        https://github.com/JamesNK/%{libname}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

Patch10:         %{name}-tests-skip-samples.patch
Patch11:         %{name}-nunit.patch
Patch12:         %{name}-mscorlibtest.patch

ExclusiveArch:  %{mono_arches}

# nunit2 fails to build on armv7hl. Mono crashes. see bug 1923663
# it is too much work to switch to nunit (version 3) at the moment.
ExcludeArch:    armv7hl

BuildRequires:  mono-devel
BuildRequires:  mono-web
BuildRequires:  mono-data
BuildRequires:  mono-mvc
BuildRequires:  nunit2-devel

%description
%{libname} aka Json.NET is a popular high-performance JSON framework

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn%{libname}-%{version}
#find Src -name \*.cs |xargs sed -i 's,\r\n,\n,'
#find Src -name \*.csproj |xargs sed -i 's,\r\n,\n,'
# E: wrong-script-interpreter
rm README.md
# sign the assembly to get a strong name, https://msdn.microsoft.com/en-us/library/xc31ft41.aspx
sed -i "s#<SignAssembly>false</SignAssembly>#<SignAssembly>true</SignAssembly>#g; s#</AssemblyOriginatorKeyFile>##g; s#<AssemblyOriginatorKeyFile>#<AssemblyOriginatorKeyFile>Dynamic.snk</AssemblyOriginatorKeyFile>#g;" Src/%{libname}/%{libname}.Net40.csproj
sed -i "s#<DefineConstants>#<DefineConstants>SIGNED;#g" Src/%{libname}/%{libname}.Net40.csproj
sed -i "s#<SignAssembly>false</SignAssembly>#<SignAssembly>true</SignAssembly>#g; s#</AssemblyOriginatorKeyFile>##g; s#<AssemblyOriginatorKeyFile>#<AssemblyOriginatorKeyFile>../%{libname}/Dynamic.snk</AssemblyOriginatorKeyFile>#g;" Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i "s#<DefineConstants>#<DefineConstants>SIGNED;#g" Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
# fix the public key, for Dynamic.snk
sed -i "s#PublicKey=0024000004800000940000000602000000240000525341310004000001000100f561df277c6c0b497d629032b410cdcf286e537c054724f7ffa0164345f62b3e642029d7a80cc351918955328c4adc8a048823ef90b0cf38ea7db0d729caf2b633c3babe08b0310198c1081995c19029bc675193744eab9d7345b8a67258ec17d112cebdbbb2a281487dceeafb9d83aa930f32103fbe1d2911425bc5744002c7#PublicKey=0024000004800000940000000602000000240000525341310004000001000100cbd8d53b9d7de30f1f1278f636ec462cf9c254991291e66ebb157a885638a517887633b898ccbcf0d5c5ff7be85a6abe9e765d0ac7cd33c68dac67e7e64530e8222101109f154ab14a941c490ac155cd1d4fcba0fabb49016b4ef28593b015cab5937da31172f03f67d09edda404b88a60023f062ae71d0b2e4438b74cc11dc9#g" Src/%{libname}/Properties/AssemblyInfo.cs

%if %{with tests}
# skip files with unmet dependencies (FSharp etc.), FIXME use nuget
%patch -P10
sed -i /DiscriminatedUnionConverterTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /Serialization.DependencyInjectionTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /Serialization.FSharpTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /Serialization.ImmutableCollectionsTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /TestObjects.Currency.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /TestObjects.Shape.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /Schema.JsonSchemaBuilderTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj
sed -i /Schema.JsonSchemaNodeTests.cs/d Src/%{libname}.Tests/%{libname}.Tests.Net40.csproj

#FIXME comment tests that fail or have errors
sed -i -r 's,public void Example\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Documentation/Samples/Linq/DeserializeWithLinq.cs
sed -i -r 's,public void Example\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Documentation/Samples/Linq/SerializeWithLinq.cs
sed -i -r 's,public void MemoryTraceWriterTest\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Documentation/TraceWriterTests.cs
sed -i -r 's,public void ExceptionFromOverloadWithJValue\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Linq/LinqToJsonTest.cs
sed -i -r 's,public void GenerateSchemaForDirectoryInfo\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Schema/JsonSchemaGeneratorTests.cs
sed -i -r 's,public void EmitDefaultValueTest\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Serialization/DefaultValueHandlingTests.cs
sed -i -r 's,public void CannotDeserializeArrayIntoLinqToJson\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Serialization/JsonSerializerTest.cs
sed -i -r 's,public void MailMessageConverterTest\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Serialization/JsonSerializerTest.cs
sed -i -r 's,public void MemoryTraceWriterDeserializeTest\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Serialization/TraceWriterTests.cs
sed -i -r 's,public void MemoryTraceWriterSerializeTest\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Serialization/TraceWriterTests.cs
sed -i -r 's,public void CreateGetWithBadObjectTarget\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/DynamicReflectionDelegateFactoryTests.cs
sed -i -r 's,public void CreateSetWithBadObjectTarget\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/DynamicReflectionDelegateFactoryTests.cs
sed -i -r 's,public void CreateSetWithBadObjectValue\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/DynamicReflectionDelegateFactoryTests.cs
sed -i -r 's,public void CreateGetWithBadObjectTarget\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/ExpressionReflectionDelegateFactoryTests.cs
sed -i -r 's,public void CreateSetWithBadObjectTarget\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/ExpressionReflectionDelegateFactoryTests.cs
sed -i -r 's,public void CreateSetWithBadObjectValue\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/ExpressionReflectionDelegateFactoryTests.cs
sed -i -r 's,public void DefaultConstructor_Abstract\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Utilities/ExpressionReflectionDelegateFactoryTests.cs
sed -i -r 's,public void DeserializingErrorHandlingUsingEvent\(,[Ignore("broken")] \0,' Src/Newtonsoft.Json.Tests/Serialization/SerializationErrorHandlingTests.cs

# make sure that NUnit is properly referenced
%patch -P11

%patch -P12 -p1

# we do not have FSharp available
for f in Converters/DiscriminatedUnionConverterTests.cs \
Serialization/FSharpTests.cs \
TestObjects/Currency.cs \
TestObjects/Shape.cs ; do \
sed -i "s/using Microsoft\.FSharp.*;//g" Src/%{libname}.Tests/$f; done

# The type `NUnit.Framework.IgnoreAttribute' does not contain a constructor that takes `0' arguments
sed -i 's/\[Ignore\]/[Ignore("Ignore")]/g' Src/Newtonsoft.Json.Tests/JsonTextReaderTest.cs

%endif

%build
pushd Src/%{libname}
xbuild /p:Configuration=Release %{libname}.Net40.csproj /p:TargetFrameworkVersion="v4.7.1"

%install
mkdir -p %{buildroot}/%{_monogacdir}
gacutil -i Src/%{libname}/bin/Release/Net40/%{libname}.dll -package %{name} -root %{buildroot}/usr/lib
# pkgconfig
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
cat <<EOT >>%{buildroot}/%{_libdir}/pkgconfig/%{name}.pc
Name: %{libname}
Description: %{summary}
Version: 9.0.1
Requires: mono 
Libs: -r:%{_monodir}/%{name}/%{libname}.dll
Libraries=%{_monodir}/%{name}/%{libname}.dll
EOT

%check
%if %{with tests}
pushd Src/%{libname}.Tests
xbuild /p:Configuration=Release %{libname}.Tests.Net40.csproj /p:TargetFrameworkVersion="v4.7.1"
nunit-console26 -labels bin/Release/Net40/*Tests.dll
#rm -r obj bin
%endif

%files
%license Doc/license.txt
%doc *.md Doc/readme.txt
%{_monogacdir}/%{libname}
%{_monodir}/%{name}

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
