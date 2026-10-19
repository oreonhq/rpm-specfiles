%global source0_hash dd8e6c255fd3bed5eeb190b59027c88b38e63c1be0932ddce9cfeb48f3c43d0f
%global avahi_version 0.6
%global fuse_version 3.0.0
%global glib2_version 2.70.0
%global gsettings_desktop_schemas_version 3.33.0
%global goa_version 3.53.1
%global gudev_version 147
%global libarchive_version 3.0.22
%global libcdio_paranoia_version 0.78.2
%global libgcrypt_version 1.2.2
%global libgphoto2_version 2.5.0
%global libimobiledevice_version 1.2
%global libmtp_version 1.1.15
%global libnfs_version 1.9.8
%global libplist_version 2.2
%global libsmbclient_version 4.12.0
%global libsoup_version 3.0.0
%global libusb_version 1.0.21
%global systemd_version 206
%global talloc_version 1.3.0
%global udisks2_version 1.97
%global major_minor_version %(echo %{version} | cut -d "." -f 1-2)
Name:    gvfs
Version: 1.62.0
Release:        1%{?dist}
Summary:        Backends for the gio framework in GLib
License: LGPL-2.0-or-later AND GPL-3.0-only AND MPL-2.0 AND BSD-3-Clause-Sun
URL:     https://wiki.gnome.org/Projects/gvfs
Source0:        https://download.gnome.org/sources/%{name}/%{major_minor_version}/%{name}-%{version}.tar.xz
Requires: %{name}-client%{?_isa} = %{version}-%{release}
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gsettings-desktop-schemas >= %{gsettings_desktop_schemas_version}
Requires: polkit
Requires: udisks2 >= %{udisks2_version}
Requires: /usr/bin/wsdd
Obsoletes: gnome-mount <= 0.8
Obsoletes: gnome-mount-nautilus-properties <= 0.8
Obsoletes: gvfs-obexftp < 1.17.91-2
Obsoletes: gvfs-devel < 1.55.1-1
Obsoletes: gvfs-tests < 1.55.1-3
%ifarch s390 s390x
Obsoletes: gvfs-gphoto2 < 1.55.1-4
Obsoletes: gvfs-mtp < 1.55.1-4
%endif
# oreon:deps
BuildRequires:  /usr/bin/ssh
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libexif-devel
BuildRequires:  libsmbclient-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(talloc)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  systemd-devel
# /oreon:deps
%description
The gvfs package provides backend implementations for the gio
framework in GLib. It includes ftp, sftp, cifs.

%package client
Summary: Client modules of backends for the gio framework in GLib
Conflicts: %{name} < 1.25.2-2
%description client
The gvfs package provides client modules of backend implementations for the gio
framework in GLib.

%package fuse
Summary: FUSE support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(fuse3) >= %{fuse_version}
Requires: fuse3 >= %{fuse_version}
%description fuse
This package provides support for applications not using gio
to access the gvfs filesystems.

%package smb
Summary: Windows fileshare support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: libsmbclient-devel >= %{libsmbclient_version}
BuildRequires: pkgconfig(talloc) >= %{talloc_version}
%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using gvfs.

%ifnarch s390 s390x
%package gphoto2
Summary: gphoto2 support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libgphoto2) >= %{libgphoto2_version}
BuildRequires: libexif-devel
%description gphoto2
This package provides support for reading and writing files on
PTP based cameras (Picture Transfer Protocol) and MTP based
media players (Media Transfer Protocol) to applications using gvfs.

%endif

%ifnarch s390 s390x
%package mtp
Summary: MTP support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(libmtp) >= %{libmtp_version}
BuildRequires: pkgconfig(libusb-1.0) >= %{libusb_version}
%description mtp
This package provides support for reading and writing files on
MTP based devices (Media Transfer Protocol) to applications using gvfs.
%endif

%package goa
Summary: GOA support for gvfs
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-client%{?_isa} = %{version}-%{release}
BuildRequires: pkgconfig(goa-1.0) >= %{goa_version}
%description goa
This package provides seamless integration with gnome-online-accounts
file services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
       -Dman=true \
%ifarch s390 s390x
       -Dafc=false \
       -Dgphoto2=false \
       -Dlibusb=false \
       -Dmtp=false \
%endif
        %{nil}
%meson_build
%install
%meson_install
cp -p daemon/trashlib/COPYING COPYING.GPL3
%find_lang gvfs
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

killall -USR1 gvfsd >&/dev/null || :
%post smb

killall -USR1 gvfsd >&/dev/null || :
%ifnarch s390 s390x
%post gphoto2

killall -USR1 gvfsd >&/dev/null || :
%post mtp

killall -USR1 gvfsd >&/dev/null || :
%endif
%post goa

killall -USR1 gvfsd >&/dev/null || :
%ifnarch s390 s390x
%endif
%files -f %{oreon_filedir}/main.list
%files -n gvfs-client -f %{oreon_filedir}/gvfs-client.list
%files -n gvfs-fuse -f %{oreon_filedir}/gvfs-fuse.list
%files -n gvfs-smb -f %{oreon_filedir}/gvfs-smb.list
%files -n gvfs-gphoto2 -f %{oreon_filedir}/gvfs-gphoto2.list
%files -n gvfs-mtp -f %{oreon_filedir}/gvfs-mtp.list
%files -n gvfs-goa -f %{oreon_filedir}/gvfs-goa.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.60.0-1
- Prepare for Oreon 11 (RP1)
