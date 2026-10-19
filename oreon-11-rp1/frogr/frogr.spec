%global source0_hash 7507ce92001c6f1faa4e7c57513d9fa14da90051e6c26a14f34aaa9801625df9
Name:           frogr
Version:        1.8.1
Summary:        Flickr Remote Organizer for GNOME
Summary(de):    Flickr-Verwaltung für GNOME
Release:        1%{?dist}
License:        GPL-3.0-only
URL:            https://wiki.gnome.org/Apps/Frogr
Source0:        https://download.gnome.org/sources/%{name}/1.8.1/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
%description
Frogr is a small application for the GNOME desktop that allows users
to manage their accounts in the Flickr image hosting website. It
supports all the basic tasks, including uploading pictures, adding
descriptions, setting tags and managing sets.

%description -l de
Frogr ist eine Anwendung für die GNOME-Arbeitsumgebung zur Verwaltung der
Konten des Flickr-Bilderdienstes. Unterstützt werden sämtliche grundlegende
Aufgaben, wie das Hochladen von Bildern, Hinzufügen von Beschreibungen,
Setzen von Markierungen und Verwalten von Alben.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.frogr.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.frogr.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
