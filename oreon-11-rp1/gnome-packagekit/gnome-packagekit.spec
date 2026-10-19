%global source0_hash cda455a652a923b2ea2f70316bd0fdd8296f7b62eef3fafd9ce50c8e66c5f195
Name:      gnome-packagekit
Version:   43.0
Release:        9%{?dist}
Summary:        Session applications to manage packages
License:   GPL-2.0-or-later
URL:       https://www.freedesktop.org/software/PackageKit/
Source0:        http://download.gnome.org/sources/gnome-packagekit/43/%{name}-%{version}.tar.xz
Requires: %{name}-installer
Requires: %{name}-updater
# oreon:deps
BuildRequires:  PackageKit-devel
BuildRequires:  appstream
BuildRequires:  cairo-devel
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-utils
BuildRequires:  fontconfig-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  itstool
BuildRequires:  libcanberra-devel
BuildRequires:  libgudev1-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  polkit-devel
BuildRequires:  startup-notification-devel
BuildRequires:  systemd-devel
BuildRequires:  xorg-x11-proto-devel
# /oreon:deps
%description
gnome-packagekit provides session applications for the PackageKit API.
There are several utilities designed for installing, updating and
removing packages on your system.

%package common
Summary: Common files required for %{name}
Requires:  adwaita-icon-theme
Requires:  PackageKit%{?_isa} >= 0.5.0
Requires:  PackageKit-libs >= 0.5.0
Requires:  shared-mime-info
Requires:  iso-codes
Requires:  libcanberra%{?_isa} >= 0.10
%description common
Files shared by all subpackages of %{name}

%package installer
Summary: PackageKit package installer
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%description installer
A graphical package installer for PackageKit which is used to manage software
not shown in GNOME Software.

%package updater
Summary: PackageKit package updater
Requires: %{name}-common%{?_isa} = %{version}-%{release}
%description updater
A graphical package updater for PackageKit which is used to update packages
without rebooting.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%meson
%meson_build
%install
%meson_install
%find_lang %name --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-packagekit-common -f %{oreon_filedir}/gnome-packagekit-common.list
%files -n gnome-packagekit-installer -f %{oreon_filedir}/gnome-packagekit-installer.list
%files -n gnome-packagekit-updater -f %{oreon_filedir}/gnome-packagekit-updater.list

%changelog

%autochangelog
