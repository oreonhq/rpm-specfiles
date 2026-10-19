%global source0_hash 499e4f945d2198858515f625478ca1057cad3150de995f7d82bdb2a85b8ddcaa
%global debug_package %{nil}
Name:    mono-tools
Summary:        A collection of tools for mono applications
Version: 4.2
Release:        34%{?dist}
License: MIT
URL:     http://www.mono-project.com/Main_Page
Source0:        http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.gz
Patch1:  mono-tools-4.2-sharpziplib.patch
Patch2:  mono-tools-4.2-fix-xml-wellformed-comment.patch
Patch3:  mono-tools-4.2-fix-cecil.patch
Requires: mono-core >= 4.0 links monodoc
Requires: mono-cecil
Requires: sharpziplib
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  gnome-desktop-sharp-devel
BuildRequires:  gnome-sharp-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  hunspell-devel
BuildRequires:  libgdiplus-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-cecil
BuildRequires:  mono-cecil-devel
BuildRequires:  mono-data
BuildRequires:  mono-data-oracle
BuildRequires:  mono-devel
BuildRequires:  mono-web-devel
BuildRequires:  monodoc-devel
BuildRequires:  nunit
BuildRequires:  nunit-devel
BuildRequires:  pkgconfig
BuildRequires:  sharpziplib-devel
# /oreon:deps
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

autoconf
%configure --libdir=%{_prefix}/lib --disable-docs
make V=1
%install
make DESTDIR=%{buildroot} install
desktop-file-install \
        --dir %{buildroot}%{_datadir}/applications \
        --add-category Development \
        --delete-original \
        %{buildroot}%{_datadir}/applications/monodoc.desktop
mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/
%find_lang %{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mono-tools-devel -f %{oreon_filedir}/mono-tools-devel.list
%files -n mono-tools-monodoc -f %{oreon_filedir}/mono-tools-monodoc.list
%files -n mono-tools-gendarme -f %{oreon_filedir}/mono-tools-gendarme.list

%changelog

%autochangelog
