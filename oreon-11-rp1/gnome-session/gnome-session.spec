%global source0_hash 5195c4f60542a953ab6ebd288f3785b8e7746292d8c167e0c99d353438a184d1
%define po_package gnome-session
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d "." -f 1)
Name:           gnome-session
Version:        51.0
Release:        1%{?dist}
Summary:        GNOME session manager
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-session
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
Patch:          0001-Fedora-Set-grub-boot-flags-on-shutdown-reboot.patch
Requires: dconf
Requires: gsettings-desktop-schemas >= 0.1.7
Requires: dbus
Conflicts: gnome-desktop3 < 44.4-2
Conflicts: shared-mime-info < 2.0-4
Requires: shared-mime-info
# oreon:deps
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  xmlto
# /oreon:deps
%description
gnome-session manages a GNOME desktop or GDM login session. It starts up
the other core GNOME components and handles logout and saving the session.

%package wayland-session
Summary: Desktop file for wayland based gnome session
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: xorg-x11-server-Xwayland%{?_isa} >= 1.20.99.1
Requires: gnome-shell
Obsoletes: gnome-session-xsession < %{version}-%{release}
%description wayland-session
Desktop file to add GNOME on wayland to display manager session menu.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{po_package}
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gnome-session-wayland-session -f %{oreon_filedir}/gnome-session-wayland-session.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50.0-1
- Prepare for Oreon 11 (RP1)
