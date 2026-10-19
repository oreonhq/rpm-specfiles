%global source1_hash 4897dd106d573e9dacda8509ca5af1a0e008755bf9c383ef6777ac490223031f
%global source0_hash 4662fc1b10e7e6740ccde2896cccd18dab96584abb7c623091afd7eeb2745ba0
%global upstream_name level-zero-raytracing-support
%global tbb_version 2021.6.0
Name: intel-level-zero-gpu-raytracing
Version: 1.2.0
Release:        1%{?dist}
Summary:        oneAPI Level Zero Ray Tracing Support library
License: Apache-2.0
URL: https://github.com/intel/level-zero-raytracing-support
Source0:        https://github.com/intel/%{upstream_name}/archive/v%{version}.tar.gz
Source1: https://github.com/uxlfoundation/oneTBB/archive/v%{tbb_version}.tar.gz
Requires: oneapi-level-zero
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  ninja-build
BuildRequires:  pkg-config
# /oreon:deps
%description
The oneAPI Level Zero Ray Tracing Support library implements high performance
CPU based construction algorithms for 3D acceleration structures that are
compatible with the ray tracing hardware of Intel GPUs.

This library is used by Intel oneAPI Level Zero to implement part of the
RTAS builder extension.

This library should not get used directly but only through Level Zero.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{upstream_name}-%{version}

# Needs a specific name for static linking
tar xf %{SOURCE1}
mv oneTBB-%{tbb_version} tbb

%build

%cmake \
   -DCMAKE_BUILD_TYPE=Release \
   -DCMAKE_INSTALL_PREFIX=/usr
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
