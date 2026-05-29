%global source0_hash none

# Need to be specific for flatpak builds, otherwise it'll create rules
# in other directory than /app/etc which will make builds fail.
# On Fedora, this should be the same definition.
%if 0%{?flatpak}
%global _udevrulesdir %{_prefix}/lib/udev/rules.d
%endif

%global xyz_version 3.18.1
%global xy_version %(sed 's/\\(.*\\)\\..*/\\1/'<<<%{xyz_version})

Name:		fuse3
Version:	%{xyz_version}
Release:	2%{?dist}
Summary:	File System in Userspace (FUSE) v3 utilities
License:	GPL-1.0-or-later
URL:		https://github.com/libfuse/libfuse/
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-/fuse-.tar.gz
Source1:        https://github.com/libfuse/libfuse/releases/download/fuse-/fuse-.tar.gz.sig
Source2:        https://raw.githubusercontent.com/libfuse/libfuse/master/signify/fuse-%(sed.pub
Source3:	fuse.conf

%if %{undefined rhel}
BuildRequires:	signify
%endif
BuildRequires:	which
BuildRequires:	libselinux-devel
BuildRequires:	meson, ninja-build, gcc, gcc-c++
BuildRequires:	systemd-udev
# for fuse.conf
Requires:	fuse-common

# The dependency from fuse3 to fuse3-libs is already implicit through
# the generated library dependency, but unless we force the exact
# version then we risk mixing different fuse3 & fuse3-libs versions
# which is not likely to be a well-tested situation upstream.
Requires:	%{name}-libs = %{version}-%{release}

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
Requires:	%{name}-libs = %{version}-%{release}
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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%if %{undefined rhel}
# Fuse is using signify rather than PGG since 3.15.1 For more details see:
#	https://github.com/libfuse/libfuse/releases/tag/fuse-3.15.1
signify -V -m  '%{SOURCE0}' -p '%{SOURCE2}'
%endif

%autosetup -p1 -n fuse-%{version}

%build
export LC_ALL=en_US.UTF-8
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

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{xyz_version}-2
- Prepare for Oreon 11 (RP1)
