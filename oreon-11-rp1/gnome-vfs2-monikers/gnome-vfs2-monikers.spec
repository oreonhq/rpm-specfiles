%global source0_hash 25acb387efbae8a2f36aab0b4ab19363eb03270923b88b5a860e3fc87799ef3e
%define gnome_vfs_version 2.15.3
%define libbonobo_version 2.3.1
%define gconf_version 1.1.1
%define glib_version 2.9.3
%define orbit_version 2.9.0
Summary:        Monikers for the GNOME virtual file-system
Name: gnome-vfs2-monikers
Version: 2.15.3
Release:        41%{?dist}
License: LGPL-2.0-or-later
Source0:        http://ftp.gnome.org/pub/gnome/sources/gnome-vfs-monikers/2.15/gnome-vfs-monikers-%{version}.tar.bz2
Patch0: gnome-vfs2-monikers-configure-c99.patch
URL: http://www.gnome.org/
Requires:      gnome-vfs2 >= %{gnome_vfs_version}
# oreon:deps
BuildRequires:  GConf2-devel
BuildRequires:  ORBit2-devel
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  gnome-vfs2-devel
BuildRequires:  libbonobo-devel
BuildRequires:  make
BuildRequires:  perl(XML::Parser)
# /oreon:deps
%description
GNOME VFS is the GNOME virtual file system. 
Programs using bonobo can use the monikers provided
in this package to access gnome-vfs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir gnome-vfs-monikers-%{version}
%oreon_prep
%build

%configure 
make 
%install
rm -fr $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT 
rm -f $RPM_BUILD_ROOT%{_libdir}/bonobo/monikers/*.{a,la}
for serverfile in $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server; do
    sed -i -e 's|location *= *"/usr/lib\(64\)*/|location="/usr/$LIB/|' $serverfile
done
%ldconfig_scriptlets
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
