# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 3d86b6383fb5fd9eb9578d2cd47d92801191f4bf3f9bc61419bfefc8aa1e531a
%global source2_sha256 894213fafbb557d40fba28dcc66f557fa0b4bf0ab32b0e4931b1d2be47e381fc
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })} \
%{?source2_sha256:%(test -z "%{source2_sha256}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_sha256}" || { echo "oreon: Source2 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond nis %[!(0%{?rhel} >= 9)]

%global so_ver 0
%global pam_redhat_version 1.3.1

# docs require fop, which is Java-based and not included in RHEL
# PDF docs are not identical between builds, -doc needs to be archful if enabled
%ifarch %{java_arches}
%global build_pdf %[0 && %{undefined rhel}]
%else
%global build_pdf 0
%endif

Summary: An extensible library which provides authentication for applications
Name: pam
Version: 1.7.2
Release: 2%{?dist}
# The library is BSD licensed with option to relicense as GPLv2+
# - this option is redundant as the BSD license allows that anyway.
# pam_timestamp and pam_loginuid modules are GPLv2+.
License: BSD-3-Clause AND GPL-2.0-or-later
URL: http://www.linux-pam.org/
Source0: https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz
Source1: https://github.com/linux-pam/linux-pam/releases/download/v%{version}/Linux-PAM-%{version}.tar.xz.asc
Source2: https://releases.pagure.org/pam-redhat/pam-redhat-%{pam_redhat_version}.tar.xz
Source3: macros.%{name}
Source5: other.pamd
Source10: config-util.pamd
Source11: dlopen.sh
Source12: system-auth.5
Source13: config-util.5
Source15: pamtmp.conf
Source17: postlogin.5
Source18: https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
Patch1:  pam-1.7.0-redhat-modules.patch
Patch2:  pam-1.5.3-unix-nomsg.patch

%global _pam_libdir %{_libdir}
%global _pam_moduledir %{_libdir}/security
%global _pam_secconfdir %{_sysconfdir}/security
%global _pam_confdir %{_sysconfdir}/pam.d
%global _pam_vendordir %{_datadir}/pam.d

### Dependencies ###
Requires(meta): authselect >= 1.3
Requires: gdbm
Requires: libpwquality%{?_isa}
Requires: pam-libs%{?_isa} = %{version}-%{release}
Requires: setup

Suggests: libdb-convert-util

### Build Dependencies ###
BuildRequires: audit-libs-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gdbm-devel
BuildRequires: gettext-devel
BuildRequires: libeconf-devel
%if %{with nis}
BuildRequires: libnsl2-devel
%endif
BuildRequires: libselinux-devel
BuildRequires: libtirpc-devel
BuildRequires: libtool
BuildRequires: libxcrypt-devel
BuildRequires: make
BuildRequires: meson
BuildRequires: openssl-devel
BuildRequires: perl-interpreter
BuildRequires: pkgconfig
BuildRequires: sed
BuildRequires: systemd

%description
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication.

%package devel
Summary: Files needed for developing PAM-aware applications and modules for PAM
Requires: pam-libs%{?_isa} = %{version}-%{release}

%description devel
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. This package
contains header files used for building both PAM-aware applications
and modules for use with the PAM system.

%package doc
Summary: Extra documentation for PAM.
Requires: pam = %{version}-%{release}
Obsoletes: pam-docs < 1.5.2-6
Provides: pam-docs = %{version}-%{release}
BuildArch: noarch
BuildRequires: docbook5-schemas
BuildRequires: docbook5-style-xsl
BuildRequires: elinks
%if %{build_pdf}
BuildRequires: fop
%endif
BuildRequires: libxslt

%description doc
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. The pam-doc
contains extra documentation for PAM. Currently, this includes additional
documentation in txt and html format.

%package libs
Summary: Shared libraries of the PAM package
# Make sure that if we don't try to upgrade -libs but not the
# main pam package and get file conflicts:
Conflicts: pam < 1.5.2-11

%description libs
PAM (Pluggable Authentication Modules) is a system security tool that
allows system administrators to set authentication policy without
having to recompile programs that handle authentication. The pam-libs
contains the shared libraries for PAM.

%prep
%oreon_verify_sources
%setup -q -n Linux-PAM-%{version} -a 2

# Add custom modules.
mv pam-redhat-%{pam_redhat_version}/* modules

cp %{SOURCE18} .

%patch -P 1 -p1 -b .redhat-modules
%patch -P 2 -p1 -b .nomsg

%build
%meson \
  -Daudit=enabled \
  -Delogind=disabled \
%if %{without nis}
  -Dnis=disabled \
%endif
  -Dlogind=disabled \
  -Dopenssl=enabled \
  -Dpam_userdb=enabled \
  -Dpwaccess=disabled \
  -Ddb=gdbm \
  -Dselinux=enabled \
  -Dvendordir=''
%meson_build

%install
# Install the macros file
install -D -m 644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/macros.d/macros.%{name}

# Install the binaries, libraries, and modules.
%meson_install

# Temporary compat link
ln -sf pam_sepermit.so %{buildroot}%{_pam_moduledir}/pam_selinux_permit.so

# RPM uses docs from source tree
rm -rf %{buildroot}%{_datadir}/doc/Linux-PAM
# Included in setup package
rm -f %{buildroot}%{_sysconfdir}/environment

# Install default configuration files.
install -d -m 755 %{buildroot}%{_pam_confdir}
install -d -m 755 %{buildroot}%{_pam_vendordir}
install -m 644 %{SOURCE5} %{buildroot}%{_pam_confdir}/other
install -m 644 %{SOURCE10} %{buildroot}%{_pam_confdir}/config-util
install -m 600 /dev/null %{buildroot}%{_pam_secconfdir}/opasswd
install -d -m 755 %{buildroot}/var/log
install -d -m 755 %{buildroot}/var/run/faillock

# Install man pages.
install -m 644 %{SOURCE12} %{SOURCE13} %{SOURCE17} %{buildroot}%{_mandir}/man5/
ln -sf system-auth.5 %{buildroot}%{_mandir}/man5/password-auth.5
ln -sf system-auth.5 %{buildroot}%{_mandir}/man5/fingerprint-auth.5
ln -sf system-auth.5 %{buildroot}%{_mandir}/man5/smartcard-auth.5


for phase in auth acct passwd session ; do
  ln -sf pam_unix.so %{buildroot}%{_pam_moduledir}/pam_unix_${phase}.so
done

# Remove .la files and make new .so links -- this depends on the value
# of _libdir not changing, and *not* being /usr/lib.
for lib in libpam libpamc libpam_misc ; do
  rm -f %{buildroot}%{_pam_libdir}/${lib}.la
done
rm -f %{buildroot}%{_pam_moduledir}/*.la

%if "%{_pam_libdir}" != "%{_libdir}"
install -d -m 755 %{buildroot}%{_libdir}
for lib in libpam libpamc libpam_misc ; do
  pushd %{buildroot}%{_libdir}
  ln -sf %{_pam_libdir}/${lib}.so.*.* ${lib}.so
  popd
  rm -f %{buildroot}%{_pam_libdir}/${lib}.so
done
%endif

# Duplicate doc file sets.
rm -fr %{buildroot}/usr/share/doc/pam

# Install the file for autocreation of /var/run subdirectories on boot
install -m644 -D %{SOURCE15} %{buildroot}%{_prefix}/lib/tmpfiles.d/pam.conf

# Install systemd unit file.
install -m644 -D %{_vpath_builddir}/modules/pam_namespace/pam_namespace.service \
  %{buildroot}%{_unitdir}/pam_namespace.service

# Install doc files to unified location.
install -d -m 755 %{buildroot}%{_pkgdocdir}/{adg/html,mwg/html,sag/html}
install -p -m 644 doc/specs/rfc86.0.txt %{buildroot}%{_pkgdocdir}
for i in adg mwg sag; do
  install -p -m 644 %{_vpath_builddir}/doc/$i/*.txt %{buildroot}%{_pkgdocdir}/$i
%if %{build_pdf}
  install -p -m 644 %{_vpath_builddir}/doc/$i/*.pdf %{buildroot}%{_pkgdocdir}/$i
%endif
  cp -pr %{_vpath_builddir}/doc/$i/html/* %{buildroot}%{_pkgdocdir}/$i/html
done
find %{buildroot}%{_pkgdocdir} -type d | xargs chmod 755
find %{buildroot}%{_pkgdocdir} -type f | xargs chmod 644

%find_lang Linux-PAM

%check
# Make sure every module subdirectory gave us a module.  Yes, this is hackish.
for dir in modules/pam_* ; do
if [ -d ${dir} ] ; then
  [ ${dir} = "modules/pam_lastlog" ] && continue
  [ ${dir} = "modules/pam_selinux" ] && continue
  [ ${dir} = "modules/pam_sepermit" ] && continue
  [ ${dir} = "modules/pam_tty_audit" ] && continue
  if ! ls -1 %{buildroot}%{_pam_moduledir}/`basename ${dir}`*.so ; then
    echo ERROR `basename ${dir}` did not build a module.
    exit 1
  fi
fi
done

# Check for module problems.  Specifically, check that every module we just
# installed can actually be loaded by a minimal PAM-aware application.
/sbin/ldconfig -n %{buildroot}%{_pam_libdir}
for module in %{buildroot}%{_pam_moduledir}/pam*.so ; do
  if ! env LD_LIBRARY_PATH=%{buildroot}%{_pam_libdir} \
       %{SOURCE11} -ldl -lpam -L%{buildroot}%{_libdir} ${module} ; then
    echo ERROR module: ${module} cannot be loaded.
    exit 1
  fi
done

%files -f Linux-PAM.lang
%license Copyright
%license gpl-2.0.txt
%dir %{_pam_confdir}
%dir %{_pam_vendordir}
%config(noreplace) %{_pam_confdir}/other
%config(noreplace) %{_pam_confdir}/config-util
%{_rpmconfigdir}/macros.d/macros.%{name}
%{_sbindir}/pam_namespace_helper
%{_sbindir}/faillock
%attr(4755,root,root) %{_sbindir}/pam_timestamp_check
%attr(4755,root,root) %{_sbindir}/unix_chkpwd
%attr(0700,root,root) %{_sbindir}/unix_update
%attr(0755,root,root) %{_sbindir}/mkhomedir_helper
%attr(0755,root,root) %{_sbindir}/pwhistory_helper
%dir %{_pam_moduledir}
%{_pam_moduledir}/pam_access.so
%{_pam_moduledir}/pam_canonicalize_user.so
%{_pam_moduledir}/pam_chroot.so
%{_pam_moduledir}/pam_debug.so
%{_pam_moduledir}/pam_deny.so
%{_pam_moduledir}/pam_echo.so
%{_pam_moduledir}/pam_env.so
%{_pam_moduledir}/pam_exec.so
%{_pam_moduledir}/pam_faildelay.so
%{_pam_moduledir}/pam_faillock.so
%{_pam_moduledir}/pam_filter.so
%{_pam_moduledir}/pam_ftp.so
%{_pam_moduledir}/pam_group.so
%{_pam_moduledir}/pam_issue.so
%{_pam_moduledir}/pam_keyinit.so
%{_pam_moduledir}/pam_limits.so
%{_pam_moduledir}/pam_listfile.so
%{_pam_moduledir}/pam_localuser.so
%{_pam_moduledir}/pam_loginuid.so
%{_pam_moduledir}/pam_mail.so
%{_pam_moduledir}/pam_mkhomedir.so
%{_pam_moduledir}/pam_motd.so
%{_pam_moduledir}/pam_namespace.so
%{_pam_moduledir}/pam_nologin.so
%{_pam_moduledir}/pam_permit.so
%{_pam_moduledir}/pam_postgresok.so
%{_pam_moduledir}/pam_pwhistory.so
%{_pam_moduledir}/pam_rhosts.so
%{_pam_moduledir}/pam_rootok.so
%{_pam_moduledir}/pam_selinux.so
%{_pam_moduledir}/pam_selinux_permit.so
%{_pam_moduledir}/pam_sepermit.so
%{_pam_moduledir}/pam_securetty.so
%{_pam_moduledir}/pam_setquota.so
%{_pam_moduledir}/pam_shells.so
%{_pam_moduledir}/pam_stress.so
%{_pam_moduledir}/pam_succeed_if.so
%{_pam_moduledir}/pam_time.so
%{_pam_moduledir}/pam_timestamp.so
%{_pam_moduledir}/pam_tty_audit.so
%{_pam_moduledir}/pam_umask.so
%{_pam_moduledir}/pam_unix.so
%{_pam_moduledir}/pam_unix_acct.so
%{_pam_moduledir}/pam_unix_auth.so
%{_pam_moduledir}/pam_unix_passwd.so
%{_pam_moduledir}/pam_unix_session.so
%{_pam_moduledir}/pam_userdb.so
%{_pam_moduledir}/pam_usertype.so
%{_pam_moduledir}/pam_warn.so
%{_pam_moduledir}/pam_wheel.so
%{_pam_moduledir}/pam_xauth.so
%{_pam_moduledir}/pam_filter
%{_unitdir}/pam_namespace.service
%dir %{_pam_secconfdir}
%config(noreplace) %{_pam_secconfdir}/access.conf
%config(noreplace) %{_pam_secconfdir}/chroot.conf
%config(noreplace) %{_pam_secconfdir}/faillock.conf
%config(noreplace) %{_pam_secconfdir}/group.conf
%config(noreplace) %{_pam_secconfdir}/limits.conf
%dir %{_pam_secconfdir}/limits.d
%config(noreplace) %{_pam_secconfdir}/namespace.conf
%dir %{_pam_secconfdir}/namespace.d
%attr(755,root,root) %config(noreplace) %{_pam_secconfdir}/namespace.init
%config(noreplace) %{_pam_secconfdir}/pam_env.conf
%config(noreplace) %{_pam_secconfdir}/pwhistory.conf
%config(noreplace) %{_pam_secconfdir}/time.conf
%config(noreplace) %{_pam_secconfdir}/opasswd
%config(noreplace) %{_pam_secconfdir}/sepermit.conf
%dir /var/run/sepermit
%dir /var/run/faillock
%{_prefix}/lib/tmpfiles.d/pam.conf
%{_mandir}/man5/*
%{_mandir}/man8/*

%files devel
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/rfc86.0.txt
%{_includedir}/security
%{_mandir}/man3/*
%{_libdir}/libpam.so
%{_libdir}/libpamc.so
%{_libdir}/libpam_misc.so
%{_libdir}/pkgconfig/pam.pc
%{_libdir}/pkgconfig/pam_misc.pc
%{_libdir}/pkgconfig/pamc.pc

%files doc
%doc %{_pkgdocdir}

%files libs
%license Copyright
%license gpl-2.0.txt
%{_pam_libdir}/libpam.so.%{so_ver}*
%{_pam_libdir}/libpamc.so.%{so_ver}*
%{_pam_libdir}/libpam_misc.so.%{so_ver}*

%changelog
* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.2-2
- Replace %%load macros.pam with %%global _pam_* so rpmspec works without SOURCES at parse time

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.2-1
- Prepare for Oreon 11 (RP1)
