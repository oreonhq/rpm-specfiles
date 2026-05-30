%global source0_hash 2914dbbe1ebc88c7d93ad88e220aa57dabc43d216e11f06221c01edf3cc10732

Summary:	Backup and restore utilities for the XFS filesystem
Name:		xfsdump
Version:	3.2.0
Release:	4%{?dist}
# Licensing based on generic "GNU GENERAL PUBLIC LICENSE"
# in source, with no mention of version.
License:	GPL-1.0-or-later
Source0:        http://kernel.org/pub/linux/utils/fs/xfs/%{name}/%{name}-%{version}.tar.xz
Source1:        http://kernel.org/pub/linux/utils/fs/xfs/%{name}/%{name}-%{version}.tar.sign
Source2:	https://git.kernel.org/pub/scm/docs/kernel/pgpkeys.git/plain/keys/13F703E6C11CF6F0.asc
BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	libtool, gettext, gawk
BuildRequires:	xfsprogs-devel, libuuid-devel, libattr-devel ncurses-devel
BuildRequires:	gnupg2, xz
Requires:	xfsprogs >= 2.6.30, attr >= 2.0.0

%description
The xfsdump package contains xfsdump, xfsrestore and a number of
other utilities for administering XFS filesystems.

xfsdump examines files in a filesystem, determines which need to be
backed up, and copies those files to a specified disk, tape or other
storage medium.	 It uses XFS-specific directives for optimizing the
dump of an XFS filesystem, and also knows how to backup XFS extended
attributes.  Backups created with xfsdump are "endian safe" and can
thus be transfered between Linux machines of different architectures
and also between IRIX machines.

xfsrestore performs the inverse function of xfsdump; it can restore a
full backup of a filesystem.  Subsequent incremental backups can then
be layered on top of the full backup.  Single files and directory
subtrees may be restored from full or partial backups.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
xzcat '%{SOURCE0}' | %{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data=-
%setup -q

%build
%configure

make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DIST_ROOT=$RPM_BUILD_ROOT install
# remove non-versioned docs location
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/xfsdump/

# Bit of a hack to move files from /sbin to /usr/sbin
(cd $RPM_BUILD_ROOT/%{_sbindir}; mv ../../sbin/xfsdump .)
(cd $RPM_BUILD_ROOT/%{_sbindir}; mv ../../sbin/xfsrestore .)

# Create inventory dir (otherwise created @ runtime)
mkdir -p $RPM_BUILD_ROOT/%{_sharedstatedir}/xfsdump/inventory

%find_lang %{name}

%files -f %{name}.lang
%doc README doc/COPYING doc/CHANGES doc/README.xfsdump doc/xfsdump_ts.txt
%{_mandir}/man8/*
%{_sbindir}/*
%{_sharedstatedir}/xfsdump/inventory

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.0-4
- Prepare for Oreon 11 (RP1)
