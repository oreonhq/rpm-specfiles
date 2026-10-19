%global source0_hash 03ec235b3364abfd54c12acc67c6fdb93ce40fff4f29df48dc156960f3fd789d
%global forgeurl https://github.com/GLibSharp/GtkSharp
%global tag 3.22.2
%forgemeta
%global debug_package %{nil}
%global _docdir_fmt %{name}
Summary:        GTK+ 3 and GNOME 3 bindings for Mono
Name:           gtk-sharp3
Version:        3.22.2
Release:        13%{?dist}
License:        LicenseRef-Callaway-LGPLv2
Patch0:         gtk-sharp3-2.99.3-gui-thread-check.patch
Patch1:         gtk-sharp3-2.99.3-gtkrange.patch
Patch2:         gtk-sharp3-3.22.2-nolibdir.patch
Patch3:         gtk-sharp3-3.22.2-add-cairo-sharp-dll-config.patch
URL:            %forgeurl
Source0:        %{forgeurl}/archive/%{version}/GtkSharp-%{version}.tar.gz
ExclusiveArch:  %{mono_arches}
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  libglade2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  mono-devel
BuildRequires:  monodoc
BuildRequires:  perl-generators
# /oreon:deps
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
cp redhat-linux-build/Source/gtk/gtk-sharp.dll.config %{buildroot}/%{_monodir}/GtkSharp-3.0
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtk-sharp3-gapi -f %{oreon_filedir}/gtk-sharp3-gapi.list
%files -n gtk-sharp3-devel -f %{oreon_filedir}/gtk-sharp3-devel.list
%files -n gtk-sharp3-doc -f %{oreon_filedir}/gtk-sharp3-doc.list

%changelog

%autochangelog
