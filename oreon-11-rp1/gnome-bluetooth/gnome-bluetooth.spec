%global source0_hash 41f20e6d6176b72590af63552b232d83f2fffdd77ecfaa5eaf32c5a4a86fad64
%global libadwaita_version 1.6~beta
%global gtk4_version 4.15.2
Name:		gnome-bluetooth
Epoch:		1
Version:	47.2
Release:        1%{?dist}
Summary:        Bluetooth graphical utilities
License:	GPL-2.0-or-later
URL:		https://wiki.gnome.org/Projects/GnomeBluetooth
Source0:        https://download.gnome.org/sources/%{name}/47/%{name}-%{version}.tar.xz
Provides:	dbus-bluez-pin-helper
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	bluez >= 5.0
Requires:	gtk4 >= %{gtk4_version}
Requires:	libadwaita >= %{libadwaita_version}
%ifnarch s390 s390x
Requires:	pulseaudio-module-bluetooth
Requires:	bluez-obexd
%endif
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(gsound)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  python3-dbusmock
# /oreon:deps
%description
The gnome-bluetooth package contains graphical utilities to setup,
monitor and use Bluetooth devices.

%package libs
Summary:	GTK+ Bluetooth device selection widgets
License:	LGPL-2.1-or-later
%description libs
This package contains libraries needed for applications that
want to display a Bluetooth device selection widget.

%package libs-devel
Summary:	Development files for %{name}-libs
License:	LGPL-2.1-or-later
Requires:	%{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:	%{name}%{?_isa} = %{epoch}:%{version}-%{release}
%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a Bluetooth device selection widget.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{gnome_tarball_version}

%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
%find_lang gnome-bluetooth-3.0
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-bluetooth-libs -f %{oreon_filedir}/gnome-bluetooth-libs.list
%files -n gnome-bluetooth-libs-devel -f %{oreon_filedir}/gnome-bluetooth-libs-devel.list

%changelog

%autochangelog
