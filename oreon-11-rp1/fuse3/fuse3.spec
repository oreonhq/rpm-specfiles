# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bcd19582c5e30f7fe45dd86a5540e998590aa01903afc7ebcbeea6c8ac5421ee
%global source2_hash 68e9eab3bbb84a63cec0ca59eb82abb9cd1dee7059bce5bf92ca777f4186c7e0

%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
# Need to be specific for flatpak builds, otherwise it'll create rules
# in other directory than /app/etc which will make builds fail.
%if 0%{?flatpak}
%global _udevrulesdir %{_prefix}/lib/udev/rules.d
%endif

%global xyz_version 3.18.3
%global xy_version %(sed 's/\\(.*\\)\\..*/\\1/'<<<%{xyz_version})
%global _lto_cflags -flto -ffat-lto-objects

Name:		fuse3
Version:        3.18.3
Release:        1%{?dist}
Summary:	File System in Userspace (FUSE) v3 utilities
License:	GPL-1.0-or-later
URL:		https://github.com/libfuse/libfuse/
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
Source1:        fuse-3.18.3.tar.gz.sig
Source2:        https://raw.githubusercontent.com/libfuse/libfuse/master/signify/fuse-3.18.pub
Source3:	fuse.conf

BuildRequires:	which
BuildRequires:	binutils
BuildRequires:	libselinux-devel
BuildRequires:	meson
BuildRequires:	ninja-build
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	systemd-udev
BuildRequires:  oreon-rpm-macros
# for fuse.conf
Requires:	fuse-common

# The dependency from fuse3 to fuse3-libs is already implicit through
# the generated library dependency, but unless we force the exact
# version then we risk mixing different fuse3 & fuse3-libs versions
# which is not likely to be a well-tested situation upstream.
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}

%description
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE v3 userspace tools to
mount a FUSE filesystem.

%package libs
Summary:	File System in Userspace (FUSE) v3 libraries
License:	LGPL-2.1-or-later

%description libs
Devel With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains the FUSE v3 libraries.

%package devel
Summary:	File System in Userspace (FUSE) v3 devel files
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
License:	LGPL-2.1-or-later

%description devel
With FUSE it is possible to implement a fully functional filesystem in a
userspace program. This package contains development files (headers,
pgk-config) to develop FUSE v3 based applications/filesystems.

%package -n fuse-common
Summary:	Common files for File System in Userspace (FUSE) v2 and v3
License:	GPL-1.0-or-later

%description -n fuse-common
Common files for FUSE v2 and FUSE v3.

%prep
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -


%autosetup -p1 -n fuse-%{version}

%build
export LC_ALL=C.UTF-8
%meson -D udevrulesdir=%{_udevrulesdir} -D useroot=false
%meson_build

%install
%meson_install
find %{buildroot} .
# change from 4755 to 0755 to allow stripping -- fixed later in files
chmod 0755 %{buildroot}/%{_bindir}/fusermount3

# No need to create init-script
rm -f %{buildroot}%{_sysconfdir}/init.d/fuse3
# This path is hardcoded:
# https://github.com/libfuse/libfuse/blob/master/util/install_helper.sh#L43
# so flatpaks will fail unless we delete it below.
rm -f %{buildroot}/etc/init.d/fuse3


# Install config-file
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}

# Delete pointless udev rules (brc#748204)
rm -f %{buildroot}%{_udevrulesdir}/99-fuse3.rules

%check
so=$(find %{_vpath_builddir} -name 'libfuse3.so.%{version}' -type f | head -n1)
test -n "$so"
readelf --dyn-syms -W "$so" | grep -F 'fuse_session_loop_mt@@FUSE_3.12'
readelf --dyn-syms -W "$so" | grep -F 'fuse_loop_mt@@FUSE_3.12'
readelf --dyn-syms -W "$so" | grep -F 'fuse_parse_cmdline@@FUSE_3.12'

%files
%license LICENSE GPL2.txt
%doc AUTHORS ChangeLog.rst README.md
%{_sbindir}/mount.fuse3
%attr(4755,root,root) %{_bindir}/fusermount3
%{_mandir}/man1/*
%{_mandir}/man8/*

%files libs
%license LGPL2.txt
%{_libdir}/libfuse3.so.*

%files devel
%{_libdir}/libfuse3.so
%{_libdir}/pkgconfig/fuse3.pc
%{_includedir}/fuse3/

%files -n fuse-common
%config(noreplace) %{_sysconfdir}/fuse.conf

