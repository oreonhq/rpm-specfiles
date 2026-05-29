%global source0_hash f7f669d27c997d3eb3f3e014b4c0aa1aa4d07ce4d6f9e41fa835240f2bf38810

%global so_major_version 2
%global so_minor_version 0
%global so_patch_version 1

Name:           sysfsutils
Version:        2.1.1
Release:        12%{?dist}
Summary:        Utilities for interfacing with sysfs
URL:            https://github.com/linux-ras/sysfsutils
License:        GPL-2.0-only

Source0:        https://github.com/linux-ras/sysfsutils/archive/v%{version}.tar.gz

Patch0:         sysfsutils-2.1.1-fix-my-strncat.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  gcc
Requires:       libsysfs = %{version}-%{release}

%description
This package's purpose is to provide a set of utilities for interfacing
with sysfs.

%package -n libsysfs
Summary: Shared library for interfacing with sysfs
License: LGPL-2.1-or-later

%description -n libsysfs
Library used in handling linux kernel sysfs mounts and their various files.

%package -n libsysfs-devel
Summary: Static library and headers for libsysfs
License: LGPL-2.1-or-later
Requires: libsysfs = %{version}-%{release}

%description -n libsysfs-devel
libsysfs-devel provides the header files and static libraries required
to build programs using the libsysfs API.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
./autogen
%configure --disable-static
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets -n libsysfs

%files
%license COPYING cmd/GPL
%doc AUTHORS README CREDITS docs/libsysfs.txt
%{_bindir}/systool
%{_mandir}/man1/systool.1.gz

%files -n libsysfs
%license COPYING lib/LGPL
/%{_libdir}/libsysfs.so.%{so_major_version}
/%{_libdir}/libsysfs.so.%{so_major_version}.%{so_minor_version}.%{so_patch_version}

%files -n libsysfs-devel
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
/%{_libdir}/libsysfs.so
/%{_libdir}/pkgconfig/libsysfs.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-12
- Import
