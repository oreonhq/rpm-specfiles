%global source0_hash 6d2e6efaf73fa97065fc8fd58493800797ba02c905b01cc535e248b43f5610fa

Summary: Automount utilities including an updated version of Amd
Name: am-utils
Version: 6.2.0
%define upstream_version 6.2
Release: 63%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
Epoch: 5
URL: http://am-utils.org
# Git repository git://git.fsl.cs.sunysb.edu/am-utils-6.2.git
Source: ftp://ftp.am-utils.org/pub/am-utils/am-utils-%{upstream_version}.tar.gz
Source1: amd.service
Source2: am-utils.conf
Source3: am-utils.sysconf
Source4: am-utils.net.map

BuildRequires: gdbm-devel
BuildRequires: openldap-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: bison
BuildRequires: flex
BuildRequires: systemd-units
BuildRequires: texinfo
BuildRequires: gcc
BuildRequires: m4
BuildRequires: libtirpc-devel
BuildRequires: kernel-headers
#BuildRequires: libnsl2-devel
BuildRequires: rpcsvc-proto-devel
BuildRequires: make

Requires: rpcbind
Requires: grep
Requires: gawk
Requires: findutils
Requires: libtirpc
#Requires: libnsl2

Requires(pre):    /usr/bin/grep
Requires(post):   systemd-sysv
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

# Fix problems with possible future libtool rebases (#1181698)
Patch1: am-utils-6.2-dont-include-auto-generated-macros-in-aclinlude_m4.patch
Patch2: am-utils-6.2-print_nfs_common_args-is-only-needed-with-DEBUG.patch
Patch3: am-utils-6.2-uid_t-might-be-a-different-size-than-unsigned-int.patch
Patch4: am-utils-6.2-remove-set-but-not-used-variable-s.patch
Patch5: am-utils-6.2-remove-set-but-not-used-variable-again.patch
Patch6: am-utils-6.2-remove-unused-function-show_map.patch
Patch7: am-utils-6.2-remove-set-but-not-used-variable-mp_error.patch
Patch8: am-utils-6.2-32-bit-fixes.patch
Patch9: am-utils-6.2-make-sure-variables-are-initialized.patch
Patch10: am-utils-6.2-dont-use-logical-double-ampersand-when-ampersand-is-meant.patch
Patch11: am-utils-6.2-Fix-nfs-args-setting-code.patch

Patch12: am-utils-6.2-add-debug-log-trace-to-NFSv3-readdirplus.patch
Patch13: am-utils-6.2-fix-NFSv3-access-method-return-on-non-existent-mount-point.patch
Patch14: am-utils-6.2-fix-NFSv3-lookup-dir-attribute-return-value.patch
Patch15: am-utils-6.2-fix-NFSv3-readdir-post_op_dir-attributes-return.patch
Patch16: am-utils-6.2-fix-NFSv3-unlink3_or_rmdir3-post_op-attributes-return.patch

Patch17: am-utils-6.2-fix-Linux-NFS-recognition-of-umounts.patch
Patch18: am-utils-6.2-add-get_nfs_xprt-and-put_nfs_xprt-functions.patch
Patch19: am-utils-6.2-use-new-get_nfs_xprt-and-put_nfs_xprt-functions.patch
Patch20: am-utils-6.2-add-NFSv3-nfs_quick_reply-functionality.patch
Patch21: am-utils-6.2-add-NFSv3-rpc-request-validation.patch
Patch22: am-utils-6.2-fix-wcc-attr-usage-in-unlink3_or_rmdir3.patch

Patch23: am-utils-6.2-Add-the-sys-alias-for-unix-as-well-as-none-and-null.patch
Patch24: am-utils-6.2-Default-to-string-mount-options-for-NFSv4.patch
Patch25: am-utils-6.2-Improve-debugging-for-unmounting.patch
Patch26: am-utils-6.2-add-more-debugging-in-the-unmount-path.patch
Patch27: am-utils-6.2-There-is-really-no-ti-rpc-nfsv4-so-dont-send-one.patch
Patch28: am-utils-6.2-Fix-SEGV-on-amq-entries-that-print-times.patch
Patch29: am-utils-6.2-Make-hasmntval-return-an-0-on-error-1-on-success.patch
Patch30: am-utils-6.2-Update-the-ctime-of-the-directory-too-since-it-changed.patch

Patch31: am-utils-6.2-use-linux-libtirpc-if-present.patch
Patch32: am-utils-6.2-fix-compiler-assignment-warning-due-to-libtirpc.patch
Patch33: am-utils-6.2-fix-logical-not-comparison-in-get_ldap_timestamp.patch
Patch34: am-utils-6.2-fix-umount-to-mount-race.patch

Patch35: am-utils-6.2-fix-nfsv3-fh-length-in-NFS_FH_DREF.patch

Patch36: am-utils-6.2-fix-double-quote-escaping.patch
Patch37: am-utils-6.2-convert-AM_CONFIG_HEADER-to-AC_CONFIG_HEADERS.patch
Patch38: am-utils-6.2-convert-AC_HELP_STRING-to-AS_HELP_STRING.patch
Patch39: am-utils-6.2-convert-AC_TRY_COMPILE-to-AC_COMPILE_IFELSE.patch
Patch40: am-utils-6.2-convert-AC_TRY_LINK-to-AC_LINK_IFELSE.patch
Patch41: am-utils-6.2-convert-AC_TRY_RUN-to-AC_RUN_IFELSE.patch
Patch42: am-utils-6.2-update-configure_ac.patch
Patch43: am-utils-6.2-dont-prevent-building-with-autoconf-2_71.patch

Patch44: am-utils-6.2-fix-fsmount-naming-conflict.patch
Patch45: am-utils-6.2-fix-SEGV-on-quick-reply-error.patch
Patch46: am-utils-6.2-fix-mountd-version-used-when-mount-is-nfs-v4.patch

Patch47: am-utils-6.2-fix-linux-nfs-kernel-module-search.patch
Patch48: am-utils-6.2-dont-include-linux_mount_h.patch
Patch49: am-utils-6.2-fix-fedora-mock-build-fail.patch
Patch50: am-utils-configure-c99.patch

Patch51: am-utils-6.2-allow-autoconf-2.72.patch

# Not needed since autoreconf/libtool appear to do this automatically
# Leaving it set doesn't appear to be a problem so leave it set in
# case this changes.
%global _hardened_build 1

# We need to filter out some perl requirements for now.
%define _use_internal_dependency_generator 0
%define old_find_requires %{__find_requires}

# The sed munging of configure by _fix_broken_configure_for_lto
# causes a check failure so opt-out.
%global _lto_cflags %nil

%description
Am-utils includes an updated version of Amd, the popular BSD
automounter.  An automounter is a program which maintains a cache
of mounted filesystems.  Filesystems are mounted when they are
first referenced by the user and unmounted after a certain period of
inactivity. Amd supports a variety of filesystems, including NFS, UFS,
CD-ROMS and local drives.

You should install am-utils if you need a program for automatically
mounting and unmounting filesystems.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{upstream_version}

%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 22 -p1
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 25 -p1
%patch -P 26 -p1
%patch -P 27 -p1
%patch -P 28 -p1
%patch -P 29 -p1
%patch -P 30 -p1
%patch -P 31 -p1
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 34 -p1
%patch -P 35 -p1
%patch -P 36 -p1
%patch -P 37 -p1
%patch -P 38 -p1
%patch -P 39 -p1
%patch -P 40 -p1
%patch -P 41 -p1
%patch -P 42 -p1
%patch -P 43 -p1

%patch -P 44 -p1
%patch -P 45 -p1
%patch -P 46 -p1

%patch -P 47 -p1
%patch -P 48 -p1
%patch -P 49 -p1
%patch -P 50 -p1

%patch -P 51 -p1

./bootstrap

find_requires=%{old_find_requires}
echo "$find_requires | grep -v lostaltmail.conf" > find-requires
chmod +x find-requires

%build
%configure \
        --enable-shared \
        --enable-am-cflags="-DHAVE_LINUX_NFS_MOUNT_H" \
        --enable-libs="-lresolv" \
	--without-hesiod \
	--enable-debug

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_flags}

%install
%makeinstall

mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/sysconfig
mkdir -p ${RPM_BUILD_ROOT}%{_unitdir}

install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}/%{_unitdir}/
install -m 644 %{SOURCE2} ${RPM_BUILD_ROOT}/%{_sysconfdir}/amd.conf
install -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}/%{_sysconfdir}/sysconfig/amd
install -m 640 %{SOURCE4} ${RPM_BUILD_ROOT}/%{_sysconfdir}/amd.net

gzip -q9f ${RPM_BUILD_ROOT}/%{_infodir}/*info*
mkdir -p ${RPM_BUILD_ROOT}/.automount

rm -f ${RPM_BUILD_ROOT}/usr/sbin/ctl-amd

# add symlinks to shared libs
/sbin/ldconfig -n ${RPM_BUILD_ROOT}/%{_libdir}

# deprecated files
for I in %{_libdir}/libamu.a \
         %{_libdir}/libamu.la \
         %{_libdir}/libamu.so \
         %{_infodir}/dir \
         %{_sysconfdir}/amd.conf-sample \
         %{_sysconfdir}/lostaltmail.conf-sample; do

         rm -f  $RPM_BUILD_ROOT$I
done

%define __find_requires %{_builddir}/%{name}-%{version}/find-requires

%pre
# Check if we have an old fashioned amd.conf and rename if to amd.net
if test "$1" -ne 0; then
  if test -r /etc/amd.conf; then
    if grep -v -q "auto_dir" /etc/amd.conf; then
       if test ! -e /etc/amd.net; then
         mv -f /etc/amd.conf /etc/amd.net
       fi
    fi
  fi
fi

%post
/sbin/ldconfig
%systemd_post amd.service

%preun
%systemd_preun amd.service

%postun
%systemd_postun_with_restart amd.service

/sbin/ldconfig

%triggerun -- am-utils < 6.1.5-19
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply amd
# to migrate them to systemd targets
/usr/bin/systemd-sysv-convert --save amd >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
/sbin/chkconfig --del amd >/dev/null 2>&1 || :
/bin/systemctl try-restart amd.service >/dev/null 2>&1 || :

%files
%doc doc/*.ps AUTHORS BUGS ChangeLog NEWS README* scripts/*-sample
%dir /.automount
%{_bindir}/pawd
%{_sbindir}/*
%{_mandir}/man[58]/*
%{_mandir}/man1/pawd.1*
%config(noreplace) %{_sysconfdir}/amd.net
%config(noreplace) %{_sysconfdir}/amd.conf
%config(noreplace) %{_sysconfdir}/sysconfig/amd
%{_unitdir}/amd.service
%{_infodir}/*info*.gz
%{_libdir}/libamu.so*

%changelog
%autochangelog
