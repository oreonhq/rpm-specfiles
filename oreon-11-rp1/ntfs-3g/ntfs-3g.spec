%global source0_hash 350d9415c59f7c3fa74e23985ad2d56423c6a168337368f672e2e362d8f295c8
%bcond_with externalfuse
Name:           ntfs-3g
Epoch:          2
Version:        2026.9.28
Release:        1%{?dist}
Summary:        Linux NTFS userspace driver
License:        GPL-2.0-or-later
URL:            https://github.com/tuxera/ntfs-3g
Source0:        https://tuxera.com/opensource/%{name}_ntfsprogs-%{version}.tgz
Patch0:         ntfs-3g_ntfsprogs-2011.10.9-RC-ntfsck-unsupported-return-0.patch
%if %{with externalfuse}
Requires:       fuse
%endif
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       ntfsprogs-fuse = %{epoch}:%{version}-%{release}
Obsoletes:      ntfsprogs-fuse < %{epoch}:%{version}-%{release}
Provides:       fuse-ntfs-3g = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  gnutls-devel
BuildRequires:  libattr-devel
BuildRequires:  libconfig-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libtool
BuildRequires:  libuuid-devel
BuildRequires:  make
# /oreon:deps
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
Obsoletes:      ntfsprogs-devel < 2.0.0-17
%description devel
Headers and libraries for developing applications that use ntfs-3g
functionality.

%package -n ntfsprogs
Summary:        NTFS filesystem libraries and utilities
Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
Provides:       ntfsprogs-gnomevfs = %{epoch}:%{version}-%{release}
Obsoletes:      ntfsprogs-gnomevfs < %{epoch}:%{version}-%{release}
Obsoletes:      ntfsprogs < 2.0.0-17
%description -n ntfsprogs
The ntfsprogs package currently consists of a library and utilities such as
mkntfs, ntfscat, ntfsls, ntfsresize, and ntfsundelete (for a full list of
included utilities see man 8 ntfsprogs after installation).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}%{?subver} -p1

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
pushd %{buildroot}/%{_bindir}
ln -s ntfs-3g ntfsmount
popd
pushd %{buildroot}/%{_sbindir}
ln -s mount.ntfs-3g mount.ntfs-fuse
ln -s mount.ntfs-3g mount.ntfs
ln -s ../bin/ntfsck fsck.ntfs
popd
mv %{buildroot}/sbin/* %{buildroot}/%{_sbindir}
rmdir %{buildroot}/sbin
rm -rf %{buildroot}%{_defaultdocdir}/%{name}/README
%ldconfig_scriptlets libs
%oreon_autofiles ntfsprogs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ntfs-3g-libs -f %{oreon_filedir}/ntfs-3g-libs.list
%files -n ntfs-3g-devel -f %{oreon_filedir}/ntfs-3g-devel.list
%files -n ntfsprogs -f %{oreon_filedir}/ntfsprogs.list

%changelog

%autochangelog
