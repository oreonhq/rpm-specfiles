%global source0_hash d17a109b3ade999926f5b25ce25082b378399654e3b2234cad5f83cdd00a2f32
%global debug_package %{nil}
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%else
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocm-cmake%{pkg_suffix}
Name:     %{pkg_name}
Version:  %{rocm_version}
Release:        1%{?dist}
Summary:        CMake modules for common build and development tasks for ROCm
License:  MIT
URL:      https://github.com/ROCm/rocm-cmake
Source0:        https://github.com/ROCm/rocm-cmake/archive/rocm-%{version}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz
Patch0:   0001-rocm-cmake-follow-cmake-install-rules.patch
BuildArch: noarch
Requires: cmake
# oreon:deps
BuildRequires:  cmake
# /oreon:deps
%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n rocm-cmake-rocm-%{version}

# Another hardcoding of the libdir
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' share/rocmcmakebuildtools/cmake/ROCMCreatePackage.cmake
sed -i -e 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' share/rocmcmakebuildtools/cmake/ROCMInstallTargets.cmake
    
%build

%cmake -DCMAKE_INSTALL_PREFIX=%{pkg_prefix}
%cmake_build
%install
%cmake_install
rm -f %{buildroot}%{pkg_prefix}/share/doc/rocm-cmake/LICENSE
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
