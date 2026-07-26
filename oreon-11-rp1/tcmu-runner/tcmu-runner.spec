%global source0_hash 2a41c5ded0b81f820b3deabbf8b7ec5102966e51615bec8e04f3a821d9a8753c

%global __cmake_in_source_build 1

Name:           tcmu-runner
# Automatically converted from old format: LGPLV2+ or ASL 2.0 - review is highly recommended.
License:        LGPL-2.1-or-later OR Apache-2.0
Summary:        A daemon that supports LIO userspace backends
Version:        1.5.4
Release:        14%{?dist}
URL:            https://github.com/open-iscsi/tcmu-runner
Source:         https://github.com/open-iscsi/tcmu-runner/archive/v%{version}.tar.gz
Patch0:         read_conf.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires:  cmake glib2-devel libnl3-devel glusterfs-api-devel kmod-devel zlib-devel librbd-devel
BuildRequires:  gperftools-devel systemd
Requires:       targetcli
# Ceph/librbd does not have 32bit builds so we cannot either
ExcludeArch:	i686 armv7hl

%description
A daemon that handles the complexity of the LIO kernel target's userspace
passthrough interface (TCMU). It presents a C plugin API for extension modules
that handle SCSI requests in ways not possible or suitable to be handled
by LIO's in-kernel backstores.

%package -n libtcmu
Summary:        A library to ease supporting LIO userspace processing

%description -n libtcmu
libtcmu provides a library for processing SCSI commands exposed by the
LIO kernel target's TCM-User backend.

%package -n libtcmu-devel
Summary:        Development headers for libtcmu
Requires:       %{name} = %{version}-%{release}

%description -n libtcmu-devel
Development header(s) for developing against libtcmu.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381481)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DSUPPORT_SYSTEMD=ON .
make %{?_smp_mflags}
gzip --stdout tcmu-runner.8 > tcmu-runner.8.gz

%install
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 tcmu-runner.8.gz %{buildroot}%{_mandir}/man8/
mkdir -p %{buildroot}%{_includedir}
cp -a libtcmu.h libtcmu_common.h libtcmu_log.h tcmu-runner.h %{buildroot}%{_includedir}/

%ldconfig_scriptlets -n libtcmu

%files
%{_bindir}/tcmu-runner
%dir %{_libdir}/tcmu-runner
%{_libdir}/tcmu-runner/*
%{_sysconfdir}/dbus-1/system.d/tcmu-runner.conf
%{_datarootdir}/dbus-1/system-services/org.kernel.TCMUService1.service
%{_unitdir}/tcmu-runner.service
%{_sysconfdir}/logrotate.d/tcmu-runner
%dir %{_sysconfdir}/tcmu/
%config %{_sysconfdir}/tcmu/tcmu.conf
%doc README.md
%license LICENSE.*
%{_mandir}/man8/tcmu-runner.8.gz

%files -n libtcmu
%{_libdir}/*.so.*

%files -n libtcmu-devel
%{_includedir}/libtcmu.h
%{_includedir}/libtcmu_common.h
%{_includedir}/libtcmu_log.h
%{_includedir}/tcmu-runner.h
%{_libdir}/*.so

%changelog
%autochangelog
