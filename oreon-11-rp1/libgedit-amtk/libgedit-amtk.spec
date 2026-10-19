%global source0_hash 7ee3d0cce3b21f3cc6a51ba644901b467da3b3c3e0b0adf74bd56c9e0e456140
Name:           libgedit-amtk
Version:        5.10.0
Release:        1%{?dist}
Summary:        Gedit Technology - Actions, Menus and Toolbars Kit
License:        LGPL-3.0-or-later
URL:            https://gedit-text-editor.org/
Source0:        https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Obsoletes:      amtk < 5.8.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
Amtk is the acronym for “Actions, Menus and Toolbars Kit”. It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      amtk-devel < 5.8.0
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%find_lang %{name}-5
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libgedit-amtk-devel -f %{oreon_filedir}/libgedit-amtk-devel.list

%changelog

%autochangelog

