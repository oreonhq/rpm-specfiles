%global source0_hash none

%global tarball_version %(echo %{version} | tr '~' '.')

%global libhandy_version 1.5.0

Name:           gnome-disk-utility
Version:        46.1
Release:        4%{?dist}
Summary:        Disks

License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/GNOME/gnome-disk-utility
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{tarball_version}.tar.xz
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1) >= %{libhandy_version}
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  gettext
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/appstream-util

Requires:       libhandy%{?_isa} >= %{libhandy_version}
Requires:       udisks2

%description
This package contains the Disks and Disk Image Mounter applications.
Disks supports partitioning, file system creation, encryption,
fstab/crypttab editing, ATA SMART and other features

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install
%find_lang %{name}


%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.DiskUtility.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/gnome-disks
%{_bindir}/gnome-disk-image-mounter
%{_datadir}/applications/org.gnome.DiskUtility.desktop
%{_datadir}/applications/gnome-disk-image-mounter.desktop
%{_datadir}/applications/gnome-disk-image-writer.desktop
%{_datadir}/dbus-1/services/org.gnome.DiskUtility.service
%{_datadir}/glib-2.0/schemas/org.gnome.Disks.gschema.xml
%{_datadir}/icons/hicolor/*/apps/gnome-disks*
%{_datadir}/icons/hicolor/*/apps/org.gnome.DiskUtility*
%{_metainfodir}/org.gnome.DiskUtility.appdata.xml
%{_mandir}/man1/gnome-disks.1*
%{_mandir}/man1/gnome-disk-image-mounter.1*
%{_sysconfdir}/xdg/autostart/org.gnome.SettingsDaemon.DiskUtilityNotify.desktop
%{_libexecdir}/gsd-disk-utility-notify


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46.1-4
- Prepare for Oreon 11 (RP1)
