%global source0_hash 33b6337a07af2874835321d802c62cca0e6bd8ae18c4534ce1fe68f7bcf762bc
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?suse_version} && 0%{?suse_version} < 1500) || (0%{?oreon} >= 11)
%bcond_with zstd
%else
%bcond_without zstd
%endif
Name:           drpm
Version:        0.5.3
Release:        1%{?dist}
Summary:        A library for making, reading and applying deltarpm packages
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:            https://github.com/rpm-software-management/%{name}
Source0:        https://github.com/rpm-software-management/drpm/archive/refs/tags/%{version}.tar.gz#/drpm-%{version}.tar.gz
Patch01:        0001-Add-libcmocka-suppresion-file.patch
%if 0%{?suse_version}
%endif
%if %{with zstd}
%endif
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64
%endif
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libcmocka-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  rpm-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
The drpm package provides a library for making, reading and applying deltarpms,
compatible with the original deltarpm packages.

%package devel
Summary:        C interface for the drpm library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The drpm-devel package provides a C interface (drpm.h) for the drpm library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DWITH_ZSTD:BOOL=%{?with_zstd:ON}%{!?with_zstd:OFF} -DHAVE_LZLIB_DEVEL:BOOL=%{?suse_version:ON}%{!?suse_version:OFF}
%cmake_build
%cmake_build --target doc
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%if (0%{?rhel} && 0%{?rhel} < 8) || 0%{?suse_version} || (0%{?oreon} >= 11)
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%endif
%files -f %{oreon_filedir}/main.list
%files -n drpm-devel -f %{oreon_filedir}/drpm-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.3-2
- Import
