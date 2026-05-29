%global source0_hash none

# Pass --with externalfuse to compile against system fuse lib
# Default is internal fuse-lite.
%bcond_with externalfuse

# For release candidates
# %%global subver -RC

Name:           ntfs-3g
Epoch:          2
Version:        2022.10.3
Release:        1%{?dist}
Summary:        Linux NTFS userspace driver
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/tuxera/ntfs-3g
Source0:        https://download.tuxera.com/opensource/ntfs-3g_ntfsprogs-2022.10.3%{?subver}.tgz
Patch0:         ntfs-3g_ntfsprogs-2011.10.9-RC-ntfsck-unsupported-return-0.patch
# Upstream seems mostly gone, but there are some patches merged after 2022.10.3
Patch1:		https://github.com/tuxera/ntfs-3g/commit/e73d481a76a5814076ff78a1c3a70e9b7da7c0e9.patch
Patch2:		https://github.com/tuxera/ntfs-3g/commit/01b9bddc0c2165baa46abe7562550ef4e8c2752b.patch
Patch3:		https://github.com/tuxera/ntfs-3g/commit/241ddb38605b6b298174e6f1019e8e2502a45558.patch
Patch4:		https://github.com/tuxera/ntfs-3g/commit/1565b01e215c74e5c5f83f3ecde1ed682637dc5a.patch
Patch5:		https://github.com/tuxera/ntfs-3g/commit/233658e5a1599e40bbd8211e64bb98a12751b1ea.patch
Patch6:		https://github.com/tuxera/ntfs-3g/commit/75dcdc2cf37478fad6c0e3427403d198b554951d.patch

BuildRequires:  make
# ntfs-3g BuildRequires
BuildRequires:  gnutls-devel
BuildRequires:  libattr-devel
%if %{with externalfuse}
BuildRequires:  fuse-devel
Requires:       fuse
%endif
# ntfsprogs BuildRequires
BuildRequires:  libconfig-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       ntfsprogs-fuse = %{epoch}:%{version}-%{release}
Obsoletes:      ntfsprogs-fuse < %{epoch}:%{version}-%{release}
Provides:       fuse-ntfs-3g = %{epoch}:%{version}-%{release}
%if 0%{?fedora}
Recommends:     ntfs-3g-system-compression
%endif

%description
NTFS-3G is a stable, open source, GPL licensed, POSIX, read/write NTFS
driver for Linux and many other operating systems. It provides safe
handling of the Windows XP, Windows Server 2003, Windows 2000, Windows
Vista, Windows Server 2008 and Windows 7 NTFS file systems. NTFS-3G can
create, remove, rename, move files, directories, hard links, and streams;
it can read and write normal and transparently compressed files, including
streams and sparse files; it can handle special files like symbolic links,
devices, and FIFOs, ACL, extended attributes; moreover it provides full
file access right and ownership support.

%package libs
Summary:        Runtime libraries for ntfs-3g

%description libs
Libraries for applications to use ntfs-3g functionality.

%package devel
Summary:        Development files and libraries for ntfs-3g
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       ntfsprogs-devel = %{epoch}:%{version}-%{release}
# ntfsprogs-2.0.0-17 was never built. 2.0.0-16 was the last build for that
# standalone package.
Obsoletes:      ntfsprogs-devel < 2.0.0-17

%description devel
Headers and libraries for developing applications that use ntfs-3g
functionality.

%package -n ntfsprogs
Summary:        NTFS filesystem libraries and utilities
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# We don't really provide this. This code is dead and buried now.
Provides:       ntfsprogs-gnomevfs = %{epoch}:%{version}-%{release}
Obsoletes:      ntfsprogs-gnomevfs < %{epoch}:%{version}-%{release}
# Needed to fix multilib issue
# ntfsprogs-2.0.0-17 was never built. 2.0.0-16 was the last build for that
# standalone package.
Obsoletes:      ntfsprogs < 2.0.0-17

%description -n ntfsprogs
The ntfsprogs package currently consists of a library and utilities such as
mkntfs, ntfscat, ntfsls, ntfsresize, and ntfsundelete (for a full list of
included utilities see man 8 ntfsprogs after installation).

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}_ntfsprogs-%{version}%{?subver} -p1


%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
%configure \
	--disable-static \
	--disable-ldconfig \
%if %{with externalfuse}
	--with-fuse=external \
%endif
	--exec-prefix=/ \
	--enable-posix-acls \
	--enable-xattr-mappings \
	--enable-crypto \
	--enable-extras \
	--enable-quarantined
%make_build LIBTOOL=%{_bindir}/libtool


%install
%make_install LIBTOOL=%{_bindir}/libtool

find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_libdir}/*.a

rm -rf %{buildroot}/%{_sbindir}/mount.ntfs-3g
cp -a %{buildroot}/%{_bindir}/ntfs-3g %{buildroot}/%{_sbindir}/mount.ntfs-3g

# Actually make some symlinks for simplicity...
# ... since we're obsoleting ntfsprogs-fuse
pushd %{buildroot}/%{_bindir}
ln -s ntfs-3g ntfsmount
popd
pushd %{buildroot}/%{_sbindir}
ln -s mount.ntfs-3g mount.ntfs-fuse
# And since there is no other package in Fedora that provides an ntfs
# mount...
ln -s mount.ntfs-3g mount.ntfs
# Need this for fsck to find it
ln -s ../bin/ntfsck fsck.ntfs
popd

mv %{buildroot}/sbin/* %{buildroot}/%{_sbindir}
rmdir %{buildroot}/sbin

# We get this on our own, thanks.
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/README

%ldconfig_scriptlets libs

%files
%doc AUTHORS ChangeLog CREDITS NEWS README
%license COPYING
%{_sbindir}/mount.ntfs
%{_sbindir}/mount.ntfs-3g
%{_sbindir}/mount.ntfs-fuse
%{_sbindir}/mount.lowntfs-3g
%{_bindir}/ntfs-3g
%{_bindir}/ntfsmount
%{_bindir}/ntfs-3g.probe
%{_bindir}/lowntfs-3g
%{_mandir}/man8/mount.lowntfs-3g.*
%{_mandir}/man8/mount.ntfs-3g.*
%{_mandir}/man8/ntfs-3g*

%files libs
%license COPYING
%{_libdir}/libntfs-3g.so.*

%files devel
%{_includedir}/ntfs-3g/
%{_libdir}/libntfs-3g.so
%{_libdir}/pkgconfig/libntfs-3g.pc

%files -n ntfsprogs
%doc AUTHORS CREDITS ChangeLog NEWS README
%license COPYING
%{_bindir}/ntfscat
%{_bindir}/ntfscluster
%{_bindir}/ntfscmp
%{_bindir}/ntfsfix
%{_bindir}/ntfsinfo
%{_bindir}/ntfsls
%{_bindir}/ntfssecaudit
%{_bindir}/ntfsusermap
# Extras
%{_bindir}/ntfsck
%{_bindir}/ntfsdecrypt
%{_bindir}/ntfsdump_logfile
%{_bindir}/ntfsfallocate
%{_bindir}/ntfsmftalloc
%{_bindir}/ntfsmove
%{_bindir}/ntfsrecover
%{_bindir}/ntfstruncate
%{_bindir}/ntfswipe
%{_sbindir}/fsck.ntfs
%{_sbindir}/mkfs.ntfs
%{_sbindir}/mkntfs
%{_sbindir}/ntfsclone
%{_sbindir}/ntfscp
%{_sbindir}/ntfslabel
%{_sbindir}/ntfsresize
%{_sbindir}/ntfsundelete
%{_mandir}/man8/mkntfs.8*
%{_mandir}/man8/mkfs.ntfs.8*
%{_mandir}/man8/ntfs[^m][^o]*.8*
%exclude %{_mandir}/man8/ntfs-3g*

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:2022.10.3-1
- Import Fedora rawhide ntfs-3g (2022.10.3-12), HTTPS Source0 on download.tuxera.com, local Patch0

