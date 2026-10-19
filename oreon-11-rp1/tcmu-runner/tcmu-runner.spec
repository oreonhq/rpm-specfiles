%global source0_hash 0bf36c23d522825433eb407aa6b2dafbdd9db26fee405173df657ddfbee80009
%global __cmake_in_source_build 1
Name:           tcmu-runner
License:        LGPL-2.1-or-later OR Apache-2.0
Summary:        A daemon that supports LIO userspace backends
Version:        1.6.2
Release:        1%{?dist}
URL:            https://github.com/open-iscsi/tcmu-runner
Source0:        https://github.com/open-iscsi/tcmu-runner/archive/v%{version}.tar.gz
Patch0:         read_conf.patch
Requires:       targetcli
ExcludeArch:	i686 armv7hl
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  glusterfs-api-devel
BuildRequires:  gperftools-devel
BuildRequires:  kmod-devel
BuildRequires:  libnl3-devel
BuildRequires:  librbd-devel
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  zlib-devel
# /oreon:deps
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
%oreon_autofiles libtcmu usr/*/lib*.so.*
%oreon_autofiles libtcmu-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtcmu -f %{oreon_filedir}/libtcmu.list
%files -n libtcmu-devel -f %{oreon_filedir}/libtcmu-devel.list

%changelog

%autochangelog
