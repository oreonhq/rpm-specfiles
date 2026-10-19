%global source0_hash none
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
Name:           rocm
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm tools for computing on AMD GPU
License:        MIT
Source0:        License.txt
BuildArch: noarch
ExclusiveArch:  x86_64
Requires: amdsmi >= %{rocm_release}
Requires: hipblas >= %{rocm_release}
Requires: hipcc
Requires: hipfft >= %{rocm_release}
Requires: hiprand >= %{rocm_release}
Requires: hipsolver >= %{rocm_release}
Requires: hipsparse >= %{rocm_release}
Requires: rocblas >= %{rocm_release}
Requires: rocfft >= %{rocm_release}
Requires: rocm-clang
Requires: rocm-hip >= %{rocm_release}
Requires: rocminfo >= %{rocm_release}
Requires: rocm-runtime >= %{rocm_release}
Requires: rocm-smi >= %{rocm_release}
Requires: rocrand >= %{rocm_release}
Requires: rocsolver >= %{rocm_release}
Requires: rocsparse >= %{rocm_release}
%if 0%{?suse_version}
Requires: hipblaslt >= %{rocm_release}
Requires: miopen >= %{rocm_release}
Requires: rccl >= %{rocm_release}
Requires: rocalution >= %{rocm_release}
Requires: rocm-clinfo >= %{rocm_release}
Requires: rocm-core >= %{rocm_release}
Requires: rocm-opencl >= %{rocm_release}
Requires: roctracer >= %{rocm_release}
%endif
# oreon:deps

# /oreon:deps
%description
This is a collection of ROCm tools and libraries for programming
AMD graphics processing units.

%package devel
Summary:        Development environment for ROCm
Requires: amdsmi-devel >= %{rocm_release}
Requires: half-devel
Requires: hipblas-common-devel >= %{rocm_release}
Requires: hipblas-devel >= %{rocm_release}
Requires: hipcub-devel >= %{rocm_release}
Requires: hipfft-devel >= %{rocm_release}
Requires: hiprand-devel >= %{rocm_release}
Requires: hipsolver-devel >= %{rocm_release}
Requires: hipsparse-devel >= %{rocm_release}
Requires: rocblas-devel >= %{rocm_release}
Requires: rocfft-devel >= %{rocm_release}
Requires: rocm-clang-devel
Requires: rocm-cmake >= %{rocm_release}
Requires: rocm-compilersupport-macros
Requires: rocm-hip-devel >= %{rocm_release}
Requires: rocm-rpm-macros >= %{rocm_release}
Requires: rocm-rpm-macros-modules >= %{rocm_release}
Requires: rocm-runtime-devel >= %{rocm_release}
Requires: rocm-smi-devel >= %{rocm_release}
Requires: rocprim-devel >= %{rocm_release}
Requires: rocrand-devel >= %{rocm_release}
Requires: rocsolver-devel >= %{rocm_release}
Requires: rocsparse-devel >= %{rocm_release}
%if 0%{?suse_version}
Requires: hipblaslt-devel >= %{rocm_release}
Requires: miopen-devel >= %{rocm_release}
Requires: rccl-devel >= %{rocm_release}
Requires: rocalution-devel >= %{rocm_release}
Requires: rocm-core-devel >= %{rocm_release}
Requires: rocm-opencl-devel >= %{rocm_release}
Requires: roctracer-devel >= %{rocm_release}
%endif
%description devel
This is a meta package for all of the ROCm devel packages.

%package test
Summary:        Tests for ROCm
Requires: kfdtest             >= %{rocm_release}
%description test
This is a meta package for all of the ROCm test packages.

%prep

%setup -cT
install -pm 644 %{SOURCE0} .

%build

%install

%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rocm-devel -f %{oreon_filedir}/rocm-devel.list
%files -n rocm-test -f %{oreon_filedir}/rocm-test.list

%changelog

%autochangelog
