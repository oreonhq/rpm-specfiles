%global __remake_config 1

Name:    opensm
Version: 3.3.24
Release: 13%{?dist}
Summary: OpenIB InfiniBand Subnet Manager and management utilities
License: GPL-2.0-only OR Linux-OpenIB
Url:     https://github.com/linux-rdma/opensm

Source0: https://github.com/linux-rdma/opensm/releases/download/%{version}/%{name}-%{version}.tar.gz
Source2: opensm.logrotate
Source4: opensm.sysconfig
Source5: opensm.service
Source6: opensm.launch
Source7: opensm.rwtab
Source8: opensm.partitions
# oreon url source checksums begin
%global source0_sha256 a3335e371a4b044427574dff9d324c6c334e502e8facdf58bc070ee151d7e460
%global source0_file opensm-3.3.24.tar.gz
# oreon url source checksums end

BuildRequires: make
BuildRequires:  gcc
BuildRequires: libibumad-devel, systemd, systemd-units
BuildRequires: bison, flex, byacc
%if %{__remake_config}
BuildRequires: libtool, autoconf, automake
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}, logrotate, rdma
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# RDMA is not currently built on 32-bit ARM: #1484155
ExcludeArch: s390 %{arm}

%description
OpenSM is the OpenIB project's Subnet Manager for Infiniband networks.
The subnet manager is run as a system daemon on one of the machines in
the infiniband fabric to manage the fabric's routing state.  This package
also contains various tools for diagnosing and testing Infiniband networks
that can be used from any machine and do not need to be run on a machine
running the opensm daemon.

%package libs
Summary: Libraries used by opensm and included utilities

%description libs
Shared libraries for Infiniband user space access

%package devel
Summary: Development files for the opensm-libs libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development environment for the opensm libraries

%package static
Summary: Static version of the opensm libraries
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
%description static
Static version of opensm libraries

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/opensm-3.3.24.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a3335e371a4b044427574dff9d324c6c334e502e8facdf58bc070ee151d7e460" || { echo "oreon: Source0 SHA256 mismatch for opensm-3.3.24.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure --with-opensm-conf-sub-dir=rdma
%make_build
cd opensm
./opensm -c ../opensm-%{version}.conf

%install
%make_install
# remove unpackaged files from the buildroot
rm -f %{buildroot}%{_libdir}/*.la
rm -fr %{buildroot}%{_sysconfdir}/init.d
install -D -m644 opensm-%{version}.conf %{buildroot}%{_sysconfdir}/rdma/opensm.conf
install -D -m644 %{SOURCE2} %{buildroot}%{_sysconfdir}/logrotate.d/opensm
install -D -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/sysconfig/opensm
install -D -m644 %{SOURCE5} %{buildroot}%{_unitdir}/opensm.service
install -D -m755 %{SOURCE6} %{buildroot}%{_libexecdir}/opensm-launch
install -D -m644 %{SOURCE7} %{buildroot}%{_sysconfdir}/rwtab.d/opensm
install -D -m644 %{SOURCE8} %{buildroot}%{_sysconfdir}/rdma/partitions.conf
mkdir -p ${RPM_BUILD_ROOT}/var/cache/opensm

%post
%systemd_post opensm.service

%preun
%systemd_preun opensm.service

%postun
if [ -d /var/cache/opensm ]; then
	rm -fr /var/cache/opensm
fi
%systemd_postun_with_restart opensm.service

%ldconfig_scriptlets libs

%files
%dir /var/cache/opensm
%{_sbindir}/*
%{_mandir}/*/*
%{_unitdir}/*
%{_libexecdir}/*
%config(noreplace) %{_sysconfdir}/logrotate.d/opensm
%config(noreplace) %{_sysconfdir}/rdma/opensm.conf
%config(noreplace) %{_sysconfdir}/rdma/partitions.conf
%config(noreplace) %{_sysconfdir}/sysconfig/opensm
%{_sysconfdir}/rwtab.d/opensm
%doc AUTHORS ChangeLog INSTALL README NEWS
%license COPYING

%files libs
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%{_includedir}/infiniband

%files static
%{_libdir}/lib*.a

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.24-13
- Prepare for Oreon 11 (RP1)
