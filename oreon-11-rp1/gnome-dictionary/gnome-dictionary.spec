%global source0_hash 2e650c2a4cea8cc4d02d4a583c456cbbc9d1871e918c7dc4de081ded1d830db5

Name:           gnome-dictionary
Version:        40.0
Release:        14%{?dist}
Summary:        A dictionary application for GNOME

# Automatically converted from old format: GPLv3+ and LGPLv2+ and GFDL - review is highly recommended.
License:        GPL-3.0-or-later AND LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-GFDL
URL:            https://wiki.gnome.org/Apps/Dictionary
Source0:        https://download.gnome.org/sources/%{name}/40/%{name}-%{version}.tar.xz

# Fix the build with meson 0.61
# https://gitlab.gnome.org/GNOME/gnome-dictionary/-/merge_requests/18
Patch0:         meson-0.61.patch

BuildRequires:  desktop-file-utils
BuildRequires:  docbook-style-xsl
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/xsltproc

%description
gnome-dictionary lets you look up words in dictionary sources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%doc NEWS README.md
%license COPYING COPYING.docs COPYING.libs
%{_bindir}/gnome-dictionary
%{_datadir}/applications/org.gnome.Dictionary.desktop
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%{_datadir}/gdict-1.0/
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Dictionary.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Dictionary.Devel.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Dictionary-symbolic.svg
%{_datadir}/metainfo/org.gnome.Dictionary.appdata.xml
%{_mandir}/man1/gnome-dictionary.1*

%changelog
%autochangelog
