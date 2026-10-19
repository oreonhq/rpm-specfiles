%global source0_hash 043f21b27c50ed70d0638a318460e747e5a12cc2af1bce960858b7a63b981ecc
Summary:        Graphical Boot Animation and Logger
Name: plymouth
Version: 26.134.222
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: http://www.freedesktop.org/wiki/Software/Plymouth
Source0:        https://gitlab.freedesktop.org/plymouth/plymouth/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1: spinner-update.tar.gz
Source2: charge.plymouth
Patch: 0001-Revert-src-Hide-console-text-when-splash-is-requeste.patch
Patch: 0001-ply-device-manager-Fix-race-in-fb_device_has_drm_dev.patch
Requires: %{name}-core-libs = %{version}-%{release}
Requires: %{name}-scripts = %{version}-%{release}
Requires: xkeyboard-config
Suggests: logrotate
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  git
BuildRequires:  kernel-headers
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  pango-devel
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  system-logos
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.

%package system-theme
Summary: Plymouth default theme
Requires: plymouth(system-theme) = %{version}-%{release}
%description system-theme
This meta-package tracks the current distribution default theme.

%package core-libs
Summary: Plymouth core libraries
%description core-libs
This package contains the core libraries used by Plymouth.

%package graphics-libs
Summary: Plymouth graphics libraries
Requires: %{name}-core-libs = %{version}-%{release}
Requires: system-logos
%description graphics-libs
This package contains the libraries used by graphical Plymouth splashes.

%package devel
Summary: Libraries and headers for writing Plymouth splash plugins
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
%description devel
This package contains the libraries and headers needed to develop
3rd party splash plugins for Plymouth.

%package scripts
Summary: Plymouth related scripts
Requires: findutils, coreutils, gzip, cpio, dracut
Requires: xkeyboard-config
Requires: %{name} = %{version}-%{release}
%description scripts
This package contains scripts that help integrate Plymouth with
the system.

%package plugin-label
Summary: Plymouth label plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
%description plugin-label
This package contains the label control plugin for Plymouth.
It provides the ability to render text on graphical boot splashes.

%package plugin-script
Summary: Plymouth "script" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible boot splash language that
allows writing new plugins as scripts, simplifying the process
of designing custom boot splash themes.

%package plugin-fade-throbber
Summary: Plymouth "Fade-Throbber" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

%package plugin-space-flares
Summary: Plymouth "space-flares" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label = %{version}-%{release}
%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package plugin-two-step
Summary: Plymouth "two-step" plugin
Requires: %{name} = %{version}-%{release}
Requires: %{name}-graphics-libs = %{version}-%{release}
Requires: plymouth-plugin-label = %{version}-%{release}
Obsoletes: %{name}-plugin-throbgress < %{version}-%{release}
%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

# Don't build charge theme in ELN/RHEL as it's Fedora specific

%package theme-fade-in
Summary: Plymouth "Fade-In" theme
Requires: %{name}-plugin-fade-throbber = %{version}-%{release}
Requires(post): plymouth-scripts
%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.

%package theme-script
Summary: Plymouth "Script" plugin
Requires: %{name}-plugin-script = %{version}-%{release}
Requires(post): plymouth-scripts
%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It it is a simple example theme the uses the "script"
plugin.

%package theme-solar
Summary: Plymouth "Solar" theme
Requires: %{name}-plugin-space-flares = %{version}-%{release}
Requires(post): plymouth-scripts
%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.

%package theme-spinfinity
Summary: Plymouth "Spinfinity" theme
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires(post): plymouth-scripts
%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.

%package theme-spinner
Summary: Plymouth "Spinner" theme
Requires: %{name}-plugin-two-step = %{version}-%{release}
Requires: font(cantarell) font(cantarelllight)
Requires(post): plymouth-scripts
Provides: plymouth(system-theme) = %{version}-%{release}
%description theme-spinner
This package contains the "spinner" boot splash theme for
Plymouth. It features a small spinner on a dark background.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -a 1
# Change the default theme
sed -i -e 's/spinner/bgrt/g' src/plymouthd.defaults
# Use simpledrm /dev/dri/card# by default, except when LUKS disk encrpytion is used
echo UseSimpledrmNoLuks=1 >> src/plymouthd.defaults

%build

%meson -Dtracing=true  \
       -Dlogo=%{_datadir}/pixmaps/system-logo-white.png \
       -Dbackground-start-color-stop=0x0073B3           \
       -Dbackground-end-color-stop=0x00457E             \
       -Dbackground-color=0x3391cd
%meson_build
%install
%meson_install
%find_lang %{name}
find $RPM_BUILD_ROOT -name '*.la' -delete
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/plymouth
rm -rf $RPM_BUILD_ROOT%{_datadir}/plymouth/themes/glow
%ldconfig_scriptlets core-libs
%ldconfig_scriptlets graphics-libs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%postun theme-fade-in

export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "fade-in" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi
%postun theme-solar

export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi
%postun theme-spinfinity

export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "spinfinity" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi
%post theme-spinner

export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 2 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "charge" ]; then
        %{_sbindir}/plymouth-set-default-theme bgrt
    fi
fi
%postun theme-spinner

export PLYMOUTH_PLUGIN_PATH=%{_libdir}/plymouth/
if [ $1 -eq 0 ]; then
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" == "bgrt" -o \
         "$(%{_sbindir}/plymouth-set-default-theme)" == "spinner" ]; then
        %{_sbindir}/plymouth-set-default-theme --reset
    fi
fi
%files -f %{oreon_filedir}/main.list
%files -n plymouth-system-theme -f %{oreon_filedir}/plymouth-system-theme.list
%files -n plymouth-core-libs -f %{oreon_filedir}/plymouth-core-libs.list
%files -n plymouth-graphics-libs -f %{oreon_filedir}/plymouth-graphics-libs.list
%files -n plymouth-devel -f %{oreon_filedir}/plymouth-devel.list
%files -n plymouth-scripts -f %{oreon_filedir}/plymouth-scripts.list
%files -n plymouth-plugin-label -f %{oreon_filedir}/plymouth-plugin-label.list
%files -n plymouth-plugin-script -f %{oreon_filedir}/plymouth-plugin-script.list
%files -n plymouth-plugin-fade-throbber -f %{oreon_filedir}/plymouth-plugin-fade-throbber.list
%files -n plymouth-plugin-space-flares -f %{oreon_filedir}/plymouth-plugin-space-flares.list
%files -n plymouth-plugin-two-step -f %{oreon_filedir}/plymouth-plugin-two-step.list
%files -n plymouth-theme-fade-in -f %{oreon_filedir}/plymouth-theme-fade-in.list
%files -n plymouth-theme-script -f %{oreon_filedir}/plymouth-theme-script.list
%files -n plymouth-theme-solar -f %{oreon_filedir}/plymouth-theme-solar.list
%files -n plymouth-theme-spinfinity -f %{oreon_filedir}/plymouth-theme-spinfinity.list
%files -n plymouth-theme-spinner -f %{oreon_filedir}/plymouth-theme-spinner.list

%changelog

%autochangelog
