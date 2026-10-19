%global source0_hash 459a3ee133fbd850519cde15784664934d29e5dc9680f21142247746e62d9082
%global oname tgt
%ifnarch s390 s390x %{arm}
%global with_rdma 1
%endif
%ifnarch i686 armv7hl
%{!?rhel:%global with_rbd 1}
%endif
%ifnarch ppc64
%global with_glfs 1
%endif
Summary:        The SCSI target daemon and utility programs
Name:           scsi-target-utils
Version:        1.0.97
Release:        1%{?dist}
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
%if 0%{?with_rdma}
Requires:       libibverbs
Requires:       librdmacm
%endif
Requires:       lsof
Requires:       sg3_utils
Requires(post): systemd-units
# oreon:deps
BuildRequires:  docbook-style-xsl
BuildRequires:  gcc
BuildRequires:  glusterfs-api-devel
BuildRequires:  libaio-devel
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libxslt
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  pkgconfig
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post tgtd.service
%preun

%systemd_preun tgtd.service
%postun

%systemd_postun tgtd.service
%files -f %{oreon_filedir}/main.list
%files -n scsi-target-utils-gluster -f %{oreon_filedir}/scsi-target-utils-gluster.list

%changelog

%autochangelog
