%global source0_hash ed9ea3754594e8c595c306e2dff4ce1c98a057035040a9978a2f16fda26d01cb
%global forgeurl https://github.com/fzenke/auryn
%bcond serial 1
%bcond mpich 1
%bcond openmpi 1
%bcond tests 1
Name:           auryn
Version:        0.8.4
Release:        1%{?dist}
Summary:        Plastic Recurrent Network Simulator
%forgemeta
License:        GPL-3.0-only
URL:            http://www.fzenke.net/auryn/
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         auryn-boost_filesystem.patch
%global _version %{version}
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  boost-mpich
BuildRequires:  boost-mpich-devel
BuildRequires:  boost-openmpi
BuildRequires:  boost-openmpi-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
# /oreon:deps
%description
Auryn is a source package used to create highly specialized and optimized code
to simulate recurrent spiking neural networks with spike timing dependent
plasticity (STDP).

Detailed documentation and a forum for support/discussion are available at
https://fzenke.net/auryn

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if %{with doc}
%package        doc
Summary:        Examples for %{name}
BuildArch:      noarch
%description    doc
This package contains examples for %{name}
%endif

%if %{with mpich}
%package mpich
Summary:        %summary (MPICH)
BuildRequires:  mpich-devel
BuildRequires:  boost-mpich-devel
BuildRequires:  boost-mpich
Requires:       mpich
%description mpich
Auryn is a source package used to create highly specialized and optimized code
to simulate recurrent spiking neural networks with spike timing dependent
plasticity (STDP).

Detailed documentation and a forum for support/discussion are available at
https://fzenke.net/auryn

%package mpich-devel
Summary:        Development files for %{name}-mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Provides:       %{name}-mpich-static = %{version}-%{release}
%description mpich-devel
The %{name}-mpich-devel package contains libraries and header files for
developing applications that use %{name}-mpich.

%endif
# mpich

%if %{with openmpi}
%package openmpi
Summary:        %summary (OpenMPI)
BuildRequires:  openmpi-devel
BuildRequires:  boost-openmpi-devel
BuildRequires:  boost-openmpi
BuildRequires:  make
Requires:       openmpi
%description openmpi
Auryn is a source package used to create highly specialized and optimized code
to simulate recurrent spiking neural networks with spike timing dependent
plasticity (STDP).

Detailed documentation and a forum for support/discussion are available at
https://fzenke.net/auryn

%package openmpi-devel
Summary:        Development files for %{name}-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Provides:       %{name}-openmpi-static = %{version}-%{release}
%description openmpi-devel
The %{name}-openmpi-devel package contains libraries and header files for
developing applications that use %{name}-openmpi.

%endif
# openmpi

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

# Tweaks for all versions
# Don't let it set its own optimisation flags
sed -i '/SET(CMAKE_CXX_FLAGS/ d' CMakeLists.txt
# Don't make MPI mandatory. It's not needed for the serial build.
sed -i 's/MPI REQUIRED/MPI/' CMakeLists.txt
# Modify test scripts for easier use in the sub builds
sed -i '/^BUILDDIR/ d' test/*.sh
sed -i 's|^.BUILDDIR/test/||' test/*.sh

# Need to disable vector intrinsics on these architectures
%ifarch %{arm} s390x aarch64 %{power64} riscv64
    sed -i 's|^\(#define CODE_USE_SIMD_INSTRUCTIONS_EXPLICITLY\)|//\1|' src/auryn/auryn_definitions.h
%endif

%if %{with serial}
    mkdir build-serial
%endif

%if %{with mpich}
    mkdir build-mpich
%endif

%if %{with openmpi}
    mkdir build-openmpi
%endif

%build

%global do_cmake_config %{expand: \
echo
echo "*** BUILDING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
%set_build_flags
pushd build$MPI_COMPILE_TYPE  &&
    cmake \\\
        -DCMAKE_FIND_NO_INSTALL_PREFIX:BOOL=TRUE \\\
        -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS -DBOOST_TIMER_ENABLE_DEPRECATED" \\\
        -DCMAKE_C_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_CXX_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_Fortran_FLAGS_RELEASE:STRING="-DNDEBUG" \\\
        -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \\\
        -DCMAKE_INSTALL_PREFIX:PATH="$MPI_HOME" \\\
        -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \\\
        -DLIB_INSTALL_DIR:PATH=%{_libdir} \\\
        -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \\\
        -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \\\
        -DCMAKE_SKIP_RPATH:BOOL=ON \\\
        -DBUILD_SHARED_LIBS:BOOL=ON \\\
%if "%{_lib}" == "lib64"
        -DLIB_SUFFIX=64 .. &&
%else
        -DLIB_SUFFIX="" .. &&
%endif
popd || exit -1;
}
%global do_make_build %{expand: \
    make %{?_smp_mflags} -C build$MPI_COMPILE_TYPE || exit -1
}
%if %{with serial}
export MPI_COMPILE_TYPE="-serial"
export MPI_HOME=%{_prefix}
sed -i.mpi '/#define AURYN_CODE_USE_MPI/d' src/auryn/auryn_definitions.h
%{do_cmake_config}
%{do_make_build}
mv -v src/auryn/auryn_definitions.h.mpi src/auryn/auryn_definitions.h
sed -r -i 's|(\{CMAKE_INSTALL_PREFIX\}/lib)"|\164"|' \
    build$MPI_COMPILE_TYPE/src/cmake_install.cmake
%endif
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_cmake_config}
%{do_make_build}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_cmake_config}
%{do_make_build}
%{_openmpi_unload}
%endif
%install
%global do_install %{expand:
echo
echo "*** INSTALLING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" CPPROG="cp -p" -C build$MPI_COMPILE_TYPE || exit -1
}
%global do_rename %{expand:
echo
echo "*** RENAMING binaries for %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    pushd $RPM_BUILD_ROOT/$MPI_BIN/
        mv -v aube{,$MPI_SUFFIX}
        mv -v aubs{,$MPI_SUFFIX}
    popd
}
%if %{with serial}
export MPI_COMPILE_TYPE="-serial"
%{do_install}
%endif
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_install}
%{do_rename}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_install}
%{do_rename}
%{_openmpi_unload}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%if %{with tests}
%check

%global do_tests %{expand:
echo
echo "*** TESTING %{name}-%{_version}$MPI_COMPILE_TYPE ***"
echo
    pushd build$MPI_COMPILE_TYPE/test
        ../../test/run_unit_tests.sh || exit -1
    popd
}
%if %{with serial}
export MPI_COMPILE_TYPE="-serial"
%{do_tests}
%endif
%if %{with mpich}
%{_mpich_load}
export MPI_COMPILE_TYPE="-mpich"
%{do_tests}
%{_mpich_unload}
%endif
%if %{with openmpi}
%{_openmpi_load}
export MPI_COMPILE_TYPE="-openmpi"
%{do_tests}
%{_openmpi_unload}
%endif
%endif
%if %{with doc}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
