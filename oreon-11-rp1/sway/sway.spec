%global source2_hash 42ad6b1bb877e1d8e3dffd101431468573e3678d0a89efff08da8383d6efa16f
%global source0_hash a7b1becc217433c11c6284d36bcea0687b87b77b0ed26a384565292ec321f2b1
%global tag     1.12
Name:           sway
Version:        1.12
Release:        1%{?dist}
Summary:        i3-compatible window manager for Wayland
License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        https://github.com/%{name}wm/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{tag}/%{name}-%{tag}.tar.gz.sig
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg
Source100:      config.minimal
Source101:      sway-portals.conf
Source102:      README.md
Requires:       %{name}-config
Suggests:       %{name}-config-upstream
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon)
# /oreon:deps
%description
Sway is a tiling window manager supporting Wayland compositor protocol and
i3-compatible configuration.

# Configuration presets:
#
%package        config-upstream
Summary:        Upstream configuration for Sway
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-config = %{version}-%{release}
Conflicts:      %{name}-config
Requires:       sway-wallpapers
Requires:       mesa-dri-drivers
Requires:       polkit
Requires:       swaybg
Requires:       xorg-x11-server-Xwayland
Recommends:     foot
Recommends:     grim
Recommends:     wmenu
Recommends:     sway-systemd
Recommends:     swayidle
Recommends:     swaylock
Recommends:     (qt5-qtwayland if qt5-qtbase-gui)
Recommends:     (qt6-qtwayland if qt6-qtbase-gui)
%description    config-upstream
Upstream configuration for Sway.
Includes all important dependencies for a typical desktop system
with minimal or no divergence from the upstream.

%package        config-minimal
RemovePathPostfixes:  .minimal
Summary:        Minimal configuration for Sway
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-config = %{version}-%{release}
Conflicts:      %{name}-config
%description    config-minimal
Minimal configuration for Sway without any extra dependencies.
Suitable for headless or buildroot use.

# The artwork is heavy and we don't use it with our default config
%package        wallpapers
Summary:        Wallpapers for Sway
BuildArch:      noarch
License:        CC0-1.0
%description    wallpapers
Wallpaper collection provided with Sway

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -N -n %{name}-%{tag}
# apply unconditional patches
#autopatch -p1 -M99
# apply conditional patches

%build

%meson \
    -Dsd-bus-provider=libsystemd \
    -Dwerror=false
%meson_build
%install
%meson_install
install -D -m644 -pv %{SOURCE100} %{buildroot}%{_sysconfdir}/sway/config.minimal
install -D -m644 -pv %{SOURCE101} %{buildroot}%{_datadir}/xdg-desktop-portal/sway-portals.conf
install -D -m644 -pv README.md    %{buildroot}%{_pkgdocdir}/README.md
install -D -m644 -pv %{SOURCE102} %{buildroot}%{_pkgdocdir}/README.Fedora
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sway-config-upstream -f %{oreon_filedir}/sway-config-upstream.list
%files -n sway-config-minimal -f %{oreon_filedir}/sway-config-minimal.list
%files -n sway-wallpapers -f %{oreon_filedir}/sway-wallpapers.list

%changelog

%autochangelog
