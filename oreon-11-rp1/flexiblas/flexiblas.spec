%global _lto_cflags %{nil}
%global _smp_mflags -j4
%global source0_hash 175bd4ad7b44348c5dc0531c7a0169ad451cbc9a3d018dd17f01d4a0d0244680
%bcond system_lapack 0
%if 0%{?rhel} || 0%{?flatpak} || (0%{?oreon} >= 11)
%bcond_with atlas
%bcond_with blis
%else
%bcond_without atlas
%bcond_without blis
%endif
%bcond openblas 1
%undefine _ld_as_needed
%if %{with openblas}
%global default_backend openblas-openmp
%else
%global default_backend netlib
%endif
%global default_backend64 %{default_backend}64
%global major_version 3
%global minor_version 5
%global patch_version 0
Name:           flexiblas
Version:        %{major_version}.%{minor_version}.%{patch_version}
Release:        1%{?dist}
Summary:        A BLAS/LAPACK wrapper library with runtime exchangeable backends
License:        LGPL-3.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause-Open-MPI
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{name}
Source0:        https://github.com/mpimd-csc/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if %{with system_lapack}
%endif
%if %{with atlas}
%endif
%if %{with blis}
%endif
%if %{with openblas}
%endif
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  atlas-devel
BuildRequires:  blis-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-fortran
BuildRequires:  multilib-rpm-config
BuildRequires:  openblas-devel
BuildRequires:  python
# /oreon:deps
%description

%package        netlib
Summary:        FlexiBLAS wrapper library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-%{default_backend}%{?_isa} = %{version}-%{release}
%description    netlib
This package contains the wrapper library with 32-bit integer support.

%package        hook-profile
Summary:        FlexiBLAS profile hook plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    hook-profile
This package contains a plugin that enables profiling support.

%package        devel
Summary:        Development headers and libraries for FlexiBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%if 0%{?__isa_bits} == 64
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%endif
%description    devel
This package contains the development headers and libraries.

%if %{with atlas}
%package        atlas
Supplements:    (atlas and %{name})
Summary:        FlexiBLAS wrappers for ATLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    atlas
This package contains FlexiBLAS wrappers for the ATLAS project.
%endif

%if %{with blis}
%package        blis-serial
Supplements:    (blis-serial and %{name})
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    blis-serial
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 32-integer interface.

%package        blis-openmp
Supplements:    (blis-openmp and %{name})
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    blis-openmp
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 32-integer interface.

%package        blis-threads
Supplements:    (blis-threads and %{name})
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    blis-threads
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 32-integer interface.
%endif

%if %{with openblas}
%package        openblas-serial
Supplements:    (openblas-serial and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    openblas-serial
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 32-integer interface.

%package        openblas-openmp
Supplements:    (openblas-openmp and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    openblas-openmp
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 32-integer interface.

%package        openblas-threads
Supplements:    (openblas-threads and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%description    openblas-threads
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 32-integer interface.
%endif

%if 0%{?__isa_bits} == 64
%package        netlib64
Summary:        FlexiBLAS wrapper library (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-%{default_backend64}%{?_isa} = %{version}-%{release}
%description    netlib64
This package contains the wrapper library with 64-bit integer support.

%package        hook-profile64
Summary:        FlexiBLAS profile hook plugin (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    hook-profile64
This package contains a plugin that enables profiling support.

%if %{with blis}
%package        blis-serial64
Supplements:    (blis-serial64 and %{name})
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    blis-serial64
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 64-integer interface.

%package        blis-openmp64
Supplements:    (blis-openmp64 and %{name})
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    blis-openmp64
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 64-integer interface.

%package        blis-threads64
Supplements:    (blis-threads64 and %{name})
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    blis-threads64
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 64-integer interface.
%endif

%if %{with openblas}
%package        openblas-serial64
Supplements:    (openblas-serial64 and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    openblas-serial64
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 64-integer interface.

%package        openblas-openmp64
Supplements:    (openblas-openmp64 and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    openblas-openmp64
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 64-integer interface.

%package        openblas-threads64
Supplements:    (openblas-threads64 and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%description    openblas-threads64
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 64-integer interface.
%endif
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%if %{with system_lapack}
rm -rf contributed/{cblas,lapack-*,netlib-blas,win32ports}
%endif
%global _vpath_builddir build
%cmake \
%if %{with system_lapack}
    -DSYS_BLAS_LIBRARY=$(pkg-config --variable=libdir blas)/libblas.a \
    -DSYS_LAPACK_LIBRARY=$(pkg-config --variable=libdir lapack)/liblapack.a \
%endif
    -DINTEGER8=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTESTS=ON
%cmake_build
%if 0%{?__isa_bits} == 64
%global _vpath_builddir build64
%cmake \
%if %{with system_lapack}
    -DSYS_BLAS_LIBRARY=$(pkg-config --variable=libdir blas)/libblas64.a \
    -DSYS_LAPACK_LIBRARY=$(pkg-config --variable=libdir lapack)/liblapack64.a \
%endif
    -DINTEGER8=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTESTS=ON
%cmake_build
%endif
%install
%global _vpath_builddir build
%cmake_install
echo "default = %{default_backend}" > %{buildroot}%{_sysconfdir}/%{name}rc
%if 0%{?__isa_bits} == 64
%global _vpath_builddir build64
%cmake_install
echo "default = %{default_backend64}" > %{buildroot}%{_sysconfdir}/%{name}64rc
%endif
%multilib_fix_c_header --file %{_includedir}/%{name}/%{name}_config.h
rm -f %{buildroot}%{_libdir}/%{name}*/lib%{name}_hook_dummy.so
rename -- serial -serial %{buildroot}%{_libdir}/%{name}*/* || true
rename -- openmp -openmp %{buildroot}%{_libdir}/%{name}*/* || true
rename -- pthread -threads %{buildroot}%{_libdir}/%{name}*/* || true
rename -- Serial -serial %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename -- OpenMP -openmp %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
rename -- PThread -threads %{buildroot}%{_sysconfdir}/%{name}*.d/* || true
find %{buildroot}%{_sysconfdir}/%{name}*.d/* -type f \
    -exec sed -i 's Serial -serial gI' {} \;\
    -exec sed -i 's OpenMP -openmp gI' {} \;\
    -exec sed -i 's PThread -threads gI' {} \;\
    -exec sed -i 's .* \L& g' {} \;\
    -exec sh -c 'mv $0 $(dirname $0)/$(basename $0 | tr [A-Z] [a-z])' {} \;
%bcond_with full_check
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

export CTEST_OUTPUT_ON_FAILURE=1
export FLEXIBLAS_TEST=%{buildroot}%{_libdir}/%{name}/lib%{name}_%{default_backend}.so
%global _vpath_builddir build
%if %{with full_check}
%ctest -j1
%if 0%{?__isa_bits} == 64
export FLEXIBLAS64_TEST=%{buildroot}%{_libdir}/%{name}64/lib%{name}_%{default_backend64}.so
%global _vpath_builddir build64
%ctest -j1
%endif
%else
test -e %{buildroot}%{_libdir}/%{name}/lib%{name}_%{default_backend}.so
%if 0%{?__isa_bits} == 64
test -e %{buildroot}%{_libdir}/%{name}64/lib%{name}_%{default_backend64}.so
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n flexiblas-netlib -f %{oreon_filedir}/flexiblas-netlib.list
%files -n flexiblas-hook-profile -f %{oreon_filedir}/flexiblas-hook-profile.list
%files -n flexiblas-devel -f %{oreon_filedir}/flexiblas-devel.list
%files -n flexiblas-atlas -f %{oreon_filedir}/flexiblas-atlas.list
%files -n flexiblas-blis-serial -f %{oreon_filedir}/flexiblas-blis-serial.list
%files -n flexiblas-blis-openmp -f %{oreon_filedir}/flexiblas-blis-openmp.list
%files -n flexiblas-blis-threads -f %{oreon_filedir}/flexiblas-blis-threads.list
%files -n flexiblas-openblas-serial -f %{oreon_filedir}/flexiblas-openblas-serial.list
%files -n flexiblas-openblas-openmp -f %{oreon_filedir}/flexiblas-openblas-openmp.list
%files -n flexiblas-openblas-threads -f %{oreon_filedir}/flexiblas-openblas-threads.list
%files -n flexiblas-netlib64 -f %{oreon_filedir}/flexiblas-netlib64.list
%files -n flexiblas-hook-profile64 -f %{oreon_filedir}/flexiblas-hook-profile64.list
%files -n flexiblas-blis-serial64 -f %{oreon_filedir}/flexiblas-blis-serial64.list
%files -n flexiblas-blis-openmp64 -f %{oreon_filedir}/flexiblas-blis-openmp64.list
%files -n flexiblas-blis-threads64 -f %{oreon_filedir}/flexiblas-blis-threads64.list
%files -n flexiblas-openblas-serial64 -f %{oreon_filedir}/flexiblas-openblas-serial64.list
%files -n flexiblas-openblas-openmp64 -f %{oreon_filedir}/flexiblas-openblas-openmp64.list
%files -n flexiblas-openblas-threads64 -f %{oreon_filedir}/flexiblas-openblas-threads64.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{major_version}.%{minor_version}.%{patch_version}-2
- Prepare for Oreon 11 (RP1)
