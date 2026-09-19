%global source0_hash 62de64b5b804eb04104ff98fcd6a8b7276d510a49fbd9c0feb568f8996444faa

%define po_package gnome-vfs-2.0

# don't use HAL from F-16 on
%if 0%{?fedora} >= 16 || 0%{?rhel} >= 7
%bcond_with hal
%else
%bcond_without hal
%endif

# trim changelog included in binary rpms
%global _changelog_trimtime %(date +%s -d "1 year ago")

Summary: The GNOME virtual file-system libraries
Name: gnome-vfs2
Version: 2.24.4
Release: 50%{?dist}
License: LGPL-2.0-or-later and GPL-2.0-or-later
# the daemon and the library are LGPLv2+
# the modules are LGPLv2+ and GPLv2+
#VCS: git:git://git.gnome.org/gnome-vfs
Source0: http://download.gnome.org/sources/gnome-vfs/2.24/gnome-vfs-%{version}.tar.bz2
URL: http://www.gnome.org/
BuildRequires: GConf2-devel 
BuildRequires: libxml2-devel, zlib-devel
BuildRequires: glib2-devel 
BuildRequires: popt, bzip2-devel, ORBit2-devel, openjade
BuildRequires: pkgconfig
BuildRequires: automake
BuildRequires: libtool
BuildRequires: intltool
BuildRequires: autoconf
BuildRequires: gtk-doc 
BuildRequires: perl-XML-Parser 
BuildRequires: libsmbclient-devel 
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: pkgconfig(avahi-client) pkgconfig(avahi-glib)
%if %{with hal}
BuildRequires: hal-devel
%endif
BuildRequires: dbus-devel 
BuildRequires: dbus-glib-devel 
BuildRequires: gettext
BuildRequires: libacl-devel
BuildRequires: libselinux-devel
BuildRequires: keyutils-libs-devel
BuildRequires: make

Requires: %{name}-common = %{version}-%{release}

Patch3: gnome-vfs-2.9.90-modules-conf.patch

# remove gnome-mime-data dependency
Patch4: gnome-vfs-2.24.1-disable-gnome-mime-data.patch

# CVE-2009-2473 neon, gnome-vfs2 embedded neon: billion laughs DoS attack
# https://bugzilla.redhat.com/show_bug.cgi?id=518215
Patch5: gnome-vfs-2.24.3-CVE-2009-2473.patch

# send to upstream
Patch101:	gnome-vfs-2.8.2-schema_about_for_upstream.patch

# Default
Patch104:	gnome-vfs-2.8.2-browser_default.patch

# Applied upstream.
# Patch201: gnome-vfs-2.8.1-console-mount-opt.patch

# RH bug #197868
Patch6: gnome-vfs-2.15.91-mailto-command.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=333041
# https://bugzilla.redhat.com/show_bug.cgi?id=335241
Patch300: gnome-vfs-2.20.0-ignore-certain-mountpoints.patch

# backported from upstream

# gnome-vfs-daemon exits on dbus, and constantly restarted causing dbus/hal to hog CPU
# https://bugzilla.redhat.com/show_bug.cgi?id=486286
Patch404: gnome-vfs-2.24.xx-utf8-mounts.patch

# https://bugzilla.gnome.org/show_bug.cgi?id=435653
Patch405: 0001-Add-default-media-application-schema.patch
Patch406: gnome-vfs2-configure-c99.patch
Patch407: gnome-vfs2-c99.patch

# from upstream
Patch7: gnome-vfs-2.24.5-file-method-chmod-flags.patch

# fix compilation against new glib2
Patch8: gnome-vfs-2.24.4-enable-deprecated.patch

Patch9: openssl.patch

%description
GNOME VFS is the GNOME virtual file system. It is the foundation of
the Nautilus file manager. It provides a modular architecture and
ships with several modules that implement support for file systems,
http, ftp, and others. It provides a URI-based API, backend
supporting asynchronous file operations, a MIME type manipulation
library, and other features.

DEPRECATED in favor of GIO.

%package common
Summary: Common files for %{name}
Requires: %{name} = %{version}-%{release}
Requires(post): GConf2
Requires(pre): GConf2
Requires(preun): GConf2
BuildArch: noarch
%description common
%{summary}.

%package devel
Summary: Libraries and include files for developing GNOME VFS applications
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the necessary development libraries for writing
GNOME VFS modules and applications that use the GNOME VFS APIs.

%package smb
Summary: Windows fileshare support for gnome-vfs
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description smb
This package provides support for reading and writing files on windows
shares (SMB) to applications using GNOME VFS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gnome-vfs-%{version} 

%patch -P3 -p1 -b .modules-conf
%patch -P4 -p1 -b .mime-data
%patch -P5 -p1 -b .CVE-2009-2473

%patch -P6 -p1 -b .mailto-command
%patch -P7 -p1 -b .file-method-chmod-flags
%patch -P8 -p1 -b .enable-deprecated
%patch -P9 -p0 -b .openssl11

# send to upstream
%patch -P101 -p1 -b .schema_about

%patch -P104 -p1 -b .browser_default

%patch -P300 -p1 -b .ignore-certain-mount-points

%patch -P404 -p1 -b .utf8-mounts

%patch -P405 -p1 -b .default-media
%patch -P406 -p1
%patch -P407 -p1

%build
# for patch 10 and 4
libtoolize --force  || :
aclocal  || :
autoheader  || :
automake --add-missing || :
autoconf  || :

if pkg-config openssl ; then
	CPPFLAGS=`pkg-config --cflags openssl`; export CPPFLAGS
	LDFLAGS=`pkg-config --libs-only-L openssl`; export LDFLAGS
fi

CFLAGS="%optflags -fno-strict-aliasing -std=gnu17" \
%configure \
    --with-samba-includes=`pkg-config --variable=includedir smbclient` \
    --enable-samba \
    --disable-fam \
    --disable-gtk-doc \
%if %{with hal}
    --enable-hal \
%endif
    --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

# strip unneeded translations from .mo files
# ideally intltool (ha!) would do that for us
# http://bugzilla.gnome.org/show_bug.cgi?id=474987
cd po
grep -v ".*[.]desktop[.]in[.]in$\|.*[.]server[.]in[.]in$" POTFILES.in > POTFILES.keep
mv POTFILES.keep POTFILES.in
intltool-update --pot
PO_FAKE_DATE="2009-08-03 18:00+0200"   # fake this to be equal in every build
PO_FAKE_DATE_EXPR='\(.*POT-Creation-Date: *\)\(.*\)\(\\n.*\)'
sed --in-place "s/${PO_FAKE_DATE_EXPR}/\1${PO_FAKE_DATE}\3/" %{po_package}.pot
for p in *.po; do
  msgmerge $p %{po_package}.pot > $p.out
  msgfmt -o `basename $p .po`.gmo $p.out
done

%install
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
unset GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL

find $RPM_BUILD_ROOT -name '*.la' -exec rm -fv {} ';'

mv %{buildroot}%{_datadir}/dbus-1/services/gnome-vfs-daemon.service %{buildroot}%{_datadir}/dbus-1/services/org.gnome.GnomeVFS.Daemon.service

%find_lang %{po_package}

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING COPYING.LIB NEWS README
%{_bindir}/gnomevfs-*
%{_libexecdir}/gnome-vfs-daemon
%{_datadir}/dbus-1/services/org.gnome.GnomeVFS.Daemon.service
%{_libdir}/libgnomevfs-2.so.0*
%dir %{_libdir}/gnome-vfs-2.0
%dir %{_libdir}/gnome-vfs-2.0/modules
%{_libdir}/gnome-vfs-2.0/modules/libbzip2.so
%{_libdir}/gnome-vfs-2.0/modules/libcomputer.so
%{_libdir}/gnome-vfs-2.0/modules/libdns-sd.so
%{_libdir}/gnome-vfs-2.0/modules/libfile.so
%{_libdir}/gnome-vfs-2.0/modules/libftp.so
%{_libdir}/gnome-vfs-2.0/modules/libgzip.so
%{_libdir}/gnome-vfs-2.0/modules/libhttp.so
%{_libdir}/gnome-vfs-2.0/modules/libnetwork.so
%{_libdir}/gnome-vfs-2.0/modules/libnntp.so
%{_libdir}/gnome-vfs-2.0/modules/libsftp.so
%{_libdir}/gnome-vfs-2.0/modules/libtar.so
%{_libdir}/gnome-vfs-2.0/modules/libvfs-test.so

%post common
%gconf_schema_upgrade system_http_proxy system_dns_sd system_smb desktop_gnome_url_handlers desktop_default_applications

%pre common
%gconf_schema_prepare system_http_proxy system_dns_sd system_smb desktop_gnome_url_handlers desktop_default_applications

%preun common
%gconf_schema_remove system_http_proxy system_dns_sd system_smb desktop_gnome_url_handlers desktop_default_applications

%files common -f %{po_package}.lang
%dir %{_sysconfdir}/gnome-vfs-2.0
%dir %{_sysconfdir}/gnome-vfs-2.0/modules
%config %{_sysconfdir}/gnome-vfs-2.0/modules/default-modules.conf
%config %{_sysconfdir}/gnome-vfs-2.0/modules/ssl-modules.conf
%{_sysconfdir}/gconf/schemas/*.schemas

%files devel
%{_libdir}/libgnomevfs-2.so
%{_libdir}/pkgconfig/gnome-vfs-2.0.pc
%{_libdir}/pkgconfig/gnome-vfs-module-2.0.pc
%{_libdir}/gnome-vfs-2.0/include/
%{_includedir}/gnome-vfs-2.0/
%{_includedir}/gnome-vfs-module-2.0/
%{_datadir}/gtk-doc/html/gnome-vfs-2.0/

%files smb
%{_libdir}/gnome-vfs-2.0/modules/libsmb.so
%config %{_sysconfdir}/gnome-vfs-2.0/modules/smb-module.conf

%changelog
%autochangelog
