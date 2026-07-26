%global source0_hash 6db6db9a3b1b52fd0ab54f9a5bf4f299cb71e52a13ac5fdfc3e74eb46985a4e6

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-sound-recorder
Version:        43~beta
Release:        12%{?dist}
Summary:        Make simple recordings from your desktop

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Design/Apps/SoundRecorder
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  /usr/bin/appstream-util
BuildRequires:  desktop-file-utils
BuildRequires:  gstreamer1-plugins-bad-free
BuildRequires:  gstreamer1-plugins-base
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  meson
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

# Version requirement is for the first release with package.js.
Requires:       gjs >= 1.41.4
Requires:       gstreamer1
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gtk4
Requires:       libadwaita

%description
Make simple recordings from your desktop.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install
%find_lang org.gnome.SoundRecorder

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.SoundRecorder.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.SoundRecorder.desktop

%files -f org.gnome.SoundRecorder.lang
%doc AUTHORS README.md NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.SoundRecorder.desktop
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/icons/hicolor/*/apps/org.gnome.SoundRecorder.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.SoundRecorder-symbolic.svg
%{_datadir}/metainfo/org.gnome.SoundRecorder.metainfo.xml
%{_datadir}/org.gnome.SoundRecorder/

%changelog
%autochangelog
