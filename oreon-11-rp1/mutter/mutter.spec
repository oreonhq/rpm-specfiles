%global source0_hash 5d28f3ae225692428fcafb96500d673f34328b698b86960c9c1460d0b1d983b3
%global glib_version 2.81.1
%global gobject_introspection_version 1.41.4
%global gtk3_version 3.19.8
%global gtk4_version 4.14.0
%global gsettings_desktop_schemas_version 47~beta
%global libdrm_version 2.4.118
%global libinput_version 1.27.0
%global pixman_version 0.42
%global pipewire_version 1.2.7
%global lcms2_version 2.6
%global colord_version 1.4.5
%global libei_version 1.3.901
%global mutter_api_version 18
%global wayland_protocols_version 1.45
%global wayland_server_version 1.24
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:          mutter
Version:       51.0
Release:        1%{?dist}
Summary:        Window and compositing manager based on Clutter
License:       GPL-2.0-or-later
URL:           http://www.gnome.org
Source0:        http://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Requires: gnome-control-center-filesystem
Requires: glib2%{?_isa} >= %{glib_version}
Requires: gsettings-desktop-schemas%{?_isa} >= %{gsettings_desktop_schemas_version}
Requires: gnome-settings-daemon
Requires: gtk4%{?_isa} >= %{gtk4_version}
Requires: libeis%{?_isa} >= %{libei_version}
Requires: libinput%{?_isa} >= %{libinput_version}
Requires: pipewire%{_isa} >= %{pipewire_version}
Requires: startup-notification
Requires: dbus
Requires: python3-argcomplete
Requires: %{name}-common = %{version}-%{release}
Recommends: mesa-dri-drivers%{?_isa}
Provides: firstboot(windowmanager) = mutter
Provides: bundled(cogl) = 1.22.0
Provides: bundled(clutter) = 1.26.0
Conflicts: mutter < 45~beta.1-2
Conflicts: gnome-shell < 45~rc
# oreon:deps
BuildRequires:  cvt
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  git-core
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glycin-2)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gnome-settings-daemon)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(graphene-gobject-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libei-1.0)
BuildRequires:  pkgconfig(libeis-1.0)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(umockdev-1.0)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xwayland)
BuildRequires:  python3-argcomplete
BuildRequires:  python3-dbusmock
BuildRequires:  python3-docutils
BuildRequires:  sysprof-devel
# /oreon:deps
%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display engine
using the Clutter toolkit with solid window-management logic inherited
from the Metacity window manager.

While Mutter can be used stand-alone, it is primarily intended to be
used as the display core of a larger system such as GNOME Shell. For
this reason, Mutter is very extensible via plugins, which are used both
to add fancy visual effects and to rework the window management
behaviors to meet the needs of the environment.

%package common
Summary: Common files used by %{name} and forks of %{name}
BuildArch: noarch
Conflicts: mutter < 45~beta.1-2
%description common
Common files used by Mutter and soft forks of Mutter

%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libei%{?_isa} >= %{libei_version}
Requires: mesa-libEGL-devel
%description devel
Header files and libraries for developing Mutter plugins. Also includes
utilities for testing Metacity/Mutter themes.

%package  tests
Summary:  Tests for the %{name} package
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gtk3%{?_isa} >= %{gtk3_version}
Requires: libei%{?_isa} >= %{libei_version}
%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%package devkit
Summary: Mutter Development Kit
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devkit
Viewer for nested mutter instances.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -S git -n %{name}-%{tarball_version}

%build

%meson -Degl_device=true
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mutter-common -f %{oreon_filedir}/mutter-common.list
%files -n mutter-devel -f %{oreon_filedir}/mutter-devel.list
%files -n mutter-tests -f %{oreon_filedir}/mutter-tests.list
%files -n mutter-devkit -f %{oreon_filedir}/mutter-devkit.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
