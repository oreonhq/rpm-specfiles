%global source0_hash none

# Do not build with zstd for RHEL < 8
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?suse_version} && 0%{?suse_version} < 1500) || 0%{?oreon}
%bcond_with zstd
%else
%bcond_without zstd
%endif

Name:           drpm
Version:        0.5.3
Release:        2%{?dist}
Summary:        A library for making, reading and applying deltarpm packages
# the entire source code is LGPLv2+, except src/drpm_diff.c and src/drpm_search.c which are BSD
# Automatically converted from old format: LGPLv2+ and BSD - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+ AND LicenseRef-Callaway-BSD
URL:            https://github.com/rpm-software-management/%{name}
Source:        https://github.com/rpm-software-management/drpm/releases/download/0.5.3/drpm-0.5.3.tar.bz2

Patch01:        0001-Add-libcmocka-suppresion-file.patch

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.5.0
BuildRequires:  gcc

BuildRequires:  rpm-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
BuildRequires:  bzip2-devel
BuildRequires:  xz-devel
%if 0%{?suse_version}
BuildRequires:  lzlib-devel
%endif
%if %{with zstd}
BuildRequires:  pkgconfig(libzstd)
%endif

BuildRequires:  pkgconfig
BuildRequires:  doxygen

BuildRequires:  libcmocka-devel >= 1.0
%ifarch %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64
BuildRequires:  valgrind
%endif

%description
The drpm package provides a library for making, reading and applying deltarpms,
compatible with the original deltarpm packages.

%package devel
Summary:        C interface for the drpm library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The drpm-devel package provides a C interface (drpm.h) for the drpm library.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%build
%cmake -DWITH_ZSTD:BOOL=%{?with_zstd:ON}%{!?with_zstd:OFF} -DHAVE_LZLIB_DEVEL:BOOL=%{?suse_version:ON}%{!?suse_version:OFF}
%cmake_build
%cmake_build --target doc

%install
%cmake_install

%check
%ctest

%if (0%{?rhel} && 0%{?rhel} < 8) || 0%{?suse_version} || 0%{?oreon}
%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif

%files
%{_libdir}/lib%{name}.so.*
%license COPYING LICENSE.BSD

%files devel
%doc %{_vpath_builddir}/doc/html/
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.5.3-2
- Import
