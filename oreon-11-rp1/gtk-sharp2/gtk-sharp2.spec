%global source0_hash 02680578e4535441064aac21d33315daa009d742cab8098ac8b2749d86fffb6a
Name:           gtk-sharp2
Version:        2.12.45
Release:        1%{?dist}
Summary:        GTK+ and GNOME bindings for Mono
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.mono-project.com/GtkSharp
Source0:        http://download.mono-project.com/sources/gtk-sharp212/gtk-sharp-%{version}.tar.gz
Patch0:         gtk-sharp2-2.12.12-glib-include.patch
Patch1:         gtk-sharp2-2.12.12-gtkrange.patch
Patch2: gtk-sharp2-c99.patch
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mono-devel
BuildRequires:  monodoc
BuildRequires:  perl-generators
# /oreon:deps
%description
This package provides a library that allows you to build
fully native graphical GNOME applications using Mono. Gtk#
is a binding to GTK+, the cross platform user interface
toolkit used in GNOME. It includes bindings for Gtk, Atk,
Pango, Gdk. 

%package gapi
Summary:      Glib and GObject C source parser and C generator for the creation and maintenance of managed bindings for Mono and .NET
Requires:     perl-XML-LibXML-Common perl-XML-LibXML perl-XML-SAX
%description gapi
This package provides developer tools for the creation and
maintenance of managed bindings to native libraries which utilize
glib and GObject. Some examples of libraries currently bound using
the GAPI tools and found in Gtk# include Gtk, Atk, Pango, Gdk.

%package devel
Summary:      Files needed for developing with gtk-sharp2
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package provides the necessary development libraries and headers
for writing gtk-sharp2 applications.

%package doc
Summary:      Gtk# documentation
Requires:     %{name} = %{version}-%{release}
Requires:     monodoc
%description doc
This package provides the Gtk# documentation for monodoc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtk-sharp-%{version}
%patch -P0 -p1 -b .glib
%patch -P1 -p1
%patch -P 2 -p1

# Fix permissions of source files
find -name '*.c' -exec chmod a-x {} \;

%build

autoreconf -vif
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
%configure
make
%install
export MONO_SHARED_DIR=%{_builddir}/%{?buildsubdir}
make install DESTDIR=$RPM_BUILD_ROOT
find %{buildroot} -type f -name "*.la" -delete
find %{buildroot} -type f -name "*.a" -delete
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gtk-sharp2-gapi -f %{oreon_filedir}/gtk-sharp2-gapi.list
%files -n gtk-sharp2-devel -f %{oreon_filedir}/gtk-sharp2-devel.list
%files -n gtk-sharp2-doc -f %{oreon_filedir}/gtk-sharp2-doc.list

%changelog

%autochangelog
