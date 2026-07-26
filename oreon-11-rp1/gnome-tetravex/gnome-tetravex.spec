%global source0_hash 83849ac064d456e1dd46b6e201c686152624c3d1ec4b99935985a49aa79172cb

Name:           gnome-tetravex
Version:        3.38.3
Release:        2%{?dist}
Summary:        GNOME Tetravex game

# Automatically converted from old format: GPLv2+ and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://wiki.gnome.org/Apps/Tetravex
Source0:        https://download.gnome.org/sources/%{name}/3.38/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  vala

%description
A puzzle game where you have to match a grid of tiles together. The skill
level ranges from the simple two by two up to the seriously mind-bending six
by six grid.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Tetravex.desktop

%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-tetravex
%{_datadir}/applications/org.gnome.Tetravex.desktop
%{_datadir}/dbus-1/services/org.gnome.Tetravex.service
%{_datadir}/glib-2.0/schemas/org.gnome.Tetravex.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.Tetravex.*
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Tetravex-symbolic.svg
%{_datadir}/metainfo/org.gnome.Tetravex.appdata.xml
%{_mandir}/man6/gnome-tetravex.6*

%changelog
%autochangelog
