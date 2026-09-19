%global source0_hash 459a3ee133fbd850519cde15784664934d29e5dc9680f21142247746e62d9082

%global oname tgt

%ifnarch s390 s390x %{arm}
%global with_rdma 1
%endif

# ceph/librbd-devel not available on 32-bit plaforms, bugs #1727788, #1727787
%ifnarch i686 armv7hl
# Disable rbd on epel7 b/c deps are not present
%{!?rhel:%global with_rbd 1}
%endif

%ifnarch ppc64
%global with_glfs 1
%endif

Summary:        The SCSI target daemon and utility programs
Name:           scsi-target-utils
Version:        1.0.97
Release:        2%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://stgt.sourceforge.net/
Source0:        https://github.com/fujita/tgt/archive/v%{version}/tgt-v%{version}.tar.gz
Source1:        tgtd.service
Source2:        sysconfig.tgtd
Source3:        targets.conf
Source4:        sample.conf
Source5:        tgtd.conf
Patch:          0002-remove-check-for-xsltproc.patch
Patch:          0003-default-config.patch
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
%if 0%{?with_rdma}
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
Requires:       libibverbs
Requires:       librdmacm
%endif
Requires:       lsof
Requires:       sg3_utils
Requires(post): systemd-units
%description
The SCSI target package contains the daemon and tools to setup a SCSI targets.
Currently, software iSCSI targets are supported.

%if 0%{?with_rbd}
%package        rbd
Summary:        Support for the Ceph rbd backstore to scsi-target-utils
BuildRequires:  librbd-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description rbd
Adds support for the Ceph rbd backstore to scsi-target-utils.
%endif

%if 0%{?with_glfs}
%package        gluster
Summary:        Support for the Gluster backstore to scsi-target-utils
BuildRequires:  glusterfs-api-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    gluster
Adds support for the Gluster glfs backstore to scsi-target-utils.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{oname}-%{version}

%build
%{__sed} -i -e 's|-g -O2 -fno-strict-aliasing|%{optflags} -fcommon|' -e 's| -Werror | |' usr/Makefile
%{__make} %{?_smp_mflags} doc V=1
%{__make} %{?_smp_mflags} %{?with_rdma:ISCSI_RDMA=1} %{?with_rbd:CEPH_RBD=1} %{?with_glfs:GLFS_BD=1} SD_NOTIFY=1 libdir=%{_libdir}/tgt V=1

%install
install -D -p -m 0755 scripts/tgt-setup-lun %{buildroot}%{_sbindir}/tgt-setup-lun
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_unitdir}/tgtd.service
install -p -m 0755 scripts/tgt-admin %{buildroot}/%{_sbindir}/tgt-admin
install -D -p -m 0644 doc/manpages/targets.conf.5 %{buildroot}/%{_mandir}/man5/targets.conf.5
install -D -p -m 0644 doc/manpages/tgtadm.8 %{buildroot}/%{_mandir}/man8/tgtadm.8
install -p -m 0644 doc/manpages/tgt-admin.8 %{buildroot}/%{_mandir}/man8
install -p -m 0644 doc/manpages/tgt-setup-lun.8 %{buildroot}/%{_mandir}/man8
install -D -p -m 0600 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/tgtd
install -D -p -m 0600 %{SOURCE3} %{buildroot}%{_sysconfdir}/tgt/targets.conf
install -D -p -m 0600 %{SOURCE4} %{buildroot}%{_sysconfdir}/tgt/conf.d/sample.conf
install -p -m 0600 %{SOURCE5} %{buildroot}%{_sysconfdir}/tgt/tgtd.conf

pushd usr
%{__make} install %{?with_rdma:ISCSI_RDMA=1} %{?with_rbd:CEPH_RBD=1} %{?with_glfs:GLFS_BD=1} SD_NOTIFY=1 DESTDIR=%{buildroot} sbindir=%{_sbindir} libdir=%{_libdir}/tgt

%post
%systemd_post tgtd.service

%preun
%systemd_preun tgtd.service

%postun
# don't restart daemon on upgrade
%systemd_postun tgtd.service

%files
%doc README.md doc/README.iscsi doc/README.iser doc/README.lu_configuration doc/README.mmc doc/README.ssc
%{_sbindir}/tgtd
%{_sbindir}/tgtadm
%{_sbindir}/tgt-setup-lun
%{_sbindir}/tgt-admin
%{_sbindir}/tgtimg
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_unitdir}/tgtd.service
%dir %{_sysconfdir}/tgt
%dir %{_sysconfdir}/tgt/conf.d
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/sysconfig/tgtd
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/tgt/targets.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/tgt/tgtd.conf
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/tgt/conf.d/sample.conf

%if 0%{?with_rbd}
%files rbd
%{_libdir}/tgt/backing-store/bs_rbd.so
%doc doc/README.rbd
%endif

%if 0%{?with_glfs}
%files gluster
%{_libdir}/tgt/backing-store/bs_glfs.so
%doc doc/README.glfs
%endif

%changelog
%autochangelog
