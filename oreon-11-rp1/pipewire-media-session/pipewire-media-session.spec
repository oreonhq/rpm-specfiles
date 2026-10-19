%global source0_hash d3a88490b59dc99b4fd63d3349c8196d9f6dbcb635ea4ffe1407fbcde79bbc30
Name:           pipewire-media-session
Summary:        PipeWire reference session manager
Version:        0.4.3
Release:        1%{?dist}
License:        MIT
URL:            https://pipewire.org/
Source0:        https://gitlab.freedesktop.org/pipewire/media-session/-/archive/%{version}/media-session-%{version}.tar.gz
Provides:       pipewire-session-manager
Conflicts:      pipewire-session-manager
Requires:       systemd
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  systemd
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Media Session is the reference session manager for the PipeWire media server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir media-session-%{version}
%oreon_prep
%build

%meson \
    -Ddocs=disabled \
    -Dsystemd=enabled \
    -Dwith-module-sets=alsa,pulseaudio,jack
%meson_build
%install
%meson_install
%find_lang media-session
%oreon_autofiles main

%posttrans

%systemd_user_post pipewire-media-session.service
%preun

%systemd_user_preun pipewire-media-session.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
