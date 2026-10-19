%global source0_hash 9d7386abeea5ec290b4299684a0ec810d5241a40f7bb1482e794285baa1a4805
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname TransferBench
%global toolchain rocm
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/' -e 's/-mtls-dialect=gnu2//')
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global gpu_list "gfx906;gfx908;gfx90a;gfx942;gfx950;gfx1030;gfx1100;gfx1101;gfx1102;gfx1150;gfx1151;gfx1200;gfx1201"
Name:       rocm-transferbench
Version:    %{rocm_version}
Release:        1%{?dist}
Summary:        Benchmark copies between AMD GPUs
License:    MIT
URL:        https://github.com/ROCm/%{upstreamname}
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{toolchain}-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
ExclusiveArch: x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(numa)
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
# /oreon:deps
%description
TransferBench is a benchmark for simultaneous copies between
user-specified CPU and GPU devices.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build

%cmake \
    -DGPU_TARGETS=%{gpu_list} \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_BUILD_TYPE=${bt} \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/clang++ \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/clang \
    -DROCM_PATH=/usr \
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{_prefix}/share/doc/transferbench/LICENSE.md
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
