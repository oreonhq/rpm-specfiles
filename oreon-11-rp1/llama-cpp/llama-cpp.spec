%global source0_hash 056cf63483c6a6b93a05323ea5162263dfa9e7ac6664516e98ab433961d021f8
%global pypi_name gguf
%global pypi_version 0.10.0
%bcond_with examples
%if %{with examples}
%global build_examples ON
%else
%global build_examples OFF
%endif
%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond check 1
Summary:        Port of Facebook's LLaMA model in C/C++
Name:           llama-cpp
License:        MIT AND Apache-2.0 AND LicenseRef-Fedora-Public-Domain
Version:        b6153
Release:        1%{?dist}
URL:            https://github.com/ggerganov/llama.cpp
Source0:        https://github.com/ggerganov/llama.cpp/archive/%{version}.tar.gz#/llama.cpp-%{version}.tar.gz
ExclusiveArch:  x86_64 aarch64
%ifarch x86_64
%bcond_without rocm
%else
%bcond_with rocm
%endif
%if %{with rocm}
%global build_hip ON
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%else
%global build_hip OFF
%global toolchain gcc
%endif
%if %{with examples}
%endif
%if %{with rocm}
Requires:       rocblas
Requires:       hipblas
%endif
Requires:       curl
Recommends:     numactl
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-llama-cpp = %{version}-%{release}
# /oreon:deps
%description
The main goal of llama.cpp is to run the LLaMA model using 4-bit
integer quantization on a MacBook

* Plain C/C++ implementation without dependencies
* Apple silicon first-class citizen - optimized via ARM NEON, Accelerate
  and Metal frameworks
* AVX, AVX2 and AVX512 support for x86 architectures
* Mixed F16 / F32 precision
* 2-bit, 3-bit, 4-bit, 5-bit, 6-bit and 8-bit integer quantization support
* CUDA, Metal and OpenCL GPU backend support

The original implementation of llama.cpp was hacked in an evening.
Since then, the project has improved significantly thanks to many
contributions. This project is mainly for educational purposes and
serves as the main playground for developing new features for the
ggml library.

%package devel
Summary:        Port of Facebook's LLaMA model in C/C++
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The main goal of llama.cpp is to run the LLaMA model using 4-bit
integer quantization on a MacBook

* Plain C/C++ implementation without dependencies
* Apple silicon first-class citizen - optimized via ARM NEON, Accelerate
  and Metal frameworks
* AVX, AVX2 and AVX512 support for x86 architectures
* Mixed F16 / F32 precision
* 2-bit, 3-bit, 4-bit, 5-bit, 6-bit and 8-bit integer quantization support
* CUDA, Metal and OpenCL GPU backend support

The original implementation of llama.cpp was hacked in an evening.
Since then, the project has improved significantly thanks to many
contributions. This project is mainly for educational purposes and
serves as the main playground for developing new features for the
ggml library.

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%if %{with examples}
%package examples
Summary:        Examples for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3dist(numpy)
Requires:       python3dist(torch)
Requires:       python3dist(sentencepiece)
%description examples
%{summary}
%endif

%prep

%autosetup -p1 -n llama.cpp-%{version}

# verson the *.so
sed -i -e 's/POSITION_INDEPENDENT_CODE ON/POSITION_INDEPENDENT_CODE ON SOVERSION %{version}/' src/CMakeLists.txt
sed -i -e 's/POSITION_INDEPENDENT_CODE ON/POSITION_INDEPENDENT_CODE ON SOVERSION %{version}/' ggml/src/CMakeLists.txt
sed -i -e 's/POSITION_INDEPENDENT_CODE ON/POSITION_INDEPENDENT_CODE ON SOVERSION %{version}/' tools/mtmd/CMakeLists.txt
sed -i '/target_link_libraries(ggml-hip PRIVATE ggml-base.*/aset_target_properties(ggml-hip PROPERTIES SOVERSION %{version})' ggml/src/ggml-hip/CMakeLists.txt
sed -i '/target_compile_features(${GGML_CPU_NAME} PRIVATE c_std_11.*/aset_target_properties(${GGML_CPU_NAME} PROPERTIES SOVERSION %{version})' ggml/src/ggml-cpu/CMakeLists.txt

# gcc 15 include cstdint
sed -i '/#include <vector.*/a#include <cstdint>' src/llama-mmap.h
 
# no android needed
rm -rf exmples/llma.android
# git cruft
find . -name '.gitignore' -exec rm -rf {} \;

%build

%if %{with examples}
cd %{_vpath_srcdir}/gguf-py
%pyproject_wheel
cd -
%endif
%cmake \
    -DCMAKE_INSTALL_LIBDIR=%{_lib} \
    -DCMAKE_SKIP_RPATH=ON \
    -DGGML_AVX=OFF \
    -DGGML_AVX2=OFF \
    -DGGML_AVX512=OFF \
    -DGGML_AVX512_VBMI=OFF \
    -DGGML_AVX512_VNNI=OFF \
    -DGGML_FMA=OFF \
    -DGGML_F16C=OFF \
    -DGGML_HIP=%{build_hip} \
    -DAMDGPU_TARGETS=%{rocm_gpu_list_default} \
    -DLLAMA_BUILD_EXAMPLES=%{build_examples} \
    -DLLAMA_BUILD_TESTS=%{build_test}
%cmake_build
%install
%if %{with examples}
cd %{_vpath_srcdir}/gguf-py
%pyproject_install
cd -
%endif
%cmake_install
rm -rf %{buildroot}%{_libdir}/libggml_shared.*
%if %{with examples}
mkdir -p %{buildroot}%{_datarootdir}/%{name}
cp -r %{_vpath_srcdir}/examples %{buildroot}%{_datarootdir}/%{name}/
cp -r %{_vpath_srcdir}/models %{buildroot}%{_datarootdir}/%{name}/
cp -r %{_vpath_srcdir}/README.md %{buildroot}%{_datarootdir}/%{name}/
rm -rf %{buildroot}%{_datarootdir}/%{name}/examples/llama.android
%else
rm %{buildroot}%{_bindir}/convert*.py
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%if %{with test}
%if %{with check}
%check

%ctest
%endif
%endif
%files
%files -n llama-cpp-devel -f %{oreon_filedir}/llama-cpp-devel.list
%files -n llama-cpp-test -f %{oreon_filedir}/llama-cpp-test.list

%changelog

%autochangelog
