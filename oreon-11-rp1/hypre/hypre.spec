%global source0_hash 5273205a310fb6aa3ae506ce216760fb67b30e02024874f3cdb8b811e4801de7
%bcond_without openmpi
%bcond_without mpich
%bcond check 0
%bcond_without docs
%global somajor 2
%global soversion %{somajor}.1
Name:           hypre
Version:        3.2.0
Release:        1%{?dist}
Summary:        High performance matrix preconditioners
License:        Apache-2.0 OR MIT
URL:            http://www.llnl.gov/casc/hypre/
Source0:        https://github.com/%{name}-space/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch2:         hypre-2.32.0-test.patch
Patch3:         hypre-2.32.0_request_156.patch
%if %{with docs}
%endif
%global desc \
Hypre is a set of matrix preconditioning libraries to aid in the\
solution of large systems of linear equations.
# oreon:deps
BuildRequires:  /usr/bin/latexmk
BuildRequires:  SuperLU-devel
BuildRequires:  cmake
BuildRequires:  doxygen-latex
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  make
BuildRequires:  ptscotch-mpich-devel
BuildRequires:  ptscotch-openmpi-devel
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-latex
BuildRequires:  python3-sphinx-theme-alabaster
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  superlu_dist-mpich-devel
BuildRequires:  superlu_dist-openmpi-devel
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(capt-of.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fncychap.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(listofitems.sty)
BuildRequires:  tex(needspace.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabulary.sty)
BuildRequires:  tex(threeparttable.sty)
BuildRequires:  tex(ulem.sty)
# /oreon:deps
%description
%desc

%package devel
Summary:        Development files for %name
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       SuperLU-devel%{?_isa} 
Requires:       flexiblas-devel%{?_isa}
%description devel
Development files for %name

%if %{with openmpi}
%package openmpi
Summary:        High performance matrix preconditioners - openmpi
Requires:       openmpi%{?_isa}
BuildRequires:  superlu_dist-openmpi-devel
BuildRequires:  ptscotch-openmpi-devel
%description openmpi
%desc

This is the openmpi version.

%package openmpi-devel
Summary:        Development files for %name-openmpi
Requires:       %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:       openmpi-devel%{?_isa}
Requires:       superlu_dist-openmpi-devel%{?_isa}
Requires:       ptscotch-openmpi-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}
%description openmpi-devel
Development files for %name-openmpi
%endif

%if %{with mpich}
%package mpich
Summary:        High performance matrix preconditioners - mpich
Requires:       mpich%{?_isa}
BuildRequires:  superlu_dist-mpich-devel ptscotch-mpich-devel
%description mpich
%desc

This is the mpich version.

%package mpich-devel
Summary:        Development files for %name-mpich
Requires:       %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:       mpich-devel%{?_isa}
Requires:       superlu_dist-mpich-devel%{?_isa}
Requires:       ptscotch-mpich-devel%{?_isa}
Requires:       flexiblas-devel%{?_isa}
%description mpich-devel
Development files for %name-mpich
%endif

%if %{with docs}
%package doc
Summary:        Documentation for hypre
BuildArch:      noarch
%description doc
Documentation for hypre
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %name-%version
%patch -P 2 -p1 -b .test
%patch -P 3 -p1 -b .backup

find \( -name \*.[ch] -o -name \*.cxx \) -perm /=x -exec chmod 0644 {} \;

%if %{with openmpi}
cp -a src openmpi
%endif
%if %{with mpich}
cp -a src mpich
%endif

%build

%if %{with docs}
pushd src
%configure
make -C docs
rm docs/usr-manual-html/.buildinfo
popd
%endif
pushd src/cmbuild
%cmake -S .. \
       -DHYPRE_WITH_EXTRA_CFLAGS:STRING=" -O3" -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -lsuperlu -fopenmp" \
       -DHYPRE_BUILD_EXAMPLES:BOOL=ON -DHYPRE_BUILD_TESTS:BOOL=ON -DHYPRE_BUILD_TYPE:STRING=Release \
       -DHYPRE_ENABLE_SHARED:BOOL=ON -DHYPRE_WITH_OPENMP:BOOL=ON \
       -DHYPRE_SEQUENTIAL:BOOL=ON -DHYPRE_WITH_MPI:BOOL=OFF -DHYPRE_WITH_DSUPERLU:BOOL=OFF \
       -DHYPRE_WITH_SUPERLU:BOOL=ON -DTPL_SUPERLU_INCLUDE_DIRS:FILEPATH=%{_includedir}/SuperLU -DTPL_SUPERLU_LIBRARIES:STRING=%{_libdir}/libsuperlu.so \
       -DTPL_BLAS_LIBRARIES:STRING=-lflexiblas \
       -DHYPRE_WITH_OPENMP:BOOL=ON -DHYPRE_TIMING:BOOL=ON -DHYPRE_INSTALL_PREFIX:PATH=%{_libdir} -DHYPRE_INSTALL_INCLUDEDIR:PATH=%{_includedir}/%{name}
%cmake_build
popd
%if %{with openmpi}
pushd openmpi/cmbuild
%_openmpi_load
export CC=$MPI_BIN/mpicc
%cmake -S .. \
       -DHYPRE_WITH_EXTRA_CFLAGS:STRING=" -O3" -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -fopenmp -lsuperlu_dist -lptscotch" \
       -DHYPRE_BUILD_EXAMPLES:BOOL=ON -DHYPRE_BUILD_TESTS:BOOL=ON -DHYPRE_BUILD_TYPE:STRING=Release \
       -DHYPRE_ENABLE_SHARED:BOOL=ON -DHYPRE_WITH_OPENMP:BOOL=ON \
       -DHYPRE_SEQUENTIAL:BOOL=OFF -DHYPRE_WITH_MPI:BOOL=ON -DMPI_C_COMPILER:FILEPATH=$MPI_BIN/mpicc \
       -DHYPRE_WITH_SUPERLU:BOOL=ON -DTPL_SUPERLU_INCLUDE_DIRS:FILEPATH=$MPI_INCLUDE/superlu_dist -DTPL_SUPERLU_LIBRARIES:STRING=$MPI_LIB/libsuperlu_dist.so \
       -DTPL_BLAS_LIBRARIES:STRING=-lflexiblas \
       -DHYPRE_WITH_OPENMP:BOOL=ON -DHYPRE_TIMING:BOOL=ON -DHYPRE_INSTALL_PREFIX:PATH=%{_libdir}/openmpi/lib  -DHYPRE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name}
%cmake_build
popd
%_openmpi_unload
%endif
%if %{with mpich}
pushd mpich/cmbuild
%_mpich_load
export CC=$MPI_BIN/mpicc
%cmake -S .. \
       -DHYPRE_WITH_EXTRA_CFLAGS:STRING=" -O3" -DCMAKE_SHARED_LINKER_FLAGS_RELEASE:STRING="%{__global_ldflags} -fopenmp -lsuperlu_dist -lptscotch" \
       -DHYPRE_BUILD_EXAMPLES:BOOL=ON -DHYPRE_BUILD_TESTS:BOOL=ON -DHYPRE_BUILD_TYPE:STRING=Release \
       -DHYPRE_ENABLE_SHARED:BOOL=ON -DHYPRE_WITH_OPENMP:BOOL=ON \
       -DHYPRE_SEQUENTIAL:BOOL=OFF -DHYPRE_WITH_MPI:BOOL=ON -DMPI_C_COMPILER:FILEPATH=$MPI_BIN/mpicc \
       -DHYPRE_WITH_SUPERLU:BOOL=ON -DTPL_SUPERLU_INCLUDE_DIRS:FILEPATH=$MPI_INCLUDE/superlu_dist -DTPL_SUPERLU_LIBRARIES:STRING=$MPI_LIB/libsuperlu_dist.so \
       -DTPL_BLAS_LIBRARIES:STRING=-lflexiblas \
       -DHYPRE_WITH_OPENMP:BOOL=ON -DHYPRE_TIMING:BOOL=ON -DHYPRE_INSTALL_PREFIX:PATH=%{_libdir}/mpich/lib -DHYPRE_INSTALL_INCLUDEDIR:PATH=$MPI_INCLUDE/%{name}
%cmake_build
%_mpich_unload
popd
%endif
%check

%if %{with check}
pushd src/cmbuild/%_vpath_builddir/test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
./ij*
popd
%if %{with openmpi}
pushd openmpi/cmbuild/%_vpath_builddir/test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/openmpi/lib
%_openmpi_load
./ij*
%_openmpi_unload
popd
%endif
%if %{with mpich}
pushd mpich/cmbuild/%_vpath_builddir/test
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}/mpich/lib
%_mpich_load
./ij*
%_mpich_unload
popd
%endif
%endif
%install
pushd src/cmbuild
%cmake_install
popd
%if %{with openmpi}
pushd openmpi/cmbuild
%_openmpi_load
%cmake_install
%_openmpi_unload
popd
%endif
%if %{with mpich}
pushd mpich/cmbuild
%_mpich_load
%cmake_install
%_mpich_unload
popd
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n hypre-devel -f %{oreon_filedir}/hypre-devel.list
%files -n hypre-openmpi -f %{oreon_filedir}/hypre-openmpi.list
%files -n hypre-openmpi-devel -f %{oreon_filedir}/hypre-openmpi-devel.list
%files -n hypre-mpich -f %{oreon_filedir}/hypre-mpich.list
%files -n hypre-mpich-devel -f %{oreon_filedir}/hypre-mpich-devel.list
%files -n hypre-doc -f %{oreon_filedir}/hypre-doc.list

%changelog

%autochangelog
