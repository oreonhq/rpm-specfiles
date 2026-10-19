%global source0_hash 2b695f41475573aa59f1cd004b5cc3d2021d0444decf26eb8d38864348fb3577
%global apiver 6
Name:           libgedit-tepl
Version:        6.14.0
Release:        1%{?dist}
Summary:        Text editor product line library
License:        LGPL-3.0-or-later
URL:            https://gedit-text-editor.org/
Source0:        https://gitlab.gnome.org/World/gedit/%{name}/-/archive/%{version}/%{name}-%{version}.tar.bz2
Obsoletes:      tepl < 6.10.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk-doc
BuildRequires:  mesa-libEGL
BuildRequires:  meson
BuildRequires:  mutter
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libgedit-amtk-5)
BuildRequires:  pkgconfig(libgedit-gfls-1)
BuildRequires:  pkgconfig(libgedit-gtksourceview-300)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  xwayland-run
# /oreon:deps
%description
Tepl is a library that eases the development of GtkSourceView-based text
editors and IDEs. Tepl is the acronym for “Text editor product line”.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      tepl-devel < 6.10.0
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
%find_lang %{name}-%{apiver}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%{shrink:xwfb-run -c mutter -- %meson_test}
%files -f %{oreon_filedir}/main.list
%files -n libgedit-tepl-devel -f %{oreon_filedir}/libgedit-tepl-devel.list

%changelog

%autochangelog

