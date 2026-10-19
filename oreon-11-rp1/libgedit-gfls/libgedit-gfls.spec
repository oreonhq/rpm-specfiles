%global source0_hash 9c6c6469a70d829b4476debe4b8b135daaa60164a6657db1fa803f28625aee2b
Name:           libgedit-gfls
Version:        0.4.2
Release:        1%{?dist}
Summary:        Gedit Technology File Loading and Saving library
License:        LGPL-3.0-or-later
URL:            https://gedit-text-editor.org/
Source0:        https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
libgedit-gfls is part of Gedit Technology. It is a module dedicated to file
loading and saving for the needs of gedit and other similar text editors.

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

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%find_lang %{name}-1
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libgedit-gfls-devel -f %{oreon_filedir}/libgedit-gfls-devel.list

%changelog

%autochangelog
