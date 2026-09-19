%global source0_hash d3a88490b59dc99b4fd63d3349c8196d9f6dbcb635ea4ffe1407fbcde79bbc30

Name:           pipewire-media-session
Summary:        PipeWire reference session manager
Version:        0.4.3
Release:        2%{?dist}
License:        MIT
URL:            https://pipewire.org/
Source0:        https://gitlab.freedesktop.org/pipewire/media-session/-/archive/%{version}/media-session-%{version}.tar.gz

# Virtual Provides to support swapping between PipeWire session manager implementations
Provides:       pipewire-session-manager
Conflicts:      pipewire-session-manager

BuildRequires:  meson gcc pkgconfig
BuildRequires:  pkgconfig(libpipewire-0.3) >= 0.3.44
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  gettext
BuildRequires:  systemd-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

Requires:       systemd

%description
Media Session is the reference session manager for the PipeWire media server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n media-session-%{version}

%build
%meson \
    -Ddocs=disabled \
    -Dsystemd=enabled \
    -Dwith-module-sets=alsa,pulseaudio,jack
%meson_build

%install
%meson_install

%find_lang media-session

%posttrans
%systemd_user_post pipewire-media-session.service

%preun
%systemd_user_preun pipewire-media-session.service

%files -f media-session.lang
%license LICENSE COPYING
%doc README.md
%{_bindir}/pipewire-media-session
%{_userunitdir}/pipewire-media-session.service
%dir %{_datadir}/pipewire/media-session.d/
%{_datadir}/pipewire/media-session.d/alsa-monitor.conf
%{_datadir}/pipewire/media-session.d/bluez-monitor.conf
%{_datadir}/pipewire/media-session.d/media-session.conf
%{_datadir}/pipewire/media-session.d/v4l2-monitor.conf

%{_datadir}/pipewire/media-session.d/with-alsa
%{_datadir}/pipewire/media-session.d/with-jack
%{_datadir}/pipewire/media-session.d/with-pulseaudio

%changelog
%autochangelog
