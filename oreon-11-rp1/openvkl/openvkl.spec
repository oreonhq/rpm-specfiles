%global source0_hash 0c7faa9582a93e93767afdb15a6c9c9ba154af7ee83a6b553705797be5f8af62
Name:		openvkl
Version:	2.0.1
Release:        1%{?dist}
Summary:        Intel Open Volume Kernel Library
License:	Apache-2.0 AND BSL-1.0 AND MIT
URL:		https://github.com/OpenVKL/openvkl
Source0:        https://github.com/OpenVKL/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	aarch64 x86_64
# oreon:deps
BuildRequires:  blosc-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  embree-devel
BuildRequires:  gcc-c++
BuildRequires:  glfw-devel
BuildRequires:  imath-devel
BuildRequires:  ispc-static
BuildRequires:  openvdb-devel
BuildRequires:  rkcommon-devel
# /oreon:deps
%description
Intel Open Volume Kernel Library (Open VKL) is a collection of high-performance
volume computation kernels, developed at Intel. The target users of Open VKL 
are graphics application engineers who want to improve the performance of their
volume rendering applications by leveraging Open VKL’s performance-optimized 
kernels, which include volume traversal and sampling functionality for a 
variety of volumetric data formats.

Open VKL contains kernels optimized for the latest x86 processors with support
for SSE, AVX, AVX2, and AVX-512 instructions, and for ARM processors with 
support for NEON instructions. Open VKL supports Intel GPUs based on the Xe HPG
microarchitecture and Xe HPC microarchitecture under Linux.

%package devel
Summary:	Development files for %{name}
License:	Apache-2.0
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	openvdb-devel >= 7.0.0
Requires:	rkcommon-devel >= 1.11.0
%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# do not install LICENSE.txt
sed -i '/LICENSE.txt/d' openvkl/CMakeLists.txt
sed -i '/third-party-programs/d' openvkl/CMakeLists.txt
# lib64 path fix 
sed -i 's/lib\/cmake/%{_lib}\/cmake/g' utility/vdb/CMakeLists.txt
# bypass vdb_volume_dense test for now
sed -i '/vdb_volume_dense.cpp/d' testing/apps/CMakeLists.txt

%build

%cmake \
	-DBUILD_EXAMPLES=OFF \
	-DBUILD_OPENVKL_TESTING=ON \
	-DBUILD_BENCHMARKS=OFF \
	-DOpenVDB_ROOT=%{_prefix}
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
%files -f %{oreon_filedir}/main.list
%files -n openvkl-devel -f %{oreon_filedir}/openvkl-devel.list

%changelog

%autochangelog
