%global source0_hash 4fbf466189d38f709bc1e69d85518027a4623cb697368718a94932caede75f58
%global api_version 300
Name:           libgedit-gtksourceview
Version:        299.7.1
Release:        1%{?dist}
Summary:        Gedit Technology - Source code editing widget
License:        LGPL-2.1-or-later
URL:            https://gedit-text-editor.org/
Source0:        https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Patch:          rpmspec.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libgedit-gfls-1)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
libgedit-gtksourceview is a library that extends GtkTextView, the standard GTK
widget for multiline text editing. This library adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features typical
of a source code editor.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang libgedit-gtksourceview-%{api_version}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libgedit-gtksourceview-devel -f %{oreon_filedir}/libgedit-gtksourceview-devel.list

%changelog

%autochangelog

