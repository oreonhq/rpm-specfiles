%global source0_hash 45bbffbc193a1823f979731139cb5fb43076ae85759e63fb31ed928ddbc73bcb
%bcond_with gitcommit
%if %{with gitcommit}
%global commit0 312eb7e13554ce75d02c5cb27357555f1368f2d1
%global date0 20240814
%else
%global commit0 312eb7e13554ce75d02c5cb27357555f1368f2d1
%global date0 20240814
%endif
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global upstream_name XNNPACK
%global __cmake_in_source_build 1
%global debug_package %{nil}
Summary:        High-efficiency floating-point neural network inference operators
Name:           xnnpack
License:        BSD-3-Clause
Version:        0.0^git%{date0}.%{shortcommit0}
Release:        1%{?dist}
URL:            https://github.com/google/%{upstream_name}
Source0:        https://github.com/google/%{upstream_name}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
Patch0:         0001-Fix-cmake-for-pthread-and-cpuinfo-with-USE_SYSTEM_LI.patch
ExclusiveArch:  x86_64 aarch64
# oreon:deps
BuildRequires:  FP16-devel
BuildRequires:  cmake
BuildRequires:  cpuinfo-devel
BuildRequires:  fxdiv-devel
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  pthreadpool-devel
# /oreon:deps
%description
XNNPACK is a highly optimized solution for neural network inference on ARM,
x86, WebAssembly, and RISC-V platforms. XNNPACK is not intended for direct
use by deep learning practitioners and researchers; instead it provides
low-level performance primitives for accelerating high-level machine learning
frameworks, such as TensorFlow Lite, TensorFlow.js, PyTorch, ONNX Runtime,
and MediaPipe.

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{commit0}

# version of the *.so
echo "SET_TARGET_PROPERTIES(XNNPACK PROPERTIES SOVERSION \"24.08.14\")" >> CMakeLists.txt

%build

%cmake -G Ninja \
      -DBUILD_SHARED_LIBS=ON \
      -DCMAKE_C_FLAGS=-fPIC \
      -DCMAKE_CXX_FLAGS=-fPIC \
      -DXNNPACK_BUILD_BENCHMARKS=OFF \
      -DXNNPACK_BUILD_LIBRARY=ON \
      -DXNNPACK_BUILD_TESTS=OFF \
      -DXNNPACK_ENABLE_KLEIDIAI=OFF \
      -DXNNPACK_USE_SYSTEM_LIBS=ON \
      -DXNNPACK_LIBRARY_TYPE=shared
%cmake_build
%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 include/xnnpack.h %{buildroot}%{_includedir}
mkdir -p %{buildroot}%{_libdir}
strip libXNNPACK.so.24.08.14
install -p -m 755 libXNNPACK.so.24.08.14 %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}
ln -s libXNNPACK.so.24.08.14 libXNNPACK.so
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n xnnpack-devel -f %{oreon_filedir}/xnnpack-devel.list

%changelog

%autochangelog
