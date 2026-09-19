%global source0_hash 03ec235b3364abfd54c12acc67c6fdb93ce40fff4f29df48dc156960f3fd789d

%global forgeurl https://github.com/GLibSharp/GtkSharp
%global tag 3.22.2

%forgemeta

%if 0%{?rhel}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%global _monodir %{_prefix}/lib/mono
%global _monogacdir %{_monodir}/gac
%endif

%global debug_package %{nil}
%global _docdir_fmt %{name}

Summary:        GTK+ 3 and GNOME 3 bindings for Mono
Name:           gtk-sharp3
Version:        3.22.2
Release:        13%{?dist}
# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2

BuildRequires:  meson
BuildRequires:  mono-devel gtk3-devel libglade2-devel monodoc
BuildRequires:  automake, libtool
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  perl-generators
Patch0:         gtk-sharp3-2.99.3-gui-thread-check.patch
Patch1:         gtk-sharp3-2.99.3-gtkrange.patch
Patch2:         gtk-sharp3-3.22.2-nolibdir.patch
Patch3:         gtk-sharp3-3.22.2-add-cairo-sharp-dll-config.patch

URL:            %forgeurl
Source:         %forgesource

# Mono only available on these:
ExclusiveArch:  %{mono_arches}

%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to version 3 of GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk.

%package gapi
Summary:        Tools for creation and maintenance managed bindings for Mono and .NET

%description gapi
This package provides developer tools for the creation and
maintenance of managed bindings to native libraries which utilize
glib and GObject. Some examples of libraries currently bound using
the GAPI tools and found in Gtk# include Gtk, Atk, Pango, Gdk.

%package devel
Summary:        Files needed for developing with gtk-sharp3
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description devel
This package provides the necessary development libraries and headers
for writing gtk-sharp3 applications.

%package doc
Summary:        Gtk# 3 documentation
Requires:       monodoc
BuildArch:      noarch

%description doc
This package provides the Gtk# 3 documentation for monodoc.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

#fix missing gdk_api_includes references
sed -i "s/gdk_api_includes/gio_api_includes/" Source/gdk/generated/meson.build
sed -i "s/gdk_api_includes/gio_api_includes/" Source/gio/generated/meson.build
sed -i "s/gdk_api_includes/gio_api_includes/" Source/gtk/generated/meson.build
sed -i "s/gdk_api_includes/gio_api_includes/" Source/sample/valtest/generated/meson.build

%build
%meson -Dinstall=true
%meson_build

%install
%meson_install

%ldconfig_scriptlets

# see https://bugzilla.redhat.com/show_bug.cgi?id=2155849
cp redhat-linux-build/Source/gtk/gtk-sharp.dll.config %{buildroot}/%{_monodir}/GtkSharp-3.0

%files
%doc README.md
%license LICENSE
%{_monogacdir}/*
%{_monodir}/GtkSharp-3.0
%{_monodir}/atk-sharp
%{_monodir}/cairo-sharp
%{_monodir}/gdk-sharp
%{_monodir}/gtk-sharp
%{_monodir}/gio-sharp
%{_monodir}/glib-sharp
%{_monodir}/pango-sharp

%files gapi
%{_bindir}/gapi3-codegen
%{_bindir}/gapi3-fixup
%{_bindir}/gapi3-parser
%dir %{_prefix}/lib/gapi-3.0
%{_prefix}/lib/gapi-3.0/gapi_codegen.exe
%{_prefix}/lib/gapi-3.0/gapi-fixup.exe
%{_prefix}/lib/gapi-3.0/gapi-parser.exe
%{_prefix}/lib/gapi-3.0/gapi_pp.pl
%{_prefix}/lib/gapi-3.0/gapi2xml.pl
%{_datadir}/gapi-3.0
%{_libdir}/pkgconfig/gapi-3.0.pc

%files devel
%{_libdir}/pkgconfig/*-sharp-3.0.pc

%files doc
#{_prefix}/lib/monodoc/sources/*

%changelog
%autochangelog
