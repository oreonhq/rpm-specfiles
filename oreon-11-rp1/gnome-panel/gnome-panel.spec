%global source0_hash 7e8bca43a81a134c666b3a78baf2affb0c5d30efb1bca653887fc41b31dd5e64
%global po_package %{name}-3.0
%global use_evolution_data_server 1
Name:           gnome-panel
Version:        3.58.1
Release:        1%{?dist}
Summary:        GNOME Flashback panel
License:        GPL-2.0-or-later and LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/GnomePanel
Source0:        https://download.gnome.org/sources/%{name}/3.58/%{name}-%{version}.tar.xz
Requires:       gnome-desktop3
Requires:       gnome-menus >= 3.7.90
Requires:       evolution-data-server >= 3.33.2
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       hicolor-icon-theme
Suggests:       %{name}-doc
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  gtk-doc
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libgnome-menu-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  yelp-tools
# /oreon:deps
%description
Gnome Panel is a component that is part of GnomeFlashback and provides panels
and default applets for the desktop. A panel is a horizontal or vertical bar
that can be added to each side of the screen. By default there is one panel on
the top of the screen and one on the bottom, but this is configurable. The
panels are used to add applets such as a menu bar to open applications, a clock
and indicator applets which provide access to configure features of the system
such as the network, sound or the current keyboard layout. On the bottom panel
there is usually a list of open applications.

# libs package
%package        libs
Summary:        Libraries for %{name}
License:        LGPLv2+
%description    libs
Libraries for %{name}.

# devel package
%package        devel
Summary:        Devel files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
Devel files for %{name}.

# doc package
%package        doc
Summary:        Docs for %{name}
BuildArch:      noarch
%description    doc
Docs for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
rm -f libtool
autoreconf -fiv

%build

%configure              \
    --enable-gtk-doc    \
    --enable-eds=yes
%make_build
%install
%make_install
rm -rf %{buildroot}/var/scrollkeeper
find %{buildroot} -name '*.la' -delete;
%find_lang %{po_package} --all-name
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list
%files -n gnome-panel-libs -f %{oreon_filedir}/gnome-panel-libs.list
%files -n gnome-panel-devel -f %{oreon_filedir}/gnome-panel-devel.list
%files -n gnome-panel-doc -f %{oreon_filedir}/gnome-panel-doc.list

%changelog

%autochangelog
