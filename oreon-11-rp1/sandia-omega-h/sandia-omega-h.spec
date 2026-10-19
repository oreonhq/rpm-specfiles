%global source0_hash 2eadfd6d634abc0b50396a82fd446f8f0b586ba6e64788c47827162c2aadec02
%global forgeurl https://github.com/sandialabs/omega_h
%global soversion 9
%bcond mpich 1
%bcond openmpi 1
%bcond openmp 0
%bcond examples 0
%bcond tests 1
%bcond throw 0
Name:           sandia-omega-h
Version:        9.34.13
Release:        1%{?dist}
Summary:        Reliable mesh adaptation
%global tag v%{version}
%forgemeta
License:        BSD-2-Clause AND BSL-1.0 AND LicenseRef-Fedora-Public-Domain AND MIT AND BSD-3-Clause
URL:            https://sandialabs.github.io/repo/#/sandialabs/omega_h
Source0:        %{forgeurl}/archive/%{tag}/omega_h-%{version}.tar.gz
Patch:          build_flags_and_so_version.patch
ExcludeArch:    %{ix86} s390x
# oreon:deps
BuildRequires:  Random123-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description

%global _summary %{summary}
%global _summary_devel %{summary} (devel package)

%package devel
Summary:        %{_summary_devel}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%global _description_devel %{expand:
Omega_h header files and libraries needed for programs that use the
omega_h library.}
%description devel

%if %{with examples}
%package doc
Summary:        Examples for %{name}
BuildRequires:  gmsh
%global _description_doc %{expand:
Examples for using the Omega_h library.}
%description doc
%endif

%if %{with mpich}

%package mpich
Summary:        %{_summary} (MPICH build)
BuildRequires:  mpich-devel
Requires:       mpich
%description mpich

%package mpich-devel
Summary:        %{_summary_devel} (MPICH)
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       mpich-devel
%description mpich-devel

%if %{with examples}
%package mpich-doc
Summary:        Examples for %{name}-mpich
BuildRequires:  gmsh-mpich
%description mpich-doc
%endif

%endif

%if %{with openmpi}

%package openmpi
Summary:        %{_summary} (OpenMPI build)
BuildRequires:  openmpi-devel
Requires:       openmpi
%description openmpi

%package openmpi-devel
Summary:        %{_summary_devel} (OpenMPI)
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       openmpi-devel
%description openmpi-devel

%if %{with examples}
%package openmpi-doc
Summary:        Examples for %{name}-openmpi
BuildRequires:  gmsh-openmpi
%description openmpi-doc
%endif

%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Remove bundled Random123 and fix header file
rm -rvf tpl/random123
sed -i 's/random123/Random123/' src/Omega_h_random_inline.hpp

%if %{with mpich}
  mkdir build-mpich
%endif

%if %{with openmpi}
  mkdir build-openmpi
%endif

%build

%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
echo "MPI_HOME: ${MPI_HOME}"
echo "MPI_INCLUDE: ${MPI_INCLUDE}"
echo "MPI_LIB: ${MPI_LIB}"
echo
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_DO_STRIP:BOOL=OFF \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DINCLUDE_INSTALL_DIR:PATH=$MPI_INCLUDE \\\
        -DLIB_INSTALL_DIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=OFF \\\
        -DCMAKE_BUILD_TYPE:STRING="Release" \\\
        -DLIB_SUFFIX="" \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
%if %{with openmp}
        -DOmega_h_USE_OpenMP:BOOL=ON \\\
%endif
%if %{with examples}
        -DOmega_h_EXAMPLES:BOOL=ON \\\
%endif
        -DOmega_h_USE_MPI:BOOL=ON \\\
        -DTPL_ENABLE_MPI:BOOL=ON \\\
%if %{with tests}
        -DBUILD_TESTING:BOOL=ON \\\
%endif
%if %{with throw}
        -DOmega_h_THROW:BOOL=ON \\\
%endif
        -B . -S .. &&
popd || exit -1;
}
%global do_make_build %{expand: \
    %make_build -C build$MPI_COMPILE_TYPE || exit -1
}
%cmake \
%dnl Prior to Fedora 43, %%cmake set the nonstandard -DLIB_SUFFIX=...
    %["%{?_lib}" == "lib64" ? "-DLIB_SUFFIX=64" : ""] \
%if %{with openmp}
    -DOmega_h_USE_OpenMP:BOOL=ON \
%endif
%if %{with examples}
    -DOmega_h_EXAMPLES:BOOL=ON \
%endif
%if %{with tests}
    -DBUILD_TESTING:BOOL=ON \\\
%endif
%if %{with throw}
    -DOmega_h_THROW:BOOL=ON \
%endif
    -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build
%if %{with mpich}
%{_mpich_load}
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
%set_build_flags
export CC=mpicc
export CXX=mpicxx
export FC=mpif90
export F77=mpif77
export MPI_YES=ON
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}
%{_openmpi_unload}
%endif
%install
%global do_install %{expand: \
echo
echo "*** INSTALLING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
    %make_install -C build$MPI_COMPILE_TYPE || exit -1
echo "*** Adding '${MPI_SUFFIX}' to binaries ***"
echo
    pushd $RPM_BUILD_ROOT/$MPI_BIN
        mv -v ascii_vtk2osh{,$MPI_SUFFIX}
        mv -v msh2osh{,$MPI_SUFFIX}
        mv -v osh2vtk{,$MPI_SUFFIX}
        mv -v osh_adapt{,$MPI_SUFFIX}
        mv -v osh_box{,$MPI_SUFFIX}
        mv -v osh_calc{,$MPI_SUFFIX}
        mv -v osh_eval_implied{,$MPI_SUFFIX}
        mv -v osh_filesystem{,$MPI_SUFFIX}
        mv -v osh_fix{,$MPI_SUFFIX}
        mv -v osh_part{,$MPI_SUFFIX}
        mv -v osh_reorder{,$MPI_SUFFIX}
        mv -v osh_scale{,$MPI_SUFFIX}
        mv -v oshdiff{,$MPI_SUFFIX}
        mv -v vtkdiff{,$MPI_SUFFIX}
    popd
}
%cmake_install
mkdir man
mkdir -p %{buildroot}%{_mandir}/man1
export PATH="${PATH}:%{buildroot}%{_bindir}"
for BIN in $(find %{buildroot}%{_bindir} -type f -name osh_\* -printf '%%P ' -o -name \*diff -printf '%%P '); do
  if [ "${BIN}" = "osh_calc" ]; then continue; fi
  LD_LIBRARY_PATH="${LD_LIBRARY_PATH-}${LD_LIBRARY_PATH+:}%{buildroot}%{_libdir}" \
  help2man --section 1 --no-discard-stderr --no-info --name ${BIN}\
  --output man/${BIN}.1 ${BIN}
  install -m 0644 man/${BIN}.1 %{buildroot}%{_mandir}/man1
done
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{_openmpi_unload}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if %{with tests}
%check

%global do_check %{expand: \
echo
echo "*** TESTING %{name}-%{version}$MPI_COMPILE_TYPE ***"
echo
echo "*** MPI_LIB: ${MPI_LIB} ***"
echo
ctest \\\
    --test-dir build$MPI_COMPILE_TYPE \\\
    --output-on-failure --force-new-ctest-process \\\
    -j 2 --verbose --rerun-failed
}
%ctest --verbose --rerun-failed
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_check}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_check}
%{_openmpi_unload}
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n sandia-omega-h-devel -f %{oreon_filedir}/sandia-omega-h-devel.list
%files -n sandia-omega-h-mpich -f %{oreon_filedir}/sandia-omega-h-mpich.list
%files -n sandia-omega-h-mpich-devel -f %{oreon_filedir}/sandia-omega-h-mpich-devel.list
%files -n sandia-omega-h-openmpi -f %{oreon_filedir}/sandia-omega-h-openmpi.list
%files -n sandia-omega-h-openmpi-devel -f %{oreon_filedir}/sandia-omega-h-openmpi-devel.list

%changelog

%autochangelog
