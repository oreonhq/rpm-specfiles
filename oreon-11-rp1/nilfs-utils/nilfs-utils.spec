%global source0_hash 8602897ff0d2c49be9bc76311f0b102088e58b6de4f749009403de06ff2c34cd

Name:		nilfs-utils
Version:	2.2.11
Release:	8%{?dist}
Summary:	Utilities for managing NILFS v2 filesystems

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://nilfs.sourceforge.net
Source0:	http://nilfs.sourceforge.net/download/%{name}-%{version}.tar.bz2
Source1:	http://nilfs.sourceforge.net/download/%{name}-%{version}.tar.bz2.asc
Source2:	8B055AE86DEFF458.asc
BuildRequires: make
BuildRequires:	gcc, libuuid-devel, libmount-devel, gnupg2

%description
Userspace utilities for creating and mounting NILFS v2 filesystems.

%package devel
Summary:	NILFS2 filesystem-specific headers
Requires:	nilfs-utils = %{version}-%{release}

%description devel
nilfs-utils-devel contains the header files needed to develop NILFS
filesystem-specific programs.

You should install nilfs-utils-devel if you want to develop NILFS
filesystem-specific programs. If you install nilfs-utils-devel, you'll
also want to install nilfs-utils.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
# geez, make install is trying to run ldconfig on the system
%configure LDCONFIG=/bin/true --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT sbindir=%_sbindir root_sbindir=%_sbindir
rm -f $RPM_BUILD_ROOT/%{_libdir}/libnilfs*.la

%ldconfig_scriptlets

%files
%doc COPYING ChangeLog
%config(noreplace) /etc/nilfs_cleanerd.conf
%{_sbindir}/mkfs.nilfs2
%{_sbindir}/mount.nilfs2
%{_sbindir}/nilfs_cleanerd
%{_sbindir}/umount.nilfs2
%{_sbindir}/nilfs-tune
%{_sbindir}/nilfs-clean
%{_sbindir}/nilfs-resize
%{_libdir}/libnilfscleaner.so.*
%{_libdir}/libnilfsgc.so.*
%{_libdir}/libnilfs.so.*
%{_bindir}/chcp
%{_bindir}/dumpseg
%{_bindir}/lscp
%{_bindir}/lssu
%{_bindir}/mkcp
%{_bindir}/rmcp
%{_mandir}/man1/lscp.1.gz
%{_mandir}/man1/lssu.1.gz
%{_mandir}/man5/nilfs_cleanerd.conf.5.gz
%{_mandir}/man8/chcp.8.gz
%{_mandir}/man8/dumpseg.8.gz
%{_mandir}/man8/mkcp.8.gz
%{_mandir}/man8/mkfs.nilfs2.8.gz
%{_mandir}/man8/mount.nilfs2.8.gz
%{_mandir}/man8/nilfs.8.gz
%{_mandir}/man8/nilfs_cleanerd.8.gz
%{_mandir}/man8/rmcp.8.gz
%{_mandir}/man8/umount.nilfs2.8.gz
%{_mandir}/man8/nilfs-tune.8.gz
%{_mandir}/man8/nilfs-clean.8.gz
%{_mandir}/man8/nilfs-resize.8.gz

%files devel
%{_libdir}/libnilfs.so
%{_libdir}/libnilfscleaner.so
%{_libdir}/libnilfsgc.so
%{_includedir}/nilfs.h
%{_includedir}/nilfs_cleaner.h

%changelog
%autochangelog
