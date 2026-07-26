%global source0_hash none

%global debug_package %{nil}

Name:           nunit2
Version:        2.6.4
Release:        39%{?dist}
Summary:        Unit test framework for CLI
# Automatically converted from old format: MIT with advertising - review is highly recommended.
License:        LicenseRef-Callaway-MIT-with-advertising
Url:            http://www.nunit.org/
Source0:        https://github.com/nunit/nunitv2/archive/%{version}.tar.gz
Source1:        nunit2.pc
Source2:        nunit2-gui.sh
Source3:        nunit2-console.sh
Source4:        nunit2.desktop
BuildRequires:  mono-devel libgdiplus-devel desktop-file-utils mono-winforms
ExclusiveArch:  %{mono_arches}

# nunit2 fails to build on armv7hl. Mono crashes.
# https://bugzilla.redhat.com/show_bug.cgi?id=1923663
ExcludeArch:    armv7hl

%description
NUnit is a unit testing framework for all .NET languages. It serves the
same purpose as JUnit does in the Java world. It supports test
categories, testing for exceptions and writing test results in plain
text or XML.

NUnit targets the CLI (Common Language Infrastructure) and supports Mono and
the Microsoft .NET Framework.

%package gui
Summary:        Tools for run NUnit test
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       mono-winforms

%description gui
Desktop application for run NUnit test

%package doc
Summary:        Documentation package for NUnit
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description doc
Documentation for NUnit

%package        devel
Summary:        Development files for NUnit
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Development files for %{name}.

%prep
%setup -qn nunitv2-%{version}

%build

# fix compile with Mono4
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;

%{?exp_env}
%{?env_options}
xbuild /property:Configuration=Debug ./src/NUnitCore/core/nunit.core.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitCore/interfaces/nunit.core.interfaces.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitFramework/framework/nunit.framework.dll.csproj
xbuild /property:Configuration=Debug ./src/NUnitMocks/mocks/nunit.mocks.csproj
xbuild /property:Configuration=Debug ./src/ClientUtilities/util/nunit.util.dll.csproj
xbuild /property:Configuration=Debug ./src/ConsoleRunner/nunit-console/nunit-console.csproj
xbuild /property:Configuration=Debug ./src/ConsoleRunner/nunit-console-exe/nunit-console.exe.csproj
xbuild /property:Configuration=Debug ./src/GuiRunner/nunit-gui/nunit-gui.csproj
xbuild /property:Configuration=Debug ./src/GuiComponents/UiKit/nunit.uikit.dll.csproj
xbuild /property:Configuration=Debug ./src/GuiException/UiException/nunit.uiexception.dll.csproj
xbuild /property:Configuration=Debug ./src/GuiRunner/nunit-gui-exe/nunit-gui.exe.csproj

%install
%{?env_options}
mkdir -p %{buildroot}%{_monodir}/nunit2
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/NUnit2
install -p -m0644 %{SOURCE1} %{buildroot}%{_libdir}/pkgconfig
install -p -m0755 %{SOURCE2} %{buildroot}%{_bindir}/nunit-gui26
install -p -m0755 %{SOURCE3} %{buildroot}%{_bindir}/nunit-console26
install -p -m0644 src/ConsoleRunner/nunit-console-exe/App.config %{buildroot}%{_monodir}/nunit2/nunit-console.exe.config
install -p -m0644 src/GuiRunner/nunit-gui-exe/App.config %{buildroot}%{_monodir}/nunit2/nunit.exe.config
find %{_builddir}/%{?buildsubdir}/bin -name \*.dll -exec install \-p \-m0755 "{}" "%{buildroot}%{_monodir}/nunit2/" \;
find %{_builddir}/%{?buildsubdir}/bin -name \*.exe -exec install \-p \-m0755 "{}" "%{buildroot}%{_monodir}/nunit2/" \;
for i in nunit-console-runner.dll nunit.core.dll nunit.core.interfaces.dll nunit.framework.dll nunit.mocks.dll nunit.util.dll ; do
    gacutil -i %{buildroot}%{_monodir}/nunit2/$i -package nunit2 -root %{buildroot}%{_monodir}/../
done
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE4}
cp -p src/GuiRunner/nunit-gui-exe/App.ico %{buildroot}/%{_datadir}/icons/NUnit2/nunit.ico

%files
%license license.txt
%{_bindir}/nunit-console*
%dir %{_monodir}/nunit2
%{_monodir}/nunit2/nunit-console.exe*
%{_monogacdir}/nunit*
%{_monodir}/nunit2/*.dll

%files gui
%{_bindir}/nunit-gui*
%{_monodir}/nunit2/nunit.exe*
%{_datadir}/applications/nunit2.desktop
%{_datadir}/icons/NUnit2

%files doc
%license doc/license.html
%doc doc/*

%files devel
%{_libdir}/pkgconfig/nunit2.pc

%post gui
/bin/touch --no-create %{_datadir}/icons/NUnit &>/dev/null || :

%postun gui
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/NUnit &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/NUnit &>/dev/null || :
fi

%posttrans gui
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/NUnit &>/dev/null || :

%changelog
%autochangelog
