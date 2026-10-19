%global source0_hash 6c949e52c8becc2054daacd604901f66ce5cf709a5fa91c4bb7cacc939b53ea9
Name:		gnome-bluetooth3.34
Version:	3.34.5
Release:        11%{?dist}
Summary:        Bluetooth graphical utilities
License:	GPL-2.0-or-later
URL:		https://wiki.gnome.org/Projects/GnomeBluetooth
Source0:        https://download.gnome.org/sources/gnome-bluetooth/3.34/gnome-bluetooth-%{version}.tar.xz
Patch0:         0001-Fix-build-newer-meson.patch
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	bluez >= 5.0
%ifnarch s390 s390x
Requires:	pulseaudio-module-bluetooth
%endif
# oreon:deps
BuildRequires:  gettext
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  python3-dbusmock
BuildRequires:  systemd-devel
# /oreon:deps
%description
The gnome-bluetooth3.34 package contains graphical utilities to setup,
monitor and use Bluetooth devices using the old 3.34 gnome-bluetooth API.

%package libs
Summary:	GTK+ Bluetooth device selection widgets
License:	LGPLv2+
%description libs
This package contains libraries needed for applications that
want to display a Bluetooth device selection widget using the old 3.34
gnome-bluetooth API.

%package libs-devel
Summary:	Development files for %{name}-libs
License:	LGPLv2+
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description libs-devel
This package contains the libraries and header files that are needed
for writing applications that require a Bluetooth device selection widget.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gnome-bluetooth-%{version}
%oreon_prep
%build

%meson -Dgtk_doc=true
%meson_build
%install
%meson_install
rm $RPM_BUILD_ROOT/%{_bindir}/bluetooth-sendto \
  $RPM_BUILD_ROOT/%{_datadir}/applications/bluetooth-sendto.desktop \
  $RPM_BUILD_ROOT/%{_mandir}/man1/bluetooth-sendto.1*
%find_lang gnome-bluetooth2
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-bluetooth3.34-libs -f %{oreon_filedir}/gnome-bluetooth3.34-libs.list
%files -n gnome-bluetooth3.34-libs-devel -f %{oreon_filedir}/gnome-bluetooth3.34-libs-devel.list

%changelog

%autochangelog
