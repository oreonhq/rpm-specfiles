%global source0_hash e61edb71344dcd5daa6e7175dfbb274a758be8b58452773569bb35645b85a238
%global po_package %{name}-3.0
Name:           gnome-applets
Version:        3.58.0
Release:        1%{?dist}
Summary:        Small applications for the GNOME Flashback panel
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeApplets
Source0:        https://download.gnome.org/sources/%{name}/3.58/%{name}-%{version}.tar.xz
%ifnarch s390 s390x sparc64 i686
%endif
Requires:       gnome-panel >= 3.41.1
Requires:       hicolor-icon-theme
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  kernel-tools-devel
BuildRequires:  libSM-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(adwaita-icon-theme)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gucharmap-2.90)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libgnome-panel)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  yelp-tools
# /oreon:deps
%description
Gnome Applets component is part of the GnomeFlashback project. It currently
provides the following applets:

- Accessibility applet (accessx-status)
- Battery status (battstat)
- A symbol table (charpick)
- A system monitor for cpu, memory and network usage information (cpufreq)
- A drive mount applet (drivemount)
- Geyes, a funny applet that shows a pair of eyes which follow the cursor
  (geyes)
- A weather applet (gweather)
- A command execution and macro plugin (mini-commander)
- A sound applet (deprecated and replaced by libsound-applet in GnomeFlashback
  (mixer)
- A model lights plugin for modems (modemlights)
- A multi load plugin (multiload)
- A notes applets (stickynotes)
- A trash applet (trashapplet)
- A window picker applet that shows open applications as icons. This saves a lot
  of screen space and is very useful if many applications are open.
  (windowpicker)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf -fiv

%build

%configure                      \
    --disable-scrollkeeper      \
    --disable-static            \
    --enable-gtk-doc            \
    --enable-mini-commander     \
    --enable-suid=no            \
    --with-cpufreq-lib=cpupower \
    --without-hal               \
    %{nil}
%make_build
%install
%make_install
%find_lang %{po_package} --all-name
rm -rf %{buildroot}%{_datadir}/xmodmap
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
