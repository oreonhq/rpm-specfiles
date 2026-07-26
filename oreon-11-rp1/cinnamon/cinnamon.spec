%global source0_hash 220f9ba77860d63708e682aa3fdc48cd8597b41b698467f116e477b45d514249

%global __requires_exclude ^lib%{name}.so|^lib%{name}-js.so

%global cjs_version 128.1
%global cinnamon_desktop_version 6.6.0
%global cinnamon_translations_version 6.6.0
%global gobject_introspection_version 1.38.0
%global muffin_version 6.6.0
%global json_glib_version 0.13.2

%global __python %{__python3}

Name:           cinnamon
Version:        6.6.7
Release:        2%{?dist}
Summary:        Window management and application launching for GNOME
# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            https://github.com/linuxmint/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        10_cinnamon-common.gschema.override
Source2:        10_cinnamon-apps.gschema.override.in
Source3:        22_fedora.styles

Patch0:         set_wheel.patch
#Patch1:         revert_25aef37.patch
Patch2:         default_panal_launcher.patch
Patch3:         remove_crap_from_menu.patch
Patch4:         set_menu_defaults.patch
Patch5:         %{url}/pull/13646.patch#/theme-fallback.patch

ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  desktop-file-utils
BuildRequires:  python3-libsass
BuildRequires:  python3-rpm-macros
BuildRequires:  pkgconfig(cjs-1.0) >= %{cjs_version}
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(lib%{name}-menu-3.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(%{name}-desktop) >= %{cinnamon_desktop_version}
BuildRequires:  gobject-introspection >= %{gobject_introspection_version}
BuildRequires:  pkgconfig(json-glib-1.0) >= %{json_glib_version}
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(xapp)

# for screencast recorder functionality
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  intltool
BuildRequires:  pkgconfig(libcanberra)

# used in unused BigThemeImage
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libmuffin-0) >= %{muffin_version}
BuildRequires:  pkgconfig(libpulse)

# media keys
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(colord)
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libwacom)
BuildRequires:  pkgconfig(xorg-wacom)
%endif
BuildRequires:  pkgconfig(xtst)

Requires:       %{name}-desktop%{?_isa} >= %{cinnamon_desktop_version}
Requires:       muffin%{?_isa} >= %{muffin_version}
Requires:       cjs%{?_isa} >= %{cjs_version}
Requires:       gnome-menus%{?_isa} >= 3.0.0-2

# wrapper script used to restart old GNOME session if run --replace
# from the command line
Requires:       gobject-introspection%{?_isa} >= %{gobject_introspection_version}

# needed for loading SVG's via gdk-pixbuf
Requires:       librsvg2%{?_isa}

# needed as it is now split from Clutter
Requires:       json-glib%{?_isa} >= %{json_glib_version}
Requires:       upower%{?_isa}
Requires:       polkit%{?_isa} >= 0.100

# needed for session files
Requires:       %{name}-session%{?_isa}

# needed for schemas
Requires:       at-spi2-atk%{?_isa}

# needed for the user menu
Requires:       accountsservice-libs%{?_isa}

# needed for settings
Requires:       gsound
Requires:       libtimezonemap%{?_isa}
Requires:       python3-babel
Requires:       python3-distro
Requires:       python3-pytz
Requires:       python3-pexpect
Requires:       python3-gobject%{?_isa}
Requires:       python3-dbus%{?_isa}
Requires:       python3-lxml%{?_isa}
Requires:       python3-pillow%{?_isa}
Requires:       python3-pam
Requires:       python3-tinycss2
Requires:       python3-requests
Requires:       python3-setproctitle%{?_isa}
Requires:       python3-xapp
Requires:       mintlocale
Recommends:     %{name}-control-center%{?_isa}
Recommends:     gnome-online-accounts-gtk
Recommends:     %{name}-translations >= %{cinnamon_translations_version}

# needed for theme overrides
Requires:       desktop-backgrounds-basic
Requires:       desktop-backgrounds-gnome
Requires:       gnome-backgrounds
Recommends:     paper-icon-theme
Requires:       system-logos

# Theming
Requires:       google-noto-sans-fonts
Requires:       google-noto-sans-mono-fonts
Requires:       %{name}-themes >= 1:1.7.4-0.2.20181112gitb94b890
Requires:       xapp-symbolic-icons

# RequiredComponents in the session files
Requires:       nemo%{?_isa}
Requires:       %{name}-screensaver%{?_isa}

# metacity and mate-panel are needed for fallback
Recommends:     metacity%{?_isa}
Recommends:     mate-panel%{?_isa}

# required for keyboard applet
Requires:       gucharmap%{?_isa}
Requires:       ibus-libs%{?_isa}
Requires:       ibus-gtk3%{?_isa}
Recommends:     ibus%{?_isa}
Recommends:     ibus-gtk4%{?_isa}
Requires:       gtk3-immodules%{?_isa}

Requires:       xapps%{?_isa}
Requires:       python3-xapps-overrides%{?_isa}

# required for calendar applet events
Recommends:     %{name}-calendar-server%{?_isa} = %{version}-%{release}

# required for network applet
Requires:       nm-connection-editor%{?_isa}
Requires:       network-manager-applet%{?_isa}

Requires:       python3-inotify

# required for cinnamon-killer-daemon
Requires:       keybinder3%{?_isa}

# required for sound applet
Requires:       wget%{?_isa}

# required for power applet
Recommends:     tuned-ppd

# required for printer applet
Requires:       cups-client%{?_isa}

# required for spice
Requires:       gettext

# required for gesture support
Recommends:     touchegg

# required to fix system-info
Recommends:     bluez-deprecated

# required for flatpak support
Recommends:     xdg-desktop-portal-xapp

Requires:       libsoup3

Provides:       desktop-notification-daemon
Provides:       bundled(libcroco) = 0.6.12
Provides:       PolicyKit-authentication-agent = %{version}-%{release}

%description
Cinnamon is a Linux desktop which provides advanced
innovative features and a traditional user experience.

The desktop layout is similar to Gnome 2.
The underlying technology is forked from Gnome Shell.
The emphasis is put on making users feel at home and providing
them with an easy to use and comfortable desktop experience.

%package calendar-server
Summary:        Calendar server for Cinnamon
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       evolution-data-server%{?_isa}
Requires:       gnome-calendar%{?_isa}

%description calendar-server
Calendar server for Cinnamon.

%if 0%{?fedora} && 0%{?fedora} < 40
%package devel-doc
Summary:        Development Documentation files for Cinnamon
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description devel-doc
This package contains the code documentation for various Cinnamon components.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%{__sed} -i -e 's@gksu@pkexec@g' files%{_bindir}/%{name}-settings-users
%{__sed} -i -e 's@gnome-orca@orca@g' files%{_datadir}/%{name}/%{name}-settings/modules/cs_accessibility.py
# remove mintlocale im from settings
%{__sed} -i -e 's@mintlocale im@mintlocale_im_removed@g' files%{_datadir}/%{name}/%{name}-settings/%{name}-settings.py

# Fix rpmlint errors
for file in files%{_datadir}/%{name}/applets/{printers,settings-example}@cinnamon.org/*.py \
  files%{_datadir}/%{name}/%{name}-settings/bin/*.py \
  files%{_datadir}/%{name}/%{name}-looking-glass/*.py \
  files%{_datadir}/%{name}/%{name}-settings/modules/cs_{actions,applets,desklets,display,gestures}.py \
  python3/cinnamon/*.py; do
  chmod a+x $file
done
chmod a-x files%{_datadir}/%{name}/%{name}-settings/bin/__init__.py

%build
%meson \
 --libexecdir=%{_libexecdir}/cinnamon/ \
 -Ddeprecated_warnings=false \
 -Dpy3modules_dir=%{python3_sitelib} \
 -Ddocs=false

%meson_build

%install
%meson_install

# install common gschema override
%{__install} --target-directory=%{buildroot}%{_datadir}/glib-2.0/schemas \
    -Dpm 0644 %{SOURCE1}

# install gschema-override for apps
%{__sed} -e 's!@pkg_manager@!org.mageia.dnfdragora.desktop!g' \
    < %{SOURCE2} > %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-apps.gschema.override

# install gschema-override for wallpaper
%{__cat} >> %{buildroot}%{_datadir}/glib-2.0/schemas/10_%{name}-wallpaper.gschema.override << EOF
[org.cinnamon.desktop.background]
picture-uri='file:///usr/share/backgrounds/tiles/default_blue.jpg'
EOF

# install style file for mint-x and mint-y
%{__install} --target-directory=%{buildroot}%{_datadir}/%{name}/styles.d/ \
    -Dpm 0644 %{SOURCE3}

# Provide symlink for the background-propeties.
%{__ln_s} %{_datadir}/gnome-background-properties %{buildroot}%{_datadir}/%{name}-background-properties
# Delete useless gir files
%{__rm} -rf %{buildroot}%{_datadir}/%{name}/*.gir

%check
%{_bindir}/desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.rst AUTHORS
%license COPYING
%{_bindir}/cinnamon
%{_bindir}/cinnamon-dbus-command
%{_bindir}/cinnamon-desktop-editor
%{_bindir}/cinnamon-file-dialog
%{_bindir}/cinnamon-hover-click
%{_bindir}/cinnamon-install-spice
%{_bindir}/cinnamon-json-makepot
%{_bindir}/cinnamon-killer-daemon
%{_bindir}/cinnamon-launcher
%{_bindir}/cinnamon-looking-glass
%{_bindir}/cinnamon-menu-editor
%{_bindir}/cinnamon-preview-gtk-theme
%{_bindir}/cinnamon-screensaver-lock-dialog
%{_bindir}/cinnamon-session-cinnamon
%{_bindir}/cinnamon-session-cinnamon2d
%{_bindir}/cinnamon-settings
%{_bindir}/cinnamon-settings-users
%{_bindir}/cinnamon-slideshow
%{_bindir}/cinnamon-spice-updater
%{_bindir}/cinnamon-subprocess-wrapper
%{_bindir}/cinnamon-xlet-makepot
%{_bindir}/cinnamon2d
%{_bindir}/xlet-about-dialog
%{_bindir}/xlet-settings
%config(noreplace) %{_sysconfdir}/xdg/menus/*
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.Cinnamon.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.Cinnamon.Melange.service
%{_datadir}/dbus-1/services/org.Cinnamon.Slideshow.service
%{_datadir}/desktop-directories/*
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/%{name}-session/sessions/*
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/polkit-1/actions/org.%{name}.settings-users.policy
%{_datadir}/xdg-desktop-portal/x-cinnamon-portals.conf
%{_datadir}/xsessions/*
%{_datadir}/wayland-sessions/*
%{_datadir}/%{name}/
%{_datadir}/%{name}-background-properties
%{_libdir}/%{name}/
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/cinnamon/cinnamon-hotplug-sniffer
%{_libexecdir}/cinnamon/cinnamon-perf-helper
%{_mandir}/man1/*
%{python3_sitelib}/%{name}/

%files calendar-server
%{_bindir}/%{name}-calendar-server
%{_libexecdir}/%{name}/%{name}-calendar-server.py
%{_datadir}/dbus-1/services/org.%{name}.CalendarServer.service

%if 0%{?fedora} && 0%{?fedora} < 40
%files devel-doc
%doc %{_datadir}/gtk-doc/html/*/
%endif

%changelog
%autochangelog
