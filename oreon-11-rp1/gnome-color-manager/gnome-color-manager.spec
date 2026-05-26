# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3904d42abb4ea566df0b880e82bf0b9f86386c692f15b318469a4c7be33a887f
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:      gnome-color-manager
Version:   3.36.2
Release:   3%{?dist}
Summary:   Color management tools for GNOME
License:   GPL-2.0-or-later
URL:       https://gitlab.gnome.org/GNOME/gnome-color-manager
Source0:   http://download.gnome.org/sources/gnome-color-manager/3.36/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gtk3-devel >= 3.0.0
BuildRequires: gettext
BuildRequires: lcms2-devel
BuildRequires: glib2-devel >= 2.25.9-2
BuildRequires: docbook-utils
BuildRequires: colord-devel >= 0.1.12
BuildRequires: itstool
BuildRequires: meson

Requires: shared-mime-info

# obsolete sub-package
Obsoletes: gnome-color-manager-devel <= 3.1.1
Provides: gnome-color-manager-devel

%description
gnome-color-manager is a session framework that makes it easy to manage, install
and generate color profiles in the GNOME desktop.

%prep
%oreon_verify_sources
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --with-gnome

%files -f %{name}.lang
%license COPYING
%doc AUTHORS README
%{_bindir}/gcm-*
%{_datadir}/applications/gcm-*.desktop
%{_datadir}/applications/org.gnome.ColorProfileViewer.desktop
%dir %{_datadir}/gnome-color-manager
%dir %{_datadir}/gnome-color-manager/figures
%{_datadir}/gnome-color-manager/figures/*
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/scalable/*/*.svg*
%{_datadir}/metainfo/org.gnome.ColorProfileViewer.appdata.xml
%{_mandir}/man1/*.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.36.2-3
- Prepare for Oreon 11 (RP1)
