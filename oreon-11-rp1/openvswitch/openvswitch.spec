%global source0_hash 6c94e1e019a7f36ef40a9ae34fb21ab2534dbb78e5bea83338452e07a11becf2
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global _hardened_build 1
%if 0%{!?_rundir:1}
%define _rundir /run
%endif
%bcond_without dpdk
%bcond_without afxdp
%ifarch x86_64
%bcond_without check
%else
%bcond_with check
%endif
%bcond_with check_datapath_kernel
%bcond_without libcapng
%if 0%{?centos} == 7
Epoch:   1
%endif
Name: openvswitch
Summary:        Open vSwitch daemon/database/utilities
URL: https://www.openvswitch.org/
Version: 4.0.0
Release:        1%{?dist}
License: Apache-2.0 AND LGPL-2.0-or-later AND SISSL
%define dpdkarches aarch64 i686 ppc64le x86_64
%if 0%{?commit0:1}
Source0:        https://www.%{name}.org/releases/%{name}-%{version}.tar.gz
%else
%endif
Source1: openvswitch.sysusers
%if %{with afxdp}
%endif
%if %{with check_datapath_kernel}
%endif
%if %{with libcapng}
%endif
%if %{with dpdk}
%ifarch %{dpdkarches}
%endif
%endif
Requires: openssl iproute module-init-tools
%{?systemd_requires}
Requires(post): /bin/sed
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
Obsoletes: openvswitch-controller <= 0:2.1.0-1
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-openvswitch = %{version}-%{release}
# /oreon:deps
%description
Open vSwitch provides standard network bridging functions and
support for the OpenFlow protocol for remote per-flow control of
traffic.

%package -n python3-openvswitch
Summary: Open vSwitch python3 bindings
License: Apache-2.0
Requires: python3 python3-six
Obsoletes: python-openvswitch < 2.10.0-6
Provides: python-openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n python3-openvswitch
Python bindings for the Open vSwitch database

%package test
Summary: Open vSwitch testing utilities
License: Apache-2.0
BuildArch: noarch
Requires: python3-openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}
%description test
Utilities that are useful to diagnose performance and connectivity
issues in Open vSwitch setup.

%package testcontroller
Summary: Simple controller for testing OpenFlow setups
License: Apache-2.0
Requires: openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}
%description testcontroller
This controller enables OpenFlow switches that connect to it to act as
MAC-learning Ethernet switches.
It can be used for initial testing of OpenFlow networks.
It is not a necessary or desirable part of a production OpenFlow deployment.

%package devel
Summary: Open vSwitch OpenFlow development package (library, headers)
License: Apache-2.0
%description devel
This provides shared library, libopenswitch.so and the openvswitch header
files needed to build an external application.

%package ipsec
Summary: Open vSwitch IPsec tunneling support
License: Apache-2.0
Requires: openvswitch libreswan
Requires: python3-openvswitch = %{?epoch:%{epoch}:}%{version}-%{release}
%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%if %{with dpdk}
%ifarch %{dpdkarches}
%package dpdk
Summary: Open vSwitch OpenFlow development package (switch, linked with DPDK)
License: Apache-2.0
Supplements: %{name}
%description dpdk
This provides ovs-vswitchd linked with DPDK library.
%endif
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?commit0:1}
%autosetup -n ovs-%{commit0} -p 1
%else
%autosetup -p 1
%endif

%build

%if 0%{?commit0:1}
sed -i.old -e "s/^AC_INIT(openvswitch,.*,/AC_INIT(openvswitch, %{version},/" configure.ac
%endif
rm -f python/ovs/dirs.py
rm -f include/openvswitch/version.h python/ovs/version.py
./boot.sh
mkdir build build-dpdk
pushd build
ln -s ../configure
%configure \
%if %{with libcapng}
        --enable-libcapng \
%else
        --disable-libcapng \
%endif
        --disable-static \
        --enable-shared \
        --enable-ssl \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        --enable-usdt-probes \
        --with-version-suffix=-%{release} \
%if %{with afxdp}
        --enable-afxdp
%else
        --disable-afxdp
%endif
make %{?_smp_mflags}
popd
%if %{with dpdk}
%ifarch %{dpdkarches}
pushd build-dpdk
ln -s ../configure
%configure \
%if %{with libcapng}
        --enable-libcapng \
%else
        --disable-libcapng \
%endif
        --disable-static \
        --enable-shared \
        --enable-ssl \
        --enable-usdt-probes \
        --with-dpdk=shared \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        --libdir=%{_libdir}/openvswitch-dpdk \
        --program-suffix=.dpdk \
        --with-version-suffix=-%{release} \
%if %{with afxdp}
        --enable-afxdp
%else
        --disable-afxdp
%endif
make %{?_smp_mflags}
popd
%endif
%endif
pushd python
(
export CPPFLAGS="-I ../build/include -I ../include"
export LDFLAGS="%{__global_ldflags} -L ../build/lib/.libs"
%pyproject_wheel
)
popd
/usr/bin/python3 build-aux/dpdkstrip.py \
        --dpdk \
        < rhel/usr_lib_systemd_system_ovs-vswitchd.service.in \
        > rhel/usr_lib_systemd_system_ovs-vswitchd.service
%install
rm -rf $RPM_BUILD_ROOT
%if %{with dpdk}
%ifarch %{dpdkarches}
make -C build-dpdk install-exec DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{_sbindir} -mindepth 1 -maxdepth 1 -not -name ovs-vswitchd.dpdk -delete
find $RPM_BUILD_ROOT%{_libdir}/openvswitch-dpdk -mindepth 1 -maxdepth 1 -not -name "libofproto*.so.*" -not -name "libopenvswitch*.so.*" -delete
%endif
%endif
make -C build install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_sbindir}/ovs-vswitchd $RPM_BUILD_ROOT%{_sbindir}/ovs-vswitchd.nodpdk
touch $RPM_BUILD_ROOT%{_sbindir}/ovs-vswitchd
install -d -m 0755 $RPM_BUILD_ROOT%{_rundir}/openvswitch
install -d -m 0750 $RPM_BUILD_ROOT%{_localstatedir}/log/openvswitch
install -d -m 0755 $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch
install -p -D -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysusersdir}/openvswitch.conf
install -p -D -m 0644 rhel/usr_lib_udev_rules.d_91-vfio.rules \
        $RPM_BUILD_ROOT%{_udevrulesdir}/91-vfio.rules
install -p -D -m 0644 \
        rhel/usr_share_openvswitch_scripts_systemd_sysconfig.template \
        $RPM_BUILD_ROOT/%{_sysconfdir}/sysconfig/openvswitch
for service in openvswitch ovsdb-server ovs-vswitchd ovs-delete-transient-ports \
               openvswitch-ipsec; do
        install -p -D -m 0644 \
                        rhel/usr_lib_systemd_system_${service}.service \
                        $RPM_BUILD_ROOT%{_unitdir}/${service}.service
done
install -m 0755 rhel/etc_init.d_openvswitch \
        $RPM_BUILD_ROOT%{_datadir}/openvswitch/scripts/openvswitch.init
install -p -D -m 0644 rhel/etc_openvswitch_default.conf \
        $RPM_BUILD_ROOT/%{_sysconfdir}/openvswitch/default.conf
install -p -D -m 0644 rhel/etc_logrotate.d_openvswitch \
        $RPM_BUILD_ROOT/%{_sysconfdir}/logrotate.d/openvswitch
install -m 0644 vswitchd/vswitch.ovsschema \
        $RPM_BUILD_ROOT/%{_datadir}/openvswitch/vswitch.ovsschema
pushd python
%pyproject_install
[ -f "$RPM_BUILD_ROOT/%{python3_sitearch}/ovs/_json$(python3-config --extension-suffix)" ]
popd
rm -rf $RPM_BUILD_ROOT/%{_datadir}/openvswitch/python/
install -d -m 0755 $RPM_BUILD_ROOT/%{_sharedstatedir}/openvswitch
install -d -m 0755 $RPM_BUILD_ROOT%{_prefix}/lib/firewalld/services/
install -p -D -m 0755 \
        rhel/usr_share_openvswitch_scripts_ovs-systemd-reload \
        $RPM_BUILD_ROOT%{_datadir}/openvswitch/scripts/ovs-systemd-reload
touch $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch/conf.db
chmod 0640 $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch/conf.db
touch $RPM_BUILD_ROOT%{_sysconfdir}/openvswitch/system-id.conf
rm -f $RPM_BUILD_ROOT/%{_bindir}/ovs-benchmark \
        $RPM_BUILD_ROOT/%{_bindir}/ovs-docker \
        $RPM_BUILD_ROOT/%{_bindir}/ovs-l3ping \
        $RPM_BUILD_ROOT/%{_bindir}/ovs-parse-backtrace \
        $RPM_BUILD_ROOT/%{_bindir}/ovs-test \
        $RPM_BUILD_ROOT/%{_sbindir}/ovs-vlan-bug-workaround \
        $RPM_BUILD_ROOT/%{_mandir}/man1/ovs-benchmark.1* \
        $RPM_BUILD_ROOT/%{_mandir}/man8/ovs-l3ping.8* \
        $RPM_BUILD_ROOT/%{_mandir}/man8/ovs-test.8* \
        $RPM_BUILD_ROOT/%{_mandir}/man8/ovs-vlan-bug-workaround.8*
rm -f $RPM_BUILD_ROOT%{_bindir}/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man5/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man7/ovn*
rm -f $RPM_BUILD_ROOT%{_mandir}/man8/ovn*
rm -f $RPM_BUILD_ROOT%{_datadir}/openvswitch/ovn*
rm -f $RPM_BUILD_ROOT%{_datadir}/openvswitch/scripts/ovn*
rm -f $RPM_BUILD_ROOT%{_includedir}/ovn/*
%oreon_autofiles python3-openvswitch usr/lib/python3*/site-packages/openvswitch* usr/lib64/python3*/site-packages/openvswitch* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/openvswitch* usr/lib64/python3*/site-packages/openvswitch* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for dir in build \
%if %{with dpdk}
%ifarch %{dpdkarches}
build-dpdk \
%endif
%endif
; do
pushd $dir
%if %{with check}
    touch resolv.conf
    export OVS_RESOLV_CONF=$(pwd)/resolv.conf
    if make check TESTSUITEFLAGS='%{_smp_mflags}' ||
       make check TESTSUITEFLAGS='--recheck' ||
       make check TESTSUITEFLAGS='--recheck'; then :;
    else
        cat tests/testsuite.log
        exit 1
    fi
%endif
%if %{with check_datapath_kernel}
    if make check-kernel RECHECK=yes; then :;
    else
        cat tests/system-kmod-testsuite.log
        exit 1
    fi
%endif
popd
done
%preun

%if 0%{?systemd_preun:1}
    %systemd_preun %{name}.service
%else
    if [ $1 -eq 0 ] ; then
        /bin/systemctl --no-reload disable %{name}.service >/dev/null 2>&1 || :
        /bin/systemctl stop %{name}.service >/dev/null 2>&1 || :
    fi
%endif
%pre

[ -L %{_sbindir}/ovs-vswitchd ] || rm -f %{_sbindir}/ovs-vswitchd
%post

%{_sbindir}/update-alternatives --install %{_sbindir}/ovs-vswitchd \
  ovs-vswitchd %{_sbindir}/ovs-vswitchd.nodpdk 10
if [ $1 -eq 1 ]; then
    sed -i 's:^#OVS_USER_ID=:OVS_USER_ID=:' /etc/sysconfig/openvswitch
    sed -i \
        's@OVS_USER_ID="openvswitch:openvswitch"@OVS_USER_ID="openvswitch:hugetlbfs"@'\
        /etc/sysconfig/openvswitch
fi
chown -R openvswitch:openvswitch /etc/openvswitch
%if 0%{?systemd_post:1}
    %systemd_post %{name}.service
%else
    if [ $1 -eq 1 ]; then
        /bin/systemctl daemon-reload >dev/null || :
    fi
%endif
%postun

if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove ovs-vswitchd %{_sbindir}/ovs-vswitchd.nodpdk
fi
%if 0%{?systemd_postun:1}
    %systemd_postun %{name}.service
%else
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
%endif
%if %{with dpdk}
%ifarch %{dpdkarches}
%post dpdk

if grep -Fqw sse4_1 /proc/cpuinfo; then
    priority=20
else
    echo "Warning: the CPU doesn't support SSE 4.1, dpdk support is not enabled." >&2
    priority=5
fi
%{_sbindir}/update-alternatives --install %{_sbindir}/ovs-vswitchd \
  ovs-vswitchd %{_sbindir}/ovs-vswitchd.dpdk $priority
%postun dpdk

if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove ovs-vswitchd %{_sbindir}/ovs-vswitchd.dpdk
fi
%endif
%endif
%files
%files -n python3-openvswitch -f %{oreon_filedir}/python3-openvswitch.list
%files -n openvswitch-test -f %{oreon_filedir}/openvswitch-test.list
%files -n openvswitch-testcontroller -f %{oreon_filedir}/openvswitch-testcontroller.list
%files -n openvswitch-devel -f %{oreon_filedir}/openvswitch-devel.list
%files -n openvswitch-ipsec -f %{oreon_filedir}/openvswitch-ipsec.list

%changelog

%autochangelog

