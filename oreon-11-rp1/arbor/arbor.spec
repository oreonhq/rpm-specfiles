%global source2_hash 03ea9543de5dfff32bbbc57b5a5b9674386b6478368716f03857385763b7e27d
%global source1_hash 05aa7eb6ee209b3c3c8f65cab268ea984d955e8f9307037845f5c40b264b5964
%global source0_hash 920c7926453379d367c6c8bb01ff867c03e44e8a7a6a5655d5eaa3d692618ca1
%bcond mpich 1
%bcond openmpi 1
%bcond tests 1
%bcond mpi_py_unittest 0
%global forgeurl            https://github.com/arbor-sim/arbor
Name:           arbor
Version:        0.9.0
Release:        1%{?dist}
Summary:        Multi-compartment neural network simulation library
%forgemeta
URL:            %forgeurl
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/arbor-sim/arbor/master/scripts/run_python_examples.sh
Source2:        https://raw.githubusercontent.com/arbor-sim/arbor/master/scripts/run_cpp_examples.sh
License:        BSD-3-Clause
Patch:          0001-Quote-various-cmake-var-values.patch
Patch:          fix-missing-includes.patch
Patch:          0001-Fix-a-few-typos-that-cause-failure-to-compile-with-G.patch
Patch:          arbor-0.9.0-pybind11-3.0.patch
ExcludeArch:    mips64r2 mips32r2 s390x %{ix86}
%if %{with tests}
%endif
Requires:       %{py3_dist numpy}
%py_provides python3-arbor
# oreon:deps
BuildRequires:  Random123-devel
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  google-benchmark-devel
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  libunwind-devel
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  pugixml-devel
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
BuildRequires:  python3-mpi4py-mpich
BuildRequires:  python3-mpi4py-openmpi
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-svgwrite
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(seaborn)
BuildRequires:  rpm-mpi-hooks
BuildRequires:  tclap-devel
# /oreon:deps
%description

%package devel
Summary:    Development files for arbor
Requires:   arbor%{?_isa} = %{version}-%{release}
Provides:   arbor-static = %{version}-%{release}
%description devel

%package doc
Summary:        Documentation for arbor
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-svgwrite
BuildArch:      noarch
%description doc

%if %{with mpich}
%package mpich
Summary:        MPICH build for arbor
BuildRequires:  mpich-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-mpich
Requires:       mpich
Requires:       python3-mpich
Requires:       python3-mpi4py-mpich
Requires:       %{py3_dist numpy}
Provides:       python3-arbor-mpich = %{version}-%{release}
%description mpich

%package mpich-devel
Summary:    Development files for arbor-mpich
Requires:   arbor-mpich%{?_isa} = %{version}-%{release}
Provides:   arbor-mpich-static = %{version}-%{release}
%description mpich-devel
%endif

%if %{with openmpi}
%package openmpi
Summary:        OpenMPI build for arbor
BuildRequires:  openmpi-devel
BuildRequires:  rpm-mpi-hooks
BuildRequires:  python3-mpi4py-openmpi
Requires:       openmpi
Requires:       python3-openmpi
Requires:       python3-mpi4py-openmpi
Requires:       %{py3_dist numpy}
Provides:       python3-arbor-openmpi = %{version}-%{release}
%description openmpi

%package openmpi-devel
Summary:    Development files for arbor-openmpi
Requires:   arbor-openmpi%{?_isa} = %{version}-%{release}
Provides:   arbor-openmpi-static = %{version}-%{release}
%description openmpi-devel
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# correct catalogue location
sed -i 's|dummy-catalogue.so|lib/dummy-catalogue.so|' python/test/unit/test_catalogues.py

# Disable failing padded test
sed -i '/test_padded.cpp/ d' test/unit/CMakeLists.txt

# should always be included, but is currently included only if bundled pybind11
# is used
sed -i '/add_subdirectory(python)/i \
include(FindPythonModule)' CMakeLists.txt
# Do not build external libraries
sed -i -e 's/ ext-random123//' CMakeLists.txt

# Disable doc build: we built it ourselves
sed -i '/add_subdirectory(doc)/ d' CMakeLists.txt

# Remove ext folders, unbundle libraries
rm -vrf ext/google-benchmark ext/json ext/random123
mv ext/tinyopt/LICENSE ext/tinyopt/LICENSE-tinyopt

# tclap and json are both header only
find . -type f -name "CMakeLists.txt" -exec sed -i -e 's/ext-tclap//' -e 's/ext-json//' {} 2>/dev/null ';'

# Correct Python shebangs in all files
find . -type f -name "*" -exec sed -i 's|^#![  ]*/usr/bin/env.*python.*$|#!/usr/bin/python3|' {} 2>/dev/null ';'

# Fix shebang (special case)
sed -i 's|^#![  ]*/usr/env/bin.*python.*$|#!/usr/bin/python3|' example/lfp/neuron_lfp_example.py

# test scripts
cp %{SOURCE1} scripts/
cp %{SOURCE2} scripts/
chmod +x scripts/*.sh
sed -i 's/ python / python3 /' scripts/run_python_examples.sh
sed -i 's|build/|./|' scripts/run_cpp_examples.sh

# builddir for serial
mkdir build-serial

%if %{with mpich}
    mkdir build-mpich
%endif

%if %{with openmpi}
    mkdir build-openmpi
%endif

%build

%global do_cmake_config %{expand: \
echo
echo "*** BUILDING arbor-%{version}$MPI_COMPILE_TYPE ***"
echo
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH=$MPI_HOME \\\
        -DINCLUDE_INSTALL_DIR:PATH=$MPI_INCLUDE \\\
        -DLIB_INSTALL_DIR:PATH=$MPI_LIB \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DCMAKE_BUILD_TYPE:STRING="release" \\\
        -DARB_USE_BUNDLED_LIBS:BOOL=OFF \\\
        -DARB_USE_BUNDLED_PYBIND11:BOOL=OFF \\\
        -DARB_VECTORIZE:BOOL=OFF \\\
        -DARB_WITH_MPI:BOOL=$MPI_YES \\\
        -DARB_WITH_GPU:BOOL=OFF \\\
        -DARB_ARCH:STRING="none" \\\
        -DARB_CXX_FLAGS_TARGET:STRING="-ffat-lto-objects" \\\
        -DCMAKE_INSTALL_LIBDIR=%{_lib} \\\
        -DARB_WITH_PYTHON:BOOL=ON \\\
        -DARB_PYTHON_LIB_PATH:STRING=$MPI_PYTHON3_SITEARCH \\\
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 .. &&
%else
        -DLIB_SUFFIX=""  .. &&
%endif
popd || exit -1;
}
%global do_make_build %{expand: \
    %make_build -C build$MPI_COMPILE_TYPE || exit -1
    %make_build -C build$MPI_COMPILE_TYPE examples || exit -1
%if %{with tests}
    %make_build -C build$MPI_COMPILE_TYPE tests || exit -1
%endif
}
%set_build_flags
export CC=gcc
export CXX=g++
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_INCLUDE=%{_includedir}
export MPI_LIB=%{_libdir}
export MPI_YES=OFF
export MPI_COMPILE_TYPE="-serial"
export MPI_PYTHON3_SITEARCH=%{python3_sitearch}
%{do_cmake_config}
%{do_make_build}
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
echo "*** INSTALLING arbor-%{version}$MPI_COMPILE_TYPE ***"
echo
    %make_install -C build$MPI_COMPILE_TYPE || exit -1
}
export MPI_SUFFIX=""
export MPI_HOME=%{_prefix}
export MPI_BIN=%{_bindir}
export MPI_YES=OFF
export MPI_COMPILE_TYPE="-serial"
%{do_install}
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}
%if "%{_lib}" == "lib64"
    mv -v $RPM_BUILD_ROOT/%{_libdir}/mpich/lib64 $RPM_BUILD_ROOT/$MPI_LIB/
%endif
pushd $RPM_BUILD_ROOT/$MPI_BIN
    mv -v modcc{,$MPI_SUFFIX} -v
    mv -v arbor-build-catalogue{,$MPI_SUFFIX} -v
    mv -v lmorpho{,$MPI_SUFFIX} -v
popd
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%if "%{_lib}" == "lib64"
    mv -v $RPM_BUILD_ROOT/%{_libdir}/openmpi/lib64 $RPM_BUILD_ROOT/$MPI_LIB/
%endif
pushd $RPM_BUILD_ROOT/$MPI_BIN
    mv -v modcc{,$MPI_SUFFIX} -v
    mv -v arbor-build-catalogue{,$MPI_SUFFIX} -v
    mv -v lmorpho{,$MPI_SUFFIX} -v
popd
%{_openmpi_unload}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if %{with tests}
%check

%global mpirun mpirun -n %{_smp_build_ncpus}
gtest_filter="${gtest_filter--}${gtest_filter+:}*diffusion*"
pushd build-serial
    %{py3_test_envvars} %{python3} -m unittest discover -v -s ../python
    ./bin/unit ${gtest_filter+--gtest_filter=}${gtest_filter-}
    ./bin/unit-modcc
    cp ../scripts/run_cpp_examples.sh .
    ./run_cpp_examples.sh
popd
%if %{with mpich}
%{_mpich_load}
pushd build-mpich
%if %{with mpi_py_unittest}
    %{py3_test_envvars} %{mpirun} %{python3} -m unittest discover -v -s ../python
%endif
    %{mpirun} ./bin/unit-mpi
    cp ../scripts/run_cpp_examples.sh .
    ./run_cpp_examples.sh "%{mpirun}"
popd
%{py3_test_envvars} ./scripts/run_python_examples.sh  "%{mpirun}"
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
pushd build-openmpi
%if %{with mpi_py_unittest}
    %{py3_test_envvars} %{mpirun} %{python3} -m unittest discover -v -s ../python
%endif
    %{mpirun} ./bin/unit-mpi
    cp ../scripts/run_cpp_examples.sh .
    ./run_cpp_examples.sh "%{mpirun}"
popd
%{py3_test_envvars} ./scripts/run_python_examples.sh  "%{mpirun}"
%{_openmpi_unload}
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
