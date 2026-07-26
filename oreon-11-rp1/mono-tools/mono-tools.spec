%global source0_hash 499e4f945d2198858515f625478ca1057cad3150de995f7d82bdb2a85b8ddcaa

%global debug_package %{nil}

Name:    mono-tools
Summary: A collection of tools for mono applications
Version: 4.2
Release: 34%{?dist}
License: MIT
URL:     http://www.mono-project.com/Main_Page
Source0: http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Patch1:  mono-tools-4.2-sharpziplib.patch
Patch2:  mono-tools-4.2-fix-xml-wellformed-comment.patch
Patch3:  mono-tools-4.2-fix-cecil.patch

BuildRequires: make
BuildRequires: desktop-file-utils
BuildRequires: gettext-devel
BuildRequires: gnome-desktop-sharp-devel
BuildRequires: gnome-sharp-devel
BuildRequires: gtk-sharp2-devel
BuildRequires: gtk-sharp2-gapi
BuildRequires: sharpziplib-devel
BuildRequires: hunspell-devel
BuildRequires: libgdiplus-devel
BuildRequires: mono-data
BuildRequires: mono-data-oracle
BuildRequires: mono-devel >= 4.0
BuildRequires: nunit
BuildRequires: nunit-devel
BuildRequires: mono-cecil
BuildRequires: mono-cecil-devel
BuildRequires: monodoc-devel
BuildRequires: mono-web-devel
BuildRequires: pkgconfig
BuildRequires: autoconf automake libtool
Requires: mono-core >= 4.0 links monodoc
Requires: mono-cecil
Requires: sharpziplib

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Monotools are a number of tools for mono such as allowing monodoc to be run
independantly of monodevelop

%package devel
Summary: .pc file for mono-tools
Requires: %{name} = %{version}-%{release} pkgconfig

%description devel
Development file for mono-tools

%package monodoc
Summary: Monodoc documentation
Requires: %{name} = %{version}-%{release} monodoc

%description monodoc
Documentation for monotools for use with monodoc

%package gendarme
Summary: Inspect your .NET and Mono assemblies
Requires: %{name} = %{version}-%{release}

%description gendarme
Inspect your .NET and Mono assemblies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
chmod 644 COPYING

find . -name "Makefile.in" -print -exec sed -i "s#GMCS#MCS#g; s#DMCS#MCS#g" {} \;
find . -name "configure.in" -print -exec sed -i "s#GMCS#MCS#g; s#DMCS#MCS#g" {} \;
sed -i "s#mono-nunit#nunit#g" configure.in
sed -i "s#mono-nunit#nunit#g" gendarme/rules/Test.Rules/Makefile.in

# disable mdoc because it is not built by Mono 6 and mcs anymore
find . -name "Makefile.in" -print -exec sed -i "s~mdoc assemble~mkdir -p doc/generated #mdoc assemble~g" {} \;
find . -name "Makefile.in" -print -exec sed -i "s~mdoc update~mkdir -p doc/generated #mdoc update~g" {} \;
find . -name "Makefile.in" -print -exec sed -i "s~install-framework_documentationDATA: ~install-framework_documentationDATA: \ninstall-framework_documentationDATADisabled: ~g" {} \;
find . -name "Makefile.in" -print -exec sed -i "s~install-rules_documentationDATA: ~install-rules_documentationDATA: \ninstall-rules_documentationDATADisabled: ~g" {} \;

%build
# need to run autoconf >= 2.69 to support aarch64
autoconf
%configure --libdir=%{_prefix}/lib --disable-docs
make V=1
# no smp flags - breaks the build

%install
make DESTDIR=%{buildroot} install

desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
        --vendor fedora \
%endif
        --dir %{buildroot}%{_datadir}/applications \
        --add-category Development \
        --delete-original \
        %{buildroot}%{_datadir}/applications/monodoc.desktop

mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%find_lang %{name}

%files -f %{name}.lang
%doc COPYING AUTHORS ChangeLog README
%{_bindir}/create-native-map
%{_bindir}/gasnview
%{_bindir}/monodoc
%{_bindir}/mprof*
%{_bindir}/gsharp
%{_bindir}/gd2i
%{_bindir}/mperfmon
%{_bindir}/gui-compare
%{_bindir}/emveepee
%{_bindir}/minvoke
%{_prefix}/lib/gsharp/gsharp.exe*
%{_prefix}/lib/create-native-map
%{_prefix}/lib/mperfmon/*
%dir %{_prefix}/lib/gui-compare
%{_prefix}/lib/gui-compare/gui-compare.exe*
%{_prefix}/lib/mono/1.0/gasnview.exe
%{_prefix}/lib/monodoc/browser.exe
%{_prefix}/lib/minvoke/minvoke.exe
%dir %{_prefix}/lib/minvoke
%dir %{_prefix}/lib/mono-tools
%{_prefix}/lib/mono-tools/mprof*
%{_prefix}/lib/mono-tools/Mono.Profiler.Widgets*
%{_prefix}/lib/mono-tools/emveepee.exe*
%{_mandir}/man1/mprof*
%{_mandir}/man1/create-native-map.1.gz
%{_datadir}/pixmaps/monodoc.png
%{_datadir}/applications/gsharp.desktop
%{_datadir}/applications/monodoc.desktop
%{_prefix}/lib/monodoc/MonoWebBrowserHtmlRender.dll
%{_mandir}/man1/mperfmon*
%{_mandir}/man1/gd2i*
%{_datadir}/icons/hicolor/

%files gendarme
%{_bindir}/gendarme*
%{_datadir}/applications/gendarme-wizard.desktop
%{_datadir}/pixmaps/gendarme.svg
%{_mandir}/man1/gendarme*
%{_prefix}/lib/gendarme/*.dll
%{_prefix}/lib/gendarme/*.exe
%{_prefix}/lib/gendarme/*.xml

%files devel
%{_libdir}/pkgconfig/*.pc

%files monodoc
%dir %{_prefix}/lib/monodoc/web
%{_prefix}/lib/monodoc/web/*
%{_mandir}/man5/gendarme*

%changelog
%autochangelog
