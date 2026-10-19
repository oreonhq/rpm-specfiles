%global source0_hash 50c914c42406e1365169a37be475562baf28da47c45241a5f7c655c4c2640ada
%global majorver 42
%global releasever 42.0.0
%global desc %{expand: \
The Compute Library is a collection of low-level machine learning functions
optimized for Arm Cortex-A, Arm Neoverse and Arm Mali GPUs architectures.
The library provides superior performance to other open source alternatives
and immediate support for new Arm technologies e.g. SVE2.}
Name:		arm-compute-library
Version:	53.3.1
Release:        1%{?dist}
Summary:        ARM compute library
License:	MIT AND Apache-2.0
URL:		https://github.com/arm-software/ComputeLibrary
Source0:        https://github.com/arm-software/ComputeLibrary/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:	arm_compute.pc.in
Source2:	arm_compute_graph.pc.in
Patch0:		mathjax-doc.patch
Patch1:		disable-doxygen-timestamp.patch
ExcludeArch:	i686 ppc64le s390x
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libglvnd-devel
BuildRequires:  python3-scons
# /oreon:deps
%description
%{desc}
	
%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Provides:	bundle(opencl-headers) = 3.0
Provides:	bundle(stb_image-devel) = 2.19
Provides:	bundle(half-devel) = 1.12.0
Provides:	bundle(libnpy) = 0.1.0
%description devel
%{desc}

%package doc
Summary:	Documentations and examples for %{name}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	mathjax
%description doc
Contains documentations and examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n ComputeLibrary-%{version} 

# remove .bazel files
find . -name *.bazel -exec rm -f '{}' \;

# gcc 15 include cstdint
sed -i '/#include <memory>.*/a#include <cstdint>' arm_compute/core/CPP/CPPTypes.h
sed -i '/#include <cstddef>.*/a#include <cstdint>' arm_compute/runtime/MemoryRegion.h
sed -i '1i #include <cstdint>' tests/framework/instruments/hwc_names.hpp

%build

scons %{?_smp_mflags} os=linux \
	build=native \
	install_dir=install \
	set_soname=1 \
	opencl=1 \
	asserts=1 \
	embed_kernels=1 \
	benchmark_tests=0 \
	validation_tests=1 \
	examples=0 \
%ifarch aarch64
	neon=1 arch=arm64-v8a \
%else
	neon=0 arch=x86_64 \
%endif
	Werror=0 extra_cxx_flags="%{optflags}" extra_link_flags="%{build_ldflags}"
doxygen docs/Doxyfile
cat %{SOURCE1} | sed -e "s,%%prefix%%,%{_prefix},g" \
	-e "s,%%exec_prefix%%,%{_prefix},g" \
	-e "s,%%libdir%%,%{_libdir},g" \
	-e "s,%%includedir%%,%{_includedir},g" \
	-e "s,%%VERSION%%,%{version},g" \
	> build/install/arm_compute.pc
cat %{SOURCE2} | sed -e "s,%%prefix%%,%{_prefix},g" \
	-e "s,%%exec_prefix%%,%{_prefix},g" \
	-e "s,%%libdir%%,%{_libdir},g" \
	-e "s,%%includedir%%,%{_includedir},g" \
	-e "s,%%VERSION%%,%{version},g" \
	> build/install/arm_compute_graph.pc
%install
mkdir -p %{buildroot}%{_includedir}/ArmCompute
cp -a build/install/include/* %{buildroot}%{_includedir}/ArmCompute/
mkdir -p %{buildroot}%{_libdir}
rm -f build/*.a
cp -a build/libarm_compute* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -m 0644 build/install/arm_compute.pc %{buildroot}%{_libdir}/pkgconfig
install -m 0644 build/install/arm_compute_graph.pc %{buildroot}%{_libdir}/pkgconfig
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a build/docs/html %{buildroot}%{_docdir}/%{name}
%oreon_autofiles arm-compute-library-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles arm-compute-library-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

LD_LIBRARY_PATH=%{buildroot}%{_libdir}:$LD_LIBRARY_PATH ./build/tests/arm_compute_validation --filter='^(?!CL).*'
%files -f %{oreon_filedir}/main.list
%files -n arm-compute-library-devel -f %{oreon_filedir}/arm-compute-library-devel.list
%files -n arm-compute-library-doc -f %{oreon_filedir}/arm-compute-library-doc.list

%changelog

%autochangelog
