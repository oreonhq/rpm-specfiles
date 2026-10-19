%global source0_hash b4e74b92919e59cbccbc0baf611f49d50e7d160d2fda86e6eb2aed78ff20f89c
%global upstreamname hipfort
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%bcond check 1
Name:           hipfort%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        Fortran interfaces for ROCm libraries
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        https://github.com/ROCm/%{name}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Handle-cmake-DBUILD_SHARED_LIBS-ON.patch
Patch1:         0001-Generalize-hipfc-to-other-linux-distros.patch
Patch2:         0001-hipfort-remove-build-type-check.patch
Patch3:         0001-hipfort-remove-rocblas_sgemm_kernel_name.patch
Requires:       rocminfo%{pkg_suffix}
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  hipblas-devel
BuildRequires:  hipfft-devel
BuildRequires:  hiprand-devel
BuildRequires:  hipsolver-devel
BuildRequires:  hipsparse-devel
BuildRequires:  rocblas-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocrand-devel
BuildRequires:  rocsolver-devel
BuildRequires:  rocsparse-devel
# /oreon:deps
%description
This repository contains the source and testing for hipfort.
This is a FORTRAN interface library for accessing GPU Kernels.

%package devel
Summary:        The %{name} development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The headers of libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# Can not pass -L*, hipfc gets confused and treats '-' as the start of a passthrough arg 
sed -i -e 's|-o $@|-lrocfft -lrocrand -lrocblas -lrocsolver -lrocsparse -lhipfft -lhiprand -lhipblas -lhipsolver -lhipsparse -o $@|' test/Makefile.in

# For CMake 4
sed -i 's@cmake_minimum_required(VERSION 2.8.12 FATAL_ERROR@cmake_minimum_required(VERSION 3.5@' bin/CMakeLists.txt

%build

%cmake \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_Fortran_FLAGS="-fPIE -L%{pkg_prefix}/%{pkg_libdir}" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_SKIP_RPATH=ON \
    -DROCM_SYMLINK_LIBS=OFF \
    -DHIP_PLATFORM=amd \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=%{build_type}
%cmake_build
%if %{with check}
%check

export CFLAGS=""
export CXXFLAGS=""
export FFLAGS=""
export FCFLAGS=""
export LDFLAGS=""
export HIPFORT="%{pkg_prefix}"
export ROCM_PATH="%{pkg_prefix}"
%cmake_build -t all-tests-run
%endif
%install
%cmake_install
rm -rf %{buildroot}%{pkg_prefix}/include/hipfort/nvptx
rm -rf %{buildroot}%{pkg_prefix}/%{pkg_libdir}/libhipfort-nvptx*
rm %{buildroot}%{pkg_prefix}/%{pkg_libdir}/cmake/hipfort/hipfort-config.cmake
rm -f %{buildroot}%{pkg_prefix}/share/doc/hipfort/LICENSE
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n hipfort-devel -f %{oreon_filedir}/hipfort-devel.list

%changelog

%autochangelog
