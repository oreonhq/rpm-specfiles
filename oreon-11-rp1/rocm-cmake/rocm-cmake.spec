%global source0_hash d17a109b3ade999926f5b25ce25082b378399654e3b2234cad5f83cdd00a2f32

#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# there is no debug package - this is just cmake modules
%global debug_package %{nil}

%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

%bcond_with compat
%if %{with compat}
# install to /usr/lib64/rocm/rocm-<major>.<minor>
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}/
%global pkg_suffix -%{rocm_release}
%else
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%endif
%global pkg_name rocm-cmake%{pkg_suffix}

Name:     %{pkg_name}
Version:  %{rocm_version}
Release:  3%{?dist}
Summary:  CMake modules for common build and development tasks for ROCm
License:  MIT
URL:      https://github.com/ROCm/rocm-cmake
Source:   %{url}/archive/rocm-%{version}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz
# https://github.com/ROCm/rocm-cmake/issues/276
Patch0:   0001-rocm-cmake-follow-cmake-install-rules.patch

BuildArch: noarch
BuildRequires: cmake
Requires: cmake

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

%files
%if %{without compat}
%doc CHANGELOG.md
%license LICENSE
%endif
%{pkg_prefix}/share/rocm/
%{pkg_prefix}/share/rocmcmakebuildtools/

%changelog
%autochangelog
