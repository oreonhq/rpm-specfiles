%global source0_hash 67356f6d8cd75c13376203482aac004ab3964454d9aa6568d7fad6bd342250ef
%{?commit:%global shortcommit %(c=%{commit}; echo ${c:0:7})}
%{?commit:%global commitdate 20200828}
%{?commit:%global scmsnap %{commitdate}git%{shortcommit}}
%global enable_mod_dummies 1
%global enable_mod_block_blkid 1
%global enable_mod_block_dm_mpath 1
%global enable_mod_type_dm 1
%global enable_mod_type_dm__lvm 1
Name: sid
Version: 0.0.7
Release:        1%{?dist}
Summary:        Storage Instantiation Daemon (SID)
License: GPL-2.0-or-later
URL: http://sid-project.github.io
%if %{defined commit}
Source0:        https://github.com/sid-project/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
%endif
Requires: systemd
Requires: systemd-udev
Requires: %{name}-resource-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires: %{name}-tools = %{?epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  device-mapper-multipath-devel
BuildRequires:  gcc
BuildRequires:  gperf
BuildRequires:  libblkid-devel
BuildRequires:  libtool
BuildRequires:  libudev-devel
BuildRequires:  libuuid-devel
BuildRequires:  multilib-rpm-config
BuildRequires:  systemd-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Storage Instantiation Daemon (SID) aims to help with Linux storage
device state tracking that encompasses device layers, groups and whole
stacks by monitoring progression of events. Based on monitored states
and further recorded information, it is able to trigger associated
actions for well-defined triggers, including activation and deactivation
of devices and their layers in the stack.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{defined commit}
%autosetup -p1 -n sid-%{commit}
%else
%autosetup -p1 -n sid-%{version}
%endif

%global configure_mod_block_blkid --enable-mod-block-blkid

%global configure_mod_block_dm_mpath --enable-mod-block-dm_mpath

%global configure_mod_type_dm --enable-mod-type-dm

%global configure_mod_type_dm__lvm --enable-mod-type-dm-lvm

%global configure_mod_dummies --enable-mod-block-dummy --enable-mod-type-dummy

%build

autoreconf -ivf
%configure %{?configure_mod_block_blkid} %{?configure_mod_block_dm_mpath} %{?configure_mod_type_dm} %{?configure_mod_type_dm__lvm} %{?configure_mod_dummies}
%make_build
%install
make DESTDIR=%{buildroot} install
rm -f %{buildroot}/%{_libdir}/sid/*.{a,la}
rm -f %{buildroot}/%{_libdir}/sid/modules/ucmd/block/*.{a,la}
rm -f %{buildroot}/%{_libdir}/sid/modules/ucmd/type/*.{a,la}
rm -f %{buildroot}/%{_libdir}/sid/modules/ucmd/type/dm/*.{a,la}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post sid.socket sid.service
%preun

%systemd_preun sid.service sid.socket
%postun

%systemd_postun sid.service sid.socket
%package base-libs
Summary: Libraries for Storage Instantiation Daemon (SID) base
License: GPL-2.0-or-later AND BSD-3-Clause
%description base-libs
This package contains shared libraries with low-level functionality needed for
Storage Instantiation Daemon (SID), its modules and related tools. Currently,
it contains basic support for buffering, IPC, base64 encoding and other helper
functions.

%package base-libs-devel
Summary: Development files for Storage Instantiation Daemon (SID) base
License: GPL-2.0-or-later AND BSD-3-Clause
Requires: %{name}-base-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description base-libs-devel
This package contains development files for Storage Instantiation Daemon (SID)
base libraries.

%package internal-libs
Summary: Development files for Storage Instantiation Daemon (SID) internal
License: GPL-2.0-or-later AND BSD-3-Clause
Requires: %{name}-base-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description internal-libs
This package contains shared libraries with low-level functionality needed for
Storage Instantiation Daemon (SID) and its modules. Currently, it contains
basic support for bitmaps, hashing, lists, memory handling and other helper
functions.

%package internal-libs-devel
Summary: Development files for Storage Instantiation Daemon (SID) internal
License: GPL-2.0-or-later AND BSD-3-Clause
Requires: %{name}-internal-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description internal-libs-devel
This package contains development files for Storage Instantiation Daemon (SID)
internal libraries.

%package log-libs
Summary: Libraries for Storage Instantiation Daemon (SID) logging
License: GPL-2.0-or-later
%description log-libs
This package contains shared libraries with logging support needed for Storage
Instantiation daemon (SID), its modules and related tools.

%package log-libs-devel
Summary: Development files for Storage Instantiation Daemon (SID) logging
License: GPL-2.0-or-later
Requires: %{name}-log-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description log-libs-devel
This package contains development files for Storage Instantiation Daemon (SID)
logging libraries.

%package iface-libs
Summary: Libraries for Storage Instantiation Daemon (SID) interfaces
License: GPL-2.0-or-later
Requires: %{name}-internal-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires: %{name}-log-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description iface-libs
This package contains shared libraries to support interfaces used in Storage
Instantiation Daemon (SID), its modules and related tools.

%package iface-libs-devel
Summary: Development files for Storage Instantiation Daemon (SID) interfaces
License: GPL-2.0-or-later
Requires: %{name}-iface-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description iface-libs-devel
This package contains development files for Storage Instantiation Daemon (SID)
interface libraries.

%package resource-libs
Summary: Libraries for Storage Instantiation Daemon (SID) resources
License: GPL-2.0-or-later
Requires: %{name}-internal-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires: %{name}-iface-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires: systemd-libs >= 221
%description resource-libs
This package contains shared libraries to support high-level resources that
represent hierarchical units of reusable code used in Storage Instantiation
Daemon (SID), its modules and related tools. Currently, it contains support
for aggregation, key-value store, module loading and registry, worker process
control, bridging SID core and udev and creating an instance of SID as a whole.

%package resource-libs-devel
Summary: Development files for Storage Instantiation Daemon (SID) resources
License: GPL-2.0-or-later
Requires: %{name}-resource-libs%{?_isa} = %{?epoch}:%{version}-%{release}
%description resource-libs-devel
This package contains development files for Storage Instantiation Daemon (SID)
resource libraries.

%package tools
Summary: Storage Instantiation Daemon (SID) supporting tools
Requires: %{name}-iface-libs%{?_isa} = %{?epoch}:%{version}-%{release}
Requires: systemd-udev
%description tools
This package contains tools to support Storage Instantiation Daemon (SID).

%package mod-dummies
Summary: Dummy block and type module for Storage Instantiation Daemon (SID)
Requires: %{name} = %{?epoch}:%{version}-%{release}
%description mod-dummies
This package contains dummy block and type modules for Storage Instantiation
Daemon (SID). Their only purpose is to test SID module functionality and hook
execution.

%package mod-block-blkid
Summary: Blkid block module for Storage Instantiation Daemon (SID)
Requires: %{name} = %{?epoch}:%{version}-%{release}
%description mod-block-blkid
This package contains blkid block module for Storage Instantiation Daemon (SID).

%package mod-block-dm-mpath
Summary: Device-mapper multipath block module for Storage Instantiation Daemon (SID)
Requires: %{name} = %{?epoch}:%{version}-%{release}
Requires: device-mapper-multipath-libs >= 0.8.4-7
%description mod-block-dm-mpath
This package contains device-mapper multipath block module for Storage
Instantiation Daemon (SID).

%package mod-type-dm
Summary: Device-mapper type module for Storage Instantiation Daemon (SID)
Requires: %{name} = %{?epoch}:%{version}-%{release}
%description mod-type-dm
This package contains device-mapper type module for Storage Instantiation
Daemon (SID).

%package mod-type-dm-lvm
Summary: LVM type module for Storage Instantiation Daemon (SID)
Requires: %{name} = %{?epoch}:%{version}-%{release}
Requires: %{name}-mod-type-dm%{?_isa} = %{?epoch}:%{version}-%{release}
%description mod-type-dm-lvm
This package contains LVM type module for Storage Instantiation
Daemon (SID).

%files -f %{oreon_filedir}/main.list
%files -n sid-base-libs -f %{oreon_filedir}/sid-base-libs.list
%files -n sid-base-libs-devel -f %{oreon_filedir}/sid-base-libs-devel.list
%files -n sid-internal-libs -f %{oreon_filedir}/sid-internal-libs.list
%files -n sid-internal-libs-devel -f %{oreon_filedir}/sid-internal-libs-devel.list
%files -n sid-log-libs -f %{oreon_filedir}/sid-log-libs.list
%files -n sid-log-libs-devel -f %{oreon_filedir}/sid-log-libs-devel.list
%files -n sid-iface-libs -f %{oreon_filedir}/sid-iface-libs.list
%files -n sid-iface-libs-devel -f %{oreon_filedir}/sid-iface-libs-devel.list
%files -n sid-resource-libs -f %{oreon_filedir}/sid-resource-libs.list
%files -n sid-resource-libs-devel -f %{oreon_filedir}/sid-resource-libs-devel.list
%files -n sid-tools -f %{oreon_filedir}/sid-tools.list
%files -n sid-mod-dummies -f %{oreon_filedir}/sid-mod-dummies.list
%files -n sid-mod-block-blkid -f %{oreon_filedir}/sid-mod-block-blkid.list
%files -n sid-mod-block-dm-mpath -f %{oreon_filedir}/sid-mod-block-dm-mpath.list
%files -n sid-mod-type-dm -f %{oreon_filedir}/sid-mod-type-dm.list
%files -n sid-mod-type-dm-lvm -f %{oreon_filedir}/sid-mod-type-dm-lvm.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0.7-3
- Prepare for Oreon 11 (RP1)
