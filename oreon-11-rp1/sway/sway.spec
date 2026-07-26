%global source0_hash 0e37a55b7c3379230e97e1ad982542b75016a0c7d6676198604e557f9b373dae

%global tag     1.11

Name:           sway
Version:        1.11
Release:        3%{?dist}
Summary:        i3-compatible window manager for Wayland
License:        MIT
URL:            https://github.com/swaywm/sway
Source0:        %{url}/releases/download/%{tag}/%{name}-%{tag}.tar.gz
Source1:        %{url}/releases/download/%{tag}/%{name}-%{tag}.tar.gz.sig
# 0FDE7BE0E88F5E48: emersion <contact@emersion.fr>
Source2:        https://emersion.fr/.well-known/openpgpkey/hu/dj3498u4hyyarh35rkjfnghbjxug6b19#/gpgkey-0FDE7BE0E88F5E48.gpg

# Minimal configuration file for headless or buildroot use
Source100:      config.minimal
Source101:      sway-portals.conf
Source102:      README.md

# Upstream patches

# Fedora patches

# Conditional patches

BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson >= 1.3
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(json-c) >= 0.13
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput) >= 1.26.0
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsystemd) >= 239
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-server) >= 1.21.0
BuildRequires:  pkgconfig(wayland-protocols) >= 1.24
BuildRequires:  pkgconfig(wlroots-0.19)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xkbcommon) >= 1.5.0

# Require any of the available configuration packages;
# Prefer the -upstream one if none are directly specified in the package manager transaction
Requires:       %{name}-config
Suggests:       %{name}-config-upstream

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

# Require the wallpaper referenced in the config.
# Weak dependency here causes a swaynag warning during the configuration load
Requires:       sway-wallpapers
# Lack of graphical drivers may hurt the common use case
Requires:       mesa-dri-drivers
# Logind needs polkit to create a graphical session
Requires:       polkit
# swaybg is used in the default config
Requires:       swaybg
# dmenu (as well as rxvt any many others) requires XWayland on Sway
Requires:       xorg-x11-server-Xwayland

# Sway binds the terminal shortcut to one specific terminal. In our case foot
Recommends:     foot
# grim is the recommended way to take screenshots on sway 1.0+
Recommends:     grim
# wmenu is the default launcher in sway
Recommends:     wmenu
# Install configs and scripts for better integration with systemd user session
Recommends:     sway-systemd
# Both utilities are suggested in the default configuration
Recommends:     swayidle
Recommends:     swaylock

# Minimal installation doesn't include Qt Wayland backend
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
# List of dependencies for headless or buildroot use

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
# Install minimal configuration file
install -D -m644 -pv %{SOURCE100} %{buildroot}%{_sysconfdir}/sway/config.minimal
# Install portals.conf for xdg-desktop-portal
install -D -m644 -pv %{SOURCE101} %{buildroot}%{_datadir}/xdg-desktop-portal/sway-portals.conf
# install the documentation
install -D -m644 -pv README.md    %{buildroot}%{_pkgdocdir}/README.md
install -D -m644 -pv %{SOURCE102} %{buildroot}%{_pkgdocdir}/README.Fedora
# Create directory for extra config snippets
install -d -m755 -pv %{buildroot}%{_sysconfdir}/sway/config.d

%files
%license LICENSE
%doc %{_pkgdocdir}
%dir %{_sysconfdir}/sway
%dir %{_sysconfdir}/sway/config.d
%{_mandir}/man1/sway*
%{_mandir}/man5/*
%{_mandir}/man7/*
%caps(cap_sys_nice=ep) %{_bindir}/sway
%{_bindir}/swaybar
%{_bindir}/swaymsg
%{_bindir}/swaynag
%dir %{_datadir}/xdg-desktop-portal
%{_datadir}/xdg-desktop-portal/sway-portals.conf
%{bash_completions_dir}/sway*
%{fish_completions_dir}/sway*.fish
%{zsh_completions_dir}/_sway*

%files config-upstream
%config(noreplace) %{_sysconfdir}/sway/config
%{_datadir}/wayland-sessions/sway.desktop

%files config-minimal
%config(noreplace) %{_sysconfdir}/sway/config.minimal

%files wallpapers
%license assets/LICENSE
%{_datadir}/backgrounds/sway

%changelog
%autochangelog
