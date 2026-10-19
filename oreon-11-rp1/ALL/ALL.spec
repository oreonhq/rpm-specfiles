%global source0_hash f17ad452a026e3147cd3323f741f319ddb9a4c92eb792364f64eac0fc992e603
Name:           ALL
Version:        0.9.4
%global         sover 0
Release:        1%{?dist}
Summary:        A Load Balancing Library (ALL)
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            http://slms.pages.jsc.fz-juelich.de/websites/all-website/ 
Source0:        https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing/-/archive/v%{version}/loadbalancing-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         https://gitlab.jsc.fz-juelich.de/SLMS/loadbalancing/-/merge_requests/32.patch
ExcludeArch: %{ix86} s390x
Provides:       Bundled(stb_arr)
%global all_desc \
The library aims to provide an easy way to include dynamic domain-based \
load balancing into particle based simulation codes. 
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  mpich-devel
BuildRequires:  openmpi-devel
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  voro++-devel
BuildRequires:  vtk-mpich-devel
BuildRequires:  vtk-openmpi-devel
# /oreon:deps
%description
%{all_desc}

%package openmpi
Summary:    Openmpi libraries for %{name}
%description openmpi
%{all_desc}

This package contains %{name} libraries compiled with openmpi.

%package openmpi-devel
Summary:    Openmpi development headers and libraries for %{name}
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:   openmpi-devel
Requires:   vtk-openmpi-devel
Requires:   voro++-devel
%description openmpi-devel
%{all_desc}

This package contains openmpi development files of %{name}.

%package mpich
Summary:    Mpich libraries for %{name}
%description mpich
%{all_desc}

This package contains %{name} libraries compiled with mpich.

%package mpich-devel
Summary:    Mpich development headers and libraries for %{name}
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:   mpich-devel
Requires:   vtk-mpich-devel
Requires:   voro++-devel
%description mpich-devel
%{all_desc}

This package contains mpich development files of %{name}.

%package doc
Summary:    Documentation for %{name}
BuildArch:  noarch
%description doc
%{all_desc}

This package contains the documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n loadbalancing-v%{version}
rm -rf contrib/voro++

%build

%global _vpath_builddir %{_target_platform}-${mpi}
for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake \
    -DCM_ALL_VTK_OUTPUT=ON \
    -DCM_ALL_FORTRAN=ON \
    -DCM_ALL_USE_F08=ON \
    -DCM_ALL_EXTERNAL_VORONOI=ON \
    -DCM_ALL_TESTS=ON \
    -DCM_ALL_TESTS_INTEGRATION=ON \
    -DCM_ALL_AUTO_DOC=ON \
    -DCMAKE_INSTALL_LIBDIR=${MPI_LIB:-%{_libdir}} \
    -DCMAKE_INSTALL_INCLUDEDIR=${MPI_INCLUDE:-%{_includedir}} \
    %{nil}
  mkdir -p %{_vpath_builddir}/docs/doc/doxygen/html
  mkdir -p %{_vpath_builddir}/docs/doc/doxygen/xml
  %cmake_build
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
%install
for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake_install
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
rm -rv %{buildroot}/%{_docdir}/%{name}/sphinx/{.doctrees,.buildinfo}
%fdupes %{buildroot}/%{_docdir}/%{name}
%oreon_autofiles ALL-openmpi usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ALL-openmpi-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ALL-mpich usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles ALL-mpich-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles ALL-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %ctest
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done
%files -f %{oreon_filedir}/main.list
%files -n ALL-openmpi -f %{oreon_filedir}/ALL-openmpi.list
%files -n ALL-openmpi-devel -f %{oreon_filedir}/ALL-openmpi-devel.list
%files -n ALL-mpich -f %{oreon_filedir}/ALL-mpich.list
%files -n ALL-mpich-devel -f %{oreon_filedir}/ALL-mpich-devel.list
%files -n ALL-doc -f %{oreon_filedir}/ALL-doc.list

%changelog

%autochangelog
