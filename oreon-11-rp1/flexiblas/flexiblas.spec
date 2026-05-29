%global source0_hash none

%bcond system_lapack 0
%bcond atlas %[%{undefined rhel} && %{undefined flatpak} && "%{_arch}" != "riscv64" ]
%bcond blis %[%{undefined rhel} && %{undefined flatpak}]
%bcond openblas 1

# https://bugzilla.redhat.com/show_bug.cgi?id=2058840
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
Release:        2%{?dist}
Summary:        A BLAS/LAPACK wrapper library with runtime exchangeable backends

# LGPL-3.0-or-later
# libcscutils/ is LGPL-2.0-or-later
# contributed/ and test/ are BSD-3-Clause-Open-MPI
License:        LGPL-3.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause-Open-MPI
URL:            https://www.mpi-magdeburg.mpg.de/projects/%{name}
Source:        https://github.com/mpimd-csc/flexiblas/archive/v/flexiblas-.tar.gz

BuildRequires:  cmake, python
BuildRequires:  gcc, gcc-fortran
BuildRequires:  multilib-rpm-config
%if %{with system_lapack}
BuildRequires:  blas-static, lapack-static
%endif
%if %{with atlas}
BuildRequires:  atlas-devel
%endif
%if %{with blis}
BuildRequires:  blis-devel
%endif
%if %{with openblas}
BuildRequires:  openblas-devel
%endif
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%global _description %{expand:
FlexiBLAS is a wrapper library that enables the exchange of the BLAS and
LAPACK implementation used by a program without recompiling or relinking it.
}

%description %_description

%package        netlib
Summary:        FlexiBLAS wrapper library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-%{default_backend}%{?_isa} = %{version}-%{release}

%description    netlib %_description
This package contains the wrapper library with 32-bit integer support.

%package        hook-profile
Summary:        FlexiBLAS profile hook plugin
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    hook-profile %_description
This package contains a plugin that enables profiling support.

%package        devel
Summary:        Development headers and libraries for FlexiBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}
%if 0%{?__isa_bits} == 64
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}
%endif

%description    devel %_description
This package contains the development headers and libraries.

%if %{with atlas}
%package        atlas
Supplements:    (atlas and %{name})
Summary:        FlexiBLAS wrappers for ATLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    atlas %_description
This package contains FlexiBLAS wrappers for the ATLAS project.
%endif

%if %{with blis}
%package        blis-serial
Supplements:    (blis-serial and %{name})
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    blis-serial %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 32-integer interface.

%package        blis-openmp
Supplements:    (blis-openmp and %{name})
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    blis-openmp %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 32-integer interface.

%package        blis-threads
Supplements:    (blis-threads and %{name})
Summary:        FlexiBLAS wrappers for BLIS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    blis-threads %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 32-integer interface.
%endif

%if %{with openblas}
%package        openblas-serial
Supplements:    (openblas-serial and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    openblas-serial %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 32-integer interface.

%package        openblas-openmp
Supplements:    (openblas-openmp and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    openblas-openmp %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 32-integer interface.

%package        openblas-threads
Supplements:    (openblas-threads and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib%{?_isa} = %{version}-%{release}

%description    openblas-threads %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 32-integer interface.
%endif

%if 0%{?__isa_bits} == 64
%package        netlib64
Summary:        FlexiBLAS wrapper library (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-%{default_backend64}%{?_isa} = %{version}-%{release}

%description    netlib64 %_description
This package contains the wrapper library with 64-bit integer support.

%package        hook-profile64
Summary:        FlexiBLAS profile hook plugin (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    hook-profile64 %_description
This package contains a plugin that enables profiling support.

%if %{with blis}
%package        blis-serial64
Supplements:    (blis-serial64 and %{name})
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    blis-serial64 %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 64-integer interface.

%package        blis-openmp64
Supplements:    (blis-openmp64 and %{name})
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    blis-openmp64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 64-integer interface.

%package        blis-threads64
Supplements:    (blis-threads64 and %{name})
Summary:        FlexiBLAS wrappers for BLIS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    blis-threads64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 64-integer interface.
%endif

%if %{with openblas}
%package        openblas-serial64
Supplements:    (openblas-serial64 and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    openblas-serial64 %_description
This package contains FlexiBLAS wrappers for the sequential library compiled
with a 64-integer interface.

%package        openblas-openmp64
Supplements:    (openblas-openmp64 and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    openblas-openmp64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
OpenMP support with a 64-integer interface.

%package        openblas-threads64
Supplements:    (openblas-threads64 and %{name})
Summary:        FlexiBLAS wrappers for OpenBLAS (64-bit)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-netlib64%{?_isa} = %{version}-%{release}

%description    openblas-threads64 %_description
This package contains FlexiBLAS wrappers for the library compiled with
threading support with a 64-integer interface.
%endif
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

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

# Replace arch-dependent header file with arch-independent stub
%multilib_fix_c_header --file %{_includedir}/%{name}/%{name}_config.h

# remove dummy hook
rm -f %{buildroot}%{_libdir}/%{name}*/lib%{name}_hook_dummy.so

# set Fedora-friendly names
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

%check
%global _smp_mflags -j1
# limit the number of threads
# MAX_CORES=10; CORES=$(nproc)
# export OMP_NUM_THREADS=$((CORES > MAX_CORES ? MAX_CORES : CORES))
export CTEST_OUTPUT_ON_FAILURE=1
export FLEXIBLAS_TEST=%{buildroot}%{_libdir}/%{name}/lib%{name}_%{default_backend}.so
%global _vpath_builddir build
%ctest
%if 0%{?__isa_bits} == 64
export FLEXIBLAS64_TEST=%{buildroot}%{_libdir}/%{name}64/lib%{name}_%{default_backend64}.so
%global _vpath_builddir build64
%ctest
%endif

%files
%license COPYING COPYING.NETLIB
%doc ISSUES.md README.md CHANGELOG

%files netlib
%config(noreplace) %{_sysconfdir}/%{name}rc
%dir %{_sysconfdir}/%{name}rc.d
%{_sysconfdir}/%{name}rc.d/netlib.conf
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.%{major_version}
%{_libdir}/lib%{name}.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}_api.so.%{major_version}
%{_libdir}/lib%{name}_api.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}_mgmt.so.%{major_version}
%{_libdir}/lib%{name}_mgmt.so.%{major_version}.%{minor_version}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}_fallback_lapack.so
%{_libdir}/%{name}/lib%{name}_netlib.so
%{_mandir}/man1/%{name}.1*

%files hook-profile
%{_libdir}/%{name}/lib%{name}_hook_profile.so

%files devel
%{_bindir}/%{name}-config
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}_api.so
%{_libdir}/lib%{name}_mgmt.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_api.pc
%if 0%{?__isa_bits} == 64
%{_bindir}/%{name}64-config
%{_includedir}/%{name}64
%{_libdir}/lib%{name}64.so
%{_libdir}/lib%{name}64_api.so
%{_libdir}/lib%{name}64_mgmt.so
%{_libdir}/pkgconfig/%{name}64.pc
%{_libdir}/pkgconfig/%{name}64_api.pc
%endif
%{_mandir}/man3/%{name}_*
%{_mandir}/man7/%{name}-api.7*

%if %{with atlas}
%files atlas
%{_sysconfdir}/%{name}rc.d/*atlas.conf
%{_libdir}/%{name}/lib%{name}_*atlas.so
%endif

%if %{with blis}
%files blis-serial
%{_sysconfdir}/%{name}rc.d/blis-serial.conf
%{_libdir}/%{name}/lib%{name}_blis-serial.so

%files blis-openmp
%{_sysconfdir}/%{name}rc.d/blis-openmp.conf
%{_libdir}/%{name}/lib%{name}_blis-openmp.so

%files blis-threads
%{_sysconfdir}/%{name}rc.d/blis-threads.conf
%{_libdir}/%{name}/lib%{name}_blis-threads.so
%endif

%if %{with openblas}
%files openblas-serial
%{_sysconfdir}/%{name}rc.d/openblas-serial.conf
%{_libdir}/%{name}/lib%{name}_openblas-serial.so

%files openblas-openmp
%{_sysconfdir}/%{name}rc.d/openblas-openmp.conf
%{_libdir}/%{name}/lib%{name}_openblas-openmp.so

%files openblas-threads
%{_sysconfdir}/%{name}rc.d/openblas-threads.conf
%{_libdir}/%{name}/lib%{name}_openblas-threads.so
%endif

%if 0%{?__isa_bits} == 64
%files netlib64
%config(noreplace) %{_sysconfdir}/%{name}64rc
%dir %{_sysconfdir}/%{name}64rc.d
%{_sysconfdir}/%{name}64rc.d/netlib.conf
%{_bindir}/%{name}64
%{_libdir}/lib%{name}64.so.%{major_version}
%{_libdir}/lib%{name}64.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}64_api.so.%{major_version}
%{_libdir}/lib%{name}64_api.so.%{major_version}.%{minor_version}
%{_libdir}/lib%{name}64_mgmt.so.%{major_version}
%{_libdir}/lib%{name}64_mgmt.so.%{major_version}.%{minor_version}
%dir %{_libdir}/%{name}64
%{_libdir}/%{name}64/lib%{name}_fallback_lapack.so
%{_libdir}/%{name}64/lib%{name}_netlib.so
%{_mandir}/man1/%{name}64.1*

%files hook-profile64
%{_libdir}/%{name}64/lib%{name}_hook_profile.so

%if %{with blis}
%files blis-serial64
%{_sysconfdir}/%{name}64rc.d/blis-serial64.conf
%{_libdir}/%{name}64/lib%{name}_blis-serial64.so

%files blis-openmp64
%{_sysconfdir}/%{name}64rc.d/blis-openmp64.conf
%{_libdir}/%{name}64/lib%{name}_blis-openmp64.so

%files blis-threads64
%{_sysconfdir}/%{name}64rc.d/blis-threads64.conf
%{_libdir}/%{name}64/lib%{name}_blis-threads64.so
%endif

%if %{with openblas}
%files openblas-serial64
%{_sysconfdir}/%{name}64rc.d/openblas-serial64.conf
%{_libdir}/%{name}64/lib%{name}_openblas-serial64.so

%files openblas-openmp64
%{_sysconfdir}/%{name}64rc.d/openblas-openmp64.conf
%{_libdir}/%{name}64/lib%{name}_openblas-openmp64.so

%files openblas-threads64
%{_sysconfdir}/%{name}64rc.d/openblas-threads64.conf
%{_libdir}/%{name}64/lib%{name}_openblas-threads64.so
%endif
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{major_version}.%{minor_version}.%{patch_version}-2
- Prepare for Oreon 11 (RP1)
