%global source0_hash 7babff88c97da80ca0f6b1384d894a74a52474855ef3e854788b0dd6ad7b4504
%global _hardened_build 1
Name:           timeshift
Version:        25.12.4
Release:        1%{?dist}
Summary:        System restore tool for Linux
License:        GPL-3.0-or-later OR LGPL-3.0-or-later
URL:            https://github.com/linuxmint/timeshift
Source0:        https://github.com/linuxmint/%{name}/archive/refs/tags/%{version}.tar.gz
Requires:       cronie
Requires:       hicolor-icon-theme
Requires:       polkit
Requires:       psmisc
Requires:       rsync
Recommends:     btrfs-progs
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  vala
# /oreon:deps
%description
Timeshift for Linux is an application that provides functionality similar to
the System Restore feature in Windows and the Time Machine tool in Mac OS.
Timeshift protects your system by taking incremental snapshots of the file
system at regular intervals. These snapshots can be restored at a later date
to undo all changes to the system.

In RSYNC mode, snapshots are taken using rsync and hard-links. Common files
are shared between snapshots which saves disk space. Each snapshot is a full
system backup that can be browsed with a file manager.

In BTRFS mode, snapshots are taken using the in-built features of the BTRFS
filesystem. BTRFS snapshots are supported only on BTRFS systems having an
Ubuntu-type subvolume layout (with @ and @home subvolumes).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
sed -i -e 's@--thread @@g' src/makefile
sed -i -e 's@--Xcc="-O3" @@g' src/makefile
sed -i '/${app_name}-uninstall/d' src/makefile

%build

for flag in %{optflags} %{?__global_ldflags}; do
  VALAFLAGS="$VALAFLAGS -X $flag"
done
sed -i "s|^[\t ]*valac|& --ccode --save-temps -g $VALAFLAGS|" src/makefile
%make_build
for f in `find src/ -type f -name '*.c'`; do
  mv -f $f src/
done
sed -i "s|valac --ccode|valac|" src/makefile
%make_build
%install
%make_install
rm -rf %{buildroot}%{_datadir}/appdata
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gtk.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
