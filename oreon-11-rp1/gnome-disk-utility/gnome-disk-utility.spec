%global source0_hash c24e9439a04d70bcfae349ca134c7005435fe2b6f452114df878bff0b89bbffe
%global tarball_version %(echo %{version} | tr '~' '.')
%global libhandy_version 1.5.0
Name:           gnome-disk-utility
Version:        46.1
Release:        4%{?dist}
Summary:        Disks
License:        GPL-2.0-or-later AND CC0-1.0
URL:            https://gitlab.gnome.org/GNOME/gnome-disk-utility
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{version}.tar.xz
Requires:       libhandy%{?_isa} >= %{libhandy_version}
Requires:       udisks2
# oreon:deps
BuildRequires:  /usr/bin/appstream-util
BuildRequires:  /usr/bin/desktop-file-validate
BuildRequires:  /usr/bin/xsltproc
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(dvdread)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(udisks2)
# /oreon:deps
%description
This package contains the Disks and Disk Image Mounter applications.
Disks supports partitioning, file system creation, encryption,
fstab/crypttab editing, ATA SMART and other features

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.DiskUtility.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 46.1-4
- Prepare for Oreon 11 (RP1)
