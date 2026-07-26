%global source0_hash 5b9991557cc2764a8281a24aa726a645287eb075cde0f0ae7c737965264a119c

Name:           celluloid
Version:        0.29
Release:        3%{?dist}
Summary:        A simple GTK+ frontend for mpv

License:        GPL-3.0-or-later
URL:            https://github.com/celluloid-player/celluloid
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gtk4) >= 4.6.1
BuildRequires:  intltool >= 0.40.6
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  mpv-libs-devel
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       hicolor-icon-theme
Requires:       dbus-common
# missing transitive dependency of mpv-libs
Recommends:     (yt-dlp or youtube-dl)
Suggests:       yt-dlp

Provides:       gnome-mpv = %{version}-%{release}
Obsoletes:      gnome-mpv < 0.17

%description
Celluloid (formerly GNOME MPV) is a simple GTK+ frontend for mpv.
It aims to be easy to use while maintaining high level of configurability.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

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

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop

%files -f %{name}.lang
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/io.github.celluloid_player.Celluloid.appdata.xml
%{_datadir}/applications/io.github.celluloid_player.Celluloid.desktop
%{_datadir}/dbus-1/services/io.github.celluloid_player.Celluloid.service
%{_datadir}/glib-2.0/schemas/io.github.celluloid_player.Celluloid.gschema.xml
%{_datadir}/icons/hicolor/*/apps/*.svg
 %{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
