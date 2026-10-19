%global source0_hash 6f2240c94557117fdc1954145148c9dff440d1e5c1aeafc1096f3c7bc03a41b8
Name:           onednn
Version:        3.13.2
Release:        1%{?dist}
Summary:        The oneAPI Deep Neural Network Library
License:         Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSL-1.0 AND MIT
URL:               https://github.com/uxlfoundation/oneDNN
Source0:        https://github.com/uxlfoundation/oneDNN/archive/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64 ppc64le s390x
Provides: mkldnn = %{version}-%{release}
Provides: mkl-dnn = %{version}-%{release}
Obsoletes: mkl-dnn < 1.3
Provides: oneDNN = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(OpenCL)
# /oreon:deps
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
%global oreon_srcdir oneDNN-%{version}
%oreon_prep
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
rm -rf %{buildroot}%{_docdir}/dnnl
%{?_with_tests:
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ctest
}
%files -f %{oreon_filedir}/main.list
%files -n onednn-devel -f %{oreon_filedir}/onednn-devel.list

%changelog

%autochangelog
