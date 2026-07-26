%global source0_hash c8f6bcd2116551f2c5776f8c0c6dc83e17ae6f1eb5b564e0bfd97b5d65bd7e0e

%global debug_package %{nil}

Name:           nunit
Version:        3.7.1
Release:        23%{?dist}
Summary:        Unit test framework for CLI
# Automatically converted from old format: MIT with advertising - review is highly recommended.
License:        LicenseRef-Callaway-MIT-with-advertising
Url:            http://www.nunit.org/
Source0:        https://github.com/nunit/nunit/archive/%{version}.tar.gz
Source1:        nunit.pc
Source2:        nunitlite-runner.sh
BuildRequires:  mono-devel
ExclusiveArch:  %{mono_arches}
Provides:       mono-nunit = 4.0.2-5
Obsoletes:      mono-nunit < 4.0.2-6
Obsoletes:      nunit-runner <= 2.6.4-10

%description
NUnit is a unit testing framework for all .NET languages. It serves the
same purpose as JUnit does in the Java world. It supports test
categories, testing for exceptions and writing test results in plain
text or XML.

NUnit targets the CLI (Common Language Infrastructure) and supports Mono and
the Microsoft .NET Framework.

%package        devel
Summary:        Development files for NUnit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Provides:       mono-nunit-devel = 4.0.2-5
Obsoletes:      mono-nunit-devel < 4.0.2-6

%description devel
Development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn nunit-%{version}

%build

# Remove prebuilt binaries
find . -name "*.dll" -print -delete

%{?exp_env}
%{?env_options}

xbuild /property:Configuration=Release src/NUnitFramework/framework/nunit.framework-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/nunitlite/nunitlite-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/nunitlite-runner/nunitlite-runner-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/mock-assembly/mock-assembly-4.5.csproj

xbuild /property:Configuration=Release src/NUnitFramework/slow-tests/slow-nunit-tests-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/testdata/nunit.testdata-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/tests/nunit.framework.tests-4.5.csproj
xbuild /property:Configuration=Release src/NUnitFramework/nunitlite.tests/nunitlite.tests-4.5.csproj

%install
%{?env_options}
%{__mkdir_p} %{buildroot}%{_monodir}/nunit
%{__mkdir_p} %{buildroot}%{_libdir}/pkgconfig
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__mkdir_p} %{buildroot}%{_datadir}/icons/NUnit
%{__install} -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig/
%{__install} -m0755 %{SOURCE2} %{buildroot}%{_bindir}/nunitlite-runner
%{__install} -m0644 src/NUnitFramework/nunitlite-runner/App.config %{buildroot}%{_monodir}/nunit/nunitlite-runner.exe.config
find %{_builddir}/%{?buildsubdir}/bin -name \*.dll -exec %{__install} \-m0755 "{}" "%{buildroot}%{_monodir}/nunit/" \;
find %{_builddir}/%{?buildsubdir}/bin -name \*.exe -exec %{__install} \-m0755 "{}" "%{buildroot}%{_monodir}/nunit/" \;
for i in nunit.framework.dll nunit.framework.tests.dll nunitlite.dll nunit.testdata.dll; do
    gacutil -i %{buildroot}%{_monodir}/nunit/$i -package nunit -root %{buildroot}%{_monodir}/../
done

%files
%license LICENSE.txt
%{_bindir}/nunitlite-runner
%{_monogacdir}/nunit*
%{_monodir}/nunit/

%files devel
%{_libdir}/pkgconfig/nunit.pc

%changelog
%autochangelog
