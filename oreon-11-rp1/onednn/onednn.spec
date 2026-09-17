%global source0_hash 0ed141ee3ecf2856aef4966154a19b408faac50234581aeed4bd6e9dad09de68

Name:           onednn
Version:        3.11.1
Release:        %autorelease
Summary:     The oneAPI Deep Neural Network Library

License:         Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
URL:               https://github.com/uxlfoundation/oneDNN
Source0:        %{url}/archive/v%{version}/onednn-%{version}.tar.gz

# This package only work in 64bit arches for now
ExclusiveArch:  x86_64 aarch64 ppc64le s390x

BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++

# Optionals not yet enabled
BuildRequires:  pkgconfig(OpenCL)
#BuildRequires:  pkgconfig(tbb)

# Virtual provides mkldnn
Provides: mkldnn = %{version}-%{release}
Provides: mkl-dnn = %{version}-%{release}
Obsoletes: mkl-dnn < 1.3
# Provides oneDNN
Provides: oneDNN = %{version}-%{release}

%description
oneAPI Deep Neural Network Library (oneDNN) is an open-source cross-platform
performance library of basic building blocks for deep learning applications.
oneDNN is part of oneAPI. The library is optimized for Intel(R) Architecture
Processors, Intel Graphics, and Arm* 64-bit Architecture (AArch64)-based
processors. oneDNN has experimental support for the following architectures:
NVIDIA* GPU, OpenPOWER* Power ISA (PPC64), IBMz* (s390x), and RISC-V.

oneDNN is intended for deep learning applications and framework developers
interested in improving application performance on Intel CPUs and GPUs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n oneDNN-%{version}

%build
%cmake \
  -DDNNL_ARCH_OPT_FLAGS="" \
  -DDNNL_BUILD_EXAMPLES=OFF \
  -DCMAKE_C_STD=11 \
  -DCMAKE_CPP_STD=17 \
  -DONEDNN_GPU_RUNTIME=OCL

%cmake_build

%install
%cmake_install

# Remove docs
rm -rf %{buildroot}%{_docdir}/dnnl

# Some ocl/gpu tests will fails if lacking an appropriate implementation
%{?_with_tests:
%check
%ctest
}

%files
%license LICENSE THIRD-PARTY-PROGRAMS
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md
%{_libdir}/libdnnl.so.3
%{_libdir}/libdnnl.so.3.*

%files devel
%dir %{_includedir}/oneapi
%{_includedir}/oneapi/dnnl
%{_includedir}/dnnl*.h*
%{_libdir}/libdnnl.so
%dir %{_libdir}/cmake/dnnl
%{_libdir}/cmake/dnnl/*.cmake

%changelog
%autochangelog
