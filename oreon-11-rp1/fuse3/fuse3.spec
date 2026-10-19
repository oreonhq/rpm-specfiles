%global source0_hash bcd19582c5e30f7fe45dd86a5540e998590aa01903afc7ebcbeea6c8ac5421ee
%global source1_hash 713b85d079965c81010ca4facfb96a6f06c886708da5d75696f7b7d1ed9aba30
%global source2_hash 68e9eab3bbb84a63cec0ca59eb82abb9cd1dee7059bce5bf92ca777f4186c7e0
%if 0%{?flatpak}
%global _udevrulesdir %{_prefix}/lib/udev/rules.d
%endif
%global xyz_version 3.18.3
%global xy_version %(sed 's/\\(.*\\)\\..*/\\1/'<<<%{xyz_version})
Name:		fuse3
Version:	%{xyz_version}
Release:        1%{?dist}
Summary:        File System in Userspace (FUSE) v3 utilities
License:	GPL-1.0-or-later
URL:		https://github.com/libfuse/libfuse/
Source0:        https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz
Source1:	https://github.com/libfuse/libfuse/releases/download/fuse-%{version}/fuse-%{version}.tar.gz.sig
Source2:	https://raw.githubusercontent.com/libfuse/libfuse/master/signify/fuse-%{xy_version}.pub
Source3:	fuse.conf
Requires:	fuse-common
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libselinux-devel
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  systemd-udev
BuildRequires:  which
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
test "%{source2_hash}" = "none" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source2_hash}" || { echo "oreon: Source2 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir fuse-%{version}
%oreon_prep
%build

export LC_ALL=en_US.UTF-8
%meson -D udevrulesdir=%{_udevrulesdir} -D useroot=false
%meson_build
%install
%meson_install
find %{buildroot} .
chmod 0755 %{buildroot}/%{_bindir}/fusermount3
rm -f %{buildroot}%{_sysconfdir}/init.d/fuse3
rm -f %{buildroot}/etc/init.d/fuse3
install -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}
rm -f %{buildroot}%{_udevrulesdir}/99-fuse3.rules
%oreon_autofiles fuse-common usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n fuse3-libs -f %{oreon_filedir}/fuse3-libs.list
%files -n fuse3-devel -f %{oreon_filedir}/fuse3-devel.list
%files -n fuse-common -f %{oreon_filedir}/fuse-common.list

%changelog

%autochangelog
