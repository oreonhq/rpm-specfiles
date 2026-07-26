%global source0_hash 37571bef65bbec3afe4f3787a4b82fe45b856fe489ab219c7e7fa439f12f6600

Name:           getdp
# TODO: Enablee building with gmsh support as soon as getdp does not require private gmsh api anymore
Version:        3.6.0
Release:        14%{?dist}
Summary:        General Environment for the Treatment of Discrete Problems

License:        GPL-2.0-or-later
URL:            http://www.geuz.org/getdp/
Source0:        http://www.geuz.org/getdp/src/%{name}-%{version}-source.tgz

# Increase cmake minimum version to 3.5
Patch0:         getdp_cmakever.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  arpack-devel
BuildRequires:  gsl-devel
BuildRequires:  flexiblas-devel
BuildRequires:  python3-devel
BuildRequires:  petsc-devel
BuildRequires:  SuperLU-devel
BuildRequires:  libX11-devel
BuildRequires:  metis-devel
BuildRequires:  hdf5-devel
BuildRequires:  cgnslib-devel

# GPLv3+, some fortran files in contrib/pewe, some git version
Provides:       bundled(pewe)

%description
GetDP is an open source finite element solver using mixed elements to
discretize de Rham-type complexes in one, two and three dimensions. The main
feature of GetDP is the closeness between the input data defining discrete
problems (written by the user in ASCII data files) and the symbolic mathematical
expressions of these problems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}-source

# remove bundled libs
find contrib/ -mindepth 1 -maxdepth 1 -type d -not \( -name pewe \) -prune -exec rm -vrf {} ';'

# fix lib -> lib64 for petsc detection
sed -i 's|${ENV_PETSC_ARCH}/lib|${ENV_PETSC_ARCH}/%_lib|g' CMakeLists.txt

# set blas in bundled lib
sed -i 's|-llapack -lblas|-lflexiblas|' contrib/pewe/fortran/Makefile

%build
%cmake \
    -DBLAS_LAPACK_LIBRARIES="-lflexiblas" \
    -DENABLE_MULTIHARMONIC=ON \
    -DENABLE_NX=OFF           \
    -DENABLE_OPENMP=ON        \
    -DENABLE_SLEPC=OFF        \
    -DENABLE_SPARSKIT=OFF     \
    -DENABLE_BUILD_SHARED=ON  \
    -DENABLE_BUILD_DYNAMIC=ON
%cmake_build

%install
%cmake_install

# remove auto-installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
%ctest

%files
%license LICENSE.txt CREDITS.txt
%{_bindir}/%{name}
%{_libdir}/libgetdp.so.3.6
%{_libdir}/libgetdp.so.3.6.0
%{_mandir}/man1/%{name}.1*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libgetdp.so

%changelog
%autochangelog
