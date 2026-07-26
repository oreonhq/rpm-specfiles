%global source0_hash c6435378f339a66b1c58c233ad32e03721bda8aebd80c7053c3693c409ef003a

# we don't want to support hyprland
%bcond hyprland_session 0

Name:           lxqt-wayland-session
Version:        0.3.2
Release:        1%{?dist}
Summary:        Wayland session files for LXQt
# See "LICENSE" for a breakdown of license usage
License:        LGPL-2.1-only AND GPL-3.0-only AND MIT AND GPL-2.0-only AND BSD-3-Clause
URL:            https://lxqt-project.org/

Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        default-compositor-miriway

Patch0:         0001-configuration-changes-for-default-labwc-session.patch
Patch1:         0002-configuration-changes-for-default-wayfire-session.patch
Patch2:         0003-configuration-changes-for-default-niri-session.patch
Patch3:         0004-configuration-adds-miriway-session.patch
Patch4:         0005-configuration-changes-for-default-river-session.patch
Patch5:         0006-configuration-changes-for-default-sway-session.patch
BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  perl

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  cmake(lxqt)

BuildRequires:  cmake(KF6WindowSystem)

Requires:       desktop-backgrounds-compat
# Require the default compositor
Requires:       %{name}-default-compositor
# We prefer miriway
Suggests:       %{name}-default-compositor-miriway

%description
Files needed for the LXQt Wayland Session: Wayland session start script,
its desktop entry for display managers and default configurations for
actually supported compositors.

%files
%doc README.md
%license COPYING.LESSER LICENSE
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/wayland
%dir %{_datadir}/lxqt/wayland/firstrun
%{_bindir}/startlxqtwayland
%{_bindir}/lxqt-qdbus
%{_datadir}/wayland-sessions/lxqt-wayland.desktop
%{_datadir}/lxqt/wayland/firstrun/autostart
%{_datadir}/lxqt/wallpapers/origami-dark-labwc.png
%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/startlxqtwayland.1.gz

%dnl ------------------------------------------------------------------
%package -n     %{name}-default-compositor-miriway
Summary:        Sets default compositor to miriway
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       lxqt-miriway-session = %{version}-%{release}
Provides:       %{name}-default-compositor
Conflicts:      %{name}-default-compositor

%description -n %{name}-default-compositor-miriway
Sets the default compositor to miriway, and provides the miriway session
setup

%files -n %{name}-default-compositor-miriway
%license COPYING
%{_datadir}/lxqt/wayland/default-compositor

%dnl ------------------------------------------------------------------

%if %{with hyprland_session}
%package -n     lxqt-hyprland-session
Summary:        Session files for LXQt-Hyprland
License:        BSD-3-Clause
Requires:       %{name} = %{version}-%{release}
Requires:       hyprland
Supplements:    (%{name} and hyprland)

%description -n lxqt-hyprland-session
This package contains the files necessary to use Hyprland as the Wayland
compositor with LXQt.

%files -n lxqt-hyprland-session
%license LICENSE.BSD
%{_datadir}/lxqt/wayland/lxqt-hyprland.conf
%endif

%dnl ------------------------------------------------------------------
%package -n     lxqt-miriway-session
Summary:        Session files for LXQt-miriway
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
# For flag to customize decoration preference
Requires:       miriway >= 24.11.1-1
# For mir fixes for LXQt
Requires:       mir-server-libs >= 2.19.3-3
Supplements:    (%{name} and miriway)

%description -n lxqt-miriway-session
This package contains the files necessary to use Miriway as the Wayland
compositor with LXQt

%files -n lxqt-miriway-session
%license COPYING
%attr(0755,root,root) %{_datadir}/lxqt/wayland/miriway/lxqt-miriway-wrapper
%{_datadir}/lxqt/wayland/miriway/miriway-shell.config

%dnl ------------------------------------------------------------------

%package -n     lxqt-niri-session
Summary:        Session files for LXQT-niri
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       niri
Supplements:    (%{name} and niri)

%description -n lxqt-niri-session
This package contains the files necessary to use niri as the Wayland compositor
for LXQt.

%files -n lxqt-niri-session
%license COPYING
%{_datadir}/lxqt/wayland/lxqt-niri.kdl
%{_datadir}/lxqt/wayland/lxqt-niri.kdl.full
%{_datadir}/lxqt/wayland/niri/input.kdl
%{_datadir}/lxqt/wayland/niri/keybinds.kdl
%{_datadir}/lxqt/wayland/niri/outputs.kdl
%{_datadir}/lxqt/wayland/niri/visual.kdl
%{_datadir}/lxqt/wayland/niri/window-rules.kdl

%dnl ------------------------------------------------------------------

%package -n     lxqt-river-session
Summary:        Session files for LXQt-river
License:        GPL-3.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       river
Recommends:     swaybg
Recommends:     jxl-pixbuf-loader
Supplements:    (%{name} and river)

%description -n lxqt-river-session
This package contains the files necessary to use river as the Wayland
compositor with LXQt.

%files -n lxqt-river-session
%license COPYING
%attr(0755,root,root) %{_datadir}/lxqt/wayland/lxqt-river-init

%dnl ------------------------------------------------------------------

%package -n     lxqt-sway-session
Summary:        Session files for LXQt-Sway
License:        MIT
Requires:       %{name} = %{version}-%{release}
Requires:       sway
Recommends:     swaybg
Recommends:     jxl-pixbuf-loader
Supplements:    (%{name} and sway)

%description -n lxqt-sway-session
This package contains the files necessary to use Sway as the Wayland compositor
with LXQt.

%files -n lxqt-sway-session
%license LICENSE.MIT
%{_datadir}/lxqt/wayland/lxqt-sway.config

%dnl ------------------------------------------------------------------

%package -n     lxqt-wayfire-session
Summary:        Session files for LXQt-wayfire
License:        MIT
Requires:       %{name} = %{version}-%{release}
Requires:       wayfire
Recommends:     swaybg
Recommends:     jxl-pixbuf-loader
Supplements:    (%{name} and wayfire)

%description -n lxqt-wayfire-session
This package contains the files necessary to use wayfire as the Wayland
compositor with LXQt.

%files -n lxqt-wayfire-session
%license LICENSE.MIT
%{_datadir}/lxqt/wayland/lxqt-wayfire.ini

%dnl ------------------------------------------------------------------

%package -n     lxqt-labwc-session
Summary:        Session files and theme for LXQt-labwc
License:        CC-BY-SA-4.0 AND GPL-2.0-or-later
Requires:       %{name} = %{version}-%{release}
Requires:       labwc >= 0.7.2
Requires:       swaybg
Requires:       swayidle
Requires:       swaylock
Requires:       jxl-pixbuf-loader
Supplements:    (%{name} and labwc)

%description -n lxqt-labwc-session
This package contains the openbox themes and other files necessary to use
labwc as the Wayland compositor with LXQt.

%files -n lxqt-labwc-session
%license LICENSE.GPLv2
%dir %{_datadir}/lxqt/wallpapers
%dir %{_datadir}/lxqt/wayland/labwc
%dir %{_datadir}/lxqt/graphics
%{_datadir}/themes/Vent/
%{_datadir}/themes/Vent-dark/
%{_datadir}/lxqt/wallpapers/origami-dark-labwc.png
%{_datadir}/lxqt/wayland/labwc/README
%{_datadir}/lxqt/wayland/labwc/autostart
%{_datadir}/lxqt/wayland/labwc/environment
%{_datadir}/lxqt/wayland/labwc/menu.xml
%{_datadir}/lxqt/wayland/labwc/rc.xml
%{_datadir}/lxqt/wayland/labwc/themerc
%{_datadir}/lxqt/wayland/labwc/themerc-override
%{_datadir}/lxqt/graphics/lxqt-labwc.png

%dnl ------------------------------------------------------------------

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -S git_am
cp -a %{SOURCE1} default-compositor-miriway

%build
%cmake
%cmake_build

%install
%cmake_install

install -m0644 default-compositor-miriway %{buildroot}%{_datadir}/lxqt/wayland/default-compositor

%if ! %{with hyprland_session}
# Drop hyprland session files
rm -v %{buildroot}%{_datadir}/lxqt/wayland/lxqt-hyprland.conf
%endif

%fdupes %{buildroot}%{_datadir}/themes/

%changelog
%autochangelog
