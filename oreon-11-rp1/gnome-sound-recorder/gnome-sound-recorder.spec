%global source0_hash 6db6db9a3b1b52fd0ab54f9a5bf4f299cb71e52a13ac5fdfc3e74eb46985a4e6
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-sound-recorder
Version:        43~beta
Release:        12%{?dist}
Summary:        Make simple recordings from your desktop
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Design/Apps/SoundRecorder
Source0:        https://download.gnome.org/sources/%{name}/43/%{name}-43.beta.tar.xz
BuildArch:      noarch
Requires:       gjs >= 1.41.4
Requires:       gstreamer1
Requires:       gstreamer1-plugins-bad-free
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugins-good
Requires:       gtk4
Requires:       libadwaita
# oreon:deps
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
# /oreon:deps
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
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.gnome.SoundRecorder.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.SoundRecorder.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
