%global source0_hash 325cfbcf0c0296a6dd26f3b088801b7ebb8d6f109c0565c11d2d8c4af3253bff

Name:           espresso
Version:        5.0.0
Release:        2%{?dist}
Summary:        Extensible Simulation Package for Research on Soft matter
# segfault on s390x: https://github.com/espressomd/espresso/issues/3753
# segfault on armv7hl: https://src.fedoraproject.org/rpms/espresso/pull-request/4
ExcludeArch:    s390x i686 armv7hl

License:        GPL-3.0-or-later
URL:            https://espressomd.org
Source0:        https://github.com/espressomd/espresso/archive/%{version}.tar.gz#/espresso-%{version}.tar.gz
Source1:        https://i10git.cs.fau.de/walberla/walberla/-/archive/3247aa73.tar.gz#/waberla-3247aa73.tar.gz
Source2:        https://github.com/ECP-copa/Cabana/archive/0.7.0.tar.gz#/Cabana-0.7.0.tar.gz
Source3:        https://github.com/highfive-devs/highfive/archive/v3.3.0.tar.gz#/highfive-v3.3.0.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 4.0.0
BuildRequires:  ninja-build >= 1.12.1
BuildRequires:  /usr/bin/cython
%global cython /usr/bin/cython
BuildRequires:  fftw-devel
BuildRequires:  python%{python3_pkgversion}-numpy
BuildRequires:  python%{python3_pkgversion}-scipy
BuildRequires:  python%{python3_pkgversion}-six
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-packaging
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  boost-devel
BuildRequires:  hdf5-devel
BuildRequires:  gsl-devel
BuildRequires:  NLopt-devel
BuildRequires:  boost-devel
BuildRequires:  kokkos-devel
BuildRequires:  mpich-devel
BuildRequires:  boost-mpich-devel
BuildRequires:  heffte-mpich-devel
BuildRequires:  hdf5-mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  boost-openmpi-devel
BuildRequires:  heffte-openmpi-devel
BuildRequires:  hdf5-openmpi-devel
BuildRequires:  python%{python3_pkgversion}-h5py

Requires:       python%{python3_pkgversion}-numpy
Requires:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name}-devel < %{version}-%{release}

%description
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics

%package common
Summary:        Common files for %{name} packages
BuildArch:      noarch
Requires:       %{name}-common = %{version}-%{release}
%description common
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics
This package contains the license file and data files shared between the
sub-packages of %{name}.

%package -n python%{python3_pkgversion}-%{name}-openmpi
Requires:       %{name}-common = %{version}-%{release}
Requires:       python%{python3_pkgversion}-h5py
Summary:        Extensible Simulation Package for Research on Soft matter
Provides:       %{name}-openmpi = %{version}-%{release}
Obsoletes:      %{name}-openmpi < 3.3.0-12
%description -n python%{python3_pkgversion}-%{name}-openmpi
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics

This package contains %{name} compiled against Open MPI.

%package -n python%{python3_pkgversion}-%{name}-mpich
Requires:       %{name}-common = %{version}-%{release}
Requires:       python%{python3_pkgversion}-h5py
Summary:        Extensible Simulation Package for Research on Soft matter
Provides:       %{name}-mpich2 = %{version}-%{release}
Obsoletes:      %{name}-mpich2 < 3.1.1-3
Provides:       %{name}-mpich = %{version}-%{release}
Obsoletes:      %{name}-mpich < 3.3.0-12
%description -n python%{python3_pkgversion}-%{name}-mpich
ESPResSo can perform Molecular Dynamics simulations of bead-spring models
in various ensembles ((N,V,E), (N,V,T), and (N,p,T)).
ESPResSo contains a number of advanced algorithms, e.g.
    * DPD thermostat (for hydrodynamics)
    * P3M, MMM1D, ELC for electrostatic interactions
    * Lattice-Boltzmann for hydrodynamics

This package contains %{name} compiled against MPICH2.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
# ESPResSo patches would go here:
# patch 0 -p1
%setup -q -T -D -a 1
%setup -q -T -D -a 2
%setup -q -T -D -a 3
sed -ri "s|GIT_REPOSITORY +https://github.com/ECP-copa/Cabana.git|URL $(realpath Cabana-*/)|" CMakeLists.txt
sed -ri "s|GIT_REPOSITORY +https://github.com/highfive-devs/highfive.git|URL $(realpath highfive-*/)|" CMakeLists.txt
sed -ri "s|GIT_REPOSITORY +https://i10git.cs.fau.de/walberla/walberla.git|URL $(realpath walberla-*/)|" CMakeLists.txt

%build
%global defopts \\\
 -G Ninja \\\
 -D ESPRESSO_BUILD_WITH_PYTHON=ON \\\
 -D ESPRESSO_BUILD_TESTS=ON \\\
 -D CMAKE_SKIP_RPATH=ON \\\
 -D ESPRESSO_INSTALL_PYPRESSO=OFF \\\
 -D ESPRESSO_CTEST_ARGS=%{?_smp_mflags} \\\
 -D ESPRESSO_TEST_TIMEOUT=480 \\\
 -D ESPRESSO_BUILD_WITH_CUDA=OFF \\\
 -D ESPRESSO_BUILD_WITH_FFTW=ON \\\
 -D ESPRESSO_BUILD_WITH_WALBERLA=ON \\\
 -D ESPRESSO_BUILD_WITH_WALBERLA_AVX=OFF \\\
 -D ESPRESSO_BUILD_WITH_SHARED_MEMORY_PARALLELISM=ON \\\
 -D ESPRESSO_BUILD_WITH_NLOPT=ON \\\
 -D ESPRESSO_BUILD_WITH_HDF5=ON \\\
 -D ESPRESSO_BUILD_WITH_GSL=ON \\\
 -D ESPRESSO_BUILD_WITH_SCAFACOS=OFF \\\
 -D ESPRESSO_BUILD_WITH_STOKESIAN_DYNAMICS=OFF \\\
 -D ESPRESSO_MODULE_INSTALL_PATH=${MPI_PYTHON3_SITEARCH} \\\
 -D CYTHON_EXECUTABLE=%{cython}

# use a separate build subfolder for each MPI vendor
%global _vpath_builddir ${mpi:-serial}

# https://github.com/espressomd/espresso/issues/3396
%global _lto_cflags %{nil}

for mpi in mpich openmpi ; do
   module load mpi/${mpi}-%{_arch}
   old_LDFLAGS="${LDFLAGS}"
   export LDFLAGS="${LDFLAGS} -Wl,-rpath,${MPI_PYTHON3_SITEARCH}/%{name}md"
   sed '/#define ADDITIONAL_CHECKS/d' maintainer/configs/maxset.hpp > myconfig.hpp
   %{cmake} %{defopts}
   export LD_LIBRARY_PATH=$PWD/${mpi:-serial}/src/config
   %cmake_build --target espresso_packaging_dependencies
   export LDFLAGS="${old_LDFLAGS}"
   module unload mpi/${mpi}-%{_arch}
done

%install
for mpi in mpich openmpi ; do
   module load mpi/${mpi}-%{_arch}
   %cmake_install
   rm -rf %{buildroot}/usr/include
   rm -rf %{buildroot}/usr/lib/cmake
   rm -rf %{buildroot}/usr/lib64/cmake
   rm -rf %{buildroot}/usr/lib64/pkgconfig
   rm -rf %{buildroot}/usr/share/cmake
   rm -rf %{buildroot}/usr/walberla
   rm -rf %{buildroot}/${MPI_PYTHON3_SITEARCH}/object_in_fluid
   module unload mpi/${mpi}-%{_arch}
done

%check
export CTEST_OUTPUT_ON_FAILURE=1
for mpi in mpich openmpi ; do
   module load mpi/${mpi}-%{_arch}
   export LD_LIBRARY_PATH=${MPI_LIB}:%{buildroot}${MPI_PYTHON3_SITEARCH}/%{name}md
   %cmake_build --target check_unit_tests
   %cmake_build --target check_python_skip_long
   module unload mpi/${mpi}-%{_arch}
done

%files common
%doc Readme.md AUTHORS CITATION.cff CHANGELOG.md
%license COPYING

%files -n python%{python3_pkgversion}-%{name}-openmpi
%{python3_sitearch}/openmpi/%{name}md/

%files -n python%{python3_pkgversion}-%{name}-mpich
%{python3_sitearch}/mpich/%{name}md/

%changelog
%autochangelog
