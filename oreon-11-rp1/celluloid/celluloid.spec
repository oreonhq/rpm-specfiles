%global source0_hash 7fef96431842c24e5ae78a9c42bc6523818a6c45213f23ceb146d037d6ec8559
Name:           celluloid
Version:        0.30
Release:        1%{?dist}
Summary:        A simple GTK+ frontend for mpv
License:        GPL-3.0-or-later
URL:            https://github.com/celluloid-player/celluloid
Source0:        https://github.com/%{name}-player/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Requires:       dbus-common
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp
Provides:       gnome-mpv = %{version}-%{release}
Obsoletes:      gnome-mpv < 0.17
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  mpv-libs-devel
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
# /oreon:deps
%description
Celluloid (formerly GNOME MPV) is a simple GTK+ frontend for mpv.
It aims to be easy to use while maintaining high level of configurability.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
pushd redhat-linux-build
    %ninja_build
popd
%install
pushd redhat-linux-build
    %ninja_install
popd
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
