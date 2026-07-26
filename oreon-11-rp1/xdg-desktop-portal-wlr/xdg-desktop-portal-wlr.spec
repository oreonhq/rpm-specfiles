%global source0_hash 24d365bbac02f5ae3300024d84928484852d962712b6acc1f1ed7d92f2f59b2f

Name:           xdg-desktop-portal-wlr
Version:        0.8.1
Release:        2%{?dist}
Summary:        xdg-desktop-portal backend for wlroots

License:        MIT
URL:            https://github.com/emersion/%{name}
Source0:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
# Generic portals.conf(5) for any wlroots-based compositor.
# Can be loaded by setting XDG_CURRENT_DESKTOP=<compositor>:wlroots
Source3:        wlroots-portals.conf

BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  systemd-rpm-macros

BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(inih)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libspa-0.2)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wayland-scanner)

Requires:       dbus
# required for Screenshot portal implementation
Requires:       grim
Requires:       xdg-desktop-portal
# required for Screencast output selection.
# xdpw will try to use first available of the 3 utilities
Recommends:     (slurp or wofi or bemenu)
Suggests:       slurp

Enhances:       sway
Supplements:    (sway and (flatpak or snapd))

%description
%{summary}.
This project seeks to add support for the screenshot, screencast, and possibly
remote-desktop xdg-desktop-portal interfaces for wlroots based compositors.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%meson \
    -Dsd-bus-provider=libsystemd
%meson_build

%install
%meson_install
install -D -pv -m644 %{SOURCE3} \
    %{buildroot}%{_datadir}/xdg-desktop-portal/wlroots-portals.conf

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%files
%license LICENSE
%doc README.md contrib/config.sample
%{_libexecdir}/%{name}
%{_mandir}/man5/%{name}.5*
%{_datadir}/xdg-desktop-portal/portals/wlr.portal
%{_datadir}/xdg-desktop-portal/wlroots-portals.conf
%{_datadir}/dbus-1/services/*.service
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
