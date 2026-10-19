%global source1_hash 00e4a87e87b7e7612f519a41e491f16623b12423620006f59f5688bfd8d13b08
%global source0_hash 29f050480d9efe9a8bd55e274f1d571a1c6001cd1db9f8648a1888f73e4ea2ef
%global upstreamname rocprofiler-register
%global rocm_release 7.1
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}
%bcond_with compat
%if %{with compat}
%global pkg_libdir lib
%global pkg_prefix %{_prefix}/lib64/rocm/rocm-%{rocm_release}
%global pkg_suffix -%{rocm_release}
%global pkg_module rocm%{pkg_suffix}
%else
%global pkg_libdir %{_lib}
%global pkg_prefix %{_prefix}
%global pkg_suffix %{nil}
%global pkg_module default
%endif
%global glog_version 0.7.1
%bcond check 1
%if %{with check}
%global build_test ON
%else
%global build_test OFF
%endif
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%global _source_payload w7T0.xzdio
%global _binary_payload w7T0.xzdio
Name:           rocprofiler-register%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        A rocprofiler helper library
License:        MIT AND BSD-3-Clause
ExclusiveArch:  x86_64
Url:            https://github.com/ROCm/%{upstreamname}
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
Source1:        https://github.com/google/glog/archive/refs/tags/v%{glog_version}.tar.gz
Provides:       bundled(glog) = %{glog_version}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
# /oreon:deps
%description
The rocprofiler-register library is a helper library that coordinates
the modification of the intercept API table(s) of the HSA/HIP/ROCTx
runtime libraries by the ROCprofiler (v2) library. The purpose of this
library is to provide a consistent and automated mechanism of enabling
performance analysis in the ROCm runtimes which does not rely on
environment variables or unique methods for each runtime library.

When a runtime is initialized (either explicitly and lazily) and the
intercept API table is constructed, it passes this API table to
rocprofiler-register. Rocprofiler-register scans the symbols in the
address space and if it detects there is at least one visible symbol
named rocprofiler_configure (which is a function provided by tools),
it passes the intercept API table to the rocprofiler library (dlopening
the rocprofiler library if it is not already loaded). The rocprofiler
library then does an extensive scan for all the instances of the
rocprofiler_configure symbols and invokes each of them. The
rocprofiler_configure function (again, provided by a tool) returns
effectively tells rocprofiler which behaviors it wants to be notified
about, features it wants to use (e.g. API tracing, kernel dispatch
timing), etc.

%package devel
Summary:        The development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# When using the system fmt, need to change this link
sed -i 's@fmt::fmt@fmt@' source/lib/rocprofiler-register/CMakeLists.txt

# Do not hardcode install lib
sed -i 's@set(CMAKE_INSTALL_LIBDIR@#set(CMAKE_INSTALL_LIBDIR@' CMakeLists.txt

# Do not use git to fetch glog, use cached source
cd external
rm -rf glog
tar xf %{SOURCE1}
mv glog-* glog
# Need to remove the fetch
sed -i -e '/rocprofiler_register_checkout_git_submodule/,+6d' CMakeLists.txt
cd -

# Copy glog's license file
cp -p external/glog/COPYING COPYING.glog

%build

%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DROCPROFILER_REGISTER_BUILD_TESTS=%{build_test} \
    -DROCPROFILER_REGISTER_BUILD_FMT=OFF
%cmake_build
%install
%cmake_install
rm -rf %{buildroot}%{pkg_prefix}/share/rocprofiler-register
rm -rf %{buildroot}%{pkg_prefix}/share/modulefiles
rm -rf %{buildroot}%{pkg_prefix}/share/doc/rocprofiler-register/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n rocprofiler-register-7.1-devel -f %{oreon_filedir}/rocprofiler-register-7.1-devel.list

%changelog

%autochangelog
