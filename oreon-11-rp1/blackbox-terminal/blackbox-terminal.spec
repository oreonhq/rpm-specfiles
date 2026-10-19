%global source0_hash 6fda451b52ac133b78ee629211c8816dd47ee40e66b814d0c55cd0e044327fb7
%global rdnn    com.raggesilver.BlackBox
%global commit      bb1ce17d374bb339eca2c0200744012feef44c53
%global shortcommit %{sub %{commit} 1 7}
Name:           blackbox-terminal
Version:        0.15.0~^2.%{shortcommit}
Release:        1%{?dist}
Summary:        Elegant and customizable terminal for GNOME
License:        GPL-3.0-or-later AND (MIT OR Apache-2.0) AND MPL-2.0
URL:            https://gitlab.gnome.org/raggesilver/blackbox
Source0:        https://gitlab.gnome.org/raggesilver/blackbox/-/archive/%{commit}/blackbox-bb1ce17.tar.gz
Patch:          0001-Rename-executable-to-blackbox-terminal.patch
Patch:          0002-Remove-duplicate-icons.patch
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pqmarble)
BuildRequires:  pkgconfig(vte-2.91-gtk4)
BuildRequires:  vala
# /oreon:deps
%description
Black Box is an elegant and customizable terminal for GNOME.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n blackbox-%{commit}

%build

%meson -Dblackbox_is_flatpak=%{?flatpak:true}%{!?flatpak:false}
%meson_build
%install
%meson_install
%find_lang blackbox
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
