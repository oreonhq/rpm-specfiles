%global source0_hash 2b76e6da1506346c54b36ba1a3aeedcd28f4cb7d6a8793d217f209456c92dd4c
%global glib2_version 2.80
%global gtk4_version 4.17.3
%global gtksourceview_version 5.15.0
%global enchant_version 2.2.0
%global libadwaita_version 1.6.0
%global libspelling_version 0.4.0
%global tarball_version %(echo %{version} | tr '~' '.')
Name:		gnome-text-editor
Version:	51.0
Release:        1%{?dist}
Summary:        A simple text editor for the GNOME desktop
License:	GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:		https://gitlab.gnome.org/GNOME/gnome-text-editor
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires:	glib2%{?_isa} >= %{glib2_version}
Requires:	enchant2%{?_isa} >= %{enchant_version}
Requires:	gtk4%{?_isa} >= %{gtk4_version}
Requires:	gtksourceview5%{?_isa} >= %{gtksourceview_version}
Requires:	libadwaita%{?_isa} >= %{libadwaita_version}
Requires:	libspelling%{?_isa} >= %{libspelling_version}
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(editorconfig)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libspelling-1)
# /oreon:deps
%description
GNOME Text Editor is a simple text editor that focuses on session management.
It works hard to keep track of changes and state even if you quit the application.
You can come back to your work even if you've never saved it to a file.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson -Ddevelopment=false
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.TextEditor.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.TextEditor.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.1-1
- Import
