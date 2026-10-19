%global source0_hash a90077e2080531803dac154e64d6d481289a5839493ce131c4edc8b5ac1bc294
%global upstreamname roctracer
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
%global toolchain clang
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')
%bcond_with test
%bcond_with doc
%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio
Name:           roctracer%{pkg_suffix}
Version:        %{rocm_version}
Release:        1%{?dist}
Summary:        ROCm Tracer Callback/Activity Library for Performance tracing AMD GPUs
Url:            https://github.com/ROCm/%{upstreamname}
License:        MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/%{pkg_module}.%{rocm_patch}.tar.gz#/%{name}.%{rocm_patch}.tar.gz
%if 0%{?suse_version}
%else
%endif
%if %{with doc}
%endif
ExclusiveArch:  x86_64
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  python3-cppheaderparser
BuildRequires:  rocm-cmake-7.1
BuildRequires:  rocm-comgr-7.1-devel
BuildRequires:  rocm-compilersupport-7.1-macros
BuildRequires:  rocm-hip-7.1-devel
BuildRequires:  rocm-rpm-macros-7.1
BuildRequires:  rocm-runtime-7.1-devel
BuildRequires:  texlive-adjustbox
BuildRequires:  texlive-dvips
BuildRequires:  texlive-ec
BuildRequires:  texlive-hanging
BuildRequires:  texlive-latex
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-metafont
BuildRequires:  texlive-multirow
BuildRequires:  texlive-newunicodechar
BuildRequires:  texlive-stackengine
BuildRequires:  texlive-texlive-scripts
BuildRequires:  texlive-tocloft
BuildRequires:  texlive-ulem
BuildRequires:  texlive-url
BuildRequires:  texlive-wasy
BuildRequires:  texlive-wasysym
# /oreon:deps
%description
ROC-tracer

* ROC-tracer library: Runtimes Generic Callback/Activity APIs

  The goal of the implementation is to provide a generic independent
  from specific runtime profiler to trace API and asynchronous activity.

  The API provides functionality for registering the runtimes API
  callbacks and asynchronous activity records pool support.

* ROC-TX library: Code Annotation Events API

  Includes API for:

  * roctxMark
  * roctxRangePush
  * roctxRangePop

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%package devel
Summary:        The %{name} development package
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The headers of libraries for %{name}.

%if %{with doc}
%package doc
Summary:        Docs for %{name}
%description doc
%{summary}
%endif

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description test
%{summary}
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstreamname}-rocm-%{version}

# No knob in cmake to turn off testing
%if %{without test}
sed -i -e 's@add_subdirectory(test)@#add_subdirectory(test)@' CMakeLists.txt

%else

# Adjust test running script lib dir
sed -i -e 's@../lib/@../%{pkg_libdir}/@' test/run.sh

%endif

%build

%cmake \
    -DCMAKE_BUILD_TYPE=%{build_type} \
    -DCMAKE_C_COMPILER=%rocmllvm_bindir/amdclang \
    -DCMAKE_CXX_COMPILER=%rocmllvm_bindir/amdclang++ \
    -DCMAKE_CXX_FLAGS="-I%{pkg_prefix}/include"\
    -DCMAKE_EXE_LINKER_FLAGS="-L %{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DCMAKE_INSTALL_LIBDIR=%{pkg_libdir} \
    -DCMAKE_INSTALL_PREFIX=%{pkg_prefix} \
    -DCMAKE_MODULE_PATH=%{pkg_prefix}/%{pkg_libdir}/cmake/hip \
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DROCM_SYMLINK_LIBS=OFF \
    -DGPU_TARGETS=%{rocm_gpu_list_test} \
    -DHIP_PLATFORM=amd \
    -DHIP_HIPCC_FLAGS="-I%{pkg_prefix}/include -L%{pkg_prefix}/%{pkg_libdir} -lamdhip64" \
    -DBUILD_SHARED_LIBS=ON
%cmake_build
%if %{with doc}
%cmake_build -t doc
%endif
%install
%cmake_install
rm -rf rm %{buildroot}%{pkg_prefix}/share/html
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/LICENSE.md
rm -f %{buildroot}%{pkg_prefix}/share/doc/*/*/LICENSE.md
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n roctracer-7.1-devel -f %{oreon_filedir}/roctracer-7.1-devel.list
%files -n roctracer-7.1-doc -f %{oreon_filedir}/roctracer-7.1-doc.list
%files -n roctracer-7.1-test -f %{oreon_filedir}/roctracer-7.1-test.list

%changelog

%autochangelog
