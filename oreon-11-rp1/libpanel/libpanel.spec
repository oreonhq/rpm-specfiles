%global source0_hash 593888a7691f0af8aaa6e193c9e14afa86a810c0c2f27515c6d813f18733b1cd
%global tarball_version %{version}
Name:           libpanel
Version:        1.10.4
Release:        1%{?dist}
Summary:        IDE paneling library for GTK
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libpanel
Source0:        https://download.gnome.org/sources/%{name}/1.10/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
# /oreon:deps
%description
libpanel is a collection of GTK widgets for IDE-like applications targeting
GNOME using GTK and libadwaita.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Recommends:     gi-docgen-fonts
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n libpanel-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang libpanel
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libpanel-devel -f %{oreon_filedir}/libpanel-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10.4-1
- Import
