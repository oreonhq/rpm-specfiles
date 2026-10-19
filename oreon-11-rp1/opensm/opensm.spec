%global source0_hash a3335e371a4b044427574dff9d324c6c334e502e8facdf58bc070ee151d7e460
%global __remake_config 1
Name:    opensm
Version: 3.3.24
Release:        1%{?dist}
Summary:        OpenIB InfiniBand Subnet Manager and management utilities
License: GPL-2.0-only OR Linux-OpenIB
Url:     https://github.com/linux-rdma/opensm
Source0:        https://github.com/linux-rdma/opensm/releases/download/%{version}/%{name}-%{version}.tar.gz
Source2: opensm.logrotate
Source4: opensm.sysconfig
Source5: opensm.service
Source6: opensm.launch
Source7: opensm.rwtab
Source8: opensm.partitions
Requires: %{name}-libs%{?_isa} = %{version}-%{release}, logrotate, rdma
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
ExcludeArch: s390 %{arm}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  byacc
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libibumad-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-units
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q

%build

./autogen.sh
%configure --with-opensm-conf-sub-dir=rdma
%make_build
cd opensm
./opensm -c ../opensm-%{version}.conf
%install
%make_install
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%files -f %{oreon_filedir}/main.list
%files -n opensm-libs -f %{oreon_filedir}/opensm-libs.list
%files -n opensm-devel -f %{oreon_filedir}/opensm-devel.list
%files -n opensm-static -f %{oreon_filedir}/opensm-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.24-13
- Prepare for Oreon 11 (RP1)
