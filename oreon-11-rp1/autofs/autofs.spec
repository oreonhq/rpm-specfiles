%global source0_hash 46c30b763ef896f4c4a6df6d62aaaef7afc410e0b7f50d52dbfc6cf728cacd4f

#
# $Id: autofs.spec,v 1.11 2003/12/04 15:41:32 raven Exp $
#
# Use --without systemd in your rpmbuild command or force values to 0 to
# disable them.
%bcond systemd 1

# Use --without fedfs in your rpmbuild command or force values to 0 to
# disable them.
%bcond fedfs 1

# RHEL 10+ does not include NIS support
%bcond nis %{undefined rhel}

Summary: A tool for automatically mounting and unmounting filesystems
Name: autofs
Version: 5.1.9
Release: 12%{?dist}
Epoch: 1
License: GPL-2.0-or-later
Source:        https://www.kernel.org/pub/linux/daemons/autofs/v5/autofs-5.1.9.tar.gz
Patch1: autofs-5.1.9-update-configure.patch
Patch2: autofs-5.1.9-fix-ldap_parse_page_control-check.patch
Patch3: autofs-5.1.9-fix-crash-in-make_options_string.patch
Patch4: autofs-5.1.9-Fix-incompatible-function-pointer-types-in-cyrus-sasl-module.patch
Patch5: autofs-5.1.9-fix-always-recreate-credential-cache.patch
Patch6: autofs-5.1.9-fix-changelog.patch

%if %{with systemd}
BuildRequires: systemd-units
BuildRequires: systemd-devel
%endif
BuildRequires: gcc
BuildRequires: autoconf, openldap-devel, bison, flex, libxml2-devel
BuildRequires: cyrus-sasl-devel, openssl-devel module-init-tools util-linux
BuildRequires: e2fsprogs libtirpc-devel libsss_autofs
%if %{with nis}
BuildRequires: libnsl2-devel
%endif
BuildRequires: pkgconfig krb5-devel
BuildRequires: make
Conflicts: cyrus-sasl-lib < 2.1.23-9
Requires: bash coreutils sed gawk grep module-init-tools /bin/ps
%if %{with systemd}
Requires(post): systemd-sysv
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
%else
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
Requires(postun): /sbin/chkconfig
%endif
Summary(de): autofs daemon 
Summary(fr): démon autofs
Summary(tr): autofs sunucu süreci
Summary(sv): autofs-daemon

%description
autofs is a daemon which automatically mounts filesystems when you use
them, and unmounts them later when you are not using them.  This can
include network filesystems, CD-ROMs, floppies, and so forth.

%description -l de
autofs ist ein Dämon, der Dateisysteme automatisch montiert, wenn sie 
benutzt werden, und sie später bei Nichtbenutzung wieder demontiert. 
Dies kann Netz-Dateisysteme, CD-ROMs, Disketten und ähnliches einschließen. 

%description -l fr
autofs est un démon qui monte automatiquement les systèmes de fichiers
lorsqu'on les utilise et les démonte lorsqu'on ne les utilise plus. Cela
inclus les systèmes de fichiers réseau, les CD-ROMs, les disquettes, etc.

%description -l tr
autofs, kullanýlan dosya sistemlerini gerek olunca kendiliðinden baðlar
ve kullanýmlarý sona erince yine kendiliðinden çözer. Bu iþlem, að dosya
sistemleri, CD-ROM'lar ve disketler üzerinde yapýlabilir.

%description -l sv
autofs är en daemon som mountar filsystem när de använda, och senare
unmountar dem när de har varit oanvända en bestämd tid.  Detta kan
inkludera nätfilsystem, CD-ROM, floppydiskar, och så vidare.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n %{name}-%{version}
echo %{version}-%{release} > .version
%if %{with systemd}
  %define unitdir %{?_unitdir:/usr/lib/systemd/system}
  %define systemd_configure_arg --with-systemd
%endif
%if %{with fedfs}
  %define fedfs_configure_arg --enable-fedfs
%endif

%build
autoreconf -iv
LDFLAGS=-Wl,-z,now
%configure \
	--disable-mount-locking \
	--enable-ignore-busy \
	--enable-force-shutdown \
	--without-hesiod \
	--with-libtirpc \
	%{?systemd_configure_arg:} \
	%{?fedfs_configure_arg:}

make initdir=%{_initrddir} DONTSTRIP=1

%install
%if %{with systemd}
install -d -m 755 $RPM_BUILD_ROOT%{unitdir}
%else
mkdir -p -m755 $RPM_BUILD_ROOT%{_initrddir}
%endif
mkdir -p -m755 $RPM_BUILD_ROOT%{_sbindir}
mkdir -p -m755 $RPM_BUILD_ROOT%{_libdir}/autofs
mkdir -p -m755 $RPM_BUILD_ROOT%{_mandir}/{man5,man8}
mkdir -p -m755 $RPM_BUILD_ROOT/etc/sysconfig
mkdir -p -m755 $RPM_BUILD_ROOT/etc/auto.master.d

make install mandir=%{_mandir} initdir=%{_initrddir} systemddir=%{unitdir} INSTALLROOT=$RPM_BUILD_ROOT
echo make -C redhat
make -C redhat
install -m 755 -d $RPM_BUILD_ROOT/misc
%if %{with systemd}
# Configure can get this wrong when the unit files appear under /lib and /usr/lib
find $RPM_BUILD_ROOT -type f -name autofs.service -exec rm -f {} \;
install -m 644 redhat/autofs.service $RPM_BUILD_ROOT%{unitdir}/autofs.service
%define init_file_name %{unitdir}/autofs.service
%else
install -m 755 redhat/autofs.init $RPM_BUILD_ROOT%{_initrddir}/autofs
%define init_file_name /etc/rc.d/init.d/autofs
%endif
install -m 644 redhat/autofs.conf $RPM_BUILD_ROOT/etc/autofs.conf
install -m 644 redhat/autofs.sysconfig $RPM_BUILD_ROOT/etc/sysconfig/autofs

install -m 644 samples/auto.master $RPM_BUILD_ROOT/etc/auto.master
install -m 644 samples/auto.misc $RPM_BUILD_ROOT/etc/auto.misc
install -m 755 samples/auto.net $RPM_BUILD_ROOT/etc/auto.net
install -m 755 samples/auto.smb $RPM_BUILD_ROOT/etc/auto.smb
install -m 600 samples/autofs_ldap_auth.conf $RPM_BUILD_ROOT/etc/autofs_ldap_auth.conf

%post
%if %{with systemd}
%systemd_post %{name}.service
%else
if [ $1 -eq 1 ]; then
	%{_sbindir}/sbin/chkconfig --add autofs
fi
%endif

%preun
%if %{with systemd}
%systemd_preun %{name}.service
%else
if [ $1 -eq 0 ] ; then
    %{_sbindir}/service autofs stop > /dev/null 2>&1 || :
    %{_sbindir}/chkconfig --del autofs
fi
%endif

%postun
%if %{with systemd}
%systemd_postun_with_restart %{name}.service
%else
if [ $1 -ge 1 ] ; then
    %{_sbindir}/sbin/service autofs condrestart > /dev/null 2>&1 || :
fi
%endif

%triggerun -- %{name} < 5.0.6-5
# Save the current service runlevel info
# User must manually run systemd-sysv-convert --apply %%{name}
# to migrate them to systemd targets
%{_bindir}/systemd-sysv-convert --save %{name} >/dev/null 2>&1 ||:

# Run these because the SysV package being removed won't do them
%{_sbindir}/chkconfig --del %{name} >/dev/null 2>&1 || :
%{_bindir}/systemctl try-restart %{name}.service >/dev/null 2>&1 || :

%files
%doc CREDITS INSTALL COPY* README* samples/ldap* samples/autofs.schema
%config %{init_file_name}
%config(noreplace,missingok) /etc/auto.master
%config(noreplace) /etc/autofs.conf
%config(noreplace,missingok) /etc/auto.misc
%config(noreplace,missingok) /etc/auto.net
%config(noreplace,missingok) /etc/auto.smb
%config(noreplace) /etc/sysconfig/autofs
%config(noreplace) /etc/autofs_ldap_auth.conf
%{_sbindir}/automount
%if %{with fedfs}
%{_sbindir}/mount.fedfs
%{_sbindir}/fedfs-map-nfs4
%endif
%{_libdir}/libautofs.so
%{_libdir}/autofs/
%{_mandir}/*/*
%dir /etc/auto.master.d

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.9-12
- Prepare for Oreon 11 (RP1)
