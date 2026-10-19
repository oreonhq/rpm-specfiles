%global source0_hash 4399c9fa7f61e5984242e279acd1519beec246b98a676d44a4b2ab94e9eecb01
%global glib2_version 2.79.0
%global gtk4_version 4.15.0
%global libadwaita_version 1.6~beta
%global blueprint_compiler_version 0.18
Name:           showtime
Version:        50.0
Release:        1%{?dist}
Summary:        Modern video player built using GTK4
License:        GPL-3.0-or-later
URL:            https://apps.gnome.org/Showtime/
%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %(cut -d "." -f 1 <<<%{tarball_version})
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
BuildArch:      noarch
Requires:       gtk4 >= %{gtk4_version}
Requires:       libadwaita >= %{libadwaita_version}
Requires:       python3
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-base
Requires:       gstreamer1-plugin-gtk4
Requires:       (gstreamer1-plugin-openh264 if openh264)
Recommends:     gstreamer1-plugins-good
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-ugly-free
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
# /oreon:deps
%description
Play your favorite movies and video files without hassle. Showtime
features simple playback controls that fade out of your way when
you're watching, fullscreen, adjustable playback speed, multiple
language and subtitle tracks, and screenshots — everything you
need for a straightforward viewing experience.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Showtime.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
