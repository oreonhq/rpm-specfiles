%global source0_hash 35efb04063f1b7bd9d715f1d8d3ab75352b595b1fd12349d7570a7ba19ba6d86

Name:           powerpc-utils
Version:        1.3.13
Release:        5%{?dist}
Summary:        PERL-based scripts for maintaining and servicing PowerPC systems

License:        GPL-2.0-only
URL:            https://github.com/ibm-power-utilities/powerpc-utils
Source0:        https://github.com/ibm-power-utilities/powerpc-utils/archive/v1.3.13/powerpc-utils-1.3.13.tar.gz
Source1:        nx-gzip.udev
Patch0:         powerpc-utils-1.3.11-manpages.patch

ExclusiveArch:  ppc %{power64}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  zlib-devel
BuildRequires:  librtas-devel >= 1.4.0
BuildRequires:  libservicelog-devel >= 1.0.1-2
BuildRequires:  perl-generators
BuildRequires:  systemd
BuildRequires:  numactl-devel

# rtas_dump explicit dependency
Requires:       perl(Data::Dumper)
Requires:       %{name}-core = %{version}-%{release}

%description
PERL-based scripts for maintaining and servicing PowerPC systems.


%package core
Summary: Core utilities for maintaining and servicing PowerPC systems
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires: kmod
Requires: which
Requires: /usr/bin/awk
Requires: /usr/bin/basename
Requires: /usr/bin/bc
Requires: /usr/bin/cat
Requires: /usr/bin/cut
Requires: /usr/bin/echo
Requires: /usr/bin/find
Requires: /bin/grep
Requires: /usr/bin/head
Requires: /usr/bin/ls
Requires: /usr/bin/sed
Requires: /usr/bin/tr
Requires: /usr/bin/udevadm

# udev rule move
Conflicts: libnxz < 0.63-3

%description core
Core utilities for maintaining and servicing PowerPC systems.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
./autogen.sh
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=118112
CFLAGS="$RPM_OPT_FLAGS -std=gnu17"
%configure --with-systemd=%{_unitdir} --disable-werror
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT FILES= RCSCRIPTS=

#define pkgdocdir {_datadir}/doc/{name}-{version}
%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

# move doc files
mkdir -p $RPM_BUILD_ROOT%{_pkgdocdir}
install $RPM_BUILD_ROOT/usr/share/doc/packages/powerpc-utils/* -t $RPM_BUILD_ROOT%{_pkgdocdir}
rm -rf $RPM_BUILD_ROOT/usr/share/doc/packages/powerpc-utils
rm -f $RPM_BUILD_ROOT%{_pkgdocdir}/COPYING

# install udev rule for the nx-gzip accelerator
install -pDm 644  %{SOURCE1}  %{buildroot}%{_udevrulesdir}/90-nx-gzip.rules

# remove init script and perl script. They are deprecated
rm -rf $RPM_BUILD_ROOT/etc/init.d/ibmvscsis.sh $RPM_BUILD_ROOT/usr/sbin/vscsisadmin

# symlink uspchrp
ln -s serv_config %{buildroot}%{_sbindir}/uspchrp
ln -s serv_config.8 %{buildroot}%{_mandir}/man8/uspchrp.8

# deprecated, use sosreport instead
rm -f $RPM_BUILD_ROOT%{_sbindir}/snap $RPM_BUILD_ROOT%{_mandir}/man8/snap.8*

# drop needless stuffs
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/powerpc-utils

# keep service name
mv $RPM_BUILD_ROOT%{_unitdir}/hcn-init-NetworkManager.service $RPM_BUILD_ROOT%{_unitdir}/hcn-init.service

%post core
%systemd_post hcn-init.service
# update the smt.state file with current SMT
/usr/sbin/smtstate --save >/dev/null 2>&1 || :

%preun core
%systemd_preun smtstate.service
%systemd_preun hcn-init.service

%postun core
%systemd_postun_with_restart smtstate.service
%systemd_postun_with_restart hcn-init.service 

%posttrans core
systemctl enable hcn-init.service >/dev/null 2>&1 || :

%files
# PERL-based scripts for maintaining and servicing PowerPC systems
%doc README Changelog
%license COPYING
%{_sbindir}/hvcsadmin
%{_sbindir}/rtas_dump
%{_mandir}/man8/hvcsadmin.8*
%{_mandir}/man8/rtas_dump.8*

%files core
%doc README Changelog
%license COPYING
%dir %{_localstatedir}/lib/powerpc-utils
%config(noreplace) %{_localstatedir}/lib/powerpc-utils/smt.state
%{_unitdir}/smtstate.service
%{_unitdir}/smt_off.service
%{_unitdir}/hcn-init.service
%if 0%{?wicked}
%{_unitdir}/hcn-init-wicked.service
%else
%exclude %{_unitdir}/hcn-init-wicked.service
%endif
%{_bindir}/amsstat
%{_sbindir}/activate_firmware
%{_sbindir}/bootlist
%{_sbindir}/errinjct
%{_sbindir}/lparstat
%{_sbindir}/lsdevinfo
%{_sbindir}/lsprop
%{_sbindir}/lsslot
%{_sbindir}/ls-vdev
%{_sbindir}/ls-veth
%{_sbindir}/ls-vscsi
%{_sbindir}/nvsetenv
%{_sbindir}/ppc64_cpu
%{_sbindir}/rtas_dbg
%{_sbindir}/rtas_event_decode
%{_sbindir}/rtas_ibm_get_vpd
%{_sbindir}/serv_config
%{_sbindir}/set_poweron_time
%{_sbindir}/sys_ident
%{_sbindir}/uesensor
%{_sbindir}/update_flash
%{_sbindir}/update_flash_nv
%{_sbindir}/uspchrp
%{_sbindir}/hcncfgdrc
%{_sbindir}/hcnmgr
%{_sbindir}/hcnqrydev
%{_sbindir}/hcnrmdev
%{_sbindir}/hcnrmhcn
%{_sbindir}/hcnversion
%{_sbindir}/vcpustat
%{_sbindir}/smtstate
%{_sbindir}/nvram
%{_sbindir}/ofpathname
%{_sbindir}/pseries_platform
%{_sbindir}/drmgr
%{_sbindir}/lparnumascore
%{_udevrulesdir}/90-nx-gzip.rules
%{_mandir}/man1/amsstat.1*
%{_mandir}/man5/lparcfg.5*
%{_mandir}/man8/activate_firmware.8*
%{_mandir}/man8/bootlist.8*
%{_mandir}/man8/errinjct.8*
%{_mandir}/man8/lparstat.8*
%{_mandir}/man8/lsdevinfo.8*
%{_mandir}/man8/lsprop.8*
%{_mandir}/man8/lsslot.8*
%{_mandir}/man8/ls-vdev.8*
%{_mandir}/man8/ls-veth.8*
%{_mandir}/man8/ls-vscsi.8*
%{_mandir}/man8/nvsetenv.8*
%{_mandir}/man8/ppc64_cpu.8*
%{_mandir}/man8/rtas_dbg.8*
%{_mandir}/man8/rtas_event_decode.8*
%{_mandir}/man8/rtas_ibm_get_vpd.8*
%{_mandir}/man8/serv_config.8*
%{_mandir}/man8/set_poweron_time.8*
%{_mandir}/man8/sys_ident.8*
%{_mandir}/man8/uesensor.8*
%{_mandir}/man8/update_flash.8*
%{_mandir}/man8/pseries_platform.8*
%{_mandir}/man8/update_flash_nv.8*
%{_mandir}/man8/uspchrp.8*
%{_mandir}/man8/vcpustat.8.gz
%{_mandir}/man8/smtstate.8.gz
%{_mandir}/man8/hcnmgr.8*
%{_mandir}/man8/nvram.8*
%{_mandir}/man8/ofpathname.8*
%{_mandir}/man8/drmgr.8*
%{_mandir}/man8/drmgr-hooks.8*
%{_mandir}/man8/lparnumascore.8*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.13-5
- Import
